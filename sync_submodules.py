#!/usr/bin/env python3
"""Sync all submodules in hot_cudas to their upstream latest HEAD via GitHub Git Data API."""
import json, os, subprocess, sys

TOKEN = os.environ["GH_TOKEN"]
# Auto-detect repo from git remote
result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
remote = result.stdout.strip()
# Extract owner/repo from https://github.com/OWNER/REPO.git
parts = remote.rstrip("/").rstrip(".git").split("/")
OWNER, REPO = parts[-2], parts[-1]

def api(method, endpoint, data=None):
    cmd = ["curl", "-s", "-X", method,
           "-H", f"Authorization: token {TOKEN}",
           "-H", "Content-Type: application/json",
           "-H", "Accept: application/vnd.github+json"]
    if data:
        cmd += ["-d", json.dumps(data)]
    cmd.append(f"https://api.github.com{endpoint}")
    r = subprocess.run(cmd, capture_output=True, timeout=30)
    return json.loads(r.stdout.decode("utf-8", errors="replace"))

def get_upstream_sha(owner_repo):
    """Get default branch HEAD SHA."""
    r = api("GET", f"/repos/{owner_repo}")
    if isinstance(r, dict) and r.get("default_branch"):
        branch = r["default_branch"]
        r2 = api("GET", f"/repos/{owner_repo}/git/refs/heads/{branch}")
        if isinstance(r2, list) and len(r2) > 0:
            return r2[0]["object"]["sha"]
        elif isinstance(r2, dict) and r2.get("object", {}).get("sha"):
            return r2["object"]["sha"]
    return None

# Parse .gitmodules
submodules = []  # [(upstream_url, top_dir, sub_name)]
with open(".gitmodules") as f:
    current = {}
    for line in f:
        line = line.strip()
        if line.startswith("[submodule"):
            if current.get("url") and current.get("path"):
                path = current["path"]
                top_dir = path.split("/")[0]
                sub_name = path.split("/", 1)[1] if "/" in path else path
                upstream = current["url"].replace("https://github.com/", "").rstrip(".git")
                submodules.append((upstream, top_dir, sub_name, path))
            current = {}
        elif "=" in line:
            k, v = line.split("=", 1)
            current[k.strip()] = v.strip()
    # Last entry
    if current.get("url") and current.get("path"):
        path = current["path"]
        top_dir = path.split("/")[0]
        sub_name = path.split("/", 1)[1] if "/" in path else path
        upstream = current["url"].replace("https://github.com/", "").rstrip(".git")
        submodules.append((upstream, top_dir, sub_name, path))

print(f"Found {len(submodules)} submodules")

# Get current repo state
r = api("GET", f"/repos/{OWNER}/{REPO}/git/refs/heads/main")
main_sha = r["object"]["sha"]
r = api("GET", f"/repos/{OWNER}/{REPO}/git/commits/{main_sha}")
tree_sha = r["tree"]["sha"]
r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{tree_sha}")

old_subtrees = {}
root_files = {}
for item in r["tree"]:
    if item["mode"] == "040000":
        old_subtrees[item["path"]] = item["sha"]
    else:
        root_files[item["path"]] = item

# Fetch upstream SHAs and update subtrees
updated = 0
new_subtree_shas = {}

for upstream, top_dir, sub_name, full_path in submodules:
    new_sha = get_upstream_sha(upstream)
    if not new_sha:
        print(f"  SKIP: {upstream} (cannot fetch)")
        if top_dir in old_subtrees:
            new_subtree_shas[top_dir] = old_subtrees[top_dir]
        continue

    sub_tree_sha = old_subtrees.get(top_dir)
    if not sub_tree_sha:
        print(f"  SKIP: {top_dir} (not in repo)")
        continue

    r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{sub_tree_sha}")
    entries = r.get("tree", [])

    changed = False
    new_entries = []
    for entry in entries:
        if entry["mode"] == "160000":
            old_sha = entry["sha"]
            if old_sha != new_sha:
                print(f"  UPDATE: {top_dir} {old_sha[:10]} -> {new_sha[:10]}")
                changed = True
            entry = dict(entry, sha=new_sha)
        new_entries.append(entry)

    if changed:
        r = api("POST", f"/repos/{OWNER}/{REPO}/git/trees", {"tree": new_entries})
        new_subtree_shas[top_dir] = r["sha"]
        updated += 1
    else:
        new_subtree_shas[top_dir] = sub_tree_sha

print(f"\nUpdated: {updated}/{len(submodules)}")

if updated == 0:
    print("All submodules already up to date.")
    sys.exit(0)

# Build new root tree
root_entries = []
for item in r.get("tree", []):
    # Re-read tree for root entries
    pass

r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{tree_sha}")
for item in r["tree"]:
    if item["mode"] == "040000" and item["path"] in new_subtree_shas:
        root_entries.append({"path": item["path"], "mode": "040000", "type": "tree", "sha": new_subtree_shas[item["path"]]})
    elif item["mode"] != "040000":
        root_entries.append(item)

r = api("POST", f"/repos/{OWNER}/{REPO}/git/trees", {"tree": root_entries})
new_tree_sha = r.get("sha")

r = api("POST", f"/repos/{OWNER}/{REPO}/git/commits", {
    "message": f"chore: sync {updated} submodules with upstream [skip ci]",
    "tree": new_tree_sha,
    "parents": [main_sha]
})
new_commit = r.get("sha")

r = api("PATCH", f"/repos/{OWNER}/{REPO}/git/refs/heads/main", {"sha": new_commit})
if r.get("object", {}).get("sha") == new_commit:
    print(f"Pushed commit {new_commit[:10]}: synced {updated} submodules")
else:
    print(f"ERROR: {json.dumps(r)[:300]}")
    sys.exit(1)
