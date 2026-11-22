import { ProjectShortcuts } from "@/components/project-shortcuts";
import Image from "next/image";
import Link from "next/link";
import { Reveal } from "@/components/motion";
import { Experiments } from "@/components/experiments";
import { JourneyTimeline } from "@/components/journey-timeline";

export default function HomePage() {
  return (
    <main id="main">
      <section className="hero container" id="home">
        <Reveal className="hero-intro" as="div" direction="down" delay={0}>
          <span className="hello">Hello!</span>
          <h1>
            I’m <span>Hassaan.</span>
            <small>Sales &amp; Business Developer</small>
          </h1>
          <p className="hero-caption">
            Listen to the Problem • Tailor the Solution • Deliver the Value
          </p>
        </Reveal>
        <div className="hero-stage">
          <Reveal className="hero-proof" as="div" direction="up" delay={0.25}>
            <div>
              <strong>₹2L</strong>
              <span>EdTech sales closed</span>
            </div>
            <div>
              <strong>250+</strong>
              <span>Consultations done</span>
            </div>
          </Reveal>
          <Reveal
            className="portrait hero-portrait"
            as="div"
            direction="up"
            delay={0.15}
            parallax={20}
          >
            <div className="portrait-circle"></div>
            <Image
              src="/assets/hassaan-hero-suit.png"
              alt="Muhammad Hassaan in a black suit with his arms crossed"
              preload
              sizes="(max-width: 700px) 90vw, 42vw"
              width={1023}
              height={1537}
            />
          </Reveal>
          <Reveal
            className="hero-approach"
            as="div"
            direction="up"
            delay={0.35}
          >
            <p className="eyebrow">My approach</p>
            <p>
              Listen closely.
              <br />
              Understand the need.
              <br />
              Follow through.
            </p>
          </Reveal>
          <Reveal className="hero-actions" as="div" direction="up" delay={0.4}>
            <Link className="button" href="#experiments">
              Explore my work ↗
            </Link>
            <Link className="button outline" href="#connect">
              Let’s connect
            </Link>
          </Reveal>
        </div>
        <Link className="scroll-hint" href="#experiments">
          Scroll to explore ↓
        </Link>
      </section>
      <section
        className="experiments dark-panel section-space"
        id="experiments"
      >
        <Reveal className="section-heading" as="div" direction="up" delay={0}>
          <div>
            <p className="eyebrow">Learning by doing</p>
            <h2>
              My <em>Experiments</em>
            </h2>
          </div>
          <p>A few ideas I took into the real world.</p>
        </Reveal>
        <Experiments />
      </section>
      <section className="about container section-space" id="about">
        <p className="eyebrow">A little about me</p>
        <Reveal className="section-title" as="h2" direction="up" delay={0}>
          Curious about <em>people.</em>
          {" "}Driven to <em>build.</em>
        </Reveal>
        <div className="about-panel">
          <Reveal className="about-person" as="div" direction="up" delay={0.05}>
            <div className="portrait about-portrait">
              <div className="portrait-circle"></div>
              <Image
                src="/assets/hassaan-about-black-original.png"
                alt="Hassaan wearing a black T-shirt and glasses"
                sizes="(max-width: 700px) 220px, 330px"
                width={1440}
                height={1350}
              />
            </div>
            <h3>Muhammad Hassaan</h3>
            <p>MBA candidate · Masters’ Union</p>
          </Reveal>
          <Reveal className="about-copy" as="div" direction="up" delay={0.15}>
            <h3>Good sales starts with listening.</h3>
            <p>
              I’m Muhammad Hassaan, an MBA candidate at Masters’ Union with a
              focus on sales and business development.
            </p>
            <p>
              I enjoy understanding what people need, asking better questions,
              and helping them find a solution that fits.
            </p>
            <p>
              Through consulting, community building and EdTech sales, I’ve
              learned by starting things, speaking to customers and following
              through.
            </p>
            <div className="curiosity">
              <p className="eyebrow">What keeps me curious</p>
              <div className="pills">
                <span>People</span>
                <span>Business</span>
                <span>Building</span>
              </div>
            </div>
          </Reveal>
        <Reveal className="principles" as="div" direction="up" delay={0.1}>
          <div>
            <span>01</span>
            <h3>Listen first</h3>
            <p>Understand before recommending.</p>
          </div>
          <div>
            <span>02</span>
            <h3>Learn by doing</h3>
            <p>Turn ideas into practical experiments.</p>
          </div>
          <div>
            <span>03</span>
            <h3>Follow through</h3>
            <p>Stay involved beyond the first conversation.</p>
          </div>
        </Reveal>
        </div>
      </section>
      <JourneyTimeline />
      <section className="projects-intro container section-space" id="projects">
        <p className="eyebrow">My projects</p>
        <div className="project-intro-panel">
          <Reveal
            className="portrait project-portrait"
            as="div"
            direction="up"
            delay={0.1}
          >
            <div className="portrait-circle"></div>
            <Image
              src="/assets/hassaan-projects-blazer.png"
              alt="Hassaan wearing a gray blazer with his arms crossed"
              sizes="(max-width: 700px) 230px, 42vw"
              width={1292}
              height={1218}
            />
          </Reveal>
          <Reveal
            className="project-intro-copy"
            as="div"
            direction="up"
            delay={0.15}
          >
            <p className="eyebrow muted">Built while learning</p>
            <h2>
              Ideas I wanted to <em>try for real.</em>
            </h2>
            <p>
              At Masters’ Union, I’ve had the space to build things and take
              them to potential customers. These projects are where I’m learning
              what people want, how to reach them and what makes them buy.
            </p>
            <ProjectShortcuts />
            <Link className="button" href="/projects">
              Go through the projects ↗
            </Link>
          </Reveal>
        </div>
      </section>
      <section className="connect dark-panel section-space" id="connect">
        <p className="eyebrow">Connect with me</p>
        <Reveal className="connect-heading" as="div" direction="up" delay={0}>
          <h2>
            Let’s start with
            <br />
            <em>a conversation.</em>
          </h2>
          <p>
            Have a sales role in mind?
            <br />
            I’d love to hear about it.
          </p>
        </Reveal>
        <Reveal className="contact-box" as="div" direction="up" delay={0.1}>
          <a className="email-main" href="mailto:hassaanshaik.work@gmail.com">
            hassaanshaik.work@gmail.com <span>↗</span>
          </a>
          <div className="social-grid">
            <a
              href="https://www.linkedin.com/in/hassaan-shaik/"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span className="social-icon">in</span>LinkedIn <span>↗</span>
            </a>
            <a
              href="https://www.instagram.com/hassaan.builds/"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span className="social-icon" aria-hidden="true">
                <svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" focusable="false">
                  <rect x="3" y="3" width="18" height="18" rx="5" />
                  <circle cx="12" cy="12" r="4" />
                  <circle cx="17.5" cy="6.5" r="1" fill="var(--orange)" stroke="none" />
                </svg>
              </span>Instagram <span>↗</span>
            </a>
            <a href="mailto:hassaanshaik.work@gmail.com">
              <span className="social-icon">✉</span>Email <span>↗</span>
            </a>
          </div>
          <div className="resume-row">
            <a
              className="button"
              href="/assets/Muhammad-Hassaan-Resume.pdf"
            >
              Resume
            </a>
            <p>Sales &amp; Business Development</p>
          </div>
        </Reveal>
        <Reveal className="footer" as="footer" direction="up" delay={0.1}>
          <Link className="brand" href="#home">
            <span className="monogram">H</span>Muhammad Hassaan
          </Link>
          <p>© 2026 Muhammad Hassaan</p>
          <Link href="#home">Back to top ↑</Link>
        </Reveal>
      </section>
    </main>
  );
}
