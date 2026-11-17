#!/usr/bin/env python3
"""Refresh only the existing numeric GitHub profile stats in the SVG artwork."""
import json
import os
import re
import urllib.request

OWNER = "saranghaeyong"
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def api_get(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "saranghaeyong-profile-updater",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)

def replace_text(svg, x, y, value):
    pattern = re.compile(
        rf'(<text\\b(?=[^>]*\\bx="{re.escape(str(x))}")'
        rf'(?=[^>]*\\by="{re.escape(str(y))}")[^>]*>).*?(</text>)',
        re.DOTALL,
    )
    updated, count = pattern.subn(lambda m: m.group(1) + str(value) + m.group(2), svg, count=1)
    if count != 1:
        raise RuntimeError(f"Could not find exactly one SVG text element at x={x}, y={y}")
    return updated

def main():
    user = api_get(f"{API}/users/{OWNER}")
    repositories = []
    page = 1
    while True:
        batch = api_get(f"{API}/users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        if not batch:
            break
        repositories.extend(batch)
        page += 1

    public_repo_count = len(repositories)
    total_stars = sum(int(item.get("stargazers_count", 0)) for item in repositories)
    followers = int(user.get("followers", 0))
    by_name = {item["name"].lower(): int(item.get("stargazers_count", 0)) for item in repositories}

    with open("hero.svg", encoding="utf-8") as file:
        hero = file.read()
    hero = replace_text(hero, 64, 358, public_repo_count)
    hero = replace_text(hero, 188, 358, total_stars)
    hero = replace_text(hero, 312, 358, followers)
    with open("hero.svg", "w", encoding="utf-8") as file:
        file.write(hero)

    with open("projects.svg", encoding="utf-8") as file:
        projects = file.read()
    featured = [
        (380, "SRNTV-Launcher"),
        (792, "3d-portfolio"),
        (1208, "OPEN-PORTFOLIO"),
    ]
    for x, name in featured:
        projects = replace_text(projects, x, 180, f"⭐ {by_name.get(name.lower(), 0)}")
    projects = replace_text(projects, 80, 324, public_repo_count)
    projects = replace_text(projects, 230, 324, total_stars)
    with open("projects.svg", "w", encoding="utf-8") as file:
        file.write(projects)

    print(
        f"Updated profile stats: {public_repo_count} public repositories, "
        f"{total_stars} stars, {followers} followers."
    )

if __name__ == "__main__":
    main()
