# Oorja Kapoor portfolio: reconstruction brief

Reference: https://oorjakapoor.com/ — inspected 31 October 2026.
Scope: research only; no portfolio implementation yet.

## Method and evidence boundary

Applied the reverse-engineer-anything skill's observation/inference/unknown distinction. No REA MCP tools were available. Its read-only doctor reported missing Codex registration and Node v26.8.2 outside the package's supported range. No configuration repair or Node upgrade was performed. The skill is available locally, but the actual REA engine was not used to inspect this site. Findings below come from live browser screenshots, accessibility trees, read-only DOM inspection, and tested UI controls. Evidence labels below are local observation references, not REA-issued Evidence IDs.

- B01: Homepage at initial 319×743 viewport: illustrated portrait hero, name, compass menu, headline and role/location.
- B02: Homepage at 1440×900 before and after scrolling: large character scene pulls back to reveal mountain, introduction, orange contact button, dotted climbing route, and floating destination card. An About card was visible in the final sampled state; Work text was present in the DOM in an earlier state.
- B03: Opened homepage menu: dark overlay/card, informal thank-you note, dog photo, Compass label, navigation, resume/social/contact links.
- B04: Work desktop screenshot, full DOM text and link inventory: four numbered project sections and image strips.
- B05: Human desktop/mobile screenshots and DOM: biography, three portrait controls, social/contact links. Clicking Photo 2 changes the displayed image.
- B06: Play desktop/mobile screenshots and all four opened overlays: artwork collection, tennis game preview/link, short-film player, cow scene-builder preview/link.
- B07: Dime screenshot, full text, typography measurements, image/tab inventory.
- B08: Clinikk full DOM text and heading inventory.
- B09: Magic Studio full DOM text and heading inventory.
- B10: Misc accessibility tree and carousel interaction: clicking the second tab changes its selected state.
- B11: Mobile Work screenshot and DOM at 390×844; Play collage and Human stacked layout at the same size.
- B12: Homepage script/style URLs and image paths read from DOM: /_next/static/chunks/, turbopack-named runtime chunk, local asset directories.

## Page map

| Route | Purpose | Main content |
| --- | --- | --- |
| `/` | Cinematic introduction | Character-and-dogs illustration, mountain, sky/clouds, fireflies, scroll reveal, headline, role/location, contact, destination cards |
| `/work` | Selected projects | Dime, Clinikk, Magic Studio, Misc; numbered summaries, image strips, project links |
| `/human` | Personal introduction | Three selectable portraits, personal headline, two bio paragraphs, social/contact links |
| `/play` | Creative experiments | Artwork, Dodge It, short film, Moo Street; cards open overlays |
| `/work/dime` | Finance brand/website case study | Intro, role, timeline, external project link, screen carousel, design rationale, brand system, palette, testimonial |
| `/work/clinikk` | Healthcare product case study | Intro, role, timeline, external link, screens, coverage/onboarding rationale, testimonial |
| `/work/teams-lbyb` | Magic Studio team headshots case study | Intro, role, timeline, screen gallery, zero-state discussion, before/after dashboard analysis, product impact |
| `/work/misc` | Branding collection | Intro, role, flexible timeline, six-screen carousel, three testimonials |

Evidence: B01–B11. These are the eight routes reached through the site's primary navigation and project links, not a proof that no other routes exist.

## Visual system

- Dark/black surfaces with warm cream text, vivid orange headings and CTA buttons, subtle divider lines, generous whitespace. Homepage uses blue/purple skies and orange clouds.
- Display type: computed family `awesomeSerif` with a fallback. Body: `Nunito Sans` with a fallback. These are observed family names; font files, license, and complete weight inventory were not inspected.
- Measured cream text: RGB 242,230,189 (`#F2E6BD`). Measured orange heading: RGB 235,68,0 (`#EB4400`). Do not assume every orange element uses the same token.
- Dime desktop: H1 64px, H2 48px, introductory/body paragraphs 18px; other text varies by context. Mobile Work H1 56px. These are samples, not a complete type scale.
- Expressive serif wordmark, large editorial headings, plain sans-serif supporting text, uppercase compact button labels and diagonal arrows.
- Rounded image cards and buttons; thin ruled grids around case-study metadata. Subtle texture/grain is visible in the scene and imagery.
- Work, Play and case studies share a large theatrical footer with an oversized closing wordmark, a short creator credit, and rights text.

Evidence: B02, B04–B11. Recreation should match proportions and visual hierarchy after inserting the user's actual content.

## Homepage scene and motion

Desktop begins with the illustrated person and dogs dominant on a rocky peak. Scrolling changes scene scale and composition: the mountain becomes visible, the character group becomes small near its summit, and the introduction/contact content appears at left. A dotted trail and destination card occupy the mountain region. Separate image layers were observed for characters, characters without feet, mountain, and fireflies.

Observed paths include `/assets-home/characters.webp`, `characters-nofeet.webp`, `mountain-hd-2x.webp`, `firefly.svg`, `frame.png`, `menu-mtn.webp`, and `floating-cloud-1.webp`.

On mobile the hero is composed vertically: name/menu at top, character artwork above a black fade, centered cream headline and role line below. It should be treated as a distinct responsive composition.

Evidence: B01–B03, B12. Layered parallax/scroll animation is a reasonable implementation inference. Exact animation library, easing, duration, scroll thresholds, destination-card sequence and click mechanics remain unverified.

## Shared navigation and contact

- Name link generally returns home; Human desktop emphasizes the image/bio layout instead of repeating the same name header.
- Compass button opens navigation. Interior desktop pages show the current page beside its icon; mobile condenses to the icon.
- Menu contains Work, Human, Play, external resume, Instagram, LinkedIn, and Contact. Interior menus also expose a mountain/home link.
- Menu combines a playful thank-you panel/photo with the navigation panel and orange contact strip. A Close control was observed on the mobile overlay.
- Contact is a `mailto:` link with a prefilled subject/body template, not an observed on-site contact form.
- Resume points to a Google Drive file. Resume and social destinations were inventoried but not opened.

Evidence: B01, B03–B06.

## Work and case studies

Desktop Work uses a large orange heading followed by four numbered rows. Each combines project name, short description and CTA, followed by a wide horizontal strip of project imagery. Mobile stacks the number/title, gallery and full-width CTA; do not assume a mobile accordion from the initially visible content, since no accordion control was established.

Case studies use a smaller header with home/name and Back to Work, a centered introductory column, role/timeline metadata, then media and editorial explanation. Dime and Clinikk expose external project links. Magic Studio and Misc do not show that same CTA in the inspected text.

| Project | Role | Timeline | Distinctive structure |
| --- | --- | --- | --- |
| Dime | Brand + Website design | 2 months | Five screen tabs, brand system, palette explanation, testimonial |
| Clinikk | Product + experience designer | 3 months | Four principal screen subjects, cognitive/accessibility context, onboarding explanation, testimonial |
| Magic Studio | Product + experience designer | 4 months | Team dashboard, zero state, invitation workflow, before/after product model and business rationale |
| Misc | Branding | Several years | Six screen tabs, collected identities, three testimonials |

The carousel control was tested on Misc: selecting tab two moves selection from tab one to tab two. Drag/swipe, looping, autoplay and keyboard behavior were not established. All four project pages were inspected, but every media frame and every scroll-triggered effect was not individually exercised.

Evidence: B04, B07–B11.

## Human

Desktop: large portrait area left, headline/body/social/contact column right, decorative cloud crossing the composition. Three dot buttons select portraits. Mobile: rounded portrait first, cloud accent, dot control, headline, divider, bio, then links farther down. Assets were observed under `/assets-about/` as `about1.jpg`, `about2.jpg`, `about3.jpg`.

Evidence: B05, B11.

## Play

Desktop has four cards in one row under a centered orange title. Mobile arranges tilted/overlapping cards in a collage over a faint grid, with orange glow near the footer.

- Artwork opens an overlay with a heading, brief introduction and ten image entries including posters, illustrations and animated-poster entries.
- Dodge It opens an overlay titled Grand Slam with a video preview, play/pause and mute controls, short description and external View Game link to `https://dodge-topaz.vercel.app/`.
- Short film opens a video overlay for The Daily Commute with playback and mute controls.
- Moo Street opens a video/description overlay and external View Game link to `https://moostreet.vercel.app/`.
- All four overlays expose a Close button. The external games were not opened, camera access was not requested, and hand tracking was not tested. Their implementation descriptions are claims presented by the site, not independently verified behavior.
- Video controls appeared, but duration initially read 0:00; full playback/loading was not verified.

Evidence: B06, B11.

## Technical assessment

Observed Next.js-style `/_next/static/chunks/` script and CSS URLs, plus a Turbopack-named runtime chunk. This strongly indicates a Next.js build. Source repository, framework version, hosting provider, backend, CMS and animation dependencies remain unknown. Do not describe this investigation as source recovery or decompilation.

Images are central to the design. Reproducing the layout alone will not reproduce its character: the personalized hero illustration, layered scene assets, portrait treatment, project mockups, artwork and previews need equivalents suited to the user.

## Inputs for the user's version

1. Display name, professional title, location, short headline and preferred email.
2. Bio, background/education, experience and personal tone.
3. Portraits and a preferred hero character/scene direction; any pets or personal motifs to include.
4. Selected projects: title, short description, role, timeline, process/problem/outcome, screenshots, live links, and testimonials if available.
5. Creative experiments/artwork/videos for Play, or the desired replacement content.
6. Resume file/link and social/profile URLs.

## Completion checklist

- Answered: primary route map, content inventory, core visual language, shared navigation/contact destinations, all four Play overlay types, case-study structures, responsive samples, observed stack signals.
- Partially answered: homepage motion choreography, project-gallery interaction range, complete spacing/font token system, every asset's intrinsic resolution, loading and video playback behavior.
- Unresolved: source/component architecture, exact breakpoints, animation dependencies/timings, reduced-motion behavior, keyboard/focus management, external game internals, backend/hosting.

Next step: use the user's details to implement a closely matched layout and interaction system, with personalized artwork/content. No application code has been created or changed during this research pass.
