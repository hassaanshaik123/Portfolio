# Portfolio interaction revision — 31 October 2026

## Evidence and scope

The supplied 107.08-second MOV shows the Oorja Kapoor reference site, not the first Hassaan build. It was decoded locally at two frames per second (214 frames), with representative sequence review across 0–106.5s and closer inspection around the zoom, trail selection, accordion and portrait transitions. The audio was extracted and processed locally; speech was faint and did not produce reliable instructions. The user explicitly confirmed: **“Follow the demonstrated interactions.”**

The original recording, extracted frames, audio and automatic transcripts remain local under the ignored `output/recording-review/` and `riffrec-feedback/` directories. They are excluded from the Site source and deployment. No recording or audio was uploaded for transcription.

### Observations

| Evidence | Recording time | Observed behavior |
| --- | --- | --- |
| V01 | 00:00–00:08, 00:48–00:58, 01:16–01:22, 01:30–01:44 | Close-up character scene pulls back to a full mountain. Text appears at left. Bright grain/pixelated light washes across the transition. Reverse navigation returns to the close-up. |
| V02 | 00:08–00:25 | Dashed trail has four interactive square stops. Hover creates a star/label and updates the floating destination card. |
| V03 | 00:26–00:46 | Numbered project rows expand/collapse. The active row shows its description, orange CTA, and horizontal media strip. Collapsed rows remain compact. |
| V04 | 00:59–01:14 | Human uses a full-height portrait beside biography text, an overlapping orange cloud, photo dots, and cycling images with a block dissolve. |
| V05 | 01:22–01:29 | Resume opens a separate destination. The user has not supplied their own resume URL, so their version must remain visibly pending. |
| V06 | 00:48, 01:15, 01:30 | Returning to the mountain preserves a coherent route into the scene, rather than an unrelated marketing section. |

### REA inspection

The skill was applied through the installed REA CLI to the reference site's publicly served JavaScript/CSS captured in `output/reference-runtime/`. The complete captured artifact digest is `8f1caef580be339de9386806d4355704394bae07630855c1872901776189ae5d`.

REA returned partial observation **`ev_0a9a847c272dc16286d5e0c28ee1cfe2e0bb85ab2e2d1d2cc7971d247728cddc`**. Several sources, including the scene bundle, were processed before a framework/vendor source (`3rxl-jt3pdxgx.js`) reached the provider's 300-second per-source timeout. Its result explicitly states that graph coverage is incomplete and that scripts were parsed as inert text, not executed. This is **not** a claim of complete reverse engineering. The retained result is local at `/tmp/portfolio-rea-evidence-complete.json`.

Direct inspection of the captured scene bundle `39p4b58e-0ajf.js` found separate sky, mountain and character textures; viewport-dependent world geometry; a shader that composites layers with grain/light effects; and labeled trail points. This corroborates the visual reconstruction approach. It does not establish exact timing or global equivalence.

## Requirements implemented

- R01 / V01: Make the mountain scene the full homepage. Remove the previous extra intro/path sections below it.
- R02 / V01: Replace the single-image pan with independently composited sky, mountain, character and foreground layers. Use a real pull-back with a grain/light transition, reversible through normal scrolling.
- R03 / V02: Add four trail destinations, hover/focus labels and star states, and a matching destination card. Use Work, About, Experience and Resume, preserving the user's instruction to omit Play.
- R04 / V03: Make project rows expandable, with one active gallery, compact inactive rows, a visible project CTA, horizontal dragging/swiping, and keyboard/arrow controls.
- R05 / V04: Add automatic portrait cycling, manual dots/next-photo control, block-dissolve transitions, an orange cloud and the split biography layout.
- R06 / V05: Keep Resume clearly marked “Coming soon”; do not invent a URL or attach the private dossier as a public resume.
- R07: Preserve all supplied identity, education, project and venture facts. Keep the academic/diagnostic nature of the work clear; do not invent decks or measured outcomes.
- R08: Adapt the overview for small screens, preserve keyboard navigation, suppress invisible interactive controls until revealed, and provide reduced-motion behavior.

## Implementation surfaces

- `js/main.js`: homepage layer markup and trail, destination card, expandable project markup, horizontal gallery content, portrait controls.
- `js/interactions.js`: scene geometry and rendering, WebGL light/grain compositing with DOM fallback, trail selection, project expansion/dragging/arrows, portrait cycling/dissolve.
- `css/styles.css`: scene framing, small-screen geometry, typography, hover/focus states, gallery transitions and portrait composition.
- `scripts/build-site.mjs`: packages only selected website assets and all nine routes.

## Generated scene assets

The built-in image-generation tool was used with the user's supplied illustration as the edit/style reference. The original file remains unchanged. All project-bound outputs were copied into the workspace and optimized to WebP with transparency preserved:

- `/Users/muhammadhassaan/Documents/GitHub/Portfolio/assets/scene-trio.webp`
- `/Users/muhammadhassaan/Documents/GitHub/Portfolio/assets/scene-mountain.webp`
- `/Users/muhammadhassaan/Documents/GitHub/Portfolio/assets/scene-sky.webp`
- `/Users/muhammadhassaan/Documents/GitHub/Portfolio/assets/scene-ledge.webp`
- `/Users/muhammadhassaan/Documents/GitHub/Portfolio/assets/scene-cloud.webp`

Prompt briefs: isolate the same man/lion/cub on transparency; create an isolated tall sunset-lit rocky mountain matching the illustration; reconstruct a wide sky-only backplate; isolate a broad nearly level rocky ledge for the opening foreground; and create one organically edged orange sunset cloud on transparency. All prompts prohibited text and unrelated subjects. No CLI image-generation fallback was used.

Instrument Serif is an open-source display-font substitute, not the reference's exact Awesome Serif font. Its license is retained in `assets/fonts/InstrumentSerif-OFL.txt`.

## Limits

This is a reconstruction of the demonstrated interaction language with personalized artwork and content. It is not a pixel-identical copy of the original artist's illustrations or transition timings. The recording shows desktop behavior; mobile geometry and touch controls are implementation choices. Full project decks and a resume URL are still not supplied.

## Verification

Browser checks covered the close-up and completed mountain overview, the reveal control, keyboard focus updating the destination card, trail-to-Human navigation, one-open-at-a-time project expansion, horizontal gallery arrows, completed manual portrait selection, mobile gallery controls, and all nine page routes. At 390px all routes had no document-level horizontal overflow or broken loaded images. Browser console errors were absent in the checked flows. Reduced-motion branches and WebGL failure fallback were inspected in source; no OS accessibility preference was changed for testing.

Project slides summarize the supplied analysis scope with typographic graphics; they are not fabricated screenshots of decks that have not been provided.

## Publication

Published successfully to the existing private Site: https://muhammad-hassaan-portfolio.goldmoon1.chatgpt.site

Source commit: `8508e79c2651a56630c603d03869ca848173f2fd`. Deployment: `appgdep_6ae5e157f3908191959e322bcc279a65`.
