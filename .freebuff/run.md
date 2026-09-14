# Run doc — Muhammad Hassaan portfolio (static site)

## What this is
A dependency-free static site: plain HTML + one CSS file + one vanilla JS file.
No build step, no package manager, no env files. Serve the repo root over HTTP
and everything works (root-relative asset paths like `css/styles.css` require a
real HTTP server — opening `index.html` via `file://` will 404 the CSS/JS).

## How to reproduce artifacts
Nothing to reproduce — there are no build artifacts, env files, or installs.
`Assets/` (portrait + resume PDF) is committed content, not a generated artifact.

## How to run the server
From the repo root:

```bash
nohup python3 -m http.server 8473 --bind 127.0.0.1 > .freebuff/preview.log 2>&1 < /dev/null &
```

Then wait for `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8473/index.html`
to return `200` and register the preview with the server's pid.

- **Port:** 8473 (arbitrary free choice; the site has no default port of its own).
  If 8473 is taken, pick any free port — no config change needed since all
  asset paths are root-relative.
- **Pages:** index.html · projects.html · entrepreneurship.html · about.html ·
  resume.html · content.html · work-with-me.html
- **Theme:** light (milky white) by default; dark mode via the nav toggle,
  persisted in `localStorage['mh-theme']`.
- **Kill:** `lsof -t -i :8473 | xargs kill`
