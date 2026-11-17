import Link from "next/link";
import { Button } from "@/components/ui/button";
export default function NotFound() {
  return (
    <main
      id="main"
      className="container grid min-h-[65vh] place-content-center gap-6 text-center"
    >
      <p className="eyebrow">404</p>
      <h1 className="text-5xl">That page wandered off.</h1>
      <p className="text-[var(--muted)]">
        You can find my experience and projects back on the homepage.
      </p>
      <Button asChild className="button mx-auto">
        <Link href="/">Back to home ↗</Link>
      </Button>
    </main>
  );
}
