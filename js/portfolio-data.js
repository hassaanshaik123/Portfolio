/**
 * Muhammad Hassaan — Portfolio Data Configuration
 * Centralized data store for all projects, MVPs, decks, resume, and social links.
 * Strictly factual data — no invented metrics or claims.
 */

const PORTFOLIO_DATA = {
  profile: {
    name: "Muhammad Hassaan",
    title: "Business Developer",
    specialization: "B2B Sales | Consultative Selling",
    location: "New Delhi, India",
    education: "MBA, Masters' Union School of Business",
    heroHeading: "Turning Problems into tailored Solutions that get closed.",
    heroSubheading: "Business Developer · B2B Sales | Consultative Selling",
    locationBadge: "New Delhi, India"
  },

  navigation: [
    { id: "work", label: "Work", index: "01" },
    { id: "about", label: "About Me", index: "02" },
    { id: "ideas", label: "Ideas & MVP", index: "03" },
    { id: "mentorship", label: "Mentorship", index: "04" },
    { id: "resume", label: "Resume", index: "05" },
    { id: "connect", label: "Connect", index: "06" }
  ],

  // Category A: Entrepreneurship Experiments
  entrepreneurship: [
    {
      id: "stroque",
      number: "001",
      title: "Stroque Consulting",
      category: "Human Consulting Firm",
      role: "Founder & Senior Handwriting Analyst",
      duration: "November 2022 – Present",
      cardHighlight: "$26K+ Revenue",
      description: "Helps individuals improve their personal and professional lives through handwriting analysis, personalized consultations, and Grapho-Therapy.",
      metrics: [
        { value: "$26,000+", label: "Total Revenue" },
        { value: "300+", label: "People Helped" },
        { value: "250+", label: "Consultation Calls" },
        { value: "130+", label: "Supported via Grapho-Therapy" }
      ],
      modal: {
        overview: "Stroque Consulting is a human consulting venture founded on the intersection of handwriting psychology and personalized growth advisory. The firm helps individuals overcome behavioral blocks, improve leadership traits, and refine personal and professional habits through targeted Grapho-Therapy and in-depth diagnostic consultations.",
        problem: "Traditional coaching and self-improvement frameworks often apply generalized templates that ignore individual subconscious behavioral patterns. Clients struggle to pinpoint the root cognitive or emotional friction holding back their executive presence, communication, and decision-making.",
        responsibilities: [
          "End-to-end founder responsibilities spanning client acquisition, consultative sales, and diagnostic delivery.",
          "Conducted 250+ 1-on-1 diagnostic consultation calls translating handwriting analysis into actionable growth plans.",
          "Designed and administered tailored Grapho-Therapy exercises for over 130 individuals.",
          "Managed revenue operations, client onboarding, referrals, and long-term engagement retention."
        ],
        approach: "Consultative, diagnostic-first client engagement. Rather than hard-selling standardized packages, every engagement began with a sample assessment highlighting unaddressed friction points, demonstrating tangible diagnostic value before recommending personalized Grapho-Therapy regimens.",
        results: "Grew the venture to over $26,000 in revenue through high-trust consultative selling and word-of-mouth referrals, delivering measurable habit transformation across 300+ clients."
      }
    },
    {
      id: "hustlers-edge",
      number: "002",
      title: "Hustlers' Edge",
      category: "Skill Development Community",
      role: "Founder & Community Lead",
      duration: "August 2024 – April 2026",
      cardHighlight: "140+ Earners",
      description: "Helped final-year undergraduate students and early-career professionals from Tier 2 and Tier 3 markets learn in-demand skills and monetize them.",
      metrics: [
        { value: "140+", label: "Five-Figure Earners (INR)" },
        { value: "200+", label: "Community Members" },
        { value: "Tier 2 & 3", label: "Focus Demographic" },
        { value: "0 to 1", label: "Ecosystem Builder" }
      ],
      modal: {
        overview: "Hustlers' Edge was initiated to bridge the severe opportunity and monetization divide faced by ambitious college students and early-career talent outside metropolitan hubs. The community paired practical modern skill acquisition with direct freelancing and consultative sales pipelines.",
        problem: "Students in Tier 2 and Tier 3 markets receive theoretical education with almost zero real-world sales, outreach, or digital monetization training. Despite having drive, they lack structured guidance on how to land paying clients, price their skills, and close commercial projects.",
        responsibilities: [
          "Founded and scaled the community to 200+ active members across multiple regional clusters.",
          "Curated live playbooks on client outreach, consultative pitching, cold outreach, and negotiation.",
          "Mentored members individually to audit portfolios, review outbound pitches, and handle client objections.",
          "Built peer accountability systems that tracked weekly revenue milestones and project delivery."
        ],
        approach: "Action-oriented mentorship driven by real deliverables. Community members were trained on identifying market needs, packaging niche offerings, executing consultative outreach, and closing client contracts with structured pricing frameworks.",
        results: "Guided 140+ individuals from zero digital income to generating consistent five-figure monthly incomes in INR, establishing an enduring peer network of self-sustaining earners."
      }
    },
    {
      id: "idigitalpreneur",
      number: "003",
      title: "Idigitalpreneur Pvt. Ltd.",
      category: "EdTech / Affiliate Business Development",
      role: "Business Development — Affiliate",
      duration: "February 2023 – April 2024",
      cardHighlight: "30% Sales Efficiency Improvement",
      description: "Managed cold outreach, customer objections, and end-to-end sales activities.",
      metrics: [
        { value: "30%", label: "Sales Efficiency Improvement" },
        { value: "~$2,000", label: "Closed Inbound Deals" },
        { value: "$60", label: "Average Ticket Size" },
        { value: "20+", label: "Sales Reps Trained" }
      ],
      modal: {
        overview: "Executed core business development and consultative sales within an EdTech ecosystem, handling outbound prospecting, inbound discovery pipelines, objection handling, and sales team enablement.",
        problem: "Prospective learners were hesitant to invest in self-paced skill programs due to low commitment trust and lack of personalized curriculum guidance, resulting in friction during inbound conversion calls.",
        responsibilities: [
          "Executed high-volume cold outreach and handled inbound discovery conversations end-to-end.",
          "Navigated complex buyer objections regarding price, time commitment, and outcome credibility.",
          "Trained 20+ junior sales representatives in consultative selling techniques and objection reframing.",
          "Audited sales pipeline data to identify drop-off triggers and streamline conversion workflows."
        ],
        approach: "Replaced scripted hard-selling with consultative active listening. By mapping prospect career pain points to tailored modular learning paths, conversations shifted from price defense to return-on-investment alignment.",
        results: "Closed approximately $2,000 in inbound sales deals ($60 average ticket size), trained 20+ sales peers, and drove a documented 30% improvement in team-wide sales efficiency."
      }
    }
  ],

  // Category B: Academic Projects (Decks)
  academicProjects: [
    {
      id: "bharti-airtel",
      number: "004",
      title: "Bharti Airtel Growth Strategy",
      subtitle: "Business Strategy",
      deckUrl: null, // Editable placeholder — set to null until supplied
      description: "Strategic growth and market expansion analysis formulating competitive vectors for telecom and enterprise digital offerings."
    },
    {
      id: "ownwise",
      number: "005",
      title: "Ownwise",
      subtitle: "Decoding Business Models II",
      deckUrl: null,
      description: "Comprehensive breakdown of business model mechanics, unit economics, value chain positioning, and moat sustainability."
    },
    {
      id: "stride",
      number: "006",
      title: "Stride",
      subtitle: "Decoding Business Models II",
      deckUrl: null,
      description: "Deconstruction of platform monetization, customer acquisition cost vs. lifetime value dynamics, and scalable network effects."
    }
  ],

  // Category C: Business Problems (Decks)
  businessProblems: [
    {
      id: "gostops",
      number: "007",
      title: "GoSTOPS",
      subtitle: "Business Problem Analysis",
      deckUrl: null,
      description: "In-depth diagnostic examining operational hospitality bottlenecks, traveler touchpoints, and revenue optimization opportunities."
    },
    {
      id: "pepperfry",
      number: "008",
      title: "Pepperfry",
      subtitle: "Business Problem Analysis",
      deckUrl: null,
      description: "Identification of post-purchase service friction and three strategic recommendations to elevate customer retention and sales."
    }
  ],

  // Section 8: Ideas & MVP
  startupIdeas: [
    {
      id: "clario",
      tag: "MVP 01",
      name: "Clario.AI",
      summary: "An AI-powered reading and listening assistant that simplifies long-form articles, case studies, and news into downloadable audio.",
      stage: "Early MVP / Phase 1 (Simplified English Audio)",
      modal: {
        tagline: "Simplifying dense long-form knowledge into intuitive audio notes.",
        whyStarted: "During my MBA at Masters' Union, I noticed that complex case studies were extremely time-consuming and difficult for students to digest. Further qualitative research indicated similar challenges among MBA students, UPSC aspirants, and professional readers struggling with reading fatigue.",
        problem: "High-stakes students and professionals encounter hundreds of pages of complex literature, policy papers, and industry cases weekly. Traditional text-to-speech tools sound robotic, preserve unnecessarily convoluted jargon, and lack conceptual summarization.",
        solution: "Clario.AI converts complex written material into simplified, plain-language explanations paired with downloadable, natural-sounding audio notes that can be listened to on-the-go.",
        stage: "Early MVP / Phase 1, initially focusing on simplified English audio with high comprehension fidelity.",
        roadmap: "Expanding into regional-language audio synthesis, contextual vocabulary pop-ups, and interactive podcast-style discussion summaries."
      }
    },
    {
      id: "lyvo",
      tag: "MVP 02",
      name: "LYVO",
      summary: "A conversational support marketplace connecting young people with life coaches.",
      stage: "Ideation completed; market research ongoing",
      modal: {
        tagline: "A safe, accessible space for young people to be heard and guided.",
        whyStarted: "My personal experience of loneliness and the difficulty of finding empathetic, non-judgmental listeners for everyday life struggles inspired me to explore a dedicated platform where young people could have supportive, structured conversations.",
        problem: "Young adults navigating career transitions, social isolation, and personal uncertainty frequently face an all-or-nothing dilemma: either suffer quietly or book clinical psychotherapy, which can feel intimidating, expensive, and misaligned for non-clinical personal guidance.",
        solution: "An accessible digital marketplace connecting young individuals with vetted life coaches for empathetic, conversational coaching, active listening, and habit guidance.",
        positioningNote: "LYVO is positioned strictly as conversational coaching, mentorship, and life support — not as a replacement for clinical psychiatric or professional mental healthcare.",
        stage: "Ideation completed; market research and coach qualification framework ongoing."
      }
    },
    {
      id: "buildsy",
      tag: "MVP 03",
      name: "Buildsy",
      summary: "An AI-powered tool-stack recommendation platform for first-time builders.",
      stage: "Market research completed; MVP development in progress",
      modal: {
        tagline: "The optimal, budget-conscious software stack for your exact venture.",
        whyStarted: "When building my first products, I struggled to select suitable tools, spent weeks evaluating conflicting software stacks, and wasted money on unnecessary enterprise subscriptions that didn't fit my stage.",
        problem: "First-time founders and non-technical entrepreneurs face cognitive overload from thousands of SaaS tools. They often overspend on bloated software before achieving validation, or choose incompatible architectures that require costly rebuilds later.",
        solution: "Buildsy analyzes a builder's idea, budget, technical skill level, and launch stage to recommend the leanest, most cost-effective tool stack tailored specifically to their roadmap.",
        stage: "Market research completed; MVP engine development in progress."
      }
    },
    {
      id: "raah",
      tag: "MVP 04",
      name: "RAAH.AI",
      summary: "An AI-powered career diagnostic platform evaluating career readiness across eight role tracks and five assessment dimensions.",
      stage: "Stage Not Yet Specified",
      modal: {
        tagline: "Comprehensive career readiness diagnostics and role alignment.",
        whyStarted: "I experienced firsthand the uncertainty of choosing a career trajectory and knowing whether my innate strengths genuinely suited a specific corporate or business role.",
        problem: "Students and young professionals often enter career tracks based on surface prestige rather than diagnostic fit, leading to mid-career misalignment, disengagement, and unaddressed competency gaps.",
        solution: "A diagnostic platform evaluating career readiness across 8 distinct role tracks and 5 multidimensional assessment vectors to identify natural strengths, blind spots, and concrete preparation roadmaps.",
        stage: "Stage not yet specified."
      }
    }
  ],

  // Section 11: Connect Links
  connectLinks: [
    {
      id: "instagram",
      platform: "Instagram",
      label: "@muhammadhassaan",
      url: null, // Awaiting user input
      icon: "instagram"
    },
    {
      id: "linkedin",
      platform: "LinkedIn",
      label: "Muhammad Hassaan",
      url: null, // Awaiting user input
      icon: "linkedin"
    },
    {
      id: "email",
      platform: "Email",
      label: "hassaanshaik.work@gmail.com",
      url: "mailto:hassaanshaik.work@gmail.com",
      icon: "mail"
    },
    {
      id: "topmate",
      platform: "Topmate",
      label: "Book a Session",
      url: null, // Awaiting user input
      icon: "calendar"
    },
    {
      id: "github",
      platform: "GitHub",
      label: "View Code",
      url: null, // Awaiting user input
      icon: "github"
    }
  ],

  // Resume status
  resume: {
    heading: "Resume",
    subheading: "A closer look at my experience.",
    buttonLabel: "View Resume",
    status: "coming-soon",
    fileUrl: null // Awaiting user PDF
  }
};

// Freeze data to prevent unintentional runtime mutations
Object.freeze(PORTFOLIO_DATA);
