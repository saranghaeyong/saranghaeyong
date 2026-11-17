# Deadpool Developer Profile — Setup Guide

This profile is fully configurable through **`profile-data.yml`**.  
No other file needs editing for normal customisation.

---

## Quick Start

1. Open `profile-data.yml` in any text editor to review/edit personal details.
2. Edit SVG files directly for visual changes beyond the data file.
3. Commit and push; badges and stats update automatically via GitHub Actions.

```bash
git add .
git commit -m "Update Deadpool profile"
git push
```

---

## What Each Section Controls

| Field | Where it appears |
|---|---|
| `display_name` | Hero banner name |
| `headline` | Hero banner tagline |
| `location` | About Me section |
| `education_*` | Education section |
| `languages` + `skills` + `frameworks` + `tools` | Tech sections (SVG badges) |
| `projects[*]` | Projects table rows |
| `email`, `linkedin`, `portfolio` | Contact links at the bottom |

---

## Adding a New Language or Skill

Inside `profile-data.yml`, append to the relevant list:

```yaml
languages:
  - name: Python
    color: "#3572A5"
```

```yaml
skills:
  - name: Python
    color: "#3572A5"
```

The README auto-regenerates from this file when pushed to `main`.

---

## Manual Image Updates

The README uses these SVG banners — edit them directly if you want
visual changes beyond the data file:

| File | Purpose |
|---|---|
| `hero.svg` | Main hero banner |
| `about.svg` | About-me card |
| `skills.svg` | Tech skills showcase |
| `projects.svg` | Projects highlights |
| `connect.svg` | Contact / social links |

All SVGs use the Deadpool colour palette:

- **Black** `#0d0d0d` / `#1a1a1a`
- **Red** `#e2383f` / `#ff2929` / `#c41e3a`
- **White** `#f0f0f0`
- **Dark Grey** `#2a2a2a` / `#3d3d3d`

---

## GitHub Actions Workflows

Two workflows keep dynamic content fresh:

1. **`github-snake.yml`** — Generates a snake animation from your contribution graph daily.
2. **`github-stats.yml`** — Fetches live stats and pins repositories on push.

Both run only on `main` and require no extra secrets.

---

## Publishing to Your Own Repository

When ready to go live:

```bash
# 1. Create a new repo on GitHub (public) with README init disabled.
# 2. Link it as origin:
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.git

# 3. Push everything:
git branch -M main
git push -u origin main --force
```

> ⚠️ Do **not** push to the original `Meghamittal0920` repository.

---

## Notes

- All statistics are pulled live from GitHub services — no fake numbers.
- The contribution-graph SVG updates automatically via GitHub Actions.
- Keep GIFs to a minimum; this profile prefers clean vector art.
- The backup of the original profile lives on branch `backup-before-deadpool`.
