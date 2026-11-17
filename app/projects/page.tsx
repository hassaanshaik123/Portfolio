import type { Metadata } from "next";
import Link from "next/link";
import { Reveal } from "@/components/motion";
import { ProjectGrid } from "@/components/project-grid";
export const metadata: Metadata = {
  title: "Projects",
  description:
    "Explore SoundBuddy, Clario AI, Buildsy and LYVO, product and business experiments by Muhammad Hassaan.",
};
export default function ProjectsPage() {
  return (
    <main id="main" className="projects-page container">
      <Reveal>
        <Link className="back-home" href="/">
          ← Back to home
        </Link>
      </Reveal>
      <Reveal as="h1" direction="down" delay={0.1}>
        Things I’ve been <em>building.</em>
      </Reveal>
      <Reveal as="p" className="projects-lead" delay={0.2}>
        A closer look at the products, the problems behind them and my part in
        the work.
      </Reveal>
      <ProjectGrid />
      <Reveal as="footer" className="project-footer">
        <Link href="/">Muhammad Hassaan</Link>
        <Link href="/#connect">Let’s connect ↗</Link>
      </Reveal>
    </main>
  );
}
