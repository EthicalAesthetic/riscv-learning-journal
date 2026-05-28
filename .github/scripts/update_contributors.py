"""
Fetches all merged PR authors from GitHub API and rewrites
the contributors table in README.md between the marker comments.
"""

import os
import re
import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO         = os.environ["REPO"]          # e.g. "your-username/riscv-learning-journal"
README_PATH  = "README.md"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

START_MARKER = "<!-- ALL-CONTRIBUTORS-LIST:START -->"
END_MARKER   = "<!-- ALL-CONTRIBUTORS-LIST:END -->"


def get_merged_pr_authors() -> list[dict]:
    """Return unique contributors from all merged PRs, sorted by first contribution."""
    url = f"https://api.github.com/repos/{REPO}/pulls"
    params = {"state": "closed", "per_page": 100, "page": 1}
    seen    = {}   # login -> contributor dict (keeps first occurrence)

    while True:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        pulls = resp.json()
        if not pulls:
            break

        for pr in pulls:
            # skip unmerged PRs and bot accounts
            if not pr.get("merged_at"):
                continue
            user = pr.get("user", {})
            login = user.get("login", "")
            if not login or "[bot]" in login:
                continue
            if login not in seen:
                seen[login] = {
                    "login":      login,
                    "avatar_url": user.get("avatar_url", ""),
                    "html_url":   user.get("html_url", f"https://github.com/{login}"),
                    "pr_title":   pr.get("title", ""),
                    "merged_at":  pr.get("merged_at", ""),
                }

        # check if there's a next page
        link_header = resp.headers.get("Link", "")
        if 'rel="next"' not in link_header:
            break
        params["page"] += 1

    # sort by merge date so earliest contributor appears first
    return sorted(seen.values(), key=lambda x: x["merged_at"])


def build_table(contributors: list[dict]) -> str:
    if not contributors:
        return (
            f"{START_MARKER}\n"
            "| Avatar | Name | First contribution |\n"
            "|--------|------|--------------------|\n"
            "| — | Be the first contributor — open a PR! | — |\n"
            f"{END_MARKER}"
        )

    rows = [
        "| Avatar | Name | First contribution |",
        "|--------|------|--------------------|",
    ]
    for c in contributors:
        avatar = f'<img src="{c["avatar_url"]}&s=40" width="40" height="40" alt="{c["login"]}">'
        name   = f'[{c["login"]}]({c["html_url"]})'
        pr     = c["pr_title"][:60] + ("…" if len(c["pr_title"]) > 60 else "")
        rows.append(f"| {avatar} | {name} | {pr} |")

    table_body = "\n".join(rows)
    return f"{START_MARKER}\n{table_body}\n{END_MARKER}"


def update_readme(new_block: str) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )

    if not pattern.search(content):
        print("ERROR: contributor markers not found in README.md")
        print(f"Make sure README.md contains:\n  {START_MARKER}\n  {END_MARKER}")
        raise SystemExit(1)

    updated = pattern.sub(new_block, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"README.md updated with {new_block.count('|') // 4} contributor(s).")


if __name__ == "__main__":
    contributors = get_merged_pr_authors()
    print(f"Found {len(contributors)} unique contributor(s).")
    table = build_table(contributors)
    update_readme(table)
