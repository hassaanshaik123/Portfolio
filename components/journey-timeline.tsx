"use client";

import { useState } from "react";
import { Dialog as DialogPrimitive } from "radix-ui";
import { X } from "lucide-react";
import TeamLanyardRail, { type LanyardMember } from "@/components/ui/team-lanyard-rail";

const entries = [
  { id: "stroque", name: "Stroque Consulting", role: "Founder & Handwriting Analyst", date: "Nov 2022 to present", image: "/assets/journey/Stroque-logo.jpg", details: ["Founded a consulting practice serving 250+ paying clients, generating approximately ₹19.5 lakh in cumulative revenue since early 2023.", "Led discovery conversations to understand personal and professional goals, then tailored handwriting assessments and follow-on packages to client needs.", "Secured a three-month C-suite engagement at ₹30,000 per month."] },
  { id: "soundbuddy", name: "SoundBuddy", role: "Product Growth & Sales Contributor", date: "Nov 2026 to present", image: "/assets/journey/soundbuddy-logo.png", details: ["Pioneered shared listening to expand SoundBuddy’s market reach.", "Contributed to a 125% increase in customer acquisition following the shared-listening launch.", "Used warm-network outreach to accelerate early revenue generation."] },
  { id: "7senses", name: "7 Senses", role: "Sales Growth and Strategy", date: "Jul 2026 to Sep 2026", image: "/assets/journey/7-senses.jpeg", details: ["Helped acquire 500+ customers in three months through organic content and in-store sales.", "Brought in 230+ customers at near-zero acquisition cost by promoting preorders through WhatsApp.", "Developed an impulse-buy strategy that reached 85+ buyers in a single day at an average order value of ₹380.", "Secured partnerships with four national suppliers, using shopper research and product testing to guide sourcing."] },
  { id: "masters-union", name: "Masters’ Union", role: "MBA Candidate", date: "2026 to present", image: "/assets/journey/masters-union.png", details: ["Pursuing an MBA in Technology & Business Management (YLC).", "Awarded the Pankaj Bansal Scholarship, placing among the top 8% of 500 students.", "Won Startup Weekend, placing first among 25 teams."] },
  { id: "hustlers", name: "Hustlers’ Edge", role: "Founder & Community Lead", date: "Aug 2024 to Apr 2026", image: "/assets/journey/hustlersedge-logo.jpg", details: ["Built a skill-based community of 200+ members through referrals, outreach and organic content, keeping acquisition cost near zero.", "Helped members develop prospecting, portfolio positioning, negotiation and client-closing skills.", "Tracked buyer pipelines in Odoo CRM and partnered with EdTech providers to connect members with relevant training."] },
  { id: "delhi", name: "University of Delhi", role: "Undergraduate", date: "2022 to 2025", image: "/assets/journey/university-of-delhi.png", details: ["Completed a BA in Economics and Political Science at Satyawati College (Evening), graduating with First Division and placing in the top 15% of the college.", "Founded and led the Entrepreneurship & Development Cell, growing it to 110+ students.", "Helped three student ventures secure ₹6 lakh in funding through the DU incubation ecosystem and delivered an entrepreneurship event for 200+ attendees."] },
  { id: "idp", name: "iDigitalpreneur", role: "Independent Sales Affiliate", date: "Feb 2023 to Apr 2024", image: "/assets/journey/idp-logo.jpg", details: ["Closed ₹2 lakh in EdTech sales and earned ₹60,000 in commissions, handling discovery, objections and follow-ups.", "Improved inbound conversion by 15% through consultative conversations and tailored follow-ups.", "Trained 20+ sales peers in consultative selling and buyer objection management."] },
];

const cards: LanyardMember[] = entries.map((entry) => ({ ...entry, team: entry.date, bio: entry.details[0], tone: 1 }));

export function JourneyTimeline() {
  const [selected, setSelected] = useState<number | null>(null);
  const entry = selected === null ? null : entries[selected];
  return (
    <section className="timeline container section-space journey-id-section" id="timeline">
      <p className="eyebrow">My timeline</p>
      <h2 className="section-title">My journey through <em>IDCards.</em></h2>
      <TeamLanyardRail items={cards} className="journey-id-rail" caption="Tap on the ID card to explore what I have done" onBadgeClick={setSelected} labels={{ flip: "Click or press Enter to explore this experience", back: "Explore this experience", show: "Show experience" }} />
      <DialogPrimitive.Root open={entry !== null} onOpenChange={(open) => { if (!open) setSelected(null); }}>
        <DialogPrimitive.Portal>
          <DialogPrimitive.Overlay className="journey-dialog-overlay" />
          <DialogPrimitive.Content className="journey-dialog">
            {entry && <>
              <div className="journey-dialog-header">
                {entry.image ? <img src={entry.image} alt={`${entry.name} logo`} /> : <span className="journey-lettermark" aria-hidden="true">{entry.id === "7senses" ? "7S" : "DU"}</span>}
                <div><p className="eyebrow">{entry.date}</p><DialogPrimitive.Title>{entry.name}</DialogPrimitive.Title><DialogPrimitive.Description>{entry.role}</DialogPrimitive.Description></div>
              </div>
              <ul>{entry.details.map((detail) => <li key={detail}>{detail}</li>)}</ul>
              <DialogPrimitive.Close className="journey-dialog-back">Back to my journey</DialogPrimitive.Close>
            </>}
            <DialogPrimitive.Close className="journey-dialog-close" aria-label="Close experience"><X size={22} /></DialogPrimitive.Close>
          </DialogPrimitive.Content>
        </DialogPrimitive.Portal>
      </DialogPrimitive.Root>
    </section>
  );
}
