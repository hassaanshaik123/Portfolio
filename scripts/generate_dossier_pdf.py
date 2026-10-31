#!/usr/bin/env python3
"""
Generates a comprehensive, multi-page professional PDF dossier for Muhammad Hassaan.
Pure Python — no external dependencies.
"""
import sys
import os

class SimplePDFBuilder:
    def __init__(self, filename, page_width=612, page_height=792, margin=45):
        self.filename = filename
        self.pw = page_width
        self.ph = page_height
        self.m = margin
        self.pages = []
        self.current_page_ops = []
        self.y = self.ph - self.m
        
    def new_page(self):
        if self.current_page_ops:
            self.pages.append(self.current_page_ops)
            self.current_page_ops = []
        self.y = self.ph - self.m
        # Page header
        self.set_color(0.5, 0.5, 0.5)
        self.text("MUHAMMAD HASSAAN — PROFESSIONAL DOSSIER & RESUME COMPANION", self.m, self.ph - 28, "F1", 7.5)
        self.stroke_line(self.m, self.ph - 32, self.pw - self.m, self.ph - 32, 0.4)
        
        # Page footer
        page_num = len(self.pages) + 1
        self.stroke_line(self.m, 32, self.pw - self.m, 32, 0.4)
        self.text(f"Confidential · Master Experience Profile · Page {page_num}", self.m, 22, "F1", 7.5)
        self.text("hassaanshaik.work@gmail.com", self.pw - self.m - 120, 22, "F1", 7.5)
        self.set_color(0.1, 0.1, 0.1)

    def ensure_space(self, needed_pt):
        if self.y - needed_pt < self.m + 25:
            self.new_page()

    def set_color(self, r, g, b, is_fill=True):
        cmd = f"{r:.3f} {g:.3f} {b:.3f} rg\n" if is_fill else f"{r:.3f} {g:.3f} {b:.3f} RG\n"
        self.current_page_ops.append(cmd)

    def stroke_line(self, x1, y1, x2, y2, width=0.5):
        self.current_page_ops.append(f"{width:.2f} w\n{x1:.2f} {y1:.2f} m\n{x2:.2f} {y2:.2f} l\nS\n")

    def fill_rect(self, x, y, w, h):
        self.current_page_ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re\nf\n")

    def stroke_rect(self, x, y, w, h, width=0.5):
        self.current_page_ops.append(f"{width:.2f} w\n{x:.2f} {y:.2f} {w:.2f} {h:.2f} re\nS\n")

    def text(self, txt, x, y, font="F1", size=10):
        # Sanitize unicode punctuation to clean ASCII/WinAnsi equivalents
        clean = (
            txt.replace("—", " - ")
            .replace("–", " - ")
            .replace("·", "·")
            .replace("“", '"')
            .replace("”", '"')
            .replace("‘", "'")
            .replace("’", "'")
            .replace(">", ">")
        )
        # Convert any remaining non-latin1 characters
        safe_chars = []
        for ch in clean:
            cp = ord(ch)
            if cp < 128:
                safe_chars.append(ch)
            elif ch == "·":
                safe_chars.append("-")
            elif ch == "©":
                safe_chars.append("(c)")
            else:
                safe_chars.append(" ")
        clean_txt = "".join(safe_chars).replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        op = f"BT\n/{font} {size} Tf\n{x:.2f} {y:.2f} Td\n({clean_txt}) Tj\nET\n"
        self.current_page_ops.append(op)

    def draw_heading_1(self, title):
        self.ensure_space(35)
        self.y -= 14
        self.set_color(0.08, 0.08, 0.1)
        self.text(title.upper(), self.m, self.y, "F2", 11)
        self.set_color(0.7, 0.55, 0.35, is_fill=False)
        self.stroke_line(self.m, self.y - 4, self.pw - self.m, self.y - 4, 1.2)
        self.y -= 16

    def draw_heading_2(self, title, subtitle=""):
        self.ensure_space(28)
        self.y -= 8
        self.set_color(0.12, 0.12, 0.15)
        self.text(title, self.m, self.y, "F2", 10.5)
        if subtitle:
            self.set_color(0.45, 0.45, 0.5)
            # Estimate width
            tw = len(title) * 6.2 + 10
            self.text(f"·  {subtitle}", self.m + tw, self.y, "F1", 9)
        self.y -= 14

    def draw_paragraph(self, text, size=9, leading=13, font="F1", color=(0.2, 0.2, 0.25)):
        self.set_color(*color)
        words = text.split()
        lines = []
        cur_line = []
        max_chars = int((self.pw - 2 * self.m) / (size * 0.52))
        
        for w in words:
            if len(" ".join(cur_line + [w])) <= max_chars:
                cur_line.append(w)
            else:
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))

        for line in lines:
            self.ensure_space(leading)
            self.text(line, self.m, self.y, font, size)
            self.y -= leading
        self.y -= 4

    def draw_bullet(self, bold_prefix, text, size=8.5, leading=12):
        self.ensure_space(leading)
        self.set_color(0.7, 0.55, 0.35)
        self.text(">", self.m + 4, self.y, "F2", 8)
        
        full_text = f"{bold_prefix} {text}" if bold_prefix else text
        words = full_text.split()
        lines = []
        cur_line = []
        max_chars = int((self.pw - 2 * self.m - 16) / (size * 0.52))
        
        for w in words:
            if len(" ".join(cur_line + [w])) <= max_chars:
                cur_line.append(w)
            else:
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))

        for i, line in enumerate(lines):
            self.ensure_space(leading)
            if i == 0 and bold_prefix:
                # First line has bold prefix
                self.set_color(0.12, 0.12, 0.15)
                self.text(line, self.m + 16, self.y, "F1", size)
            else:
                self.set_color(0.25, 0.25, 0.3)
                self.text(line, self.m + 16, self.y, "F1", size)
            self.y -= leading

    def draw_stats_strip(self, items):
        """Draw 4 metric callout boxes in a row"""
        self.ensure_space(42)
        box_gap = 8
        n = len(items)
        box_w = (self.pw - 2 * self.m - (n - 1) * box_gap) / n
        box_h = 34
        top_y = self.y
        
        for i, (val, lbl) in enumerate(items):
            bx = self.m + i * (box_w + box_gap)
            by = top_y - box_h
            # Background fill
            self.set_color(0.965, 0.965, 0.96)
            self.fill_rect(bx, by, box_w, box_h)
            # Border
            self.set_color(0.85, 0.85, 0.82, is_fill=False)
            self.stroke_rect(bx, by, box_w, box_h, 0.6)
            # Top highlight accent line
            self.set_color(0.7, 0.55, 0.35, is_fill=False)
            self.stroke_line(bx, by + box_h, bx + box_w, by + box_h, 1.2)
            # Text
            self.set_color(0.1, 0.1, 0.12)
            self.text(val, bx + 8, by + 18, "F2", 11)
            self.set_color(0.45, 0.45, 0.5)
            self.text(lbl.upper(), bx + 8, by + 7, "F1", 6.5)
            
        self.y = top_y - box_h - 12

    def build(self):
        if self.current_page_ops:
            self.pages.append(self.current_page_ops)

        objects = []
        # 1. Catalog
        # 2. Pages
        # 3..n+2 Pages objects
        # Fonts: F1 (Helvetica), F2 (Helvetica-Bold), F3 (Helvetica-Oblique)
        num_pages = len(self.pages)
        
        # Build xref table
        pdf = bytearray()
        pdf.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        
        offsets = {}
        
        def add_obj(obj_id, body_bytes):
            offsets[obj_id] = len(pdf)
            pdf.extend(f"{obj_id} 0 obj\n".encode("latin1"))
            pdf.extend(body_bytes)
            pdf.extend(b"\nendobj\n")

        # Fonts
        f1_id = num_pages + 3
        f2_id = num_pages + 4
        f3_id = num_pages + 5
        
        # Catalog
        add_obj(1, b"<< /Type /Catalog /Pages 2 0 R >>")
        
        # Pages Tree
        kids = " ".join([f"{i+3} 0 R" for i in range(num_pages)])
        add_obj(2, f"<< /Type /Pages /Kids [{kids}] /Count {num_pages} >>".encode("latin1"))
        
        # Page Objects & Content Streams
        content_id_start = num_pages + 6
        for i, ops in enumerate(self.pages):
            page_id = i + 3
            c_id = content_id_start + i
            page_dict = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.pw} {self.ph}] /Resources << /Font << /F1 {f1_id} 0 R /F2 {f2_id} 0 R /F3 {f3_id} 0 R >> >> /Contents {c_id} 0 R >>".encode("latin1")
            add_obj(page_id, page_dict)

        # Fonts dicts
        add_obj(f1_id, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        add_obj(f2_id, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        add_obj(f3_id, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")

        # Content streams
        for i, ops in enumerate(self.pages):
            c_id = content_id_start + i
            stream_data = "".join(ops).encode("latin1")
            stream_body = f"<< /Length {len(stream_data)} >>\nstream\n".encode("latin1") + stream_data + b"\nendstream"
            add_obj(c_id, stream_body)

        total_objs = content_id_start + num_pages - 1
        xref_offset = len(pdf)
        pdf.extend(f"xref\n0 {total_objs + 1}\n".encode("latin1"))
        pdf.extend(b"0000000000 65535 f \n")
        for i in range(1, total_objs + 1):
            pdf.extend(f"{offsets[i]:010d} 00000 n \n".encode("latin1"))
            
        pdf.extend(f"trailer\n<< /Size {total_objs + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("latin1"))
        
        with open(self.filename, "wb") as f:
            f.write(pdf)
        print(f"Generated {self.filename} with {num_pages} pages ({len(pdf)} bytes).")

def build_full_dossier():
    output_path = os.path.join(process_cwd(), "Muhammad_Hassaan_Professional_Dossier.pdf")
    doc = SimplePDFBuilder(output_path, page_width=612, page_height=792, margin=45)
    
    # ---------------- PAGE 1: EXECUTIVE PROFILE & VENTURES ----------------
    doc.new_page()
    
    # Executive Header
    doc.set_color(0.1, 0.1, 0.12)
    doc.text("MUHAMMAD HASSAAN", doc.m, doc.y, "F2", 22)
    doc.y -= 14
    doc.set_color(0.7, 0.55, 0.35)
    doc.text("BUSINESS DEVELOPER  |  B2B SALES  |  CONSULTATIVE SELLING", doc.m, doc.y, "F2", 9.5)
    doc.y -= 12
    doc.set_color(0.4, 0.4, 0.45)
    doc.text("MBA, Masters' Union School of Business  ·  New Delhi, India  ·  hassaanshaik.work@gmail.com", doc.m, doc.y, "F1", 8.5)
    doc.y -= 6
    doc.stroke_line(doc.m, doc.y, doc.pw - doc.m, doc.y, 1.2)
    doc.y -= 14
    
    # Core Statement Box
    doc.set_color(0.965, 0.96, 0.94)
    doc.fill_rect(doc.m, doc.y - 32, doc.pw - 2 * doc.m, 32)
    doc.set_color(0.7, 0.55, 0.35, is_fill=False)
    doc.stroke_line(doc.m, doc.y - 32, doc.m, doc.y, 2.5)
    doc.set_color(0.15, 0.15, 0.18)
    doc.text('"Turning Problems into tailored Solutions that get closed."', doc.m + 12, doc.y - 14, "F2", 10.5)
    doc.set_color(0.45, 0.45, 0.5)
    doc.text("Core Philosophy: Understand customer friction deeply before prescribing commercial answers.", doc.m + 12, doc.y - 25, "F3", 8)
    doc.y -= 44

    # Executive Summary / Bio
    doc.draw_heading_1("Executive Profile & Selling Philosophy")
    doc.draw_paragraph(
        "Muhammad Hassaan is an entrepreneur, venture builder, and aspiring business development professional pursuing his MBA at Masters' Union School of Business. With hands-on experience building ventures from 0 to 1, scaling skill communities, and managing consultative sales pipelines, Hassaan approaches business development as diagnostic problem-solving: listening closely, dissecting customer pain points, and tailoring commercial solutions that deliver measurable ROI."
    )
    doc.draw_paragraph(
        "\"One thing I'm learning along the way is that sales can be genuinely rewarding. Not when you're trying to convince someone to buy something, but when you listen closely, understand what they actually need, and help them find the right solution. That's the side of sales I connect with most.\""
    )

    # Core Education
    doc.draw_heading_1("Academic Credentials")
    doc.draw_bullet("MBA (Candidate 2026-2028):", "Masters' Union School of Business — Focus on Business Strategy, Go-to-Market Execution & Enterprise Sales.")
    doc.draw_bullet("Undergraduate Degree (2021-2025):", "Delhi University — Analytical and commercial foundation.")
    doc.draw_bullet("XII (2021):", "Challengers Civil Services Academy · X Class (2019): Sri Chaitanya Institutions.")
    doc.y -= 6

    # Entrepreneurship Experiments (Category A)
    doc.draw_heading_1("Entrepreneurship Experiments & Track Record")
    
    # Venture 1: Stroque
    doc.draw_heading_2("01. Stroque Consulting", "Founder & Senior Handwriting Analyst (Nov 2022 – Present)")
    doc.draw_stats_strip([
        ("$26,000+", "Total Revenue"),
        ("300+", "People Helped"),
        ("250+", "Consultation Calls"),
        ("130+", "Grapho-Therapy")
    ])
    doc.draw_paragraph(
        "Human consulting practice founded on the intersection of handwriting psychology and executive habit transformation. Diagnosed behavioral and leadership friction to deliver personalized personal and professional growth regimens."
    )
    doc.draw_bullet("Sales Methodology:", "Diagnostic-first sales pipeline. Converted 250+ 1-on-1 discovery calls by presenting sample psychological audits before recommending tailored Grapho-Therapy programs.")
    doc.draw_bullet("Revenue & Scale:", "Grew venture to $26,000+ in self-generated revenue through high-trust consultative selling and word-of-mouth client referrals across 300+ individuals.")
    doc.y -= 6

    # ---------------- PAGE 2: VENTURES, ACADEMIC & BUSINESS PROBLEMS ----------------
    doc.new_page()
    
    # Venture 2: Hustlers' Edge
    doc.draw_heading_2("02. Hustlers' Edge", "Founder & Community Lead (Aug 2024 – April 2026)")
    doc.draw_stats_strip([
        ("140+", "5-Figure Earners"),
        ("200+", "Active Members"),
        ("Tier 2 & 3", "Target Demographic"),
        ("0 to 1", "Ecosystem Scale")
    ])
    doc.draw_paragraph(
        "Grassroots skill-development community built to bridge the commercialization gap for final-year undergraduate students and early-career talent from Tier 2 and Tier 3 cities."
    )
    doc.draw_bullet("Opportunity Identified:", "Discovered students possessed theoretical training but lacked practical client acquisition, negotiation, and monetization skills.")
    doc.draw_bullet("Execution Model:", "Formed strategic partnerships with ed-tech training partners for market-demand skill curriculum while running live playbooks on outbound prospecting, portfolio positioning, and deal closing.")
    doc.draw_bullet("Quantified Outcome:", "Guided 140+ individuals from zero digital earnings to generating five-figure monthly incomes in INR, establishing an enduring network of commercially empowered builders.")
    doc.y -= 8

    # Venture 3: Idigitalpreneur
    doc.draw_heading_2("03. Idigitalpreneur Pvt. Ltd.", "Business Development — Affiliate (Feb 2023 – April 2024)")
    doc.draw_stats_strip([
        ("30%", "Efficiency Gain"),
        ("~$2,000", "Inbound Deals"),
        ("$60", "Avg Ticket Size"),
        ("20+", "Sales Reps Trained")
    ])
    doc.draw_paragraph(
        "Managed end-to-end B2C and affiliate business development operations, handling outbound prospecting, inbound pipeline discovery, customer objection management, and peer sales training."
    )
    doc.draw_bullet("Consultative Sales:", "Replaced scripted hard pitches with structured objection discovery—framing program enrollment around student career ROI rather than price defense.")
    doc.draw_bullet("Team Enablement:", "Trained 20+ sales peers on consultative discovery and objection handling frameworks, resulting in a documented 30% team-wide sales efficiency improvement.")
    doc.y -= 10

    # Category B: Academic Strategy Projects
    doc.draw_heading_1("Academic Strategy Frameworks (Masters' Union)")
    doc.draw_bullet("Bharti Airtel Growth Strategy (Business Strategy):", "Formulated competitive growth vectors, enterprise connectivity expansion, and digital services diversification strategies for telecom leadership.")
    doc.draw_bullet("Ownwise (Decoding Business Models II):", "Rigorous deconstruction of platform unit economics, customer acquisition loops, gross margin structures, and sustainable competitive moats.")
    doc.draw_bullet("Stride (Decoding Business Models II):", "Analytical teardown of platform monetization mechanics, CAC:LTV ratios, marketplace network effects, and enterprise defensibility.")
    doc.y -= 8

    # Category C: Business Problem Analysis
    doc.draw_heading_1("Business Problem Diagnostics")
    doc.draw_bullet("GoSTOPS (Business Problem Analysis):", "Operational hospitality diagnostic examining friction in guest touchpoints, booking funnel drop-offs, and actionable revenue optimization levers.")
    doc.draw_bullet("Pepperfry (Customer Experience Improvement):", "Identified systemic friction in post-purchase furniture fulfillment and customer service. Formulated three strategic service interventions to improve retention and drive repeat sales.")
    doc.y -= 6

    # ---------------- PAGE 3: STARTUP IDEAS, MENTORSHIP & CONTACT ----------------
    doc.new_page()

    # Section 8: Startup Ideas & MVPs
    doc.draw_heading_1("Startup Ideas & MVP Portfolio (Product Builder)")
    
    # 01. Clario.AI
    doc.draw_heading_2("01. Clario.AI", "Stage: Early MVP / Phase 1 (Simplified English Audio)")
    doc.draw_paragraph(
        "An AI-powered reading and listening assistant that converts complex written materials, dense MBA case studies, and industry news into plain-language explanations and downloadable audio notes."
    )
    doc.draw_bullet("Why Started:", "Observed MBA peers and UPSC aspirants experiencing severe reading fatigue when processing 100+ pages of dense case studies weekly.")
    doc.draw_bullet("Solution & Roadmap:", "Converts complex text into simple explanations and high-fidelity audio notes. Phase 1 focused on English audio; Phase 2 introduces regional Indian languages and context pop-ups.")
    doc.y -= 6

    # 02. LYVO
    doc.draw_heading_2("02. LYVO", "Stage: Ideation completed; market research ongoing")
    doc.draw_paragraph(
        "A conversational support marketplace connecting young adults with life coaches for accessible, empathetic 1-on-1 conversations."
    )
    doc.draw_bullet("Why Started:", "Personal experience with isolation and the difficulty of finding empathetic, non-judgmental listeners for everyday life struggles.")
    doc.draw_bullet("Solution & Boundary Note:", "Bridges the gap between suffering in silence and clinical psychotherapy. Strictly positioned as conversational guidance and mentorship—not a clinical therapy substitute.")
    doc.y -= 6

    # 03. Buildsy
    doc.draw_heading_2("03. Buildsy", "Stage: Market research completed; MVP development in progress")
    doc.draw_paragraph(
        "An AI-powered tool-stack recommendation platform helping first-time founders and solopreneurs select the leanest, most affordable software stack tailored to their exact venture and budget."
    )
    doc.draw_bullet("Why Started:", "Struggled with tool selection during early ventures, wasting capital on bloated enterprise SaaS before product validation.")
    doc.draw_bullet("Solution:", "Analyzes venture idea, technical skill, and development stage to recommend optimal, cost-efficient software tool combinations.")
    doc.y -= 6

    # 04. RAAH.AI
    doc.draw_heading_2("04. RAAH.AI", "Stage: Diagnostic Platform (Stage Not Yet Specified)")
    doc.draw_paragraph(
        "An AI career diagnostic platform evaluating student and early-career readiness across 8 distinct role tracks and 5 multidimensional assessment vectors to identify natural strengths and skill gaps."
    )
    doc.y -= 10

    # Section 9 & 11: Mentorship & Contact Channels
    doc.draw_heading_1("Mentorship Philosophy & Contact Channels")
    doc.draw_paragraph(
        "Dedicated to mentoring aspiring founders, undergraduate students, and early-career professionals in consultative sales, practical freelancing, and venture execution. Available for B2B sales roles, growth partnerships, and venture collaborations."
    )
    
    doc.draw_bullet("Email:", "hassaanshaik.work@gmail.com (Direct response)")
    doc.draw_bullet("LinkedIn:", "Muhammad Hassaan (Professional profile & network)")
    doc.draw_bullet("Topmate:", "1-on-1 Consultative & Mentorship Sessions")
    doc.draw_bullet("Instagram:", "@muhammadhassaan  ·  GitHub: Public repositories & portfolio code")
    doc.draw_bullet("Portfolio Website:", "https://github.com/hassaanshaik123/Portfolio (Live build & case studies)")

    doc.build()
    return output_path

def process_cwd():
    return os.getcwd()

if __name__ == "__main__":
    build_full_dossier()
