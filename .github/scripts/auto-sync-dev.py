#!/usr/bin/env python3
"""
Auto-sync dev branch submodules to latest upstream.
Runs in GitHub Actions CI. Updates each submodule, reports changes, exits 0 even on partial failure.
"""
import subprocess, sys, os

REPO = os.getcwd()

# Submodules known to cause issues — skip them
SKIP = {
    'gocv/gocv',
    'tensorrt-llm/tensorrt-llm',
}

def run(cmd, timeout=180, cwd=None):
    """Run a command, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                          timeout=timeout, cwd=cwd or REPO)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, '', 'TIMEOUT'
    except Exception as e:
        return -2, '', str(e)

def main():
    # ── Get submodule list ──────────────────────────────
    code, stdout, _ = run(['git', 'submodule', 'status'])
    if code != 0:
        print(f'FATAL: git submodule status failed (code {code})', file=sys.stderr)
        sys.exit(1)

    all_subs = []
    shas_before = {}
    for line in stdout.split('\n'):
        parts = line.strip().split()
        if len(parts) >= 2:
            path = parts[1]
            sha = parts[0].lstrip('+').lstrip('-')
            all_subs.append(path)
            shas_before[path] = sha[:12]

    print(f'Total submodules: {len(all_subs)}')

    # ── Set up git identity ─────────────────────────────
    run(['git', 'config', 'user.name', 'github-actions[bot]'])
    run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'])

    # ── Update each submodule ───────────────────────────
    updated = []
    failed = []
    unchanged = 0

    for i, sub in enumerate(all_subs, 1):
        if sub in SKIP:
            unchanged += 1
            continue

        try:
            code, _, stderr = run(
                ['git', 'submodule', 'update', '--remote', '--checkout', sub],
                timeout=180
            )

            # Re-read SHA after update
            _, stdout2, _ = run(['git', 'submodule', 'status', sub])
            new_sha = stdout2.split()[0].lstrip('+').lstrip('-')[:12] if stdout2 else '?'
            old_sha = shas_before.get(sub, '?')[:12]

            if code == 0 and new_sha != old_sha:
                updated.append((sub, old_sha, new_sha))
                print(f'  [{i}/{len(all_subs)}] UPDATED {sub}: {old_sha} -> {new_sha}')
            elif code == 0:
                unchanged += 1
            else:
                err_msg = stderr[:120] if stderr else 'unknown'
                failed.append((sub, err_msg))
                print(f'  [{i}/{len(all_subs)}] FAILED {sub}: {err_msg}')
        except Exception as e:
            failed.append((sub, str(e)[:100]))
            print(f'  [{i}/{len(all_subs)}] ERROR {sub}: {e}')

    # ── Report ──────────────────────────────────────────
    print(f'\n=== SYNC RESULT ===')
    print(f'Updated:  {len(updated)}')
    print(f'Unchanged: {unchanged}')
    print(f'Failed:   {len(failed)}')
    for sub, new, old in updated:
        print(f'  {sub}: {new} -> {old}')
    for sub, err in failed:
        print(f'  {sub}: {err}')

    # ── Commit & push if changes ────────────────────────
    if updated:
        # Stage only the updated submodules (their paths in .git/modules/<path>/...)
        run(['git', 'add'] + [s[0] for s in updated])
        count = len(updated)
        msg = f'chore: auto-sync {count} submodule(s) to latest upstream (dev branch)'
        rc, _, _ = run(['git', 'commit', '-m', msg])
        if rc != 0:
            print(f'Commit returned {rc} — maybe no changes?')
            sys.exit(0)
        rc, _, _ = run(['git', 'push', 'origin', 'dev'], timeout=120)
        if rc != 0:
            print(f'WARNING: push returned {rc}')
            sys.exit(1)
        print(f'Pushed: {msg}')
    else:
        print('No changes to commit.')

    # Failures are non-fatal for the workflow — they just log
    sys.exit(0)

if __name__ == '__main__':
    main()