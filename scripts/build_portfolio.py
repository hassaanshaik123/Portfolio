#!/usr/bin/env python3
"""
Builds js/main.js and index.html for Muhammad Hassaan's portfolio
using the exact compiled engine and layout of samaymaurya.com.
"""
import os

BASE_DIR = "/Users/muhammadhassaan/Documents/GitHub/Portfolio"
REF_JS = os.path.join(BASE_DIR, "scripts", "reference_runtime.js")
if not os.path.exists(REF_JS):
    REF_JS = "/tmp/samay.js"

with open(REF_JS, "r", encoding="utf-8") as f:
    src = f.read()

def replace_between(text, start_marker, end_marker, replacement):
    s = text.find(start_marker)
    e = text.find(end_marker)
    if s == -1 or e == -1 or e <= s:
        raise RuntimeError(f"Failed to find markers: {start_marker!r} ({s}) .. {end_marker!r} ({e})")
    return text[:s] + replacement + text[e:]

# ============================================================================
# SPLICE 1: LOADER (Ah)
# ============================================================================
SPLICE_1 = r"""wh=[.22,1,.36,1],Th=[.76,0,.24,1],Eh=[`h`,`a`,`s`,`s`,`a`,`a`,`n`],Dh=2.5,Oh=[{d:`M20 280H980`,delay:.05},{d:`M60 172H940`,delay:.16},{d:`M100 350H760`,delay:.28},{d:`M110 70V380`,delay:.2},{d:`M452 100V372`,delay:.32},{d:`M788 110V400`,delay:.44},{d:`M110 372L580 84`,delay:.38}],kh=[{x:22,y:272,text:`baseline`,delay:.5},{x:62,y:164,text:`x-height`,delay:.6},{x:102,y:342,text:`descender`,delay:.7}];function Ah(){let e=um(),[t,n]=(0,v.useState)(`wait`),r=(0,v.useRef)(null),i=(0,v.useRef)(null),[a,o]=(0,v.useState)({dotX:886,shift:0}),s=nm(0),c=am(s,e=>`${String(Math.round(e)).padStart(3,`0`)}%`);return(0,v.useEffect)(()=>(`scrollRestoration`in history&&(history.scrollRestoration=`manual`),window.scrollTo(0,0),document.documentElement.classList.add(`is-loading`),r.current=setInterval(()=>Vm()?.stop(),50),()=>{r.current&&clearInterval(r.current)}),[]),(0,v.useEffect)(()=>{let e=!1,t=()=>!e&&n(e=>e===`wait`?`draw`:e),r=setTimeout(t,700);return document.fonts?.ready.then(()=>{clearTimeout(r),t()}),()=>{e=!0,clearTimeout(r)}},[]),(0,v.useLayoutEffect)(()=>{if(t!==`draw`||!i.current)return;let e=i.current.getBBox(),n=e.x+e.width+22;o({dotX:n,shift:500-(e.x+n+30)/2})},[t]),(0,v.useEffect)(()=>{if(t!==`draw`)return;let r=Fm(s,100,{duration:e?.3:2.3,ease:[.4,0,.2,1]}),i=setTimeout(()=>{Ch.whoosh(),n(`done`)},e?500:Dh*1e3);return()=>{r.stop(),clearTimeout(i)}},[t,s,e]),(0,G.jsx)(cf,{onExitComplete:()=>{r.current&&clearInterval(r.current),r.current=null,document.documentElement.classList.remove(`is-loading`);let e=Vm();if(document.querySelector(`.case-overlay[open]`)){e?.stop();return}e?.start(),e?.scrollTo(0,{immediate:!0})},children:t!==`done`&&(0,G.jsxs)(K.div,{className:`loader`,role:`status`,"aria-label":`Loading Muhammad Hassaan's portfolio`,initial:{y:0},exit:e?{opacity:0,transition:{duration:.3}}:{y:`-100%`,transition:{duration:.9,ease:Th}},children:[(0,G.jsx)(`div`,{className:`loader-texture`,style:{backgroundImage:`url(${zm})`},"aria-hidden":!0}),(0,G.jsxs)(`div`,{className:`loader-corner loader-corner--tl`,children:[(0,G.jsx)(`span`,{children:`muhammad hassaan`}),(0,G.jsx)(`span`,{children:`listening closely, solving problems`})]}),(0,G.jsxs)(`div`,{className:`loader-corner loader-corner--tr`,children:[(0,G.jsx)(`span`,{children:`visitor no. 01`}),(0,G.jsx)(`span`,{children:`glad you dropped by`})]}),t===`draw`&&(0,G.jsx)(K.svg,{className:`loader-mark`,viewBox:`0 0 1000 420`,fill:`none`,"aria-hidden":!0,exit:{opacity:0,y:-40,transition:{duration:.5,ease:wh}},children:(0,G.jsxs)(`g`,{transform:`translate(${a.shift} 0)`,children:[(0,G.jsx)(`text`,{ref:i,x:`110`,y:`280`,className:`loader-word`,opacity:`0`,children:`hassaan`}),(0,G.jsxs)(`g`,{className:`loader-guides`,children:[Oh.map(e=>(0,G.jsx)(K.path,{d:e.d,initial:{pathLength:0,opacity:0},animate:{pathLength:1,opacity:[0,1,1,.4]},transition:{pathLength:{duration:.9,delay:e.delay,ease:wh},opacity:{duration:2.1,delay:e.delay,times:[0,.1,.65,1]}}},e.d)),(0,G.jsx)(K.circle,{cx:a.dotX,cy:`252`,r:`30`,initial:{pathLength:0},animate:{pathLength:1},transition:{duration:.8,delay:.55,ease:wh}})]}),kh.map(e=>(0,G.jsx)(K.text,{x:e.x,y:e.y,className:`loader-spec`,initial:{opacity:0},animate:{opacity:[0,1,1,.5]},transition:{duration:1.8,delay:e.delay,times:[0,.15,.7,1]},children:e.text},e.text)),(0,G.jsx)(K.text,{x:`110`,y:`280`,className:`loader-word loader-word--outline`,initial:{strokeDashoffset:1400,opacity:1},animate:{strokeDashoffset:0,opacity:[1,1,0]},transition:{strokeDashoffset:{duration:1.05,delay:.5,ease:`easeInOut`},opacity:{duration:1.8,delay:.5,times:[0,.8,1]}},children:`hassaan`}),(0,G.jsx)(`text`,{x:`110`,y:`280`,className:`loader-word`,children:Eh.map((e,t)=>(0,G.jsx)(K.tspan,{initial:{fillOpacity:0},animate:{fillOpacity:1},transition:{duration:.3,delay:1.2+t*.08,ease:`easeOut`},children:e},t))}),(0,G.jsx)(K.circle,{cx:a.dotX,cy:`252`,r:`25`,className:`loader-dot`,initial:{scale:0,y:-90},animate:{scale:1,y:0},transition:{type:`spring`,stiffness:420,damping:15,delay:1.8},style:{transformBox:`fill-box`,transformOrigin:`center`}})]})}),(0,G.jsx)(`div`,{className:`loader-corner loader-corner--bl`,children:(0,G.jsx)(K.span,{className:`loader-count`,children:c})}),(0,G.jsx)(`div`,{className:`loader-corner loader-corner--br`,children:(0,G.jsx)(`span`,{children:`entrepreneurship · consultative sales · growth`})})]},`loader`)})}"""

# ============================================================================
# SPLICE 2: ENTREPRENEURSHIP EXPERIMENTS & IDEATION/MVP DATA + CASE RENDERER
# ============================================================================
SPLICE_2 = r"""var Zh={
  "stroque-consulting":{
    id:`stroque-consulting`,
    role:`Co-Founder and Sr. Handwriting Analyst`,
    timeline:`November 2022 – Present`,
    summary:`Stroque Consulting is a human consulting firm that helps individuals improve their personalities and achieve their personal and professional goals through a science called Graphology, i.e., handwriting analysis.`,
    blocks:[
      {type:`stats`,items:[
        {value:`~300`,label:`Consultation calls completed`},
        {value:`250+`,label:`People positively impacted`},
        {value:`120+`,label:`Lives transformed via graphotherapy`},
        {value:`AI → B2B`,label:`Ongoing product expansion initiative`}
      ]},
      {type:`heading`,text:`Understanding People Through Graphology`},
      {type:`paragraph`,text:`Stroque Consulting is a human consulting firm that helps individuals improve their personalities and achieve their personal and professional goals through a science called Graphology, i.e., handwriting analysis.`},
      {type:`paragraph`,text:`Every consultation begins by listening closely to the individual, analyzing behavioural patterns reflected in their handwriting, and offering tailored guidance and structured graphotherapy exercises.`},
      {type:`heading`,text:`Impact & Achievements`},
      {type:`paragraph`,text:`Since November 2022, we have completed close to 300 one-on-one consultation calls, positively impacted 250+ individuals, and transformed 120+ people's lives through dedicated graphotherapy programs.`},
      {type:`heading`,text:`Current Business Expansion — AI for B2B`},
      {type:`paragraph`,text:`We are now exploring the integration of AI into Stroque Consulting to develop an additional product offering for B2B customers.`},
      {type:`paragraph`,text:`Our existing handwriting-analysis and graphotherapy services continue as our core offerings for individuals. AI is being explored as an additional product line—an ongoing product-development and business-expansion initiative designed to help us expand beyond individual-focused consulting and serve business customers.`}
    ]
  },
  "hustlers-edge":{
    id:`hustlers-edge`,
    role:`Founder and Community Lead`,
    timeline:`August 2024 – April 2026`,
    summary:`Hustlers' Edge is a skill-based community that helps final-year graduation students and early-career professionals learn market-demand skills, particularly marketing skills, and monetize them through agency or freelancing models.`,
    blocks:[
      {type:`stats`,items:[
        {value:`200+`,label:`Community members built from inception`},
        {value:`140+`,label:`Members generating 5-figure monthly incomes`},
        {value:`₹10,00,000`,label:`Total reported revenue`},
        {value:`₹5,000`,label:`Revenue retained per student (after training partner cost)`}
      ]},
      {type:`heading`,text:`Identifying the Opportunity & Student Needs`},
      {type:`paragraph`,text:`Hustlers' Edge was built from scratch after recognizing a clear gap among final-year graduation students and early-career professionals: the need to acquire practical, market-demand skills—especially marketing skills—and a clear pathway to monetize them.`},
      {type:`heading`,text:`Skill-Development & Monetization Model`},
      {type:`paragraph`,text:`We partnered with a third-party ed-tech firm to train our students in in-demand skills while building a high-accountability community and mentorship ecosystem focused on real-world monetization through freelancing and agency models.`},
      {type:`heading`,text:`Unit Economics & Financial Clarification`},
      {type:`paragraph`,text:`Across 200+ community members built from inception, 140+ members went on to generate five-figure monthly incomes, with ₹10,00,000 in total reported revenue.`},
      {type:`quote`,text:`The ₹5,000 per student represents the revenue retained by our business after deducting the cost paid to the third-party ed-tech firm that trains our students in in-demand skills (not the student's income, gross collection before training costs, or net profit after all operating expenses).`,attribution:`Unit Economics Clarification`}
    ]
  },
  "idigitalpreneur":{
    id:`idigitalpreneur`,
    role:`Independent Business Development Associate`,
    timeline:`February 2023 – April 2024`,
    summary:`Worked as a Business Development Associate and affiliate marketer in the ed-tech space, closing B2C deals through outbound calling and prospecting.`,
    blocks:[
      {type:`stats`,items:[
        {value:`₹2,00,000`,label:`Total deals closed`},
        {value:`~₹10,000`,label:`Average ticket size`},
        {value:`₹68,000`,label:`Earned in commissions`},
        {value:`B2C Sales`,label:`Outbound calling & prospecting`}
      ]},
      {type:`heading`,text:`Consultative B2C Sales & Outbound Prospecting`},
      {type:`paragraph`,text:`At IDigitalpreneur Pvt. Ltd., I worked as an Independent Business Development Associate and affiliate marketer in the ed-tech space, driving end-to-end B2C sales from initial prospecting and outbound calling to deal closure.`},
      {type:`heading`,text:`Customer Conversations & Objection Handling`},
      {type:`paragraph`,text:`Rather than relying on pushy scripts, my focus was on genuine customer conversations—listening closely to understand each prospect's learning goals and constraints, addressing objections thoughtfully, and matching them with the right program.`},
      {type:`heading`,text:`Commercial Outcomes`},
      {type:`paragraph`,text:`Closed B2C deals worth ₹2,00,000 at an average ticket size of approximately ₹10,000, earning ₹68,000 in commissions.`}
    ]
  },
  "lyvo":{
    id:`lyvo`,
    role:`Product Concept & Ideation`,
    timeline:`Ideation Stage`,
    summary:`A conversational-support platform designed to connect lonely or distressed young people with life coaches, offering conversational guidance as an alternative or complement to appropriate professional support.`,
    blocks:[
      {type:`stats`,items:[
        {value:`Ideation`,label:`Current development stage`},
        {value:`1-on-1`,label:`Conversational sessions with life coaches`},
        {value:`Youth`,label:`Target audience seeking connection`},
        {value:`Non-Clinical`,label:`Conversational guidance & support`}
      ]},
      {type:`heading`,text:`The Problem Being Explored`},
      {type:`paragraph`,text:`Many young people experiencing loneliness or distress hesitate to approach conventional clinical channels, yet urgently need a safe, empathetic human conversation and practical life guidance.`},
      {type:`heading`,text:`Proposed Solution & Product Concept`},
      {type:`paragraph`,text:`Lyvo is a user-interface platform concept designed to connect young people with life coaches through structured conversational sessions rather than conventional clinical therapy. It is envisioned as an accessible conversational-support alternative or complement to appropriate professional support—not a clinically validated therapy product or a substitute for professional mental-health care.`}
    ]
  },
  "buildsy":{
    id:`buildsy`,
    role:`Product Builder`,
    timeline:`Minimum Viable Product (MVP)`,
    summary:`An AI-powered tool-stack recommendation platform for solopreneurs and first-time founders that recommends a personalized collection of AI tools, software plans, and pricing packages based on what the founder is building.`,
    blocks:[
      {type:`stats`,items:[
        {value:`MVP`,label:`Current development stage`},
        {value:`AI Stack`,label:`Personalized tool-stack recommendations`},
        {value:`0 → 1`,label:`Built for solopreneurs & first-time founders`},
        {value:`Budget-Fit`,label:`Phased purchasing & plan selection`}
      ]},
      {type:`heading`,text:`The Problem of Tool Selection`},
      {type:`paragraph`,text:`Solopreneurs and first-time founders face hundreds of overlapping AI tools and SaaS subscriptions, often overspending on wrong tiers or suffering from tool fatigue before launching.`},
      {type:`heading`,text:`Personalized Tool-Stack & Budget Planning`},
      {type:`paragraph`,text:`Buildsy analyzes what the founder is building, their stage, and their budget to recommend a tailored collection of AI tools and software—complete with specific plans, pricing packages, and phased purchasing considerations so first-time builders choose the right tools without unnecessary spending.`}
    ]
  },
  "raah":{
    id:`raah`,
    role:`Product Builder`,
    timeline:`Testing Stage`,
    summary:`An AI-powered career diagnostic platform undergoing testing that evaluates a candidate's career readiness across eight role tracks and five dimensions.`,
    blocks:[
      {type:`stats`,items:[
        {value:`Testing`,label:`Current development stage`},
        {value:`8 Tracks`,label:`Role tracks evaluated`},
        {value:`5 Dimensions`,label:`Readiness diagnostic framework`},
        {value:`Actionable`,label:`Targeted career-readiness roadmap`}
      ]},
      {type:`heading`,text:`Multi-Dimensional Career Readiness Analysis`},
      {type:`paragraph`,text:`Raah is an AI-powered career diagnostic platform currently undergoing testing. It evaluates a candidate's career readiness across eight distinct role tracks and five core dimensions.`},
      {type:`heading`,text:`Insights & Role-Track Recommendations`},
      {type:`paragraph`,text:`The platform provides structured career-readiness analysis, evaluation across role tracks, insights into future career opportunities, and concrete suggestions to help users bridge skill gaps and move towards their desired roles. It is presented as a product undergoing testing rather than a fully validated career prediction system.`}
    ]
  },
  "bharti-airtel":{
    id:`bharti-airtel`,
    role:`MBA Candidate · Masters' Union`,
    timeline:`Academic Project · Business Strategy`,
    summary:`Academic case-study assignment examining business strategy challenges and strategic growth opportunities for Bharti Airtel.`,
    blocks:[
      {type:`heading`,text:`Company & Business Problem`},
      {type:`paragraph`,text:`Company: Bharti Airtel (Academic Assignment — Business Strategy). Detailed assignment slides and problem statement materials will be populated upon upload.`},
      {type:`heading`,text:`Project Objective & Market/Customer Research`},
      {type:`paragraph`,text:`Structured to cover the core project objective, telecom market landscape, customer segmentation, and primary/secondary research insights.`},
      {type:`heading`,text:`Analysis, Strategy & My Contribution`},
      {type:`paragraph`,text:`Structured to present our strategic analysis, business recommendations, individual contribution, and key learnings from this college assignment.`}
    ]
  },
  "ownwise":{
    id:`ownwise`,
    role:`MBA Candidate · Masters' Union`,
    timeline:`Academic Project · DBM2`,
    summary:`Academic case-study assignment created for DBM2 analyzing Ownwise's business problem, customer insights, and strategic recommendations.`,
    blocks:[
      {type:`heading`,text:`Company & Business Problem`},
      {type:`paragraph`,text:`Company: Ownwise (Academic Assignment — DBM2). Detailed assignment deck and problem context will be populated upon upload.`},
      {type:`heading`,text:`Research, Analysis & Recommendations`},
      {type:`paragraph`,text:`Structured to showcase the project objective, market/customer research, analysis and insights, recommended business strategy, my contribution, and key learnings.`}
    ]
  },
  "stride":{
    id:`stride`,
    role:`MBA Candidate · Masters' Union`,
    timeline:`Academic Project · Fintech DBM1`,
    summary:`Academic case-study assignment for Fintech DBM1 solving a business problem for Stride.`,
    blocks:[
      {type:`heading`,text:`Company & Business Problem`},
      {type:`paragraph`,text:`Company: Stride (Academic Assignment — Fintech DBM1). Detailed assignment materials and fintech analysis will be populated upon upload.`},
      {type:`heading`,text:`Research, Analysis & Recommendations`},
      {type:`paragraph`,text:`Structured to showcase the project objective, market/customer research, analysis and insights, recommended fintech strategy, my contribution, and key learnings.`}
    ]
  },
  "gostops":{
    id:`gostops`,
    role:`MBA Candidate · Masters' Union`,
    timeline:`Business Project · College Assignment`,
    summary:`Business case-study assignment addressing strategic and operational problems for GoSTOPS.`,
    blocks:[
      {type:`heading`,text:`Company & Business Problem`},
      {type:`paragraph`,text:`Company: GoSTOPS (Business Project Assignment). Detailed case analysis and presentation materials will be populated upon upload.`},
      {type:`heading`,text:`Research, Strategy & Outcomes`},
      {type:`paragraph`,text:`Structured to showcase the business problem, project objective, traveller/market research, analysis and insights, business strategy recommendations, my contribution, and learnings.`}
    ]
  },
  "pepperfry":{
    id:`pepperfry`,
    role:`MBA Candidate · Masters' Union`,
    timeline:`Business Project · College Assignment`,
    summary:`We identified a problem in Pepperfry's post-purchase services—an area the company appeared to be neglecting despite many customer complaints falling within that stage—and proposed three recommendations to improve customer experience and boost sales.`,
    blocks:[
      {type:`image`,src:`/assets/pepperfry.png`,alt:`Pepperfry — Customer Experience Improvement Assignment`,caption:`Pepperfry Post-Purchase Customer Experience Case Assignment`},
      {type:`heading`,text:`Business Problem & Project Objective`},
      {type:`paragraph`,text:`We identified a critical gap in Pepperfry's post-purchase services—an area the company appeared to be neglecting despite a significant share of customer complaints originating in that stage of the customer journey.`},
      {type:`heading`,text:`Market/Customer Research & Insights`},
      {type:`paragraph`,text:`By analyzing customer reviews and post-purchase touchpoints (delivery, installation, returns, and support communication), we mapped where friction was eroding trust and repeat purchase intent.`},
      {type:`heading`,text:`Business Strategy, Recommendations & Learnings`},
      {type:`paragraph`,text:`We proposed three targeted recommendations to streamline post-purchase resolution, improve customer experience, and drive higher retention and sales. Additional assignment slides and details will be added upon upload.`}
    ]
  }
},
Qh=[
  {
    id:`stroque-consulting`,
    title:`Stroque Consulting`,
    context:`Co-Founder & Sr. Handwriting Analyst · Nov 2022 – Present`,
    tags:[`Graphology`,`Graphotherapy`,`Human Consulting`,`AI for B2B Expansion`],
    brands:[{name:`Stroque Consulting`,logo:`/brands/stroque.svg`}],
    attribution:`Nov 2022 – Present`,
    org:`Stroque Consulting`,
    image:`/assets/covers/stroque-consulting.svg`
  },
  {
    id:`hustlers-edge`,
    title:`Hustlers' Edge Community`,
    context:`Founder & Community Lead · Aug 2024 – Apr 2026`,
    tags:[`Skill Community`,`Marketing Skills`,`Agency & Freelancing`,`₹10L Revenue`],
    brands:[{name:`Hustlers' Edge`,logo:`/brands/hustlers-edge.svg`}],
    attribution:`Aug 2024 – Apr 2026`,
    org:`Hustlers' Edge Community`,
    image:`/assets/covers/hustlers-edge.svg`
  },
  {
    id:`idigitalpreneur`,
    title:`IDigitalpreneur Pvt. Ltd.`,
    context:`Independent Business Development Associate · Feb 2023 – Apr 2024`,
    tags:[`B2C Sales`,`Outbound Calling`,`Prospecting`,`Objection Handling`],
    brands:[{name:`IDigitalpreneur`,logo:`/brands/idigitalpreneur.svg`}],
    attribution:`Feb 2023 – Apr 2024`,
    org:`IDigitalpreneur Pvt. Ltd.`,
    image:`/assets/covers/idigitalpreneur.svg`
  }
],
$h=[
  {
    id:`lyvo`,
    title:`Lyvo — Ideation Stage`,
    stage:`Ideation Stage`,
    tags:[`Ideation Stage`,`Conversational Support`,`Life Coaching Platform`],
    cover:{src:`/assets/covers/lyvo.svg`,position:`50% 50%`},
    summary:`A conversational-support platform designed to connect lonely or distressed young people with life coaches through conversational sessions rather than conventional clinical therapy.`
  },
  {
    id:`buildsy`,
    title:`Buildsy — Minimum Viable Product`,
    stage:`Minimum Viable Product`,
    tags:[`Minimum Viable Product`,`AI Tool-Stack`,`Solopreneurs & First-Time Founders`],
    cover:{src:`/assets/covers/buildsy.svg`,position:`50% 50%`},
    summary:`An AI-powered tool-stack recommendation platform for solopreneurs and first-time founders that recommends personalized AI tools, plans, and phased pricing packages.`
  },
  {
    id:`raah`,
    title:`Raah — Testing`,
    stage:`Testing`,
    tags:[`Testing`,`AI Career Diagnostic`,`8 Role Tracks × 5 Dimensions`],
    cover:{src:`/assets/covers/raah.svg`,position:`50% 50%`},
    summary:`An AI-powered career diagnostic platform undergoing testing that evaluates a candidate's career readiness across eight role tracks and five dimensions.`
  }
],
eg=[`Lyvo — Ideation Stage`,`Buildsy — Minimum Viable Product`,`Raah — Testing`];
function tg({block:e}){switch(e.type){case`heading`:return(0,G.jsx)(`h2`,{className:`mt-14 font-serif text-[clamp(24px,3vw,32px)] text-[var(--color-ink)]`,children:e.text});case`paragraph`:return(0,G.jsx)(`p`,{className:`mt-5 max-w-[65ch] text-[17px] leading-relaxed text-[var(--color-ink-dim)]`,children:e.text});case`image`:return(0,G.jsxs)(`figure`,{className:`mt-8`,"data-scroll-depth":!0,children:[(0,G.jsx)(`img`,{src:e.src,alt:e.alt,loading:`lazy`,className:`w-full rounded-md border border-[var(--color-line)] object-cover`}),e.caption&&(0,G.jsx)(`figcaption`,{className:`mt-2 text-xs text-[var(--color-ink-dim)]`,children:e.caption})]});case`gallery`:return(0,G.jsx)(`div`,{className:`mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2`,"data-scroll-depth":!0,children:e.images.map(e=>(0,G.jsx)(`img`,{src:e.src,alt:e.alt,loading:`lazy`,className:`w-full rounded-md border border-[var(--color-line)] object-cover`},e.src))});case`video`:return(0,G.jsxs)(`figure`,{className:`mt-8`,children:[(0,G.jsx)(`video`,{src:e.src,controls:!0,playsInline:!0,className:`w-full rounded-md border border-[var(--color-line)]`}),e.caption&&(0,G.jsx)(`figcaption`,{className:`mt-2 text-xs text-[var(--color-ink-dim)]`,children:e.caption})]});case`stats`:return(0,G.jsx)(`div`,{className:`mt-8 grid grid-cols-2 gap-6 border-y border-[var(--color-line)] py-6 sm:grid-cols-4`,children:e.items.map((e,t)=>(0,G.jsxs)(`div`,{children:[(0,G.jsx)(`p`,{className:`tabular text-2xl text-[var(--color-ink)]`,children:e.value}),(0,G.jsx)(`p`,{className:`mt-1 text-xs text-[var(--color-ink-dim)]`,children:e.label})]},t))});case`quote`:return(0,G.jsxs)(`blockquote`,{className:`mt-8 border-l-2 border-[var(--color-accent)] pl-5 font-serif text-xl italic text-[var(--color-ink)]`,children:[`“`,e.text,`”`,e.attribution&&(0,G.jsxs)(`footer`,{className:`mt-2 font-sans text-sm not-italic text-[var(--color-ink-dim)]`,children:[`— `,e.attribution]})]});default:return null}}
function ng(){
  let{slug:e}=pt(),r=e?.match(/^more-(\d+)$/),i=r?$h[Number(r[1])]:void 0,lookupId=i?i.id:e,n=lookupId?Zh[lookupId]:void 0,t=Qh.find(t=>t.id===lookupId)||(i?{id:i.id,title:i.title,context:i.tags.join(` · `),org:i.stage,image:i.cover?.src}:{id:lookupId,title:lookupId,context:n?.timeline??``,org:`Masters' Union Assignment`,image:`/assets/covers/${lookupId}.svg`});
  return !n?(0,G.jsxs)(`main`,{className:`paper-grain flex min-h-screen flex-col items-center justify-center gap-4 bg-[var(--color-paper)] px-6 text-center text-[var(--color-ink)]`,children:[(0,G.jsx)(`p`,{className:`section-label text-[var(--color-ink-dim)]`,children:`Not found`}),(0,G.jsx)(`h1`,{className:`editorial-heading text-3xl`,children:`This case study doesn't exist yet.`}),(0,G.jsx)(Cn,{to:`/`,className:`mt-2 underline decoration-[var(--color-line)] underline-offset-4 hover:text-[var(--color-accent-ink)]`,children:`← Back home`})]}):(0,G.jsx)(`main`,{className:`paper-grain min-h-screen bg-[var(--color-paper)] text-[var(--color-ink)]`,children:(0,G.jsxs)(`div`,{className:`mx-auto max-w-3xl px-6 py-16 sm:px-10 sm:py-20 lg:px-0`,children:[(0,G.jsx)(Cn,{to:`/#work`,className:`tabular text-sm text-[var(--color-ink-dim)] underline decoration-[var(--color-line)] underline-offset-4 hover:text-[var(--color-accent-ink)]`,children:`← Back to portfolio`}),(0,G.jsx)(`p`,{className:`section-label mt-10 text-[var(--color-ink-dim)]`,children:`Case Study`}),(0,G.jsx)(`h1`,{className:`editorial-heading mt-3 text-[var(--color-ink)]`,children:t.title}),(0,G.jsx)(`p`,{className:`mt-3 text-lg text-[var(--color-ink-dim)]`,children:t.context}),(0,G.jsxs)(`div`,{className:`mt-6 flex flex-wrap gap-x-8 gap-y-2 border-y border-[var(--color-line)] py-4 text-sm`,children:[t.org&&(0,G.jsxs)(`div`,{children:[(0,G.jsx)(`p`,{className:`text-xs text-[var(--color-ink-dim)]`,children:`Venture / Context`}),(0,G.jsx)(`p`,{className:`text-[var(--color-ink)]`,children:t.org})]}),n.role&&(0,G.jsxs)(`div`,{children:[(0,G.jsx)(`p`,{className:`text-xs text-[var(--color-ink-dim)]`,children:`Role`}),(0,G.jsx)(`p`,{className:`text-[var(--color-ink)]`,children:n.role})]}),n.timeline&&(0,G.jsxs)(`div`,{children:[(0,G.jsx)(`p`,{className:`text-xs text-[var(--color-ink-dim)]`,children:`Duration / Stage`}),(0,G.jsx)(`p`,{className:`text-[var(--color-ink)]`,children:n.timeline})]})]}),(0,G.jsx)(`p`,{className:`mt-8 max-w-[60ch] font-serif text-2xl leading-snug text-[var(--color-ink)]`,children:n.summary}),t.image&&(0,G.jsx)(`img`,{"data-scroll-depth":!0,src:t.image,alt:t.title,className:`mt-10 w-full rounded-md border border-[var(--color-line)] object-cover`}),(0,G.jsx)(`div`,{className:`pb-16`,children:n.blocks.map((e,t)=>(0,G.jsx)(tg,{block:e},t))})]})})}"""

# ============================================================================
# SPLICE 3: IDEATION & MVP (kg), FEATURED VENTURES (Pg, Fg, Ig), AND BROWSER DATA
# We preserve Zg, n_, r_, i_, c_, l_ from samay.js and update the data arrays!
# ============================================================================
pos_zg_fn = src.find("function Zg({variant:e})")
pos_qg_var = src.find("var Qg={portfolio:")
pos_n_fn = src.find("function n_({f:e})")
pos_a_var = src.find("var a_=[`samay maurya`")
pos_c_fn = src.find("function c_({small:e=!1})")
pos_u_var = src.find("var u_=`data:image/png;base64,")

zg_fn_code = src[pos_zg_fn:pos_qg_var]
figma_fn_code = src[pos_n_fn:pos_a_var].replace("children:`Samay`", "children:`Hassaan`")
search_fn_code = src[pos_c_fn:pos_u_var]

SPLICE_3 = r"""var xg=.16,Sg=12,Cg=14,wg=26,Tg=8,Eg=[.16,1,.3,1];function Dg({items:e,open:t,index:n,from:r}){let i=um(),a=(0,v.useRef)(null),o=(0,v.useRef)([]),s=(0,v.useRef)({x:r.x,y:r.y,tx:r.x,ty:r.y,lean:0,flip:0,raf:0,last:0,open:!1});(0,v.useEffect)(()=>{let e=s.current,t=t=>{e.tx=t.clientX,e.ty=t.clientY};return window.addEventListener(`pointermove`,t,{passive:!0}),()=>window.removeEventListener(`pointermove`,t)},[]),(0,v.useLayoutEffect)(()=>{let e=s.current,n=a.current;if(!n)return;t&&!e.open&&(e.x=e.tx=r.x,e.y=e.ty=r.y,e.lean=0,e.flip=+(e.ty-(n.offsetHeight+Cg)<Tg)),e.open=t;let o=()=>{let t=n.offsetWidth,r=n.offsetHeight,i=Math.min(Math.max(e.x-t/2,Tg),window.innerWidth-t-Tg),a=e.y+(-r-Cg)*(1-e.flip)+wg*e.flip;n.style.transform=`translate3d(${i}px, ${a}px, 0) rotate(${e.lean}deg)`,e.flip>.5?n.dataset.below=``:delete n.dataset.below},c=t=>{let r=Math.min(.05,(t-(e.last||t))/1e3);if(e.last=t,i)e.x=e.tx,e.y=e.ty;else{let t=1-Math.exp(-9*r);e.x+=(e.tx-e.x)*t,e.y+=(e.ty-e.y)*t;let n=Math.max(-12,Math.min(Sg,(e.tx-e.x)*xg));e.lean+=(n-e.lean)*(1-Math.exp(-12*r))}let a=+(e.ty-(n.offsetHeight+Cg)<Tg);e.flip=i?a:e.flip+(a-e.flip)*(1-Math.exp(-14*r)),o();let s=Math.abs(e.tx-e.x)<.3&&Math.abs(e.ty-e.y)<.3&&Math.abs(e.lean)<.05&&(e.flip<.01||e.flip>.99);e.open||!s?e.raf=requestAnimationFrame(c):e.raf=0};return e.last=0,e.raf||=requestAnimationFrame(c),()=>{cancelAnimationFrame(e.raf),e.raf=0}},[t,i]),(0,v.useEffect)(()=>{o.current.forEach((e,r)=>{e&&(t&&r===n?e.play().catch(()=>{}):e.pause())})},[t,n]);let c=i?{opacity:0}:{opacity:0,scale:0},l=i?{opacity:1}:{opacity:1,scale:1};return(0,y.createPortal)((0,G.jsx)(`div`,{ref:a,className:`more-preview`,"aria-hidden":!0,children:(0,G.jsx)(K.div,{className:`more-preview-card`,initial:!1,animate:t?l:c,transition:{duration:t?.6:.4,ease:Eg},children:e.map((e,t)=>{let r=e.cover;if(!r)return null;let i=t===n;return(0,G.jsx)(K.div,{className:`more-preview-layer`,style:{zIndex:+!!i},initial:!1,animate:i?l:c,transition:{duration:i?.55:.45,ease:Eg},children:r.video?(0,G.jsx)(`video`,{ref:e=>{o.current[t]=e},src:r.video,poster:r.src,muted:!0,loop:!0,playsInline:!0,preload:`none`,style:{objectPosition:r.position}}):(0,G.jsx)(`img`,{src:r.src,alt:``,decoding:`async`,style:{objectPosition:r.position}})},e.title)})})}),document.body)}
var Og=`(hover: hover) and (pointer: fine)`;
function kg({layout:e=`rail`}){
  let t=ct(),n=um(),r=(0,v.useRef)(null),[i,a]=(0,v.useState)(null),[o,s]=(0,v.useState)(0),[c,l]=(0,v.useState)({x:0,y:0}),[u,d]=(0,v.useState)(!1),f=eg.map(e=>$h.find(t=>t.title===e)).filter(e=>e!==void 0),p=(e,t,r,o)=>{if(!window.matchMedia(Og).matches)return;i===null&&l({x:r,y:o}),d(!0),a(e),s(e);let c=t.querySelector(`.more-work-body`);c&&!n&&Fm(c,{x:10},{duration:.45,ease:[.16,1,.3,1]})},m=e=>{let t=e.querySelector(`.more-work-body`);t&&!n&&Fm(t,{x:0},{duration:.45,ease:[.16,1,.3,1]})};
  return(0,v.useEffect)(()=>{if(i===null)return;let e=-1,t=-1,n=n=>{e=n.clientX,t=n.clientY},o=()=>{if(e<0)return;let n=document.elementFromPoint(e,t);r.current?.contains(n)||a(null)};return window.addEventListener(`pointermove`,n,{passive:!0}),window.addEventListener(`scroll`,o,{passive:!0}),()=>{window.removeEventListener(`pointermove`,n),window.removeEventListener(`scroll`,o)}},[i]),(0,G.jsxs)(`div`,{className:`more-work more-work--${e}`,children:[(0,G.jsx)(`h3`,{className:`more-work-title`,"data-paint":`text`,children:`Problems that are still in ideation & MVP.`}),(0,G.jsx)(`ul`,{ref:r,className:`more-work-list`,onPointerLeave:()=>a(null),children:f.map((e,n)=>{let r=(0,G.jsxs)(G.Fragment,{children:[(0,G.jsxs)(`span`,{className:`more-work-body`,children:[(0,G.jsx)(`span`,{className:`more-work-project`,"data-paint":`text`,children:e.title}),e.tags.length>0&&(0,G.jsx)(`span`,{className:`more-work-tags`,"data-paint":`text`,children:e.tags.join(` · `)})]}),(0,G.jsx)(`span`,{className:`more-work-arrow`,"data-paint":`text`,"aria-hidden":!0,children:`↗`})]}),rowProps={className:`more-work-row`,"data-paint":`panel`,onPointerEnter:e=>p(n,e.currentTarget,e.clientX,e.clientY),onPointerLeave:e=>m(e.currentTarget),onClick:()=>a(null)};return(0,G.jsx)(`li`,{className:`more-work-item`,"data-paint":`rule`,children:(0,G.jsx)(Cn,{to:`/work/${e.id}`,state:{backgroundLocation:t},...rowProps,children:r})},e.title)})}),u&&(0,G.jsx)(Dg,{items:f,open:i!==null,index:i??o,from:c})]})}
function Ag({project:e,index:t,layout:n=`rail`}){
  let r=dt(),i=ct(),a=!!Zh[e.id],o=a?`/work/${e.id}`:e.href;
  return(0,G.jsxs)(`a`,{href:o,...a?{}:{target:`_blank`,rel:`noopener noreferrer`},className:`work-card work-card--${n}`,onClick:e=>{!a||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||(e.preventDefault(),r(o,{state:{backgroundLocation:i}}))},"aria-label":`${e.title} — open case study`,children:[(0,G.jsxs)(`div`,{className:`work-card-header`,"data-paint":`panel`,children:[(0,G.jsxs)(`div`,{className:`work-card-heading`,children:[(0,G.jsx)(`h3`,{className:`work-card-title`,"data-paint":`text`,children:e.title}),(0,G.jsx)(`ul`,{className:`work-card-tags`,"aria-label":`Project disciplines`,children:(0,G.jsx)(`li`,{"data-paint":`text`,"data-paint-box":`solid`,children:e.tags.join(` · `)})})]}),(0,G.jsxs)(`div`,{className:`work-card-meta`,children:[e.brands&&(0,G.jsx)(`div`,{className:`work-card-brands`,children:e.brands.map((e,t)=>(0,G.jsxs)(`div`,{className:`work-card-brand`,children:[t>0&&(0,G.jsx)(`span`,{className:`work-card-brand-cross`,"data-paint":`text`,"aria-label":`and`,children:`×`}),(0,G.jsx)(`span`,{className:`work-card-brand-logo${e.wordmark?` is-wordmark`:``}${e.monochrome?` is-monochrome`:``}`,"data-paint":`image`,children:(0,G.jsx)(`img`,{src:e.logo,alt:e.wordmark?e.name:``,width:e.wordmark?48:28,height:28})}),!e.wordmark&&(0,G.jsx)(`span`,{className:`work-card-brand-name`,"data-paint":`text`,children:e.name})]},e.name))}),e.attribution&&(0,G.jsx)(`p`,{className:`work-card-attribution`,"data-paint":`text`,children:e.attribution})]})]}),(0,G.jsxs)(`div`,{className:`work-card-media`,"data-paint":`media`,"data-paint-box":`solid`,children:[(0,G.jsx)(`img`,{src:e.image,alt:`${e.title} — project preview`,crossOrigin:`anonymous`,loading:t===0?`eager`:`lazy`,decoding:`async`,fetchPriority:t===0?`high`:`auto`}),e.video&&(0,G.jsx)(`video`,{src:e.video,crossOrigin:`anonymous`,muted:!0,loop:!0,playsInline:!0,autoPlay:!0,preload:`metadata`,"aria-hidden":!0})]})]})}
var jg=`(min-width: 1024px) and (min-height: 601px) and (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)`,Mg=e=>{let t=window.matchMedia(jg);return t.addEventListener(`change`,e),()=>t.removeEventListener(`change`,e)},Ng={zone:240,angle:80,rounding:150,perspective:700,ease:240,smoothing:.1,edgeBlur:3.25,direction:`in`};
function Pg(){return(0,G.jsxs)(`section`,{id:`work`,className:`dark-register work-stacked`,children:[(0,G.jsx)(`h2`,{className:`section-label work-stacked-label`,children:`01 / Entrepreneurship Experiments`}),Qh.map((e,t)=>(0,G.jsx)(Ag,{project:e,index:t,layout:`stacked`},e.id)),(0,G.jsx)(kg,{layout:`stacked`})]})}
function Fg(){let e=(0,v.useRef)(null),t=(0,v.useRef)(null),n=(0,v.useRef)(0),{scrollYProgress:r}=bg(e);return tm(r,`change`,e=>{let r=t.current;r&&(r.scrollLeft=e*n.current)}),(0,v.useLayoutEffect)(()=>{let i=e.current,a=t.current;if(!i||!a)return;let o=()=>{let e=Math.max(0,a.scrollWidth-a.clientWidth);n.current=e,i.style.setProperty(`--work-travel`,`${e}px`),a.scrollLeft=r.get()*e},s=new ResizeObserver(o);return s.observe(a),a.firstElementChild&&s.observe(a.firstElementChild),o(),()=>s.disconnect()},[r]),(0,G.jsx)(`div`,{id:`work`,ref:e,className:`work-scroll`,children:(0,G.jsxs)(`div`,{"data-scroll-stage":!0,className:`dark-register work-stage`,children:[(0,G.jsx)(`h2`,{className:`section-label work-stage-label`,children:`01 / Entrepreneurship Experiments`}),(0,G.jsx)(yg,{railRef:t,options:Ng,className:`h-full w-full`,children:(0,G.jsxs)(`div`,{className:`work-rail`,children:[Qh.map((e,t)=>(0,G.jsx)(Ag,{project:e,index:t},e.id)),(0,G.jsx)(kg,{})]})}),(0,G.jsx)(`a`,{href:`#experience`,className:`tabular work-stage-skip`,children:`SKIP AHEAD →`})]})})}
function Ig(){return(0,v.useSyncExternalStore)(Mg,()=>window.matchMedia(jg).matches,()=>!1)?(0,G.jsx)(Fg,{}):(0,G.jsx)(Pg,{})}
var Lg=[{label:`0 → 1 builder`,icon:`compass`,tone:`green`},{label:`consultative sales`,icon:`peak`,tone:`blue`},{label:`mentoring & books`,icon:`eq`,tone:`orange`}],
Rg={now:`Masters' Union`,home:`India`},
Bg=`/hero/photo-1.jpg`,
VgMentoring=[
  {
    id:`mentoring-public-talk`,
    year:`2026`,
    place:`First Ever Public Talk`,
    tag:`100+ Students`,
    note:`Prarambh — The Launch of Udyogonmukh. Addressed 100+ students under a single roof at Satyawati College (Evening), University of Delhi, sharing the journey of entrepreneurship, problem solving, and building from 0 to 1.`,
    photos:[
      {src:`/media/mentoring/mentoring-thumb-3.jpg`,videoSrc:`/media/mentoring/mentoring-video-3.mp4`,alt:`The first ever public talk — 100 students under a single roof at Satyawati College, Delhi University`},
      {src:`/media/mentoring/mentoring-thumb-1.jpg`,videoSrc:`/media/mentoring/mentoring-video-1.mp4`,alt:`Mentoring and whiteboarding session on hero section architecture`},
      {src:`/media/mentoring/mentoring-thumb-2.jpg`,videoSrc:`/media/mentoring/mentoring-video-2.mp4`,alt:`Interactive discussion and live product guidance with students`},
      {src:`/hero/photo-2.jpg`,alt:`Consultative selling mentorship session`}
    ]
  },
  {
    id:`mentoring-interactive-workshop`,
    year:`2026`,
    place:`Cohort Strategy & Whiteboard`,
    tag:`Mentorship`,
    note:`Hands-on mentorship, wireframing, and problem-solving workshops. Breaking down customer problems, tailored value propositions, and live strategy with team members.`,
    photos:[
      {src:`/media/mentoring/mentoring-thumb-1.jpg`,videoSrc:`/media/mentoring/mentoring-video-1.mp4`,alt:`Whiteboarding and cohort strategy session`},
      {src:`/media/mentoring/mentoring-thumb-2.jpg`,videoSrc:`/media/mentoring/mentoring-video-2.mp4`,alt:`1-on-1 and small-group interactive mentorship`},
      {src:`/media/mentoring/mentoring-thumb-3.jpg`,videoSrc:`/media/mentoring/mentoring-video-3.mp4`,alt:`Keynote speech on entrepreneurship and venture building`},
      {src:`/hero/photo-1.jpg`,alt:`Global market exposure at Canton Fair, Guangzhou`}
    ]
  },
  {
    id:`mentoring-students`,
    year:`2024–26`,
    place:`Hustlers' Edge Community`,
    tag:`200+ Members`,
    note:`Mentoring 200+ final-year students and early-career professionals in market-demand skills, agency operations, and consultative monetization models.`,
    photos:[
      {src:`/media/mentoring/mentoring-thumb-2.jpg`,videoSrc:`/media/mentoring/mentoring-video-2.mp4`,alt:`Hands-on student mentorship session`},
      {src:`/hero/photo-2.jpg`,alt:`Consultative approach and objection handling at Dropshipping Mela`},
      {src:`/media/mentoring/mentoring-thumb-1.jpg`,videoSrc:`/media/mentoring/mentoring-video-1.mp4`,alt:`Group strategy and problem breakdown session`},
      {src:`/hero/photo-3.jpg`,alt:`Retreat reflection and community building`}
    ]
  }
],
Vg=VgMentoring,
HgPictures=[
  {src:`/hero/photo-1.jpg`,alt:`Muhammad Hassaan at Canton Fair Phase 1, Guangzhou, China`,tall:!0,category:`pictures`},
  {src:`/hero/photo-2.jpg`,alt:`Learning and mastering consultative selling at Dropshipping Mela, Masters' Union`,category:`pictures`},
  {src:`/hero/photo-3.jpg`,alt:`Arabian Sea voyage from Kochi to Mumbai on Cordelia Cruises`,category:`pictures`},
  {src:`/media/mentoring/mentoring-thumb-1.jpg`,alt:`Mentoring workshop and whiteboard strategy session`,tall:!0,category:`pictures`},
  {src:`/media/mentoring/mentoring-thumb-2.jpg`,alt:`Interactive live discussion and mentoring with students`,category:`pictures`},
  {src:`/media/mentoring/mentoring-thumb-3.jpg`,alt:`Keynote speech — First Ever Public Talk with 100+ students at Satyawati College`,category:`pictures`}
],
HgVideos=[
  {src:`/media/mentoring/mentoring-thumb-3.jpg`,videoSrc:`/media/mentoring/mentoring-video-3.mp4`,alt:`First Ever Public Talk — 100 Students under a single roof at Satyawati College (Evening), Delhi University`,category:`videos`,isVideo:!0},
  {src:`/media/mentoring/mentoring-thumb-1.jpg`,videoSrc:`/media/mentoring/mentoring-video-1.mp4`,alt:`Whiteboarding and architecture session — mentoring cohort students`,category:`videos`,isVideo:!0},
  {src:`/media/mentoring/mentoring-thumb-2.jpg`,videoSrc:`/media/mentoring/mentoring-video-2.mp4`,alt:`Interactive mentoring and product feedback session with students`,category:`videos`,isVideo:!0}
],
Hg=[...HgPictures,...HgVideos],
Ug=`PLWx7Fxr7oZE3XICF4S1xPT5dYOAan3mi4`,Wg=`https://topmate.io/hassaanshaik03`,Gg=()=>`https://topmate.io/hassaanshaik03`,Kg=()=>`/assets/covers/gallery-pic-2.svg`,qg=()=>`/assets/covers/gallery-pic-2.svg`,Jg=[{id:`track-1`,title:`Building 0 to 1`,artist:`Muhammad Hassaan`}],
Xg=[
  {q:`who is muhammad hassaan?`,a:`Muhammad Hassaan is an entrepreneur, community builder, and MBA candidate at Masters' Union School of Business. He listens to people and solves their problems by giving them tailored solutions.`},
  {q:`what ventures has he built?`,a:`He co-founded Stroque Consulting (~300 consultation calls, 250+ people positively impacted, 120+ lives transformed via graphotherapy, now exploring AI for B2B expansion) and founded Hustlers' Edge Community (200+ members, 140+ earning 5-figure monthly incomes, ₹10,00,000 reported revenue).`},
  {q:`what is his sales philosophy?`,a:`Sales is genuinely rewarding—not when you're trying to convince someone to buy something, but when you listen closely, understand what they actually need, and help them find the right solution.`},
  {q:`what products is he exploring in ideation & MVP?`,a:`Three products: Lyvo (Ideation Stage — conversational-support platform connecting young people with life coaches), Buildsy (MVP — AI tool-stack recommendation platform for solopreneurs), and Raah (Testing — AI career diagnostic across 8 role tracks and 5 dimensions).`},
  {q:`what academic & business projects has he worked on?`,a:`Academic Projects: Bharti Airtel (Business Strategy), Ownwise (DBM2), and Stride (Fintech DBM1). Business Projects: GoSTOPS and Pepperfry.`},
  {q:`how do I connect with him?`,a:`Head down to the "Let's rise together." section at the bottom of the portfolio to reach out via LinkedIn, Instagram, Topmate, GitHub, or Email.`}
];
""" + zg_fn_code + r"""var Qg={portfolio:{name:`Hassaan Ventures`,page:`🏠 Ventures`,frames:[{id:`p1`,name:`Stroque Consulting`,kind:`hero`,x:0,y:0,w:420,h:260},{id:`p2`,name:`Hustlers' Edge`,kind:`browser`,x:470,y:0,w:380,h:250},{id:`p3`,name:`Buildsy MVP`,kind:`phone`,x:900,y:-20,w:150,h:300},{id:`p4`,name:`note`,kind:`sticky`,x:60,y:320,w:190,h:140,text:`listen closely → tailored solutions`}]},dashboard:{name:`Ideation & MVP Lab`,page:`📊 Products`,frames:[{id:`d1`,name:`Lyvo · Ideation`,kind:`dash-overview`,x:0,y:0,w:480,h:300},{id:`d2`,name:`Buildsy · MVP`,kind:`dash-table`,x:530,y:0,w:380,h:300},{id:`d3`,name:`Raah · Testing`,kind:`checkout`,x:960,y:0,w:160,h:300},{id:`d4`,name:`note`,kind:`sticky`,x:540,y:350,w:190,h:120,text:`8 role tracks × 5 dimensions`}]},ar:{name:`Stroque AI for B2B`,page:`✨ Expansion`,frames:[{id:`a1`,name:`Core Graphology`,kind:`hud-idle`,x:0,y:0,w:400,h:240},{id:`a2`,name:`B2B AI Exploration`,kind:`hud-notify`,x:450,y:0,w:400,h:240},{id:`a3`,name:`note`,kind:`sticky`,x:120,y:300,w:210,h:120,text:`expanding into B2B alongside core services`}]}},$g=[`#ffffff`,`#f1f0eb`,`#e25531`,`#ead56f`,`#4f9d69`,`#2f5bd3`],e_=[`tailored solution ✨`,`listen closely first`,`let's rise together 🚀`,`strong unit economics`,`+1 on consultative selling`],t_={move:`Move (V)`,rect:`Rectangle (R)`,text:`Text (T)`,comment:`Comment (C)`};""" + figma_fn_code + r"""var a_=[`muhammad hassaan`,`stroque consulting`,`hustlers edge community`,`masters union mba`,`consultative selling`],o_=[{label:`About me`,target:`about`,icon:`🙂`},{label:`Work log`,target:`work`,icon:`🗂️`},{label:`Mentoring`,target:`travel`,icon:`🎤`},{label:`Gallery`,target:`gallery`,icon:`📷`}];function s_(e){let t=e.toLowerCase(),n=/mentor|book|read|guide/.test(t),i=/hassaan|stroque|hustler|masters|sales|portfolio/.test(t),a=[{url:`hassaan.me › about`,title:`Muhammad Hassaan — MBA Candidate at Masters' Union`,body:`I listen to people & solve their problems by giving them tailored solutions. Building ventures from 0 to 1.`,target:`about`},{url:`hassaan.me › work-log`,title:`Work log — Stroque Consulting, Hustlers' Edge, IDigitalpreneur`,body:`Entrepreneurship experiments, community building, and consultative B2C/B2B sales.`,target:`work`},{url:`hassaan.me › gallery`,title:`Gallery — Pictures & Videos`,body:`Moments from building ventures, speaking, and campus life.`,target:`gallery`}],o=Vg.map(e=>({url:`hassaan.me › ${e.id}`,title:`${e.place} (${e.year}) — ${e.tag}`,body:e.note,target:`travel`}));return n?{results:[...o,a[0]],didYouMean:!1}:i?{results:[...a,o[0]],didYouMean:!1}:{results:a,didYouMean:!0}}""" + search_fn_code + r"""var u_=`/brands/hustlers-edge.svg`,d_=`/brands/masters-union.svg`,f_=`/brands/delhi-university.svg`;"""

# ============================================================================
# SPLICE 4: BROWSER TABS (About Me, Work Log, Mentoring/Book Reading, Gallery) & FOOTER
# ============================================================================
SPLICE_4 = r"""var b_=()=>(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.8`,children:(0,G.jsx)(`circle`,{cx:`12`,cy:`12`,r:`9`})});
function F_(){
  let e=(0,v.useRef)(null),t=um(),n=Rm(e,{once:!0,amount:.3});
  return(0,G.jsxs)(`div`,{ref:e,className:`about-say space-y-4`,"data-shown":n||t?``:void 0,children:[
    (0,G.jsx)(`p`,{children:(0,G.jsx)(`b`,{children:`I'm Muhammad Hassaan, currently pursuing my MBA at Masters' Union School of Business.`})}),
    (0,G.jsxs)(`p`,{children:[
      `I've always been interested in building things, figuring out how businesses work, and helping people find their way forward. I've spent time `,
      (0,G.jsx)(p_,{type:`circle`,delay:.35,padding:5,children:(0,G.jsx)(`b`,{children:`building ventures from 0 to 1`})}),
      `, mentoring people, and exploring different sides of business.`
    ]}),
    (0,G.jsxs)(`p`,{children:[
      `One thing I'm learning along the way is that sales can be genuinely rewarding. Not when you're trying to convince someone to buy something, but when you `,
      (0,G.jsx)(p_,{type:`highlight`,delay:.75,children:(0,G.jsx)(`b`,{children:`listen closely`})}),
      `, understand what they actually need, and help them `,
      (0,G.jsx)(p_,{type:`underline`,delay:1.1,children:(0,G.jsx)(`b`,{children:`find the right solution`})}),
      `.`
    ]}),
    (0,G.jsx)(`p`,{children:`That's the side of sales I connect with most. And it's what I'm working on getting better at every day. This website is a little space to share what I've been working on, what I've learned, and where I'm headed next.`})
  ]})
}
var I_=[
  {role:`MBA Candidate`,sub:`Stroque Consulting`,org:`Masters' Union`,period:`Current`,verified:!0},
  {role:`Founder & Community Lead`,org:`Hustlers' Edge`,period:`Aug 2024 – Apr 2026`,verified:!0},
  {role:`Undergraduate`,org:`Delhi University`,period:`Graduated`,verified:!0}
],
WorkLogEntries=[
  {role:`Co-Founder & Sr. Handwriting Analyst`,org:`Stroque Consulting`,period:`Current`,when:`Nov 2022 – Present`,logo:`/brands/stroque.svg`},
  {role:`Founder & Community Lead`,org:`Hustlers' Edge Community`,period:`Prior`,when:`Aug 2024 – Apr 2026`,logo:`/brands/hustlers-edge.svg`},
  {role:`Independent Business Development Associate`,org:`IDigitalpreneur Pvt. Ltd.`,period:`Prior`,when:`Feb 2023 – Apr 2024`,logo:`/brands/idigitalpreneur.svg`}
],
H_={"Masters' Union":`/brands/masters-union.svg`,"Hustlers' Edge":`/brands/hustlers-edge.svg`,"Delhi University":`/brands/delhi-university.svg`,"Stroque Consulting":`/brands/stroque.svg`};
function U_({icon:e}){let t={fill:`none`,stroke:`currentColor`,strokeWidth:1.6,strokeLinecap:`round`,strokeLinejoin:`round`};return(0,G.jsxs)(`svg`,{viewBox:`0 0 16 16`,width:`16`,height:`16`,className:`chip-icon`,"aria-hidden":!0,children:[e===`compass`&&(0,G.jsxs)(G.Fragment,{children:[(0,G.jsx)(`circle`,{cx:`8`,cy:`8`,r:`6.2`,...t}),(0,G.jsx)(`path`,{className:`chip-needle`,d:`M8 4.3l1.5 3.7L8 11.7 6.5 8z`,...t})]}),e===`peak`&&(0,G.jsxs)(G.Fragment,{children:[(0,G.jsx)(`path`,{d:`M1.5 13.5 7 4.8l2.6 4.2 1.7-2.4 3.2 6.9z`,...t}),(0,G.jsx)(`path`,{className:`chip-flag`,d:`M7 4.8V1.3l3.2 1.2L7 3.7`,pathLength:1,...t})]}),e===`eq`&&(0,G.jsxs)(`g`,{className:`chip-eq`,fill:`currentColor`,children:[(0,G.jsx)(`rect`,{x:`2.5`,y:`7`,width:`2.4`,height:`6.5`,rx:`1.2`}),(0,G.jsx)(`rect`,{x:`6.8`,y:`3`,width:`2.4`,height:`10.5`,rx:`1.2`}),(0,G.jsx)(`rect`,{x:`11.1`,y:`8.5`,width:`2.4`,height:`5`,rx:`1.2`})]})]})}
function W_(){
  return(0,G.jsxs)(`div`,{className:`page page-about`,children:[
    (0,G.jsxs)(`figure`,{className:`page-about-photo`,children:[
      (0,G.jsx)(`img`,{src:Bg,alt:`Muhammad Hassaan — Portrait placeholder`,loading:`lazy`}),
      (0,G.jsx)(`figcaption`,{className:`hand`,children:`yep, that’s me (photo pending upload)`})
    ]}),
    (0,G.jsxs)(`div`,{className:`page-about-copy`,children:[
      (0,G.jsxs)(`div`,{className:`page-nameplate`,children:[
        (0,G.jsxs)(`p`,{className:`page-hello`,children:[`hello, i’m`,(0,G.jsxs)(`svg`,{viewBox:`0 0 40 30`,className:`page-hello-arrow`,"aria-hidden":!0,children:[(0,G.jsx)(`path`,{d:`M2 7C17 2 29 7 31 23`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.8`,strokeLinecap:`round`}),(0,G.jsx)(`path`,{d:`M25 18l6 6 4-8`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.8`,strokeLinecap:`round`,strokeLinejoin:`round`})]})]}),
        (0,G.jsxs)(`h3`,{className:`page-name`,children:[`Muhammad`,(0,G.jsxs)(`span`,{className:`page-surname`,children:[` `,`hassaan`,(0,G.jsx)(`span`,{className:`page-dot`,"aria-hidden":!0})]})]}),
        (0,G.jsx)(`p`,{className:`page-formal`,"aria-hidden":!0,children:`if you want to be formal`})
      ]}),
      (0,G.jsxs)(`p`,{className:`page-now`,children:[`currently pursuing my MBA at`,(0,G.jsx)(`img`,{src:`/brands/masters-union.svg`,alt:``,className:`page-now-logo`}),(0,G.jsx)(`b`,{children:`Masters' Union School of Business`})]}),
      (0,G.jsx)(F_,{}),
      (0,G.jsx)(`ul`,{className:`page-traits`,children:Lg.map(e=>(0,G.jsxs)(`li`,{className:`chip chip--${e.tone}`,children:[(0,G.jsx)(U_,{icon:e.icon}),e.label]},e.label))}),
      (0,G.jsxs)(`p`,{className:`page-meta`,children:[`pursuing MBA at `,Rg.now,` · co-founder at Stroque Consulting · `,(0,G.jsx)(`a`,{href:`#contact`,children:`let's connect ↓`})]})
    ]})
  ]})
}
function G_(){
  return(0,G.jsxs)(`div`,{className:`page page-work`,children:[
    (0,G.jsx)(`p`,{className:`page-kicker`,children:`work log`}),
    (0,G.jsxs)(`h3`,{className:`page-title`,children:[`where I’ve `,(0,G.jsx)(`em`,{children:`been building.`})]}),
    (0,G.jsx)(`ul`,{className:`worklog`,children:WorkLogEntries.map((e,t)=>{let n=e.period===`Current`;return(0,G.jsxs)(`li`,{className:n?`is-now`:void 0,children:[(0,G.jsx)(`span`,{className:`worklog-index`,children:String(t+1).padStart(2,`0`)}),(0,G.jsx)(`img`,{src:e.logo,alt:``,className:`worklog-logo`}),(0,G.jsx)(`span`,{className:`worklog-org`,children:e.org}),(0,G.jsx)(`span`,{className:`worklog-role`,children:e.role}),(0,G.jsx)(`span`,{className:`worklog-when`,children:e.when})]},e.org)})}),
    (0,G.jsxs)(`div`,{className:`page-work-foot`,children:[
      (0,G.jsx)(`span`,{className:`hand`,children:`explore the full case studies above ↑`}),
      (0,G.jsx)(`a`,{href:`#work`,className:`page-btn`,children:`entrepreneurship experiments ↑`})
    ]})
  ]})
}
function K_(){
  let[e,t]=(0,v.useState)(0),n=VgMentoring[e]||VgMentoring[0],r=um(),[modalVideo,setModalVideo]=(0,v.useState)(null);
  return(0,G.jsxs)(`div`,{className:`page page-travel`,children:[
    (0,G.jsxs)(`div`,{className:`travel-list`,children:[
      (0,G.jsx)(`p`,{className:`page-kicker`,children:`mentoring & speaking`}),
      (0,G.jsxs)(`h3`,{className:`page-title`,children:[`helping people `,(0,G.jsx)(`em`,{children:`find their way forward.`})]}),
      (0,G.jsx)(`ol`,{className:`trips`,children:VgMentoring.map((item,idx)=>(0,G.jsx)(`li`,{children:(0,G.jsxs)(`button`,{type:`button`,className:`trip${idx===e?` is-active`:``}`,onClick:()=>t(idx),"data-sfx":`pop`,children:[(0,G.jsx)(`span`,{className:`trip-year`,children:item.year}),(0,G.jsx)(`span`,{className:`trip-place`,children:item.place}),(0,G.jsx)(`span`,{className:`trip-tag`,children:item.tag})]})},item.id))}),
      (0,G.jsx)(cf,{mode:`wait`,children:(0,G.jsx)(K.p,{className:`hand trip-note`,initial:{opacity:0,y:6},animate:{opacity:1,y:0},exit:{opacity:0,y:-6},transition:{duration:.25},children:n.note},n.id)})
    ]}),
    (0,G.jsxs)(`div`,{className:`travel-photos`,children:[
      (0,G.jsx)(cf,{mode:`popLayout`,children:n.photos.slice(0,4).map((p,idx)=>(0,G.jsxs)(K.figure,{className:`travel-photo travel-photo--${idx+1}`,style:{cursor:`pointer`},onClick:()=>p.videoSrc&&setModalVideo(p),initial:r?{opacity:0}:{opacity:0,y:30,rotate:[-6,5,-3,4][idx]*2,scale:.9},animate:r?{opacity:1}:{opacity:1,y:0,rotate:[-6,5,-3,4][idx],scale:1},exit:r?{opacity:0}:{opacity:0,y:-20,scale:.95},transition:{type:`spring`,stiffness:200,damping:20,delay:idx*.06},whileHover:r?void 0:{rotate:0,scale:1.05,zIndex:5},children:[
        (0,G.jsx)(`img`,{src:p.src,alt:p.alt,loading:`lazy`,draggable:!1}),
        p.videoSrc&&(0,G.jsx)(`span`,{className:`gallery-video-badge`,style:{position:`absolute`,bottom:`6px`,right:`6px`,background:`rgba(20,18,18,0.75)`,color:`#fff`,fontSize:`10px`,padding:`2px 6px`,borderRadius:`4px`,fontWeight:600},children:`▶ Watch Video`})
      ]},p.src))}),
      (0,G.jsxs)(`span`,{className:`travel-stamp`,children:[n.year,(0,G.jsx)(`small`,{children:n.place})]})
    ]}),
    modalVideo&&(0,y.createPortal)((0,G.jsxs)(`div`,{className:`lightbox gallery-lightbox`,onClick:()=>setModalVideo(null),style:{position:`fixed`,inset:0,background:`rgba(20,18,18,0.92)`,zIndex:9999,display:`flex`,alignItems:`center`,justifyContent:`center`,padding:`20px`},children:[
      (0,G.jsx)(`button`,{type:`button`,className:`lightbox-close`,onClick:()=>setModalVideo(null),style:{position:`absolute`,top:`20px`,right:`24px`,color:`#fff`,fontSize:`32px`,background:`none`,border:`none`,cursor:`pointer`},children:`×`}),
      (0,G.jsxs)(`div`,{onClick:e=>e.stopPropagation(),style:{maxWidth:`800px`,width:`100%`,maxHeight:`85vh`,display:`flex`,flexDirection:`column`,gap:`10px`},children:[
        (0,G.jsx)(`video`,{src:modalVideo.videoSrc,controls:!0,autoPlay:!0,playsInline:!0,style:{width:`100%`,maxHeight:`72vh`,borderRadius:`8px`,background:`#000`}}),
        (0,G.jsx)(`p`,{style:{color:`#f1f0eb`,fontFamily:`var(--font-serif)`,fontSize:`16px`,fontStyle:`italic`,textAlign:`center`},children:modalVideo.alt})
      ]})
    ]}),document.body)
  ]})
}
function J_({items:list,index:e,onClose:t,onStep:n,host:r,origin:i,trigger:a}){
  let o=um(),s=list[e]||list[0],c=(0,v.useRef)(null),l=(0,v.useRef)(null),[u,d]=(0,v.useState)(1),[f,p]=(0,v.useState)(()=>window.matchMedia(`(max-width: 1023px), (hover: none), (max-height: 600px)`).matches);
  (0,v.useLayoutEffect)(()=>{let e=c.current;if(!e)return;let t=a.current,n=window.scrollY,i=document.body.style.overflow,o=Vm(),s=o?.isStopped,l=window.matchMedia(`(max-width: 1023px), (hover: none), (max-height: 600px)`),u=()=>{let t=r.getBoundingClientRect();e.style.setProperty(`--viewer-left`,`${t.left}px`),e.style.setProperty(`--viewer-top`,`${t.top}px`),e.style.setProperty(`--viewer-width`,`${t.width}px`),e.style.setProperty(`--viewer-height`,`${t.height}px`),p(l.matches)};return u(),document.body.style.overflow=`hidden`,o?.stop(),e.showModal(),window.addEventListener(`resize`,u),l.addEventListener(`change`,u),()=>{window.removeEventListener(`resize`,u),l.removeEventListener(`change`,u),e.close(),document.body.style.overflow=i,s||o?.start(),window.scrollTo(0,n),t?.focus({preventScroll:!0})}},[r,a]);
  let m=e=>{d(e),Ch.click(),n(e)};
  return(0,v.useEffect)(()=>{let e=e=>{if(e.key===`ArrowRight`)m(1);else if(e.key===`ArrowLeft`)m(-1);else return;e.preventDefault()};return window.addEventListener(`keydown`,e),()=>window.removeEventListener(`keydown`,e)}),(0,v.useEffect)(()=>{let e=c.current;if(!e)return;let t=e=>{e.ctrlKey||(e.preventDefault(),e.stopPropagation())};return e.addEventListener(`wheel`,t,{passive:!1}),()=>e.removeEventListener(`wheel`,t)},[]),(0,y.createPortal)((0,G.jsxs)(K.dialog,{ref:c,className:`lightbox gallery-lightbox${f?` gallery-lightbox--viewport`:``}`,"data-lenis-prevent":!0,"aria-modal":`true`,"aria-label":s.alt,onCancel:e=>{e.preventDefault(),t()},initial:{opacity:0},animate:{opacity:1},exit:{opacity:0,transition:{duration:.22,ease:`easeOut`}},transition:{duration:.25},onClick:e=>{e.target===e.currentTarget&&t()},children:[(0,G.jsxs)(`div`,{className:`lightbox-top`,children:[(0,G.jsxs)(`span`,{className:`lightbox-count`,children:[String(e+1).padStart(2,`0`),` / `,String(list.length).padStart(2,`0`)]}),(0,G.jsx)(`button`,{type:`button`,autoFocus:!0,className:`lightbox-close`,onClick:t,"aria-label":`Close media`,children:`×`})]}),(0,G.jsx)(`div`,{className:`lightbox-stage`,onClick:e=>e.target===e.currentTarget&&t(),children:(0,G.jsx)(K.div,{className:`lightbox-zoom`,initial:o||f?{opacity:0}:{opacity:0,x:i.x,y:i.y,scale:i.scale},animate:{opacity:1,x:0,y:0,scale:1},exit:o?{opacity:0}:{opacity:0,scale:.94,transition:{duration:.2,ease:`easeIn`}},transition:{type:`spring`,stiffness:300,damping:32,mass:.8},onClick:e=>e.target===e.currentTarget&&t(),children:(0,G.jsx)(cf,{mode:`popLayout`,initial:!1,custom:u,children:(0,G.jsxs)(K.figure,{className:`lightbox-figure`,initial:o?{opacity:0}:{opacity:0,x:u*60},animate:{opacity:1,x:0},exit:o?{opacity:0}:{opacity:0,x:u*-60},transition:{type:`spring`,stiffness:300,damping:32},onClick:e=>e.target===e.currentTarget&&t(),children:[s.videoSrc?(0,G.jsx)(`video`,{src:s.videoSrc,poster:s.src,controls:!0,autoPlay:!0,playsInline:!0}):(0,G.jsx)(`img`,{src:s.src,alt:s.alt,draggable:!1}),(0,G.jsx)(`figcaption`,{className:`hand`,children:s.alt.toLowerCase()})]},s.src)})})}),(0,G.jsx)(`button`,{type:`button`,className:`lightbox-arrow lightbox-arrow--prev`,onClick:()=>m(-1),"aria-label":`Previous item`,"data-sfx":`none`,children:`←`}),(0,G.jsx)(`button`,{type:`button`,className:`lightbox-arrow lightbox-arrow--next`,onClick:()=>m(1),"aria-label":`Next item`,"data-sfx":`none`,children:`→`}),(0,G.jsx)(`div`,{className:`lightbox-strip`,"aria-hidden":!0,children:list.map((t,n)=>(0,G.jsx)(`i`,{className:n===e?`is-on`:void 0},t.src))})]}),document.body)
}
function Y_(){
  let e=(0,v.useRef)(null),[cat,setCat]=(0,v.useState)(`pictures`),[t,n]=(0,v.useState)(null),[r,i]=(0,v.useState)(null),[a,o]=(0,v.useState)({x:0,y:0,scale:.85}),s=(0,v.useRef)(null),activeList=cat===`pictures`?HgPictures:HgVideos;
  (0,v.useEffect)(()=>{i(s.current?.closest(`.browser-viewport`)??document.body)},[]);
  (0,v.useEffect)(()=>{let e=s.current?.closest(`.browser-page`);if(!e)return;let t=new MutationObserver(()=>{e.classList.contains(`is-active`)||n(null)});return t.observe(e,{attributes:!0,attributeFilter:[`class`]}),()=>t.disconnect()},[]);
  let c=(0,v.useCallback)(e=>n(t=>t===null?t:(t+e+activeList.length)%activeList.length),[n,activeList.length]);
  return(0,G.jsxs)(`div`,{className:`page page-gallery`,ref:s,children:[
    (0,G.jsxs)(`div`,{className:`gallery-head`,children:[
      (0,G.jsxs)(`div`,{children:[
        (0,G.jsx)(`p`,{className:`page-kicker`,children:`gallery · ${cat}`}),
        (0,G.jsxs)(`h3`,{className:`page-title`,children:[`moments & `,(0,G.jsx)(`em`,{children:cat===`pictures`?`photographs.`:`videos.`})]})
      ]}),
      (0,G.jsxs)(`div`,{style:{display:`flex`,alignItems:`center`,gap:`12px`,flexWrap:`wrap`},children:[
        (0,G.jsxs)(`div`,{className:`subtab-switcher`,role:`tablist`,"aria-label":`Gallery categories: Pictures and Videos`,children:[
          (0,G.jsx)(`button`,{type:`button`,role:`tab`,"aria-selected":cat===`pictures`,className:`subtab-switch-btn${cat===`pictures`?` is-active`:``}`,onClick:()=>{Ch.pop(),setCat(`pictures`),n(null)},children:`1. Pictures`}),
          (0,G.jsx)(`button`,{type:`button`,role:`tab`,"aria-selected":cat===`videos`,className:`subtab-switch-btn${cat===`videos`?` is-active`:``}`,onClick:()=>{Ch.pop(),setCat(`videos`),n(null)},children:`2. Videos`})
        ]}),
        (0,G.jsx)(`p`,{className:`hand`,children:cat===`pictures`?`photographs pending upload — tap any frame.`:`videos pending upload — tap any frame.`})
      ]})
    ]}),
    (0,G.jsx)(`div`,{className:`gallery-grid`,children:activeList.map((item,idx)=>(0,G.jsxs)(`button`,{type:`button`,className:`gallery-item${item.tall?` is-tall`:``}`,style:{position:`relative`},onClick:ev=>{e.current=ev.currentTarget;let rect=ev.currentTarget.getBoundingClientRect(),hostRect=r?.getBoundingClientRect();hostRect&&o({x:rect.left+rect.width/2-(hostRect.left+hostRect.width/2),y:rect.top+rect.height/2-(hostRect.top+hostRect.height/2),scale:Math.min(.6,Math.max(.2,rect.width/(hostRect.width*.6)))}),Ch.pop(),n(idx)},"aria-label":`Open ${cat===`pictures`?`picture`:`video`}: ${item.alt}`,"data-sfx":`none`,children:[
      (0,G.jsx)(`img`,{src:item.src,alt:item.alt,loading:`lazy`,draggable:!1}),
      item.isVideo&&(0,G.jsx)(`span`,{className:`gallery-video-badge`,children:`▶ Video Placeholder`})
    ]},item.src))}),
    (0,G.jsx)(cf,{children:t!==null&&r&&(0,G.jsx)(J_,{items:activeList,index:t,onClose:()=>n(null),onStep:c,host:r,origin:a,trigger:e},`lightbox`)})
  ]})
}
var X_=new WeakMap;function Z_(e,t,n){let r=X_.get(e);r||X_.set(e,r=new Map),r.get(t)!==n&&(r.set(t,n),e.style.setProperty(t,n))}
var Q_=[
  {id:`about`,title:`about me`,path:`about`,icon:`🙂`},
  {id:`work`,title:`work log`,path:`work-log`,icon:`🗂️`},
  {id:`travel`,title:`mentoring`,path:`mentoring`,icon:`🎤`},
  {id:`gallery`,title:`gallery`,path:`gallery`,icon:`📷`}
],
$_=[
  {id:`fig-portfolio`,kind:`figma`,title:`Hassaan Ventures — Figma`,url:`figma.com/design/hassaan-ventures`,file:`portfolio`},
  {id:`fig-dashboard`,kind:`figma`,title:`Ideation & MVP Lab — Figma`,url:`figma.com/design/ideation-mvp-lab`,file:`dashboard`},
  {id:`claude`,kind:`claude`,title:`Claude`,url:`claude.ai/new`},
  {id:`gpt`,kind:`gpt`,title:`ChatGPT`,url:`chatgpt.com`},
  {id:`fig-ar`,kind:`figma`,title:`Stroque AI for B2B — Figma`,url:`figma.com/design/stroque-b2b`,file:`ar`}
],
ev=`(max-width: 1023px), (hover: none), (max-height: 600px)`,tv=e=>{let t=window.matchMedia(ev);return t.addEventListener(`change`,e),()=>t.removeEventListener(`change`,e)},nv=()=>(0,v.useSyncExternalStore)(tv,()=>window.matchMedia(ev).matches,()=>!1);
function rv({kind:e}){return e===`figma`?(0,G.jsxs)(`svg`,{viewBox:`0 0 38 57`,className:`tab-favicon`,"aria-hidden":!0,children:[(0,G.jsx)(`path`,{d:`M19 28.5a9.5 9.5 0 1 1 19 0 9.5 9.5 0 0 1-19 0z`,fill:`#1abcfe`}),(0,G.jsx)(`path`,{d:`M0 47.5A9.5 9.5 0 0 1 9.5 38H19v9.5a9.5 9.5 0 1 1-19 0z`,fill:`#0acf83`}),(0,G.jsx)(`path`,{d:`M19 0v19h9.5a9.5 9.5 0 1 0 0-19H19z`,fill:`#ff7262`}),(0,G.jsx)(`path`,{d:`M0 9.5A9.5 9.5 0 0 0 9.5 19H19V0H9.5A9.5 9.5 0 0 0 0 9.5z`,fill:`#f24e1e`}),(0,G.jsx)(`path`,{d:`M0 28.5A9.5 9.5 0 0 0 9.5 38H19V19H9.5A9.5 9.5 0 0 0 0 28.5z`,fill:`#a259ff`})]}):e===`claude`?(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,className:`tab-favicon`,"aria-hidden":!0,children:(0,G.jsx)(`path`,{d:`M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1 19.1 4.9`,stroke:`#d97757`,strokeWidth:`2.3`,strokeLinecap:`round`})}):e===`gpt`?(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,className:`tab-favicon`,"aria-hidden":!0,children:(0,G.jsx)(`circle`,{cx:`12`,cy:`12`,r:`8.5`,fill:`none`,stroke:`#10a37f`,strokeWidth:`2.2`})}):(0,G.jsxs)(`svg`,{viewBox:`0 0 24 24`,className:`tab-favicon`,"aria-hidden":!0,children:[(0,G.jsx)(`circle`,{cx:`11`,cy:`11`,r:`6.5`,fill:`none`,stroke:`#4285f4`,strokeWidth:`2.2`}),(0,G.jsx)(`path`,{d:`m16 16 4.5 4.5`,stroke:`#ea4335`,strokeWidth:`2.2`,strokeLinecap:`round`})]})}
var av=2;function ov(e,t,n){let r=e instanceof HTMLElement?e:null;for(;r&&r!==t;){let e=getComputedStyle(r);if((e.overflowY===`auto`||e.overflowY===`scroll`)&&r.scrollHeight>r.clientHeight+1){if((n>0?r.scrollHeight-r.clientHeight-r.scrollTop:r.scrollTop)>av)return r}r=r.parentElement}return null}
function sv(){
  let e=um(),t=(0,v.useRef)(null),n=(0,v.useRef)(null),r=nv(),i=(0,v.useRef)(null),a=(0,v.useRef)(null),o=(0,v.useRef)(null),[s,c]=(0,v.useState)($_),[l,u]=(0,v.useState)({kind:`group`,index:0}),p=(0,v.useRef)(0),m=(0,v.useRef)(0);
  (0,v.useEffect)(()=>{let r=t.current,a=n.current,o=i.current;if(!r||!a||!o||e)return;let s=0,c=()=>{s=0;let e=window.innerHeight,t=o.getBoundingClientRect().top,n=a.getBoundingClientRect().top,i=Math.min(1,Math.max(0,(e*.92-n)/(e*.52))),c=Math.min(1,Math.max(0,(e-t)/(e*.62)));Z_(r,`--enter`,c.toFixed(3)),Z_(r,`--about-reveal`,i.toFixed(3))},l=()=>{s||=requestAnimationFrame(c)};c(),window.addEventListener(`scroll`,l,{passive:!0}),window.addEventListener(`resize`,l);let u=new ResizeObserver(l);return u.observe(a),u.observe(o),()=>{cancelAnimationFrame(s),window.removeEventListener(`scroll`,l),window.removeEventListener(`resize`,l),u.disconnect()}},[e]);
  let{scrollYProgress:h}=bg(i),g=e=>{Ch.click(),a.current?.scrollTo({top:0});let t=i.current;if(!r&&t){let n=t.offsetHeight-window.innerHeight;if(n>0){let r=t.getBoundingClientRect().top+window.scrollY+(e+.35)/Q_.length*n,i=Vm();i?i.scrollTo(r):window.scrollTo({top:r,behavior:`smooth`})}}u({kind:`group`,index:e})};
  tm(h,`change`,e=>{if(r)return;let t=Math.min(Q_.length-1,Math.max(0,Math.floor(e*Q_.length)));t!==m.current&&(m.current=t,Ch.click(),a.current?.scrollTo({top:0}),u({kind:`group`,index:t}))});
  let _=e=>{Ch.click(),u({kind:`extra`,id:e})},y=(e,t)=>{e.stopPropagation(),Ch.click(),c(e=>{let n=e.findIndex(e=>e.id===t),r=e.filter(e=>e.id!==t);return l.kind===`extra`&&l.id===t&&u(r.length?{kind:`extra`,id:r[Math.min(n,r.length-1)].id}:{kind:`group`,index:0}),r})},b=(e,t)=>{c(n=>n.map(n=>n.id===e?{...n,title:t}:n))},x=()=>{let e=`search-${++p.current}`;c(t=>[...t,{id:e,kind:`search`,title:`New tab`,url:`google.com`}]),u({kind:`extra`,id:e}),requestAnimationFrame(()=>{o.current?.scrollTo({left:o.current.scrollWidth,behavior:`smooth`})})},S=e=>{let t=Q_.findIndex(t=>t.id===e);t>=0&&g(t)},C=(0,v.useRef)(null),w=e=>{e.pointerType===`mouse`||e.target.closest(`button, a, input`)||(C.current={x:e.clientX,y:e.clientY})},T=e=>{let t=C.current;if(C.current=null,!t||l.kind!==`group`)return;let n=e.clientX-t.x,r=e.clientY-t.y;Math.abs(n)<56||Math.abs(n)<Math.abs(r)*1.4||g((l.index+(n<0?1:-1)+Q_.length)%Q_.length)},E=s.find(e=>l.kind===`extra`&&e.id===l.id),D=l.kind===`group`?l.index:-1,O=D>=0?Q_[D].id:E?.id??`about`,k=E?`${E.url.split(`/`)[0]}`:`hassaan.me/`,A=E?E.url.includes(`/`)?`/${E.url.split(`/`).slice(1).join(`/`)}`:``:Q_[Math.max(0,D)].path,j=(0,v.useMemo)(()=>({about:(0,G.jsx)(W_,{}),work:(0,G.jsx)(G_,{}),travel:(0,G.jsx)(K_,{}),gallery:(0,G.jsx)(Y_,{})}),[]),M=e=>e.kind===`figma`?(0,G.jsx)(i_,{file:e.file}):e.kind===`claude`?(0,G.jsx)(Zg,{variant:`claude`}):e.kind===`gpt`?(0,G.jsx)(Zg,{variant:`gpt`}):(0,G.jsx)(l_,{onOpen:S,onTitle:t=>b(e.id,t)}),N=t=>{let n=l.kind===`extra`&&l.id===t.id;return(0,G.jsxs)(K.div,{layout:!e,initial:e?{opacity:0}:{opacity:0,width:0},animate:e?{opacity:1}:{opacity:1,width:`auto`},exit:e?{opacity:0}:{opacity:0,width:0},transition:{duration:.18},role:`tab`,tabIndex:0,"aria-selected":n,className:`tab tab--extra${n?` is-active`:``}`,onClick:()=>_(t.id),onKeyDown:e=>{(e.key===`Enter`||e.key===` `)&&(e.preventDefault(),_(t.id))},children:[(0,G.jsx)(rv,{kind:t.kind}),(0,G.jsx)(`span`,{className:`tab-title`,children:t.title}),(0,G.jsx)(`button`,{type:`button`,className:`tab-close`,"aria-label":`Close ${t.title}`,onClick:e=>y(e,t.id),"data-sfx":`none`,children:`×`})]},t.id)},P=s.filter(e=>e.kind!==`search`),F=s.filter(e=>e.kind===`search`),ee=D>=0&&D<Q_.length-1?Q_[D+1].title:null;
  return(0,G.jsxs)(`section`,{id:`experience`,ref:t,className:`browser-section paper-grain`,"aria-labelledby":`about-heading`,children:[
    (0,G.jsxs)(`div`,{className:`about-head`,ref:n,children:[
      (0,G.jsxs)(`div`,{className:`about-head-main`,children:[
        (0,G.jsx)(`p`,{className:`section-label`,children:`04 / About Me, Mentoring & Gallery`}),
        (0,G.jsxs)(`h2`,{id:`about-heading`,className:`about-title`,children:[
          (0,G.jsx)(`span`,{className:`about-title-line about-title-line--1`,children:`The person`}),` `,
          (0,G.jsxs)(`span`,{className:`about-title-line about-title-line--2`,children:[`behind the `,(0,G.jsxs)(`em`,{children:[`tabs.`,(0,G.jsx)(`svg`,{viewBox:`0 0 320 24`,className:`about-title-scribble`,"aria-hidden":!0,children:(0,G.jsx)(`path`,{d:`M4 16c30-10 58 6 92 2s60-12 96-6 58 10 86 4 28-6 38-5`,fill:`none`,stroke:`var(--color-accent)`,strokeWidth:`4`,strokeLinecap:`round`,pathLength:`1`})})]})]})
        ]})
      ]}),
      (0,G.jsxs)(`p`,{className:`about-note`,children:[(0,G.jsxs)(`svg`,{viewBox:`0 0 70 60`,className:`about-note-arrow`,"aria-hidden":!0,children:[(0,G.jsx)(`path`,{d:`M64 6C40 6 14 18 10 48`,fill:`none`,stroke:`currentColor`,strokeWidth:`2.2`,strokeLinecap:`round`}),(0,G.jsx)(`path`,{d:`M2 38l8 12 10-10`,fill:`none`,stroke:`currentColor`,strokeWidth:`2.2`,strokeLinecap:`round`,strokeLinejoin:`round`})]}),`yes, I have too many tabs open`]})
    ]}),
    (0,G.jsx)(`div`,{className:`browser-stage`,ref:i,style:r?void 0:{height:`calc(${Q_.length*75+100} * var(--stage-vh))`},children:(0,G.jsxs)(`div`,{"data-scroll-stage":!0,className:`browser-sticky`,children:[(0,G.jsxs)(`div`,{className:`browser`,children:[(0,G.jsxs)(`div`,{className:`browser-chrome`,children:[(0,G.jsxs)(`div`,{className:`browser-tabs`,children:[(0,G.jsxs)(`span`,{className:`browser-lights`,"aria-hidden":!0,children:[(0,G.jsx)(`i`,{}),(0,G.jsx)(`i`,{}),(0,G.jsx)(`i`,{})]}),(0,G.jsxs)(`div`,{className:`browser-tabs-scroll`,ref:o,role:`tablist`,"aria-label":`Browser tabs`,"data-lenis-prevent-wheel":!0,children:[(0,G.jsx)(cf,{initial:!1,children:P.map(N)}),(0,G.jsx)(`span`,{className:`tab-group-label`,children:`hassaan`}),(0,G.jsx)(`div`,{className:`tab-group`,children:Q_.map((e,t)=>(0,G.jsxs)(`button`,{type:`button`,role:`tab`,"aria-selected":t===D,className:`tab tab--group${t===D?` is-active`:``}`,onClick:()=>g(t),children:[(0,G.jsx)(`span`,{className:`tab-emoji`,"aria-hidden":!0,children:e.icon}),(0,G.jsx)(`span`,{className:`tab-title`,children:e.title})]},e.id))}),(0,G.jsx)(cf,{initial:!1,children:F.map(N)}),(0,G.jsx)(`button`,{type:`button`,className:`tab-new`,onClick:x,"aria-label":`Open a new tab`,"data-sfx":`pop`,children:`+`})]})]}),(0,G.jsxs)(`div`,{className:`browser-toolbar`,children:[(0,G.jsx)(`span`,{className:`browser-nav`,"aria-hidden":!0,children:`← → ↻`}),(0,G.jsxs)(`div`,{className:`browser-url`,children:[(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,width:`12`,height:`12`,"aria-hidden":!0,children:(0,G.jsx)(`path`,{d:`M7 10V8a5 5 0 0 1 10 0v2h1v10H6V10zm2 0h6V8a3 3 0 0 0-6 0z`,fill:`currentColor`})}),(0,G.jsx)(`span`,{children:k}),(0,G.jsx)(cf,{mode:`wait`,initial:!1,children:(0,G.jsx)(K.b,{initial:{opacity:0,y:4},animate:{opacity:1,y:0},exit:{opacity:0,y:-4},transition:{duration:.18},children:A},O)})]}),(0,G.jsx)(`span`,{className:`browser-avatar`,"aria-hidden":!0,children:(0,G.jsx)(`img`,{src:Bg,alt:``})})]})]}),(0,G.jsxs)(`div`,{className:`browser-viewport`,ref:a,onPointerDown:w,onPointerUp:T,onPointerCancel:()=>C.current=null,children:[Q_.map((e,t)=>(0,G.jsx)(`div`,{role:`tabpanel`,"aria-hidden":t!==D,className:`browser-page${t===D?` is-active`:``}`,children:j[e.id]},e.id)),s.map(e=>{let t=l.kind===`extra`&&l.id===e.id;return(0,G.jsx)(`div`,{role:`tabpanel`,"aria-hidden":!t,className:`browser-page browser-page--app${t?` is-active`:``}`,children:M(e)},e.id)}),D>=0&&(0,G.jsx)(`div`,{className:`browser-next`,children:ee?(0,G.jsxs)(`button`,{type:`button`,onClick:()=>g(D+1),children:[(0,G.jsx)(`span`,{className:`browser-next-hint`,children:r?`swipe or tap`:`keep scrolling`}),`next: `,(0,G.jsx)(`b`,{children:ee}),` `,r?`→`:`↓`]}):(0,G.jsxs)(`button`,{type:`button`,onClick:()=>g(0),children:[`that’s the tour — `,(0,G.jsx)(`b`,{children:`back to about me`}),` ↺`]})})]})]}),(0,G.jsx)(`div`,{className:`browser-progress`,"aria-hidden":!0,children:Q_.map((e,t)=>(0,G.jsx)(`i`,{className:t===D?`is-on`:void 0},e.id))})]})})
  ]})
}
var cv=[
  {label:`LinkedIn`,href:`https://www.linkedin.com/in/hassaan-shaik/`,path:`M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065m1.782 13.019H3.555V9h3.564zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0`},
  {label:`Instagram`,href:`https://www.instagram.com/hassaan.builds/`,path:`M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4H7.6m9.65 1.5a1.25 1.25 0 0 1 1.25 1.25A1.25 1.25 0 0 1 17.25 8 1.25 1.25 0 0 1 16 6.75a1.25 1.25 0 0 1 1.25-1.25M12 7a5 5 0 0 1 5 5 5 5 0 0 1-5 5 5 5 0 0 1-5-5 5 5 0 0 1 5-5m0 2a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3Z`},
  {label:`Topmate`,href:`https://topmate.io/hassaanshaik03`,path:`M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z`},
  {label:`GitHub`,href:`https://github.com/hassaanshaik123`,path:`M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.11.79-.25.79-.56v-2c-3.2.7-3.88-1.54-3.88-1.54-.52-1.33-1.28-1.68-1.28-1.68-1.05-.72.08-.71.08-.71 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.18-3.09-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11.02 11.02 0 0 1 5.78 0c2.2-1.49 3.16-1.18 3.16-1.18.63 1.59.24 2.76.12 3.05.74.81 1.18 1.83 1.18 3.09 0 4.41-2.7 5.38-5.26 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.68.8.56A11.5 11.5 0 0 0 12 .5Z`},
  {label:`Email`,href:`mailto:hassaanshaik.work@gmail.com`,path:`M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z`}
];
function lv({active:e=!0}){
  let t=(0,v.useRef)(null),n=(0,v.useRef)(!1);
  return(0,v.useEffect)(()=>{let r=t.current;if(!r||!e||n.current)return;let i=new IntersectionObserver(([e])=>{!e.isIntersecting||document.hidden||n.current||(n.current=!0,Ch.end(),i.disconnect())},{rootMargin:`0px 0px -12% 0px`,threshold:0});return i.observe(r),()=>i.disconnect()},[e]),(0,G.jsxs)(`footer`,{id:`contact`,ref:t,className:`site-footer`,children:[
    (0,G.jsxs)(`div`,{className:`footer-ridge`,"aria-hidden":`true`,children:[
      (0,G.jsxs)(`svg`,{viewBox:`0 0 1440 420`,preserveAspectRatio:`none`,children:[
        (0,G.jsx)(`path`,{className:`footer-ridge-far`,d:`M0 420V300l120-32 90 24 120-52 100 46 130-60 100 50 130-44 110 48 130-36 120 42 120-38 110 38 60-18v122Z`}),
        (0,G.jsx)(`path`,{className:`footer-ridge-near`,d:`M0 420V352l150-12 150-22 130-30 130-52 60-40 40-46 32-54 20-38 12-20 18 36 24 54 34 62 40 50 60 36 80 20 80-26 60-46 60 38 80 38 80 26 100 18v126Z`}),
        (0,G.jsx)(`path`,{className:`footer-ridge-line`,d:`M0 352l150-12 150-22 130-30 130-52 60-40 40-46 32-54 20-38 12-20 18 36 24 54 34 62 40 50 60 36 80 20 80-26 60-46 60 38 80 38 80 26 100 18`}),
        (0,G.jsx)(`path`,{className:`footer-ridge-zone`,d:`M392 70H1064`})
      ]}),
      (0,G.jsx)(`span`,{className:`footer-summit`}),
      (0,G.jsxs)(`span`,{className:`footer-summit-label`,children:[`fly high `,(0,G.jsx)(`span`,{"aria-hidden":`true`,children:`·`}),` rise together`]}),
      (0,G.jsx)(`span`,{className:`footer-zone-label`,children:`next horizon — building 0 to 1`})
    ]}),
    (0,G.jsxs)(`div`,{className:`footer-body paper-grain`,children:[
      (0,G.jsxs)(`div`,{className:`footer-inner`,children:[
        (0,G.jsxs)(`div`,{className:`footer-say`,children:[
          (0,G.jsxs)(`h2`,{className:`footer-title`,children:[`Let's `,(0,G.jsx)(`em`,{children:`rise together.`})]}),
          (0,G.jsx)(`p`,{className:`footer-note`,children:`Whether you want to talk about building ventures from 0 to 1, consultative sales, business development, or solving meaningful problems together — I'd love to listen and connect.`}),
          (0,G.jsx)(`span`,{className:`footer-hand`,children:`all set to fly high now! 🤞`})
        ]}),
        (0,G.jsxs)(`div`,{className:`footer-reach`,children:[
          (0,G.jsxs)(`a`,{className:`footer-resume`,href:`https://topmate.io/hassaanshaik03`,target:`_blank`,rel:`noopener noreferrer`,children:[
            (0,G.jsx)(`span`,{children:`Contact me`}),
            (0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,"aria-hidden":`true`,children:(0,G.jsx)(`path`,{d:`M7 17 17 7M9 7h8v8`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.8`,strokeLinecap:`round`,strokeLinejoin:`round`})})
          ]}),
          (0,G.jsx)(`a`,{className:`footer-email`,href:`mailto:hassaanshaik.work@gmail.com`,children:`hassaanshaik.work@gmail.com`}),
          (0,G.jsx)(`ul`,{className:`footer-socials`,children:cv.map(e=>(0,G.jsx)(`li`,{children:(0,G.jsxs)(`a`,{href:e.href,target:e.href.startsWith(`http`)?`_blank`:void 0,rel:e.href.startsWith(`http`)?`noopener noreferrer`:void 0,children:[(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,"aria-hidden":`true`,children:(0,G.jsx)(`path`,{d:e.path})}),e.label]})},e.label))})
        ]})
      ]}),
      (0,G.jsxs)(`div`,{className:`footer-colophon`,children:[
        (0,G.jsxs)(`span`,{children:[`© `,new Date().getFullYear(),` Muhammad Hassaan · Masters' Union School of Business`]}),
        (0,G.jsx)(`p`,{children:`Let's rise together.`})
      ]})
    ]})
  ]})
}"""

# ============================================================================
# SPLICE 5: 3D DOOR WORKSTATION ENTRY (bB, CB, wB, TB, EB, DB)
# Replaces the VR headset with an interactive 3D Door in Three.js!
# ============================================================================
SPLICE_5 = r"""var _B=``;
function bB({clone:e=!1,openProgress:t=0,hingeRef:n}){
  return(0,G.jsxs)(`group`,{scale:1.15,children:[
    (0,G.jsx)(`mesh`,{position:[0,0,-0.08],children:[(0,G.jsx)(`boxGeometry`,{args:[1.62,2.62,0.14]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#242620`,roughness:0.45,metalness:0.15})]}),
    (0,G.jsx)(`mesh`,{position:[0,0,-0.05],children:[(0,G.jsx)(`planeGeometry`,{args:[1.34,2.36]}),(0,G.jsx)(`meshBasicMaterial`,{color:`#141212`})]}),
    (0,G.jsx)(`mesh`,{position:[0,0,-0.03],children:[(0,G.jsx)(`planeGeometry`,{args:[1.24,2.24]}),(0,G.jsx)(`meshBasicMaterial`,{color:`#e25531`,transparent:!0,opacity:0.22})]}),
    (0,G.jsxs)(`group`,{ref:n,position:[-0.67,0,0.01],rotation:[0,-t*Math.PI*0.74,0],children:[
      (0,G.jsx)(`mesh`,{position:[0.67,0,0],children:[(0,G.jsx)(`boxGeometry`,{args:[1.34,2.36,0.09]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#b53c1f`,roughness:0.38,metalness:0.12})]}),
      (0,G.jsx)(`mesh`,{position:[0.67,0.56,0.052],children:[(0,G.jsx)(`boxGeometry`,{args:[1.02,0.82,0.025]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#8f2d15`,roughness:0.48,metalness:0.08})]}),
      (0,G.jsx)(`mesh`,{position:[0.67,-0.56,0.052],children:[(0,G.jsx)(`boxGeometry`,{args:[1.02,0.82,0.025]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#8f2d15`,roughness:0.48,metalness:0.08})]}),
      (0,G.jsx)(`mesh`,{position:[1.16,-0.04,0.08],children:[(0,G.jsx)(`sphereGeometry`,{args:[0.065,24,24]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#ead56f`,roughness:0.2,metalness:0.85})]}),
      (0,G.jsx)(`mesh`,{position:[1.16,-0.04,0.05],children:[(0,G.jsx)(`cylinderGeometry`,{args:[0.035,0.035,0.06,16]}),(0,G.jsx)(`meshStandardMaterial`,{color:`#ead56f`,roughness:0.25,metalness:0.8})]})
    ]})
  ]})
}
function CB({progress:e,onTriggerOpen:t}){
  let r=(0,v.useRef)(null),hinge=(0,v.useRef)(null),n=dI(e=>e.invalidate);
  return(0,v.useEffect)(()=>(n(),e.on(`change`,()=>n())),[e,n]),fI(()=>{
    if(!r.current)return;
    let p=e.get(),
        approach=Math.min(p/.25,1),
        swing=Math.min(Math.max((p-.12)/.5,0),1),
        enter=Math.min(Math.max((p-.52)/.38,0),1),
        ease=x=>1-(1-x)**3,
        sc=.92+ease(approach)*0.65+ease(enter)*2.6;
    r.current.scale.setScalar(sc);
    r.current.rotation.y=(1-ease(approach))*0.28-ease(swing)*0.08;
    r.current.rotation.x=.06*(1-ease(swing));
    r.current.position.y=-.18*(1-ease(approach))+.12*ease(enter);
    r.current.position.z=ease(enter)*1.65;
    r.current.visible=p<.995;
    if(hinge.current){
      hinge.current.rotation.y=-ease(swing)*Math.PI*0.76;
    }
  }),(0,G.jsx)(`group`,{ref:r,onClick:t,children:(0,G.jsx)(bB,{hingeRef:hinge})})
}
function wB({progress:e,onTriggerOpen:t}){
  return(0,G.jsxs)(RL,{frameloop:`demand`,camera:{position:[0,0,6],fov:32},dpr:[1,1.6],gl:{antialias:!0,alpha:!0},children:[
    (0,G.jsx)(`ambientLight`,{intensity:.85,color:`#ffffff`}),
    (0,G.jsx)(`hemisphereLight`,{args:[`#fff8f0`,`#242620`,.65]}),
    (0,G.jsx)(`directionalLight`,{position:[3,4,5],intensity:1.8,color:`#ffffff`}),
    (0,G.jsx)(`directionalLight`,{position:[-4,2,-3],intensity:.75,color:`#d8631f`}),
    (0,G.jsx)(`pointLight`,{position:[0,0,1.2],intensity:1.2,color:`#ead56f`}),
    (0,G.jsx)(CB,{progress:e,onTriggerOpen:t})
  ]})
}
function TB(){try{let e=document.createElement(`canvas`);return!!(e.getContext(`webgl`)||e.getContext(`experimental-webgl`))}catch{return!1}}
var EB=[{at:0,text:`Click the door (or scroll) to open & enter my workstation.`},{at:.25,text:`Opening the door — let's go look inside.`}];
function DB(){
  let e=(0,v.useRef)(null),{scrollYProgress:t}=bg(e),n=um(),[r,i]=(0,v.useState)(!0);
  (0,v.useEffect)(()=>{i(TB())},[]);
  let a=am(t,e=>Math.max(0,Math.min((e-.78)/.12,1))*3.4),
      o=am(t,[0,.15,.68,.84,1],[1,1,1,0,0]),
      [s,c]=(0,v.useState)(EB[0].text),
      openDoorAndEnter=(0,v.useCallback)(()=>{
        Ch.clunk();
        setTimeout(()=>Ch.whoosh(),260);
        let workEl=document.getElementById(`work`);
        if(!workEl)return;
        let lenis=Vm();
        if(lenis){
          lenis.scrollTo(workEl,{duration:2.2});
        }else{
          workEl.scrollIntoView({behavior:`smooth`});
        }
      },[]);
  return(0,v.useEffect)(()=>t.on(`change`,e=>{let t=[...EB].reverse().find(t=>e>=t.at);t&&c(t.text)}),[t]),n||!r?(0,G.jsxs)(`section`,{className:`paper-grain flex min-h-[70vh] flex-col items-center justify-center gap-6 bg-[var(--color-paper)] px-6 py-24 text-center`,children:[(0,G.jsx)(`p`,{className:`max-w-sm text-lg text-[var(--color-ink-dim)]`,children:`Open the Door — heading straight into Entrepreneurship Experiments.`}),(0,G.jsx)(`a`,{href:`#work`,className:`text-sm font-medium text-[var(--color-ink)] underline decoration-[var(--color-accent)] decoration-2 underline-offset-4`,children:`Open the Door →`})]}):(0,G.jsx)(`div`,{ref:e,className:`headset-wrapper`,children:(0,G.jsxs)(`div`,{"data-scroll-stage":!0,className:`headset-stage overflow-hidden bg-[var(--color-paper)]`,children:[(0,G.jsx)(`div`,{className:`absolute inset-0`,style:{cursor:`var(--cursor-pointer)`},onClick:openDoorAndEnter,children:(0,G.jsx)(wB,{progress:t,onTriggerOpen:openDoorAndEnter})}),(0,G.jsxs)(K.div,{style:{opacity:o},className:`pointer-events-none absolute inset-x-0 bottom-[9%] flex flex-col items-center gap-3 text-center`,children:[(0,G.jsxs)(`button`,{type:`button`,onClick:openDoorAndEnter,className:`door-stage-cta`,children:[(0,G.jsx)(`span`,{className:`door-stage-cta-dot`,"aria-hidden":!0}),(0,G.jsx)(`span`,{children:`Open the Door`}),(0,G.jsx)(`span`,{"aria-hidden":!0,children:`→`})]}),(0,G.jsx)(`p`,{className:`text-base text-[var(--color-ink-dim)] sm:text-lg`,children:s})]}),(0,G.jsx)(`a`,{href:`#work`,className:`tabular absolute bottom-8 right-6 z-20 text-[11px] text-[var(--color-ink-dim)] underline decoration-[var(--color-line)] underline-offset-4 transition-colors hover:text-[var(--color-ink)] sm:right-10`,children:`SKIP TO WORKSTATION →`}),(0,G.jsx)(K.div,{"aria-hidden":!0,"data-progress-iris":!0,style:{scale:a},className:`pointer-events-none absolute left-1/2 top-1/2 h-[60vmax] w-[60vmax] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[var(--color-void)]`})]})})
}"""

# ============================================================================
# SPLICE 6: HERO PINBOARD, CAT IN WORDMARK, HERO SECTION, OUTRO, WORKSTATION INTRO, AND SUMMIT SECTION
# ============================================================================
pos_vb = src.find("function VB(){")
pos_tv_scanner = src.find("function tV(e,t){")
pos_nv_cat = src.find("var nV=`M262 120")
pos_vv = src.find("var vV={Juspay:")
pos_qu = src.find("function QU({anchor:")
pos_fw = src.find("var fW=[{from:0")

vb_to_tv_code = src[pos_vb:pos_tv_scanner]
cat_sprite_to_vv_code = src[pos_nv_cat:pos_vv].replace("Samay's cat", "Hassaan's cat")
qu_to_fw_code = src[pos_qu:pos_fw]

SPLICE_6 = r"""var zB=[
  {src:`/hero/photo-1.jpg`,fallback:`/hero/photo-1.jpg`,alt:`Muhammad Hassaan at Canton Fair Phase 1 in Guangzhou, China`,caption:`Canton Fair Phase 1 · Guangzhou, China.`,tilt:-7},
  {src:`/hero/photo-2.jpg`,fallback:`/hero/photo-2.jpg`,alt:`Muhammad Hassaan learning consultative selling at Dropshipping Mela, Masters' Union`,caption:`consultative selling · Dropshipping Mela, Masters' Union.`,tilt:3},
  {src:`/hero/photo-3.jpg`,fallback:`/hero/photo-3.jpg`,alt:`Muhammad Hassaan on his first cruise across the Arabian Sea from Kochi to Mumbai on Cordelia Cruises`,caption:`first cruise in the Arabian Sea · Kochi to Mumbai, Cordelia Cruises.`,tilt:-4}
];
function BB(){let[e,t]=(0,v.useState)(null),n=um();return(0,G.jsxs)(`div`,{className:`hero-pinboard`,children:[zB.map((r,i)=>{let a=e===i;return(0,G.jsxs)(K.figure,{className:`hero-polaroid hero-polaroid--${i+1}`,initial:!1,animate:{rotate:a?0:r.tilt,scale:a?1.14:1,y:a?-22:0,zIndex:a?10:i+1,boxShadow:a?`0 28px 50px #2426203a, 0 0 0 1px #2426200a`:`0 12px 30px #2426201f, 0 0 0 1px #2426200a`},whileHover:a||n?void 0:{rotate:r.tilt*.35,y:-8,zIndex:9},whileTap:n?void 0:{scale:a?1.08:.97},transition:{type:`spring`,stiffness:260,damping:20},onClick:()=>t(a?null:i),role:`button`,"data-sfx":`pop`,tabIndex:0,"aria-pressed":a,"aria-label":`${r.caption} — ${a?`put the photo back`:`bring the photo forward`}`,onKeyDown:e=>{(e.key===`Enter`||e.key===` `)&&(e.preventDefault(),t(a?null:i))},children:[(0,G.jsx)(`div`,{className:`hero-polaroid-window`,children:(0,G.jsx)(`img`,{src:r.src,alt:r.alt,loading:i===0?`eager`:`lazy`,decoding:`async`,draggable:!1,onError:e=>{let t=e.currentTarget;t.src!==r.fallback&&(t.src=r.fallback)}})}),(0,G.jsx)(`figcaption`,{className:`hero-polaroid-caption`,children:r.caption})]},r.src)}),(0,G.jsxs)(`span`,{className:`hero-hand`,"aria-hidden":!0,children:[(0,G.jsx)(kB,{className:`hero-arrow`}),`that’s me`]})]})}
""" + vb_to_tv_code + r"""function tV(e,t){let n=e.firstChild,r=e.querySelector(`.hero-wordmark-baseline`);if(!n||n.nodeType!==Node.TEXT_NODE||!r)return null;let i=getComputedStyle(e),a=Number.parseFloat(i.fontSize),o=`${i.fontStyle} ${i.fontWeight} ${WB}px ${i.fontFamily}`,s=`${o}|${[...document.fonts].map(e=>e.status).join(``)}`;YB.has(s)||YB.set(s,QB(o));let c=YB.get(s);if(!c)return null;let{bowl:u}=c,d=u.bottom-u.top,f=Math.max(...[...u.rows.values()].map(e=>e.right-e.left)),m=Math.max(GB/(a/WB),f*1.02),g=a/WB,_=t.getBoundingClientRect(),v=r.getBoundingClientRect().top-_.top,y=e=>{let t=document.createRange();return t.setStart(n,e),t.setEnd(n,e+1),t.getBoundingClientRect().left-_.left},b=(e,t,n)=>({x:e+(t-qB)*g,bottom:v+(n-JB)*g}),x=(n.textContent??``).toLowerCase(),S=x.lastIndexOf(`a`),C=x.indexOf(`a`);if(S<0||C<0)return null;let w=u.bottom-d*.04;return{body:m*g,shelf:v-c.xHeight*g,y:{id:`y`,scale:.92,...b(y(S),eV(u,u.top+d*.55),w)},a:{id:`a`,scale:.84,...b(y(C),eV(u,u.top+d*.55),w)}}}""" + cat_sprite_to_vv_code + r"""var vV={"Masters' Union":`/brands/masters-union.svg`,"Hustlers' Edge":`/brands/hustlers-edge.svg`,"Delhi University":`/brands/delhi-university.svg`};
function yV({background:e=!1}){
  let t=e?`p`:`h1`,n=(0,v.useRef)(null);
  return(0,G.jsxs)(`header`,{className:`hero paper-grain`,children:[
    (0,G.jsx)(VB,{}),
    (0,G.jsxs)(`nav`,{className:`hero-nav`,"aria-label":`Primary`,children:[
      (0,G.jsxs)(`ul`,{className:`hero-nav-links`,children:[
        (0,G.jsx)(`li`,{children:(0,G.jsx)(`a`,{href:`#work`,children:`work`})}),
        (0,G.jsx)(`li`,{children:(0,G.jsx)(`a`,{href:`#experience`,children:`about me`})}),
        (0,G.jsx)(`li`,{children:(0,G.jsxs)(`a`,{href:`#experience`,className:`hero-nav-resume`,children:[`resume`,(0,G.jsx)(`svg`,{width:`12`,height:`12`,viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`2.2`,strokeLinecap:`round`,strokeLinejoin:`round`,"aria-hidden":!0,children:(0,G.jsx)(`path`,{d:`M12 4v12m0 0l-5-5m5 5l5-5M5 20h14`})})]})})
      ]}),
      (0,G.jsxs)(`a`,{href:`#contact`,className:`hero-say-hey`,children:[`say hey`,(0,G.jsx)(`svg`,{width:`12`,height:`12`,viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`2.2`,strokeLinecap:`round`,strokeLinejoin:`round`,"aria-hidden":!0,children:(0,G.jsx)(`path`,{d:`M7 17L17 7M8 7h9v9`})})]})
    ]}),
    (0,G.jsx)(`div`,{className:`hero-eyebrow`,children:(0,G.jsx)(`p`,{className:`section-label`,children:`Entrepreneurship · Consultative Sales · Business Development`})}),
    (0,G.jsxs)(`div`,{className:`hero-stage`,children:[
      (0,G.jsx)(`div`,{className:`hero-intro-row`,children:(0,G.jsxs)(`div`,{className:`hero-intro-wrap`,children:[(0,G.jsx)(`p`,{className:`hero-intro`,children:`Hey! I'm`}),(0,G.jsx)(OB,{className:`hero-squiggle`})]})}),
      (0,G.jsxs)(t,{className:`hero-name`,children:[
        (0,G.jsxs)(`span`,{ref:n,className:`hero-name-word`,children:[`Hassaan`,(0,G.jsx)(`span`,{className:`hero-wordmark-baseline`,"aria-hidden":`true`})]}),
        (0,G.jsx)(AB,{}),
        (0,G.jsx)(`span`,{className:`sr-only`,children:` — I listen to people & solve their problems by giving them tailored solutions.`})
      ]}),
      (0,G.jsx)(_V,{wordmarkRef:n,disabled:e}),
      (0,G.jsx)(BB,{})
    ]}),
    (0,G.jsxs)(`div`,{className:`hero-foot`,children:[
      (0,G.jsxs)(`p`,{className:`hero-statement`,children:[
        `I listen to people & solve their problems by giving them `,
        (0,G.jsx)(p_,{type:`circle`,delay:.35,children:(0,G.jsx)(`em`,{children:`tailored solutions`})}),
        `.`
      ]}),
      (0,G.jsx)(`div`,{className:`hero-blurb`,children:(0,G.jsxs)(`p`,{children:[
        (0,G.jsx)(RB,{icon:`dashboard`,children:`0→1 ventures`}),
        `, `,
        (0,G.jsx)(RB,{icon:`phone`,children:`consultative sales`}),
        ` & `,
        (0,G.jsx)(RB,{icon:`glasses`,children:`problem solving`}),
        `.`
      ]})})
    ]}),
    (0,G.jsxs)(`div`,{className:`hero-context`,children:[
      (0,G.jsx)(`p`,{className:`section-label`,children:`Experiences`}),
      (0,G.jsx)(`ul`,{className:`hero-orgs`,"aria-label":`Mini Experience`,children:I_.map(e=>{
        let t=e.period===`Current`;
        return(0,G.jsxs)(`li`,{className:`hero-org${t?` hero-org--current`:``}`,children:[
          vV[e.org]?(0,G.jsx)(`img`,{src:vV[e.org],alt:``,className:`hero-org-mark`,width:32,height:32}):(0,G.jsx)(`span`,{className:`hero-org-mark hero-org-mark--mono`,"aria-hidden":!0,children:e.org[0]}),
          e.sub?(0,G.jsxs)(`span`,{className:`hero-org-stack`,children:[
            (0,G.jsx)(`span`,{className:`hero-org-name`,children:e.org}),
            (0,G.jsx)(`span`,{className:`hero-org-sub`,children:e.sub})
          ]}):(0,G.jsx)(`span`,{className:`hero-org-name`,children:e.org}),
          t&&(0,G.jsxs)(`span`,{className:`hero-org-now`,children:[(0,G.jsx)(`span`,{className:`hero-org-now-dot`,"aria-hidden":!0}),`currently here`]})
        ]},e.org)
      })})
    ]})
  ]})
}
function bV(e,t,n){let r=Wc(t,n);return am(e,e=>r(e))}
function xV({text:e,base:t,className:n,progress:r,start:i,end:a}){let o=bV(r,[i,a],[.12,1]),s=bV(r,[i,a],[.16,0]),c=bV(r,[i,a],[5,0]),l=am(s,e=>`${e}em`),u=am(c,e=>`blur(${e}px)`);return(0,G.jsx)(K.span,{className:`${t} ${n??``}`,style:{opacity:o,y:l,filter:u},children:e})}
var SV=[{from:0,to:.3,lines:[[{text:`all`},{text:`set`},{text:`to`}],[{text:`fly`},{text:`high`},{text:`now!`}]]},{from:.26,to:.62,lines:[[{text:`let's`},{text:`rise`}],[{text:`together.`,className:`outro-accent`}]]}],CV=.04;
function wV({beat:e,index:t,progress:n}){let r=t===SV.length-1,i=[e.from,e.from+CV,e.to-CV,e.to],a=bV(n,r?[e.from,e.from+CV,.92,1]:i,[0,1,1,0].map((e,n)=>t===0&&n===0?1:e)),o=bV(n,i,[34,0,0,r?-18:-44]),s=e.lines.flat(),c=(e.to-e.from)*.62/s.length,l=e.lines.map((t,n)=>e.lines.slice(0,n).reduce((e,t)=>e+t.length,0));return(0,G.jsx)(K.div,{className:`outro-beat`,style:{opacity:a,y:o},children:e.lines.map((t,r)=>(0,G.jsx)(`div`,{className:`outro-line`,children:t.map((t,i)=>{let a=e.from+CV*.5+c*(l[r]+i);return(0,G.jsx)(xV,{text:t.text,base:`outro-word`,className:t.className,progress:n,start:a,end:a+c*1.4},`${r}-${t.text}`)})},r))})}
function TV(){let e=(0,v.useRef)(null),{scrollYProgress:t}=bg(e);return um()?(0,G.jsxs)(`section`,{className:`outro outro--static`,"aria-label":`Sign-off`,children:[(0,G.jsx)(`p`,{className:`outro-line`,children:`all set to fly high now!`}),(0,G.jsxs)(`p`,{className:`outro-line`,children:[`let's rise `,(0,G.jsx)(`em`,{className:`outro-accent`,children:`together.`})]})]}):(0,G.jsx)(`div`,{className:`outro`,ref:e,children:(0,G.jsx)(`div`,{"data-scroll-stage":!0,className:`outro-stage`,children:SV.map((e,n)=>(0,G.jsx)(wV,{beat:e,index:n,progress:t},n))})})}
function MiniDoorSpin(){
  let e=(0,v.useRef)(null),hinge=(0,v.useRef)(null);
  return fI(t=>{
    if(!e.current)return;
    let n=t.clock.getElapsedTime();
    e.current.rotation.y=Math.sin(n*.85)*.38;
    e.current.rotation.x=.1+Math.sin(n*1.2)*.04;
    e.current.position.y=Math.sin(n*1.5)*.06;
    if(hinge.current){
      hinge.current.rotation.y=-(0.32+Math.sin(n*1.4)*0.18);
    }
  }),(0,G.jsx)(`group`,{ref:e,scale:1.15,children:(0,G.jsx)(bB,{hingeRef:hinge,openProgress:0.25})})
}
function EV({active:e=!0,idle:t=`never`,layoutSize:r=!1}){
  return(0,G.jsxs)(RL,{resize:{offsetSize:r},frameloop:e?`always`:t,camera:{position:[0,0,6],fov:30},dpr:[1,1.6],gl:{antialias:!0,alpha:!0},children:[
    (0,G.jsx)(`ambientLight`,{intensity:.9}),
    (0,G.jsx)(`directionalLight`,{position:[3,4,5],intensity:1.6}),
    (0,G.jsx)(`directionalLight`,{position:[-4,2,-3],intensity:.6,color:`#d8631f`}),
    (0,G.jsx)(MiniDoorSpin,{})
  ]})
}
var DV=168,OV=e=>e/DV,kV=OV(8.4),AV=1-OV(34),
jV=[
  {from:0,to:OV(76),underline:!0,lines:[[{text:`welcome`},{text:`to`},{text:`my`}],[{text:`workstation.`,className:`intro-accent`}]]},
  {from:OV(72),to:1,lines:[[{text:`Open`},{text:`the`},{text:`Door`,className:`intro-accent`}]]}
];
function MV(e,t,n){let r=Wc(t,n);return am(e,e=>r(e))}
function NV({word:e,progress:t,start:n,end:r}){let i=MV(t,[n,r],[.12,1]),a=MV(t,[n,r],[.18,0]),o=MV(t,[n,r],[6,0]),s=am(a,e=>`${e}em`),c=am(o,e=>`blur(${e}px)`);return(0,G.jsx)(K.span,{className:`intro-word ${e.className??``}`,style:{opacity:i,y:s,filter:c},children:e.text})}
function PV({progress:e,start:t}){let[n,r]=(0,v.useState)(()=>e.get()>=t),[i,a]=(0,v.useState)(n);tm(e,`change`,e=>{let i=n?e>=t-OV(3):e>=t;i!==n&&(r(i),i&&a(!0))});let o=MV(e,[AV-OV(6),AV+OV(1.2)],[1,0]),[s,c]=(0,v.useState)(!0);return tm(o,`change`,e=>c(e>.001)),(0,G.jsx)(K.span,{className:`intro-glyph`,style:{opacity:o,cursor:`var(--cursor-pointer)`},onClick:()=>{Ch.clunk();let w=document.getElementById(`work`);Vm()?Vm().scrollTo(w,{duration:2.2}):w?.scrollIntoView({behavior:`smooth`})},"aria-hidden":!0,children:(0,G.jsx)(K.span,{className:`intro-glyph-in`,initial:!1,animate:n?{opacity:1,scale:1,rotate:0}:{opacity:0,scale:.4,rotate:-25},transition:{duration:n?.75:.4,ease:[.22,1,.36,1]},onAnimationComplete:()=>a(n),children:(0,G.jsx)(EV,{active:i&&s})})})}
function FV({progress:e,start:t,end:n}){let r=MV(e,[t,n],[0,1]),i=am(r,e=>+(e>.01));return(0,G.jsx)(`svg`,{viewBox:`0 0 400 22`,className:`intro-underline`,fill:`none`,preserveAspectRatio:`none`,"aria-hidden":!0,children:(0,G.jsx)(K.path,{d:`M4 14c40-10 70 6 112 2s64-12 104-6 62 10 96 4 52-8 80-4`,stroke:`var(--color-accent)`,strokeWidth:`4`,strokeLinecap:`round`,style:{pathLength:r,opacity:i}})})}
function IV({beat:e,index:t,progress:n}){let r=t===jV.length-1,i=[e.from,e.from+kV,e.to-kV,e.to],a=MV(n,r?[e.from,e.from+kV,AV+OV(4.8),1-OV(7.2)]:i,[0,1,1,0].map((e,n)=>t===0&&n===0?1:e)),o=MV(n,i,[t===0?0:40,0,0,r?0:-50]),s=MV(n,r?[AV,1-OV(7.2)]:[e.to-kV,e.to],[1,r?3.2:.97]),c=e.lines.flat(),l=t===0?e.from:e.from+kV*.5,u=r?(AV-e.from)*.55:(e.to-e.from)*.6,d=u/c.length,f=e.lines.map((t,n)=>e.lines.slice(0,n).reduce((e,t)=>e+t.length,0));return(0,G.jsxs)(K.div,{className:`intro-beat${r?` intro-beat--zoom`:``}`,style:{opacity:a,y:o,scale:s},children:[e.lines.map((e,t)=>(0,G.jsx)(`div`,{className:`intro-line`,children:e.map((e,r)=>{let i=l+d*(f[t]+r),a=i+d*1.4;return(0,G.jsx)(NV,{word:e,progress:n,start:i,end:a},`${t}-${e.text}`)})},t)),r&&(0,G.jsx)(PV,{progress:n,start:e.from+u*.9}),e.underline&&(0,G.jsx)(FV,{progress:n,start:e.from+u*.85,end:e.to-kV*2})]})}
function LV(){let e=(0,v.useRef)(null),{scrollYProgress:t}=bg(e),n=um(),r=MV(t,[0,OV(14),OV(30)],[1,1,0]),i=MV(t,[AV+OV(14.4),1-OV(2.4)],[1,0]);return n?(0,G.jsxs)(`section`,{className:`intro-static paper-grain`,"aria-label":`Welcome to my workstation`,children:[(0,G.jsxs)(`p`,{className:`intro-line`,children:[`welcome to my `,(0,G.jsx)(`span`,{className:`intro-accent`,children:`workstation.`})]}),(0,G.jsx)(`p`,{className:`intro-line`,children:`Open the Door`})]}):(0,G.jsxs)(`section`,{ref:e,className:`intro`,"aria-label":`Welcome to my workstation`,children:[(0,G.jsx)(`p`,{className:`sr-only`,children:`Welcome to my workstation. Open the Door.`}),(0,G.jsxs)(K.div,{"data-scroll-stage":!0,className:`intro-stage paper-grain`,style:{opacity:i},"aria-hidden":!0,children:[jV.map((e,n)=>(0,G.jsx)(IV,{beat:e,index:n,progress:t},n)),(0,G.jsxs)(K.p,{className:`intro-hint`,style:{opacity:r},children:[`keep scrolling `,(0,G.jsx)(`span`,{children:`↓`})]})]})]})}
var VU=[{id:`academic`,label:`Academic Projects`},{id:`business`,label:`Business Projects`}],
GU=(e,t)=>e.category===t,
YU=[
  {kind:`image`,id:`bharti-airtel`,category:`academic`,src:`/assets/covers/bharti-airtel.svg`,thumb:`/assets/covers/bharti-airtel.svg`,ratio:1200/900,cardRatio:1200/900,device:!1,caption:`Bharti Airtel — Business Strategy`,href:`/work/bharti-airtel`},
  {kind:`image`,id:`ownwise`,category:`academic`,src:`/assets/covers/ownwise.svg`,thumb:`/assets/covers/ownwise.svg`,ratio:1200/900,cardRatio:1200/900,device:!1,caption:`Ownwise — DBM2`,href:`/work/ownwise`},
  {kind:`image`,id:`stride`,category:`academic`,src:`/assets/covers/stride.svg`,thumb:`/assets/covers/stride.svg`,ratio:1200/900,cardRatio:1200/900,device:!1,caption:`Stride — Fintech DBM1`,href:`/work/stride`},
  {kind:`image`,id:`gostops`,category:`business`,src:`/assets/covers/gostops.svg`,thumb:`/assets/covers/gostops.svg`,ratio:1200/900,cardRatio:1200/900,device:!1,caption:`GoSTOPS — Business Project`,href:`/work/gostops`},
  {kind:`image`,id:`pepperfry`,category:`business`,src:`/assets/pepperfry.png`,thumb:`/assets/pepperfry.png`,ratio:1024/491,cardRatio:1200/900,device:!1,caption:`Pepperfry — Business Project`,href:`/work/pepperfry`}
],
XU={W:1440,H:560},
ZU=[
  {id:`academic`,label:`Academic Projects`,vx:460,vy:115},
  {id:`business`,label:`Business Projects`,vx:980,vy:146}
];
""" + qu_to_fw_code + r"""var fW=[{from:0,to:.8,lines:[{words:[{text:`Solving`},{text:`business`},{text:`problems`}]},{words:[{text:`put`},{text:`forward`},{text:`by`},{text:`companies`,className:`summit-accent`}]},{words:[{text:`as`},{text:`college`,className:`summit-accent`},{text:`assignments.`,className:`summit-accent`}],tail:!0}]}],pW=.04,mW=.7;
function hW({beat:e,index:t,progress:n}){let r=t===fW.length-1,i=[e.from,e.from+pW,r?mW:e.to-pW,e.to],a=bV(n,i,[0,1,1,0].map((e,n)=>t===0&&n===0?1:e)),o=bV(n,i,[34,0,0,r?-72:-44]),s=e.lines.flatMap(e=>e.words),c=(e.to-e.from)*(r?.42:.62)/s.length,l=e.lines.map((t,n)=>e.lines.slice(0,n).reduce((e,t)=>e+t.words.length,0));return(0,G.jsx)(K.div,{className:`summit-beat`,style:{opacity:a,y:o},children:e.lines.map((t,r)=>(0,G.jsx)(`div`,{className:`summit-line${t.tail?` summit-line--tail`:``}`,children:t.words.map((t,i)=>{let a=e.from+pW*.5+c*(l[r]+i);return(0,G.jsx)(xV,{text:t.text,base:`summit-word`,className:t.className,progress:n,start:a,end:a+c*1.4},`${r}-${t.text}`)})},r))})}
function gW({peaks:e}){return(0,G.jsxs)(G.Fragment,{children:[(0,G.jsx)(`div`,{className:`summit-horizon`,"aria-hidden":`true`,children:(0,G.jsx)(QU,{})}),(0,G.jsx)(`div`,{className:`summit-peaks`,role:`group`,"aria-label":`Assignment categories`,children:e})]})}
function _W({peaks:e}){let t=(0,v.useRef)(null),n=(0,v.useRef)(null),{scrollYProgress:r}=bg(t),i=(0,v.useRef)({x:50,y:40,frame:0}),[a,o]=(0,v.useState)(!1);return(0,v.useEffect)(()=>{let e=e=>{n.current?.style.setProperty(`--stage`,e.toFixed(4)),o(e>=.84)};return e(r.get()),r.on(`change`,e)},[r]),(0,v.useEffect)(()=>()=>cancelAnimationFrame(i.current.frame),[]),(0,G.jsx)(`div`,{className:`summit-arrival`,ref:t,children:(0,G.jsxs)(`div`,{"data-scroll-stage":!0,className:`summit-arrival-stage`,ref:n,"data-markers-ready":a,onPointerMove:e=>{if(e.pointerType!==`mouse`)return;let t=n.current;if(!t)return;let r=t.getBoundingClientRect();i.current.x=(e.clientX-r.left)/r.width*100,i.current.y=(e.clientY-r.top)/r.height*100,!i.current.frame&&(i.current.frame=requestAnimationFrame(()=>{i.current.frame=0,t.style.setProperty(`--mx`,`${i.current.x.toFixed(2)}%`),t.style.setProperty(`--my`,`${i.current.y.toFixed(2)}%`),t.style.setProperty(`--lit`,`1`)}))},onPointerLeave:()=>n.current?.style.setProperty(`--lit`,`0`),children:[(0,G.jsx)(`div`,{className:`summit-light`,"aria-hidden":`true`}),(0,G.jsx)(`div`,{className:`summit-daylight`,"aria-hidden":`true`}),(0,G.jsx)(`div`,{className:`summit-firstlight`,"aria-hidden":`true`}),fW.map((e,t)=>(0,G.jsx)(hW,{beat:e,index:t,progress:r},t)),(0,G.jsx)(gW,{peaks:e})]})})}
function vW({peaks:e}){return(0,G.jsx)(`div`,{className:`summit-arrival summit-arrival--static`,children:(0,G.jsxs)(`div`,{className:`summit-arrival-stage`,children:[(0,G.jsxs)(`div`,{className:`summit-beat`,children:[(0,G.jsx)(`p`,{className:`summit-line`,children:`Solving business problems`}),(0,G.jsxs)(`p`,{className:`summit-line`,children:[`put forward by `,(0,G.jsx)(`em`,{className:`summit-accent`,children:`companies`})]}),(0,G.jsx)(`p`,{className:`summit-line summit-line--tail`,children:`as college assignments.`})]}),(0,G.jsx)(gW,{peaks:e})]})})}
var yW=VU;
function bW(){
  let e=(0,v.useRef)(null),t=(0,v.useRef)(null),n=(0,v.useRef)(null),[r,i]=(0,v.useState)(`academic`),[a,o]=(0,v.useState)(``),[s,c]=(0,v.useState)(null),l=um(),u=YU.filter(e=>GU(e,r)),d=e=>YU.filter(t=>GU(t,e)).length;
  (0,v.useEffect)(()=>{let r=e.current;if(!r||l)return;let i=0,a=()=>{i=0;let e=t.current?.getBoundingClientRect(),a=window.innerHeight,o=e?Math.min(1,Math.max(0,(a*.95-e.top)/(a*.95))):1,s=o.toFixed(3),c=r.querySelector(`.summit-arrival-stage`);c&&Z_(c,`--crest`,s);let l=n.current;l&&l.dataset.crest!==s&&(l.dataset.crest=s,l.style.translate=`0 ${(40*(1-o)).toFixed(1)}px`,l.style.opacity=String(Math.max(.05,o)))},o=()=>{i||=requestAnimationFrame(a)};return a(),window.addEventListener(`scroll`,o,{passive:!0}),window.addEventListener(`resize`,o),()=>{cancelAnimationFrame(i),window.removeEventListener(`scroll`,o),window.removeEventListener(`resize`,o)}},[l]);
  let f=ZU.map(e=>(0,G.jsxs)(`button`,{type:`button`,className:`summit-peak${r===e.id?` is-on`:``}`,"aria-pressed":r===e.id,"aria-controls":`summit-frames`,style:{"--peak-x":`${e.vx/XU.W*100}%`,"--peak-top":`${e.vy/XU.H*100}%`},onClick:()=>i(e.id),onPointerEnter:()=>o(e.id),onPointerLeave:()=>o(``),onFocus:()=>o(e.id),onBlur:()=>o(``),children:[(0,G.jsx)(`span`,{className:`summit-peak-label`,children:e.label}),(0,G.jsx)(`span`,{className:`summit-peak-lead`,"aria-hidden":`true`}),(0,G.jsx)(`span`,{className:`summit-peak-mark`,"aria-hidden":`true`})]},e.id));
  return(0,G.jsxs)(`section`,{className:`summit`,ref:e,"aria-label":`Solving business problems put forward by companies as college assignments.`,"data-peek":a,children:[
    l?(0,G.jsx)(vW,{peaks:f}):(0,G.jsx)(_W,{peaks:f}),
    (0,G.jsxs)(`div`,{className:`summit-inner`,ref:t,children:[
      (0,G.jsxs)(`header`,{className:`summit-head`,children:[
        (0,G.jsxs)(`div`,{className:`summit-head-main`,children:[
          (0,G.jsx)(`p`,{className:`section-label`,children:`02 / Academic & Business Projects`}),
          (0,G.jsxs)(`h2`,{className:`editorial-heading`,children:[
            (0,G.jsx)(`span`,{className:`summit-head-line`,children:`Solving business problems put forward by companies`}),` `,
            (0,G.jsx)(`em`,{className:`editorial-accent summit-head-line`,children:`as college assignments.`})
          ]})
        ]}),
        (0,G.jsx)(`div`,{className:`summit-head-side`,children:(0,G.jsx)(`p`,{className:`summit-aside`,"aria-hidden":`true`,children:`Academic Projects · Business Projects`})})
      ]}),
      (0,G.jsx)(`div`,{className:`summit-lanes`,role:`tablist`,"aria-label":`Filter assignments by category`,children:yW.map(e=>(0,G.jsxs)(`button`,{type:`button`,role:`tab`,id:`lane-${e.id}`,"aria-selected":r===e.id,"aria-controls":`summit-frames`,tabIndex:r===e.id?0:-1,className:`summit-lane${r===e.id?` is-on`:``}`,onClick:()=>i(e.id),onKeyDown:e=>{let t=yW.findIndex(e=>e.id===r),n=t;if(e.key===`ArrowRight`)n=(t+1)%yW.length;else if(e.key===`ArrowLeft`)n=(t-1+yW.length)%yW.length;else return;e.preventDefault(),i(yW[n].id)},children:[e.label,(0,G.jsx)(`span`,{className:`summit-lane-count`,children:d(e.id)})]},e.id))}),
      (0,G.jsx)(`div`,{className:`summit-rise`,ref:n,children:(0,G.jsx)(cf,{mode:`wait`,initial:!1,children:(0,G.jsx)(K.div,{id:`summit-frames`,role:`tabpanel`,"aria-labelledby":`lane-${r}`,className:`summit-frames`,initial:!l&&{opacity:0,y:12},animate:{opacity:1,y:0},exit:l?{opacity:1}:{opacity:0,y:-10},transition:{duration:.32,ease:[.22,1,.36,1]},children:(0,G.jsx)(dW,{items:u,peek:a,onOpen:c})},r)})})
    ]}),
    (0,G.jsx)(rW,{items:u,openId:s,onChange:c})
  ]})
}"""

# ============================================================================
# SPLICE 7: TOOLS MARQUEE (Section 7), MAIN HOME PAGE (wW), AND CASE OVERVIEWS (hG, wG)
# Preserves jW..mG helper functions!
# ============================================================================
pos_jw = src.find("function jW(e=.22")
pos_mg = src.find("var mG=e=>`/case-studies/")
jw_to_mg_code = src[pos_jw:pos_mg]

SPLICE_7 = r"""var ToolsList=[
  {name:`ChatGPT`,svg:(0,G.jsxs)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.7`,strokeLinecap:`round`,strokeLinejoin:`round`,children:[(0,G.jsx)(`path`,{d:`M12 3a4.5 4.5 0 0 0-3.89 2.25L4.5 11.5a4.5 4.5 0 0 0 0 4.5l2.2 3.8a4.5 4.5 0 0 0 6.15 1.65L19 17.9a4.5 4.5 0 0 0 1.65-6.15l-2.2-3.8A4.5 4.5 0 0 0 12 3Z`}),(0,G.jsx)(`circle`,{cx:`12`,cy:`12`,r:`2.6`})]})},
  {name:`Claude`,svg:(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`#d97757`,strokeWidth:`2.1`,strokeLinecap:`round`,children:(0,G.jsx)(`path`,{d:`M12 2.5v19M5.3 5.3l13.4 13.4M2.5 12h19M5.3 18.7 18.7 5.3M8.5 3.2l7 17.6M3.2 15.5l17.6-7`})})},
  {name:`Antigravity`,svg:(0,G.jsxs)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`#e25531`,strokeWidth:`1.9`,strokeLinecap:`round`,strokeLinejoin:`round`,children:[(0,G.jsx)(`path`,{d:`M12 3 4 20h3.6l1.8-4h5.2l1.8 4H20L12 3Z`}),(0,G.jsx)(`circle`,{cx:`12`,cy:`11`,r:`1.8`,fill:`#e25531`})]})},
  {name:`Freebuff`,svg:(0,G.jsxs)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.9`,strokeLinecap:`round`,strokeLinejoin:`round`,children:[(0,G.jsx)(`rect`,{x:`3.5`,y:`3.5`,width:`17`,height:`17`,rx:`4`}),(0,G.jsx)(`path`,{d:`M8.5 16V8h7M8.5 12h5`})]})},
  {name:`Vercel`,svg:(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,fill:`currentColor`,children:(0,G.jsx)(`path`,{d:`M12 3 22 20H2L12 3Z`})})},
  {name:`Lovable`,svg:(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,fill:`#e25531`,children:(0,G.jsx)(`path`,{d:`M12 20.5s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.2a4.3 4.3 0 0 1 7.5 3.1c0 5.6-7.5 10.2-7.5 10.2Z`})})},
  {name:`Emergent`,svg:(0,G.jsxs)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.9`,strokeLinecap:`round`,strokeLinejoin:`round`,children:[(0,G.jsx)(`path`,{d:`M12 2.5 14.8 9l6.7 2.8-6.7 2.8L12 21.5l-2.8-6.9-6.7-2.8L9.2 9 12 2.5Z`})]})},
  {name:`GitHub`,svg:(0,G.jsx)(`svg`,{viewBox:`0 0 24 24`,fill:`currentColor`,children:(0,G.jsx)(`path`,{d:`M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.11.79-.25.79-.56v-2c-3.2.7-3.88-1.54-3.88-1.54-.52-1.33-1.28-1.68-1.28-1.68-1.05-.72.08-.71.08-.71 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.18-3.09-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11.02 11.02 0 0 1 5.78 0c2.2-1.49 3.16-1.18 3.16-1.18.63 1.59.24 2.76.12 3.05.74.81 1.18 1.83 1.18 3.09 0 4.41-2.7 5.38-5.26 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.68.8.56A11.5 11.5 0 0 0 12 .5Z`})})}
];
function ToolsMarqueeSection(){
  let renderGroup=k=>(0,G.jsx)(`div`,{className:`tools-marquee-group`,"aria-hidden":k===1||void 0,children:ToolsList.map(t=>(0,G.jsxs)(`div`,{className:`tools-marquee-item`,children:[(0,G.jsx)(`span`,{className:`tools-marquee-icon`,"aria-hidden":!0,children:t.svg}),(0,G.jsx)(`span`,{className:`tools-marquee-name`,children:t.name})]},`${k}-${t.name}`))},k);
  return(0,G.jsxs)(`section`,{className:`tools-marquee-section paper-grain`,"aria-labelledby":`tools-building-heading`,children:[
    (0,G.jsxs)(`div`,{className:`tools-marquee-head`,children:[
      (0,G.jsx)(`p`,{className:`section-label`,children:`03 / Toolkit`}),
      (0,G.jsx)(`h2`,{id:`tools-building-heading`,className:`editorial-heading`,children:`Tools I use for building-`})
    ]}),
    (0,G.jsx)(`div`,{className:`tools-marquee-viewport`,children:(0,G.jsxs)(`div`,{className:`tools-marquee-track`,children:[renderGroup(0),renderGroup(1)]})})
  ]})
}
var wW=(0,v.memo)(function({background:e=!1}){return(0,v.useEffect)(()=>{let e=window.location.hash;if(!e)return;let t=0,n=!1,r=performance.now(),i=()=>{if(n)return;if((document.querySelector(`.loader`)||document.documentElement.classList.contains(`is-loading`))&&performance.now()-r<1e4){t=requestAnimationFrame(i);return}let a=document.getElementById(e.slice(1));if(!a)return;let o=Vm();o?(o.resize(),o.scrollTo(a,{immediate:!0,force:!0})):a.scrollIntoView()};return t=requestAnimationFrame(i),()=>{n=!0,cancelAnimationFrame(t)}},[]),(0,G.jsxs)(`main`,{children:[(0,G.jsx)(yV,{background:e}),(0,G.jsx)(LV,{}),(0,G.jsx)(DB,{}),(0,G.jsx)(`div`,{className:`work-departure`,children:(0,G.jsx)(Ig,{})}),(0,G.jsx)(bW,{}),(0,G.jsx)(ToolsMarqueeSection,{}),(0,G.jsx)(sv,{}),(0,G.jsx)(TV,{}),(0,G.jsx)(lv,{active:!e}),(0,G.jsx)(CW,{})]})});
""" + jw_to_mg_code + r"""var hG={
  "stroque-consulting":{
    title:`Stroque Consulting —`,
    titleAccent:`Graphology, Graphotherapy & AI for B2B.`,
    deck:`Stroque Consulting is a human consulting firm that helps individuals improve their personalities and achieve their personal and professional goals through a science called Graphology, i.e., handwriting analysis.`,
    summary:[
      `As Co-Founder and Sr. Handwriting Analyst (November 2022 – Present), I have completed close to 300 consultation calls, positively impacted 250+ people, and transformed 120+ people's lives through graphotherapy.`,
      `Current Business Expansion — AI for B2B: We are now exploring the integration of AI into Stroque Consulting to develop an additional product offering for B2B customers. Our existing handwriting-analysis and graphotherapy services will continue as our core offerings, while AI is explored as an ongoing product-development and business-expansion initiative to serve business customers.`
    ],
    facts:[
      {label:`Role`,value:`Co-Founder and Sr. Handwriting Analyst`},
      {label:`Venture`,value:`Stroque Consulting`,brands:[{name:`Stroque Consulting`,logo:`/brands/stroque.svg`}]},
      {label:`Duration`,value:`November 2022 – Present`}
    ],
    outcomes:[
      {value:`~300`,label:`people completed consultation calls`},
      {value:`250+`,label:`people positively impacted`},
      {value:`120+`,label:`lives transformed through graphotherapy`}
    ],
    outcomesLabel:`Impact & Achievements`,
    screens:[
      {src:`/assets/covers/stroque-consulting.svg`,width:1600,height:1000,caption:`Stroque Consulting — Core Graphology & Ongoing AI for B2B Exploration`,alt:`Stroque Consulting overview`}
    ],
    readMinutes:3
  },
  "hustlers-edge":{
    title:`Hustlers' Edge —`,
    titleAccent:`Skill-Based Community & Monetization.`,
    deck:`Hustlers' Edge is a skill-based community that helps final-year graduation students and early-career professionals learn market-demand skills, particularly marketing skills, and monetize them through agency or freelancing models.`,
    summary:[
      `Built from inception (August 2024 – April 2026) to 200+ community members, helping 140+ members generate five-figure monthly incomes through freelancing and agency models, with ₹10,00,000 in total reported revenue.`,
      `Unit Economics & Financial Clarification: The ₹5,000 revenue retained per student represents the revenue retained by our business after deducting the cost paid to the third-party ed-tech firm that trains our students in in-demand skills.`
    ],
    facts:[
      {label:`Role`,value:`Founder and Community Lead`},
      {label:`Venture`,value:`Hustlers' Edge Community`,brands:[{name:`Hustlers' Edge`,logo:`/brands/hustlers-edge.svg`}]},
      {label:`Duration`,value:`August 2024 – April 2026`}
    ],
    outcomes:[
      {value:`200+`,label:`community members built from inception`},
      {value:`140+`,label:`members generating 5-figure monthly incomes`},
      {value:`₹10,00,000`,label:`total reported revenue`},
      {value:`₹5,000`,label:`revenue retained per student after 3rd-party training cost`}
    ],
    outcomesLabel:`Impact & Business Metrics`,
    screens:[
      {src:`/assets/covers/hustlers-edge.svg`,width:1600,height:1000,caption:`Hustlers' Edge Community — Skill Development & Monetization Ecosystem`,alt:`Hustlers' Edge overview`}
    ],
    readMinutes:3
  },
  "idigitalpreneur":{
    title:`IDigitalpreneur Pvt. Ltd. —`,
    titleAccent:`Outbound Prospecting & B2C Deal Closure.`,
    deck:`Worked as a Business Development Associate and affiliate marketer in the ed-tech space, closing B2C deals through outbound calling and prospecting.`,
    summary:[
      `Focused on prospecting, outbound calling, customer conversations, understanding customer requirements, objection handling, B2C sales, and deal closure (February 2023 – April 2024).`,
      `Commercial Outcomes: Closed deals worth ₹2,00,000 with an average ticket size of approximately ₹10,000, earning ₹68,000 in commissions.`
    ],
    facts:[
      {label:`Role`,value:`Independent Business Development Associate`},
      {label:`Company`,value:`IDigitalpreneur Pvt. Ltd.`,brands:[{name:`IDigitalpreneur`,logo:`/brands/idigitalpreneur.svg`}]},
      {label:`Duration`,value:`February 2023 – April 2024`}
    ],
    outcomes:[
      {value:`₹2,00,000`,label:`closed deals through outbound calling & prospecting`},
      {value:`~₹10,000`,label:`average ticket size`},
      {value:`₹68,000`,label:`earned in commissions`}
    ],
    outcomesLabel:`Commercial Outcomes`,
    screens:[
      {src:`/assets/covers/idigitalpreneur.svg`,width:1600,height:1000,caption:`IDigitalpreneur Pvt. Ltd. — Consultative B2C Sales & Outbound Prospecting`,alt:`IDigitalpreneur overview`}
    ],
    readMinutes:2
  }
};
function wG({id:e,hero:t}){
  let n=hG[e],r=ct(),i=NW(),a=dt();
  if((0,v.useEffect)(()=>{i?.scrollRef.current?.scrollTo(0,0)},[i]),!n)return(0,G.jsx)(ng,{});
  let o=r.state,s={...o,caseDepth:(o?.caseDepth??1)+1};
  return(0,G.jsxs)(`main`,{className:`cov paper-grain${t?` cov--hero`:``}`,children:[
    t??(0,G.jsx)(`div`,{className:`cov-stage`,children:n.screens?.map(e=>(0,G.jsxs)(`figure`,{className:`cov-screen`,children:[(0,G.jsx)(`img`,{src:e.src,alt:e.alt,width:e.width,height:e.height,decoding:`async`}),(0,G.jsx)(`figcaption`,{children:e.caption})]},e.src))}),
    (0,G.jsxs)(`div`,{className:`cov-body`,id:`summary`,children:[
      !t&&(0,G.jsxs)(G.Fragment,{children:[
        (0,G.jsxs)(`h1`,{className:`cov-title`,children:[n.title,` `,n.titleAccent&&(0,G.jsx)(`em`,{children:n.titleAccent})]}),
        (0,G.jsx)(`p`,{className:`cov-deck`,children:n.deck})
      ]}),
      (0,G.jsx)(`div`,{className:`cov-summary`,children:n.summary.map(e=>(0,G.jsx)(`p`,{children:e},e))}),
      n.outcomes&&(0,G.jsx)(`ul`,{className:`cov-outcomes`,"aria-label":n.outcomesLabel??`Outcomes`,style:{"--cov-n":n.outcomes.length},children:n.outcomes.map(e=>(0,G.jsxs)(`li`,{children:[(0,G.jsx)(`strong`,{children:e.value}),(0,G.jsx)(`span`,{children:e.label})]},e.label))}),
      (0,G.jsx)(`dl`,{className:`cov-facts`,children:n.facts.map(e=>(0,G.jsxs)(`div`,{children:[(0,G.jsx)(`dt`,{children:e.label}),e.brands?(0,G.jsxs)(`dd`,{className:`cov-brands`,children:[e.brands.map((e,t)=>(0,G.jsxs)(`span`,{className:`cov-brand`,children:[t>0&&(0,G.jsx)(`span`,{className:`cov-brand-cross`,"aria-label":`and`,children:`×`}),(0,G.jsx)(`img`,{src:e.logo,alt:``,width:22,height:22}),e.name]},e.name))]}):(0,G.jsx)(`dd`,{children:e.value})]},e.label))}),
      (0,G.jsxs)(`div`,{className:`cov-next`,children:[
        (0,G.jsxs)(Cn,{className:`cov-cta`,to:`/work/${e}/full`,state:s,onClick:t=>{!i||t.metaKey||t.ctrlKey||t.shiftKey||t.altKey||(t.preventDefault(),i.sandNavigate(()=>a(`/work/${e}/full`,{state:s})))},children:[`Read the full case study `,(0,G.jsx)(`span`,{"aria-hidden":`true`,children:`→`})]}),
        (0,G.jsxs)(`span`,{className:`cov-time`,children:[n.readMinutes,` min read`]})
      ]})
    ]})
  ]})
}"""

# ============================================================================
# SPLICE 8: ROUTER, SEO METADATA, AND ROOT RENDER ($K)
# ============================================================================
SPLICE_8 = r"""function GK({overview:e,full:t}){let{pathname:n}=ct(),r=n.replace(/\/+$/,``).endsWith(`/full`);return(0,G.jsxs)(G.Fragment,{children:[(0,G.jsx)(v.Activity,{mode:r?`hidden`:`visible`,children:e}),(0,G.jsx)(v.Activity,{mode:r?`visible`:`hidden`,children:t})]})}
var KK=`https://muhammadhassaan.com`,
qK=[
  {path:`/`,title:`Muhammad Hassaan — Entrepreneurship · Consultative Sales · Business Development`,description:`Hey! I'm Hassaan. I listen to people & solve their problems by giving them tailored solutions. MBA Candidate at Masters' Union School of Business.`,image:`/assets/covers/stroque-consulting.svg`,imageAlt:`Muhammad Hassaan Portfolio`},
  ...Object.keys(Zh).flatMap(id=>[
    {path:`/work/${id}`,title:`${Zh[id].id} | Muhammad Hassaan`,description:Zh[id].summary,image:`/assets/covers/stroque-consulting.svg`,imageAlt:`Muhammad Hassaan Case Study`},
    {path:`/work/${id}/full`,title:`${Zh[id].id} — Full Case Study | Muhammad Hassaan`,description:Zh[id].summary,image:`/assets/covers/stroque-consulting.svg`,imageAlt:`Muhammad Hassaan Full Case Study`}
  ])
];
function JK(e){let t=e.replace(/\/+$/,``)||`/`;return qK.find(e=>e.path===t)??(t.startsWith(`/work/`)?qK[0]:{path:`/404`,title:`Page Not Found | Muhammad Hassaan`,description:`Return to Muhammad Hassaan's portfolio.`,image:`/assets/covers/stroque-consulting.svg`,imageAlt:`Muhammad Hassaan Portfolio`,noindex:!0})}
function ZK(){let{pathname:e}=ct();return(0,v.useEffect)(()=>{let t=JK(e);document.title=t.title},[e]),null}
function QK(){return(0,G.jsxs)(`main`,{className:`paper-grain flex min-h-screen flex-col items-center justify-center gap-4 bg-[var(--color-paper)] px-6 text-center text-[var(--color-ink)]`,children:[(0,G.jsx)(`p`,{className:`section-label`,children:`404 · Not found`}),(0,G.jsx)(`h1`,{className:`editorial-heading text-3xl`,children:`This page could not be found.`}),(0,G.jsx)(Cn,{to:`/`,className:`mt-2 underline underline-offset-4`,children:`← Back to the portfolio`})]})}
function HassaanCaseRoute(){
  let{pathname:p}=ct(),parts=p.replace(/\/+$/,``).split(`/`),isFull=parts[parts.length-1]===`full`,slug=isFull?parts[parts.length-2]:parts[parts.length-1];
  return isFull?(0,G.jsx)(ng,{}):hG[slug]?(0,G.jsx)(wG,{id:slug}):(0,G.jsx)(ng,{});
}
function $K(){
  let e=ct(),t=e.pathname.startsWith(`/work/`)&&JK(e.pathname).path!==`/404`,n=e.state?.backgroundLocation;
  return(0,G.jsxs)(G.Fragment,{children:[
    (0,G.jsx)(ZK,{}),
    (0,G.jsx)(Xh,{}),
    (0,G.jsx)(Ah,{}),
    (0,G.jsx)(Mh,{}),
    (0,G.jsxs)(Lt,{location:t?n??`/`:e,children:[
      (0,G.jsx)(Ft,{path:`/`,element:(0,G.jsx)(wW,{background:t})}),
      (0,G.jsx)(Ft,{path:`*`,element:(0,G.jsx)(QK,{})})
    ]}),
    t&&(0,G.jsx)(WK,{children:(0,G.jsxs)(Lt,{location:e,children:[
      (0,G.jsx)(Ft,{path:`/work/:slug/full`,element:(0,G.jsx)(HassaanCaseRoute,{})}),
      (0,G.jsx)(Ft,{path:`/work/:slug`,element:(0,G.jsx)(HassaanCaseRoute,{})})
    ]})})
  ]})
}
(0,b.createRoot)(document.getElementById(`root`)).render((0,G.jsx)(v.StrictMode,{children:(0,G.jsx)(Sn,{children:(0,G.jsx)($K,{})})}));"""

# Apply all 8 splices in order
out = src
out = replace_between(out, "wh=[.22,1,.36,1],Th=[.76,0,.24,1],Eh=", "var jh=`a, button", SPLICE_1)
out = replace_between(out, 'var Zh={"expense-approvals"', "var rg=`#version 300 es", SPLICE_2)
out = replace_between(out, "var xg=.16,Sg=12", "function p_({children:e", SPLICE_3)
out = replace_between(out, "var b_=()=>(0,G.jsx)", "function uv(){return uv=", SPLICE_4)
out = replace_between(out, "var _B=`/models/lowpoly_vr_glasses/scene.gltf`", "function OB({className:e})", SPLICE_5)
out = replace_between(out, "var zB=[{src:`/hero/photo-1.jpg`", "var xW=[`.work-departure`", SPLICE_6)
out = replace_between(out, "var wW=(0,v.memo)", "var bK=`case-sand`", SPLICE_7)
out = replace_between(out, "function GK({overview:e,full:t})", "export{Zn as a", SPLICE_8)

# Clean up remaining references in the Browser's mini-apps (Claude/ChatGPT, Figma canvas, Google Search)
out = out.replace("I only know one topic tonight: Samay.", "I only know one topic tonight: Hassaan.")
out = out.replace("What do you want to know about Samay?", "What do you want to know about Hassaan?")
out = out.replace("pick a question above — I only know about Samay 🙂", "pick a question above — I only know about Hassaan 🙂")
out = out.replace("children:[`samay`,(0,G.jsx)(`i`,{})]", "children:[`hassaan`,(0,G.jsx)(`i`,{})]")
out = out.replace("children:`samay.`", "children:`hassaan.`")
out = out.replace("hello from samay’s canvas 👋", "hello from hassaan’s canvas 👋")
out = out.replace("title:`Samay is here`,children:`S`", "title:`Hassaan is here`,children:`H`")
out = out.replace("`samay maurya`", "`muhammad hassaan`")
out = out.replace("Um=`samay-sfx`,Wm=10,Gm=`samay-sfx-settings`", "Um=`hassaan-sfx`,Wm=10,Gm=`hassaan-sfx-settings`")

js_out_path = os.path.join(BASE_DIR, "js", "main.js")
with open(js_out_path, "w", encoding="utf-8") as f:
    f.write(out)

html_out = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/png" href="/assets/h-logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=Caveat:wght@500;600&display=swap"
      rel="stylesheet"
    />
    <!-- seo:start -->
    <title data-seo>Muhammad Hassaan — Entrepreneurship · Consultative Sales · Business Development</title>
    <meta data-seo name="description" content="Hey! I'm Hassaan. I listen to people &amp; solve their problems by giving them tailored solutions. MBA Candidate at Masters' Union School of Business." />
    <meta data-seo name="robots" content="index, follow, max-image-preview:large" />
    <meta data-seo property="og:type" content="website" />
    <meta data-seo property="og:site_name" content="Muhammad Hassaan" />
    <meta data-seo property="og:locale" content="en_US" />
    <meta data-seo property="og:title" content="Muhammad Hassaan — Entrepreneurship · Consultative Sales · Business Development" />
    <meta data-seo property="og:description" content="Hey! I'm Hassaan. I listen to people &amp; solve their problems by giving them tailored solutions." />
    <meta data-seo property="og:image" content="/assets/covers/stroque-consulting.svg" />
    <!-- seo:end -->
    <script type="module" src="/js/main.js"></script>
    <link rel="stylesheet" href="/css/styles.css" />
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_out)

print("Successfully built js/main.js and index.html! Output JS size:", len(out))
