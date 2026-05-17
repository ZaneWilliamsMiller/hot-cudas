import json, subprocess, os, sys, base64, platform
"""
Sync all submodules in hot_cudas repo with upstream latest HEAD.
Works on both Linux (GitHub Actions) and Windows (local).
Usage: GH_TOKEN=xxx python3 sync_submodules.py
"""

TOKEN = os.environ.get("GH_TOKEN", "")
if not TOKEN:
    print("ERROR: Set GH_TOKEN env var")
    sys.exit(1)

OWNER = "ZaneWilliamsMiller"
REPO = "hot_cudas"
CURL = "curl.exe" if platform.system() == "Windows" else "curl"

def api(method, endpoint, data=None):
    cmd = [CURL, "-s", "-X", method,
           "-H", f"Authorization: token {TOKEN}",
           "-H", "Content-Type: application/json",
           "-H", "Accept: application/vnd.github+json",
           "-H", "X-GitHub-Api-Version: 2022-11-28"]
    if data:
        cmd += ["-d", json.dumps(data)]
    cmd.append(f"https://api.github.com{endpoint}")
    r = subprocess.run(cmd, capture_output=True, timeout=30)
    try:
        return json.loads(r.stdout.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return {"error": r.stdout.decode("utf-8", errors="replace")[:200]}

def get_upstream_sha(owner_repo):
    """Get default branch HEAD SHA for a repo."""
    r = api("GET", f"/repos/{owner_repo}")
    if isinstance(r, dict) and r.get("default_branch"):
        branch = r["default_branch"]
        r2 = api("GET", f"/repos/{owner_repo}/commits/{branch}")
        if isinstance(r2, dict) and r2.get("sha"):
            return r2["sha"]
    # Fallback: try refs API
    for branch in ["main", "master"]:
        r2 = api("GET", f"/repos/{owner_repo}/git/refs/heads/{branch}")
        if isinstance(r2, list) and len(r2) > 0:
            return r2[0]["object"]["sha"]
        elif isinstance(r2, dict) and r2.get("object", {}).get("sha"):
            return r2["object"]["sha"]
    return None

# Try to read .gitmodules from local file first (when running inside checkout)
gm_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".gitmodules")
if os.path.exists(gm_path):
    with open(gm_path, "r", encoding="utf-8") as f:
        gm_content = f.read()
    print("Read .gitmodules from local file")
else:
    # Fallback to GitHub API
    r = api("GET", f"/repos/{OWNER}/{REPO}/contents/.gitmodules")
    if isinstance(r, dict) and r.get("content"):
        gm_content = base64.b64decode(r["content"]).decode("utf-8")
        print("Read .gitmodules from GitHub API")
    else:
        print(f"ERROR: Cannot read .gitmodules: {r.get('message', r.get('error', 'unknown'))}")
        sys.exit(1)

# Parse .gitmodules
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
# Last entry
if current.get("url") and current.get("path"):
    path = current["path"]
    top_dir = path.split("/")[0]
    upstream = current["url"].replace("https://github.com/", "").rstrip(".git")
    submodules.append((upstream, top_dir, path))

print(f"Found {len(submodules)} submodules")

# Get current repo state
r = api("GET", f"/repos/{OWNER}/{REPO}/git/refs/heads/main")
if not isinstance(r, dict) or not r.get("object", {}).get("sha"):
    print(f"ERROR: Cannot get main ref: {r}")
    sys.exit(1)
main_sha = r["object"]["sha"]

r = api("GET", f"/repos/{OWNER}/{REPO}/git/commits/{main_sha}")
tree_sha = r["tree"]["sha"]
r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{tree_sha}")

old_subtrees = {}
for item in r.get("tree", []):
    if item["mode"] == "040000":
        old_subtrees[item["path"]] = item["sha"]

# Fetch upstream SHAs and update subtrees
updated = 0
new_subtree_shas = {}

for upstream, top_dir, full_path in submodules:
    new_sha = get_upstream_sha(upstream)
    if not new_sha:
        print(f"  SKIP: {upstream} (cannot fetch)")
        if top_dir in old_subtrees:
            new_subtree_shas[top_dir] = old_subtrees[top_dir]
        continue

    sub_tree_sha = old_subtrees.get(top_dir)
    if not sub_tree_sha:
        print(f"  SKIP: {top_dir} (not in repo tree)")
        continue

    r = api("GET", f"/repos/{OWNER}/{REPO}/git/trees/{sub_tree_sha}")
    entries = r.get("tree", [])
    if not entries:
        print(f"  SKIP: {top_dir} (empty subtree)")
        new_subtree_shas[top_dir] = sub_tree_sha
        continue

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
        if r.get("sha"):
            new_subtree_shas[top_dir] = r["sha"]
            updated += 1
        else:
            print(f"  ERROR creating tree for {top_dir}: {r.get('message', 'unknown')}")
            new_subtree_shas[top_dir] = sub_tree_sha
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
if not new_tree.get("sha"):
    print(f"ERROR creating root tree: {new_tree}")
    sys.exit(1)

new_commit = api("POST", f"/repos/{OWNER}/{REPO}/git/commits", {
    "message": f"chore: sync {updated} submodules with upstream",
    "tree": new_tree["sha"],
    "parents": [main_sha]
})
commit_sha = new_commit.get("sha", "")
if not commit_sha:
    print(f"ERROR creating commit: {new_commit}")
    sys.exit(1)

r = api("PATCH", f"/repos/{OWNER}/{REPO}/git/refs/heads/main", {"sha": commit_sha})
result_sha = r.get("object", {}).get("sha", "")
if result_sha == commit_sha:
    print(f"DONE! Synced {updated} submodules. Commit: {commit_sha[:10]}")
else:
    err = r.get("message", json.dumps(r)[:200])
    print(f"ERROR updating ref: {err}")
    sys.exit(1)
