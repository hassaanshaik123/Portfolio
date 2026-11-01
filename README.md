# Muhammad Hassaan — Portfolio

A static, responsive portfolio rebuilt around the interactions demonstrated in the supplied reference walkthrough. The site includes a layered scroll-driven mountain scene, interactive trail navigation, expanding horizontal project galleries, cycling portraits, Experience, and five analysis pages. No build dependencies or remote fonts are required.

## Build and preview

```sh
node scripts/build-site.mjs
python3 -m http.server 4173 --directory dist --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. Always serve `dist/` so direct project routes work.

## Update content

- `js/portfolio-data.js`: profile, links, five project summaries, venture experience and metrics.
- `js/main.js`: page layouts, menu, trail and gallery markup.
- `js/interactions.js`: scene geometry/WebGL transition, trail selection, gallery expansion/dragging/arrows, portrait cycling and dissolve.
- `css/styles.css`: visual system and responsive layouts.
- `assets/scene-*.webp`: generated scene layers derived from the supplied illustration; original hero artwork is preserved.
- `assets/fonts/InstrumentSerif-*`: locally hosted open-source display font and license.
- `docs/recording-feedback.md`: timestamped observations, requirements, REA coverage limits and asset-generation briefs.
- `assets/portraits/`: optimized portraits already available in the portfolio workspace.

Masters’ Union is used consistently, based on the supplied education details. Play is omitted. Resume is visibly marked coming soon until a URL is supplied. Project pages summarize the dossier; full decks and implementation results have not been supplied. Academic exercises and independent diagnostics are identified as such.

The original dossier and unrelated workspace assets are excluded from the deployment and sanitized Sites source checkout. Only explicitly selected website assets are copied by the build. `.openai/hosting.json` retains the private Sites identity.

## Verification

Checked all nine page routes, desktop/mobile scene states, trail focus/navigation, project expansion, horizontal gallery controls, portrait selection, and asset loading. Native dialog provides focus containment and Escape dismissal. Reduced-motion users receive a static revealed hero and manual portrait changes.
