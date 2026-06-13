# Research Digest — public archive

The published archive of the [Research Agent](https://github.com/chandraxdev/Agents)'s digests,
served as a static site via GitHub Pages.

- **Live site:** https://chandraxdev.github.io/digests/
- **RSS:** https://chandraxdev.github.io/digests/feed.xml

## What this is

A Jekyll site (built automatically by GitHub Pages). Each issue is a Markdown post in `_posts/`.
New issues are rendered from the research agent's newsletter output and pushed here; Pages rebuilds
on every push.

This repo contains **only the published digests** — no system code, no configuration, and no personal
data. The agent that produces them lives in a separate private repository.

## Layout

- `_posts/YYYY-MM-DD-<slug>.md` — one issue per file (Jekyll post with front matter).
- `index.md` — the home page (lists issues newest-first).
- `_config.yml` — site configuration (theme, feed).

## Local preview (optional)

```
gem install bundler jekyll
jekyll serve
```
