const experiments = [
  {
    id: "stroque",
    name: "Stroque Consulting",
    role: "Founder & Handwriting Analyst",
    date: "Nov 2022 to present",
    image: "assets/stroque.jpg",
    preview:
      "An impact-led consulting venture that taught me to listen, understand and build trust.",
    originTitle: "Why I started",
    origin:
      "I wanted to help people work through personal and professional challenges. A writing sample became my starting point for conversations about their goals.",
    work: "I led discovery conversations, introduced assessments through sample audits and tailored follow-up packages. One executive signed up for three months at ₹30,000 per month.",
    metrics: [
      ["250+", "Consultations done"],
      ["5", "HR partners"],
      ["20+", "Recruitment cases supported"],
    ],
    endTitle: "What comes next",
    end: "At Masters’ Union, I’m developing software to test and automate parts of the manual process I used with hiring teams.",
  },
  {
    id: "hustlers",
    name: "Hustlers’ Edge Community",
    role: "Founder & Community Lead",
    date: "Aug 2024 to Apr 2026",
    image: "assets/hustlers.jpg",
    preview:
      "A community helping students turn practical skills into their first income.",
    originTitle: "Why I started",
    origin:
      "I saw students looking for jobs without the skills employers wanted. I wanted to help them learn practical skills and earn from their work, even before finding a job.",
    work: "I grew the community through referrals, outreach and organic content. I guided members through prospecting, positioning their work, negotiating and finding their first paying clients.",
    metrics: [
      ["200+", "Community members"],
      ["140+", "People started earning five figures per month (INR)"],
      ["Near zero", "Acquisition cost"],
    ],
    endTitle: "What I learned",
    end: "Getting people to join was only the beginning. I also had to understand where they were stuck and help them take the next step towards finding a client.",
  },
  {
    id: "idp",
    name: "iDigitalpreneur",
    role: "Independent Sales Affiliate",
    date: "Feb 2023 to Apr 2024",
    image: "assets/idigitalpreneur.png",
    preview:
      "My first step into sales: discovery, real conversations and learning to close.",
    originTitle: "How it started",
    origin:
      "I wanted to try something in business, so I joined iDigitalpreneur as a sales affiliate. Talking to students about their goals gave me my first real experience of selling.",
    work: "Got exposure to consultative selling and raised inbound conversion by 15%. Also trained 20+ sales peers on consultative selling and handling objections.",
    metrics: [
      ["₹2L", "EdTech sales closed"],
      ["₹60K", "Sales commissions earned"],
      ["15%", "Improvement in inbound conversion"],
    ],
    endTitle: "What I learned",
    end: "I found that I enjoyed sales most when I understood what someone needed and could recommend something that fit. That experience shaped how I approach discovery conversations today.",
  },
];
const projects = [
  {
    id: "soundbuddy",
    name: "SoundBuddy",
    url: "https://soundbuddy.tech",
    category: "Mac audio app",
    preview:
      "Built a Mac audio app for product managers and then expanded to normal users.",
    role: "Product Growth & Sales Contributor",
    originTitle: "The starting point",
    origin:
      "SoundBuddy began as a Mac audio app for product managers. We explored shared listening as a way to make it useful to a wider group of Mac users.",
    work: "I helped identify shared listening as a growth opportunity and took the update to potential customers through warm-network outreach and automated Reddit messages.",
    endTitle: "My contribution",
    end: "My work focused on finding new uses for the product, reaching potential customers and contributing to early sales.",
  },
  {
    id: "clario",
    name: "Clario AI",
    category: "Audio learning concept",
    preview:
      "A concept for turning long articles into simpler audio notes in regional languages, for MBA students and UPSC aspirants.",
    note: "Articles to regional audio notes",
    originTitle: "The idea",
    origin:
      "Clario AI is a text-to-speech product concept for MBA students and UPSC aspirants who need to work through long articles.",
    work: "The concept combines regional-language audio notes with explanations in simple language. The existing project work covers product discovery, user research and the learning experience.",
    endTitle: "Current stage",
    end: "A product concept exploring how AI and text-to-speech can make long reading material easier to work through.",
  },
  {
    id: "buildsy",
    name: "Buildsy",
    category: "AI tool stack planner",
    preview:
      "Share an idea, answer six questions and get a tool stack shaped around your MVP and budget.",
    note: "Built for first-time and solo builders",
    originTitle: "The problem",
    origin:
      "First-time builders face a lot of tool choices before they can start an MVP. Buildsy helps them work out what they need and how it fits their budget.",
    work: "A builder shares an idea and answers six questions. Buildsy then puts together a personalized AI tool stack and budget allocation for building the first version.",
    endTitle: "Who it is for",
    end: "Solo builders and one-person companies looking for an affordable set of tools to get their idea off the ground.",
  },
  {
    id: "lyvo",
    name: "LYVO",
    category: "In development",
    preview:
      "An AI life coach experiment exploring how conversation can help people reflect, find direction and plan their next steps.",
    note: "Exploring conversational wellbeing",
    originTitle: "Why we started",
    origin:
      "We wanted to explore how conversation could help people who feel stuck reflect on what they are going through and find a sense of direction.",
    work: "We are developing an AI life coach and experimenting with conversations that help people describe their concerns and think through possible next steps.",
    endTitle: "Current stage",
    end: "LYVO is in development. We are still exploring the experience and what useful conversational support could look like.",
  },
];
const arrow = '<span aria-hidden="true">↗</span>';
const nav = document.querySelector("#site-nav");
const onProjects = document.body.dataset.page === "projects";
const home = onProjects ? "index.html" : "";
nav.innerHTML = `<a class="brand" href="index.html" aria-label="Hassaan home"><span class="monogram">H</span>Hassaan</a><button class="menu-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Open navigation"><span></span><span></span><span></span></button><div id="nav-links" class="nav-links">${[
  ["About", "about"],
  ["Experiments", "experiments"],
  ["Projects", "projects"],
  ["Timeline", "timeline"],
]
  .map(
    ([label, id]) =>
      `<a href="${onProjects && id === "projects" ? "projects.html" : home + "#" + id}"${onProjects && id === "projects" ? ' aria-current="page"' : ""}>${label}</a>`,
  )
  .join(
    "",
  )}<a class="button small" href="${home}#connect">Connect ${arrow}</a></div>`;
const themeToggle = document.createElement("button");
themeToggle.className = "theme-toggle";
themeToggle.type = "button";
nav.append(themeToggle);
const sunIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg>';
const moonIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M20.5 14A8.5 8.5 0 0 1 10 3.5 8.5 8.5 0 1 0 20.5 14Z"/></svg>';
function updateThemeToggle() {
  const dark = document.documentElement.dataset.theme === "dark";
  themeToggle.innerHTML = dark ? sunIcon : moonIcon;
  themeToggle.setAttribute("aria-label", dark ? "Switch to day mode" : "Switch to night mode");
  themeToggle.title = dark ? "Switch to day mode" : "Switch to night mode";
  themeToggle.setAttribute("aria-pressed", String(dark));
}
themeToggle.addEventListener("click", () => {
  const theme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  window.portfolioTheme.set(theme);
});
window.addEventListener("portfolio-theme-change", updateThemeToggle);
updateThemeToggle();
const menu = document.querySelector(".menu-toggle");
menu.addEventListener("click", () => {
  const open = menu.getAttribute("aria-expanded") !== "true";
  menu.setAttribute("aria-expanded", String(open));
  menu.setAttribute(
    "aria-label",
    open ? "Close navigation" : "Open navigation",
  );
  nav.classList.toggle("menu-open", open);
});
nav.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => {
    nav.classList.remove("menu-open");
    menu.setAttribute("aria-expanded", "false");
    menu.setAttribute("aria-label", "Open navigation");
  }),
);
const cards = document.querySelector("#experiment-cards");
if (cards)
  cards.innerHTML = experiments
    .map(
      (x, i) =>
        `<article class="experiment-card ${i === 1 ? "orange-card" : ""}"><h3>${i === 1 ? "Hustlers’ Edge" : x.name}</h3><p class="date">${x.date}</p><img src="${x.image}" alt="${x.name} logo" loading="lazy"><p>${x.preview}</p><button class="story-link" data-story="${x.id}"><span>The story<span class="sr-only"> of ${x.name}</span></span><span class="circle">↗</span></button></article>`,
    )
    .join("");
const grid = document.querySelector("#project-grid");
if (grid)
  grid.innerHTML = projects
    .map(
      (x) =>
        `<article class="project-card"><div class="project-art ${x.id}" aria-label="${x.name} temporary artwork"><span>${x.name}</span></div><div class="project-copy"><p class="eyebrow">${x.category}</p><h2>${x.name}</h2><p>${x.preview}</p><div class="project-bottom"><small>${x.role ? "My role: " + x.role : x.note}</small><button class="circle" data-story="${x.id}" aria-label="Read ${x.name} story">↗</button></div></div></article>`,
    )
    .join("");
const dialog = document.querySelector("#story-dialog");
const storyContent = document.querySelector("#story-content");
let storyTrigger;
function closeStory() {
  dialog.close();
}
document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-story]");
  if (!button) return;
  const x = [...experiments, ...projects].find(
    (item) => item.id === button.dataset.story,
  );
  storyTrigger = button;
  storyContent.innerHTML = `<header class="story-header">${x.image ? `<img src="${x.image}" alt="${x.name} logo">` : ""}<div><h2 id="story-title">${x.name}</h2><p>${x.role || x.category}</p>${x.url ? `<a class="button small" href="${x.url}" target="_blank" rel="noopener noreferrer">Visit ${x.name} ↗</a>` : ""}${x.date ? `<p class="story-date">${x.date}</p>` : ""}</div></header><div class="story-columns"><section><h3>${x.originTitle}</h3><p>${x.origin}</p></section><section><h3>What I did</h3><p>${x.work}</p></section></div>${x.metrics ? `<div class="story-metrics">${x.metrics.map(([n, t]) => `<div><strong>${n}</strong><span>${t}</span></div>`).join("")}</div>` : ""}<section class="story-ending"><h3>${x.endTitle}</h3><p>${x.end}</p></section><button class="back-story" type="button">Back to ${x.image ? "experiments" : "projects"}</button>`;
  dialog.showModal();
  dialog.scrollTop = 0;
  document.body.classList.add("dialog-open");
  storyContent
    .querySelector(".back-story")
    .addEventListener("click", closeStory);
});
document.querySelector(".close-dialog").addEventListener("click", closeStory);
dialog.addEventListener("click", (e) => {
  if (e.target === dialog) {
    const r = dialog.getBoundingClientRect();
    if (
      e.clientX < r.left ||
      e.clientX > r.right ||
      e.clientY < r.top ||
      e.clientY > r.bottom
    )
      closeStory();
  }
});
dialog.addEventListener("close", () => {
  document.body.classList.remove("dialog-open");
  storyTrigger?.focus();
});
// Reveal individual elements only after the opening screen has finished.
(() => {
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  document.querySelectorAll(".reveal").forEach(el => el.classList.add("is-visible"));
  if (reducedMotion.matches) return;
  const groups = [
    [".nav-wrap", "down", 0],
    [".hello", "down", 60],
    [".hero h1", "down", 140],
    [".hero-caption", "up", 240],
    [".hero-portrait", "portrait", 180],
    [".hero-proof > div", "up", 340],
    [".hero-approach", "up", 420],
    [".hero-actions", "up", 500],
    [".scroll-note", "up", 560],
    ["main > section:not(.hero) > .eyebrow, .section-title, .section-heading, .timeline-heading, .connect-heading", "up", 0],
    [".about-person", "portrait", 80],
    [".about-copy > *, .principles > div", "up", 80],
    [".experiment-card", "up", 60],
    [".milestone, .stroque-thread", "up", 60],
    [".project-portrait", "portrait", 80],
    [".project-intro-copy > *", "up", 80],
    [".email-main, .social-grid > a, .resume-row, .footer", "up", 60],
    [".back-home, .projects-page > h1, .projects-lead", "down", 60],
    [".project-card, .project-footer", "up", 80],
  ];
  groups.forEach(([selector, direction, delay]) => {
    document.querySelectorAll(selector).forEach((el, index) => {
      if (el.hasAttribute("data-motion") || el.parentElement.closest("[data-motion]")) return;
      el.dataset.motion = direction;
      el.style.setProperty("--motion-delay", `${delay + (index % 4) * 85}ms`);
    });
  });
  let started = false;
  function startMotion() {
    if (started) return;
    started = true;
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("motion-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -20px 0px" });
    document.querySelectorAll("[data-motion]").forEach(el => observer.observe(el));
  }
  if (document.documentElement.classList.contains("intro-pending")) {
    window.addEventListener("portfolio-intro-complete", startMotion, { once: true });
  } else startMotion();
})();
