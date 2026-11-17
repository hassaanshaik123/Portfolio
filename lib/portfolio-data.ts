export interface Story {
  id: string;
  name: string;
  role?: string;
  date?: string;
  image?: string;
  category?: string;
  preview: string;
  originTitle: string;
  origin: string;
  work: string;
  metrics?: [string, string][];
  endTitle: string;
  end: string;
  note?: string;
  url?: string;
}

export const experiments: Story[] = [
  {
    id: "stroque",
    name: "Stroque Consulting",
    role: "Founder & Handwriting Analyst",
    date: "Nov 2022 to present",
    image: "/assets/stroque.jpg",
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
    image: "/assets/hustlers.jpg",
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
    image: "/assets/idigitalpreneur.png",
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

export const projects: Story[] = [
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
