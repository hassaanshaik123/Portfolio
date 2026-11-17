# Muhammad Hassaan’s portfolio

A Next.js App Router portfolio with TypeScript, Tailwind CSS, shadcn/ui (Radix), Motion and next-themes.

## Run locally

```sh
npm ci
npm run dev
```

Open http://127.0.0.1:3000. For a production check:

```sh
npm run typecheck
npm run build
npm start
```

With the local server running, `npm test` checks server-rendered content, both routes, legacy redirects, resume/portrait delivery and the 404 page. Set `BASE_URL` to test a different local port.

Webpack is selected explicitly because the local execution environment restricts the port used by Turbopack’s CSS worker. The application remains a standard Next.js deployment.

## Where to edit

- `app/page.tsx`: homepage sections and approved copy.
- `app/projects/page.tsx`: projects page at `/projects`.
- `lib/portfolio-data.ts`: experiment/project cards, stories and external project links.
- `components/ui`: official shadcn button, dialog and sheet components.
- `components/motion.tsx`: one-time scroll reveals, parallax and reading progress.
- `components/providers.tsx`: theme persistence and the opening morphing square.
- `app/globals.css`: Tailwind entry point, shadcn tokens and portfolio styling.
- `public/assets`: original portraits, company logos, local fonts and downloadable resume.

Legacy `/index.html` and `/projects.html` URLs redirect to the new routes. Local media/feedback folders from earlier work are outside the application and have not been changed.

## Motion and accessibility

Motion is limited to opacity and transforms: a layered hero entrance after the opening sequence, a spring-smoothed hero parallax, reading-progress bar, one-time viewport reveals, drawing timeline path, desktop pointer tilt and dialog/sheet transitions. Reduced-motion preferences disable parallax and the opening sequence; content stays readable. Mobile navigation and story dialogs use Radix focus trapping, Escape dismissal and focus restoration. Themes follow the device preference until a visitor explicitly chooses a theme.

No database or CMS is required for the current portfolio. Content is rendered on the server for fast initial delivery; interactive motion and controls hydrate on the client.

## Deployment

Vercel should detect **Next.js**, use `npm run build`, and use its default output settings (no static output directory override). The migration is local until explicitly approved for a Git push and production deployment.
