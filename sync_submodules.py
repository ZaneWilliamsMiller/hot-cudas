import json, subprocess, os, sys
"""
Sync submodules in hot_cudas repo with upstream.
Run: python sync_submodules.py
Can be scheduled via cron/schtasks for automatic daily sync.
"""
TOKEN = os.environ.get("GH_TOKEN", "")
if not TOKEN:
    print("ERROR: Set GH_TOKEN env var")
    sys.exit(1)

OWNER = "ZaneWilliamsMiller"
REPO = "hot_cudas"

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
    r = api("GET", f"/repos/{owner_repo}")
    if isinstance(r, dict) and r.get("default_branch"):
        branch = r["default_branch"]
        r2 = api("GET", f"/repos/{owner_repo}/git/refs/heads/{branch}")
        if isinstance(r2, list) and len(r2) > 0:
            return r2[0]["object"]["sha"]
        elif isinstance(r2, dict) and r2.get("object", {}).get("sha"):
            return r2["object"]["sha"]
    return None

# Parse .gitmodules from repo
r = api("GET", f"/repos/{OWNER}/{REPO}/contents/.gitmodules")
import base64
gm_content = base64.b64decode(r["content"]).decode("utf-8")

submodules = []
current = {}
for line in gm_content.split("\n"):
    line = line.strip()
    if line.startswith("[submodule"):
        if current.get("url") and current.get("path"):
            path = current["path"]
            top_dir = path.split("/")[0]
            upstream = current["url"].replace("https://github.com/", "").rstrip(".git")
            submodules.append((upstream, top_dir, path))
        current = {}
    elif "=" in line:
        k, v = line.split("=", 1)
        current[k.strip()] = v.strip()
if current.get("url") and current.get("path"):
    path = current["path"]
    top_dir = path.split("/")[0]
    upstream = current["url"].replace("https://github.com/", "").rstrip(".git")
    submodules.append((upstream, top_dir, path))

print(f"Found {len(submodules)} submodules")

# Get current repo state
r = api("GET", f"/repos/{OWNER}/{REPO}/git/refs/heads/main")
main_sha = r["object"]["sha"]
r = api("GET", f"/repos/{OWNER}/{REPO}/git/commits/{main_sha}")
tree_sha = r["tree"]["sha"]
r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{tree_sha}")

old_subtrees = {}
for item in r["tree"]:
    if item["mode"] == "040000":
        old_subtrees[item["path"]] = item["sha"]

# Fetch upstream SHAs and update
updated = 0
new_subtree_shas = {}

for upstream, top_dir, full_path in submodules:
    new_sha = get_upstream_sha(upstream)
    if not new_sha:
        print(f"  SKIP: {upstream}")
        if top_dir in old_subtrees:
            new_subtree_shas[top_dir] = old_subtrees[top_dir]
        continue

    sub_tree_sha = old_subtrees.get(top_dir)
    if not sub_tree_sha:
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
r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{tree_sha}")
for item in r["tree"]:
    if item["mode"] == "040000" and item["path"] in new_subtree_shas:
        root_entries.append({"path": item["path"], "mode": "040000", "type": "tree", "sha": new_subtree_shas[item["path"]]})
    elif item["mode"] != "040000":
        root_entries.append(item)

new_tree = api("POST", f"/repos/{OWNER}/{REPO}/git/trees", {"tree": root_entries})
new_commit = api("POST", f"/repos/{OWNER}/{REPO}/git/commits", {
    "message": f"chore: sync {updated} submodules with upstream",
    "tree": new_tree["sha"],
    "parents": [main_sha]
})

commit_sha = new_commit["sha"]
r = api("PATCH", f"/repos/{OWNER}/{REPO}/git/refs/heads/main", {"sha": commit_sha})
result_sha = r.get("object", {}).get("sha", "")
if result_sha == commit_sha:
    print(f"DONE! Synced {updated} submodules. Commit: {commit_sha[:10]}")
else:
    err_msg = r.get("message", json.dumps(r)[:200])
    print(f"ERROR updating ref: {err_msg}")
