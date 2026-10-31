/**
 * Muhammad Hassaan — Business Development Portfolio
 * Interactions Engine:
 *  1. Signature Compass Navigation & Real-Time Bearing Needle Rotation
 *  2. IntersectionObserver Section Tracking & Active State Management
 *  3. Smooth Scroll Navigation with Precise Viewport Offset
 *  4. Mobile Compass Drawer with Touch & Keyboard Controls
 */

(function () {
  "use strict";

  // Section Compass Bearings (in degrees)
  const SECTION_BEARINGS = {
    hero: 0,
    work: 45,
    about: 105,
    ideas: 165,
    mentorship: 225,
    resume: 285,
    connect: 330
  };

  // DOM Elements
  const compassNeedle = document.getElementById("compassNeedle");
  const navLinks = document.querySelectorAll(".compass-link");
  const mobileNavLinks = document.querySelectorAll(".compass-mobile-item");
  const mobileToggle = document.getElementById("compassMobileToggle");
  const mobileMenu = document.getElementById("compassMobileMenu");
  const sections = document.querySelectorAll("section[id]");

  let activeSectionId = "hero";

  /**
   * Rotate Compass Needle to Bearing Angle
   * @param {number} degrees
   */
  function rotateCompass(degrees) {
    if (!compassNeedle) return;
    compassNeedle.style.transform = `rotate(${degrees}deg)`;
  }

  /**
   * Set Active Navigation Link
   * @param {string} id
   */
  function setActiveNav(id) {
    if (activeSectionId === id) return;
    activeSectionId = id;

    // Update Desktop Nav Links
    navLinks.forEach((link) => {
      const target = link.getAttribute("href")?.replace("#", "");
      if (target === id) {
        link.classList.add("is-active");
      } else {
        link.classList.remove("is-active");
      }
    });

    // Update Mobile Nav Links
    mobileNavLinks.forEach((item) => {
      const target = item.getAttribute("href")?.replace("#", "");
      if (target === id) {
        item.classList.add("is-active");
      } else {
        item.classList.remove("is-active");
      }
    });

    // Orient the Compass Needle to this section's bearing
    const bearing = SECTION_BEARINGS[id] ?? 0;
    rotateCompass(bearing);
  }

  /**
   * IntersectionObserver for Smooth Wayfinding Tracking
   */
  const observerOptions = {
    root: null,
    rootMargin: "-20% 0px -60% 0px",
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute("id");
        if (id) {
          setActiveNav(id);
        }
      }
    });
  }, observerOptions);

  sections.forEach((sec) => sectionObserver.observe(sec));

  /**
   * Smooth Scroll Handler with Proper Header Offset
   */
  function handleNavClick(event) {
    const link = event.currentTarget;
    const targetHref = link.getAttribute("href");
    if (!targetHref || !targetHref.startsWith("#")) return;

    const targetId = targetHref.substring(1);
    const targetElement = document.getElementById(targetId);

    if (targetElement) {
      event.preventDefault();

      // Close mobile drawer if open
      if (mobileMenu && mobileMenu.classList.contains("is-open")) {
        closeMobileMenu();
      }

      const headerOffset = 90;
      const elementPosition = targetElement.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });

      // Update URL hash without jump
      history.replaceState(null, "", targetHref);
    }
  }

  // Bind Click Handlers
  navLinks.forEach((link) => link.addEventListener("click", handleNavClick));
  mobileNavLinks.forEach((link) => link.addEventListener("click", handleNavClick));

  /**
   * Mobile Menu Controls
   */
  function toggleMobileMenu() {
    if (!mobileMenu) return;
    const isOpen = mobileMenu.classList.toggle("is-open");
    if (mobileToggle) {
      mobileToggle.setAttribute("aria-expanded", String(isOpen));
    }
  }

  function closeMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove("is-open");
    if (mobileToggle) {
      mobileToggle.setAttribute("aria-expanded", "false");
    }
  }

  if (mobileToggle) {
    mobileToggle.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMobileMenu();
    });
  }

  // Close Mobile Menu on Outside Click
  document.addEventListener("click", (e) => {
    if (
      mobileMenu &&
      mobileMenu.classList.contains("is-open") &&
      !mobileMenu.contains(e.target) &&
      !mobileToggle.contains(e.target)
    ) {
      closeMobileMenu();
    }
  });

  // Close Mobile Menu on Escape Key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && mobileMenu && mobileMenu.classList.contains("is-open")) {
      closeMobileMenu();
    }
  });

  // Initial Needle Position
  rotateCompass(0);

  /* --------------------------------------------------------------------------
     5. REUSABLE ACCESSIBLE PROJECT MODAL (Entrepreneurship Experiments)
     -------------------------------------------------------------------------- */
  const modalBackdrop = document.getElementById("projectModalBackdrop");
  const modalCloseBtn = document.getElementById("modalCloseBtn");
  let lastActiveElement = null;

  /**
   * Open Modal for a Specific Project
   * @param {string} projectId
   */
  function openProjectModal(projectId) {
    if (!modalBackdrop || typeof PORTFOLIO_DATA === "undefined") return;

    const project = PORTFOLIO_DATA.entrepreneurship.find((p) => p.id === projectId);
    if (!project) return;

    lastActiveElement = document.activeElement;

    // Populate Modal Elements
    const numberEl = document.getElementById("modalProjectNumber");
    const categoryEl = document.getElementById("modalProjectCategory");
    const highlightEl = document.getElementById("modalProjectHighlight");
    const titleEl = document.getElementById("modalProjectTitle");
    const roleEl = document.getElementById("modalProjectRole");
    const statsGridEl = document.getElementById("modalStatsGrid");
    const overviewEl = document.getElementById("modalProjectOverview");
    const problemEl = document.getElementById("modalProjectProblem");
    const responsibilitiesEl = document.getElementById("modalProjectResponsibilities");
    const approachEl = document.getElementById("modalProjectApproach");
    const resultsEl = document.getElementById("modalProjectResults");

    if (numberEl) numberEl.textContent = project.number;
    if (categoryEl) categoryEl.textContent = project.category;
    if (highlightEl) highlightEl.textContent = project.cardHighlight;
    if (titleEl) titleEl.textContent = project.title;
    if (roleEl) roleEl.innerHTML = `<strong>${project.role}</strong> · ${project.duration}`;

    // Populate Key Metrics
    if (statsGridEl && Array.isArray(project.metrics)) {
      statsGridEl.innerHTML = project.metrics
        .map(
          (m) => `
          <div class="modal-stat-box">
            <span class="modal-stat-val">${m.value}</span>
            <span class="modal-stat-lbl">${m.label}</span>
          </div>
        `
        )
        .join("");
    }

    // Populate Narrative Sections
    if (overviewEl) overviewEl.textContent = project.modal.overview;
    if (problemEl) problemEl.textContent = project.modal.problem;

    if (responsibilitiesEl && Array.isArray(project.modal.responsibilities)) {
      responsibilitiesEl.innerHTML = project.modal.responsibilities
        .map((r) => `<li>${r}</li>`)
        .join("");
    }

    if (approachEl) approachEl.textContent = project.modal.approach;
    if (resultsEl) resultsEl.textContent = project.modal.results;

    // Open Modal
    modalBackdrop.classList.add("is-open");
    modalBackdrop.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";

    // Focus Close Button for accessibility
    setTimeout(() => {
      if (modalCloseBtn) modalCloseBtn.focus();
    }, 50);
  }

  /**
   * Close Project Modal
   */
  function closeProjectModal() {
    if (!modalBackdrop) return;
    modalBackdrop.classList.remove("is-open");
    modalBackdrop.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";

    if (lastActiveElement && typeof lastActiveElement.focus === "function") {
      lastActiveElement.focus();
    }
  }

  // Bind Project Card Clicks
  const projectCards = document.querySelectorAll("[data-project-trigger]");
  projectCards.forEach((card) => {
    card.addEventListener("click", () => {
      const pid = card.getAttribute("data-project-trigger");
      if (pid) openProjectModal(pid);
    });

    // Support Enter or Space on keyboard
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        const pid = card.getAttribute("data-project-trigger");
        if (pid) openProjectModal(pid);
      }
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener("click", closeProjectModal);
  }

  // Close on Backdrop Click
  if (modalBackdrop) {
    modalBackdrop.addEventListener("click", (e) => {
      if (e.target === modalBackdrop) {
        closeProjectModal();
      }
    });
  }

  // Close on Escape Key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modalBackdrop && modalBackdrop.classList.contains("is-open")) {
      closeProjectModal();
    }
  });

  /* --------------------------------------------------------------------------
     6. REUSABLE STARTUP IDEA MODAL (Ideas & MVP Section)
     -------------------------------------------------------------------------- */
  const startupModalBackdrop = document.getElementById("startupModalBackdrop");
  const startupModalCloseBtn = document.getElementById("startupModalCloseBtn");

  /**
   * Open Modal for a Specific Startup
   * @param {string} startupId
   */
  function openStartupModal(startupId) {
    if (!startupModalBackdrop || typeof PORTFOLIO_DATA === "undefined") return;

    const startup = PORTFOLIO_DATA.startupIdeas.find((s) => s.id === startupId);
    if (!startup) return;

    lastActiveElement = document.activeElement;

    // Elements
    const tagEl = document.getElementById("modalStartupTag");
    const stageEl = document.getElementById("modalStartupStage");
    const nameEl = document.getElementById("modalStartupName");
    const taglineEl = document.getElementById("modalStartupTagline");
    const whyEl = document.getElementById("modalStartupWhy");
    const problemEl = document.getElementById("modalStartupProblem");
    const solutionEl = document.getElementById("modalStartupSolution");
    const stageTextEl = document.getElementById("modalStartupStageText");
    const extraBoxEl = document.getElementById("modalStartupExtraBox");

    if (tagEl) tagEl.textContent = startup.tag;
    if (stageEl) stageEl.textContent = startup.stage;
    if (nameEl) nameEl.textContent = startup.name;
    if (taglineEl) taglineEl.textContent = startup.modal.tagline;
    if (whyEl) whyEl.textContent = startup.modal.whyStarted;
    if (problemEl) problemEl.textContent = startup.modal.problem;
    if (solutionEl) solutionEl.textContent = startup.modal.solution;
    if (stageTextEl) stageTextEl.textContent = startup.stage;

    // Handle extra callouts (Roadmap or Positioning Note)
    if (extraBoxEl) {
      if (startup.modal.roadmap) {
        extraBoxEl.style.display = "block";
        extraBoxEl.innerHTML = `
          <p class="modal-callout-title">Product Roadmap &amp; Next Phases</p>
          <p class="modal-callout-text">${startup.modal.roadmap}</p>
        `;
      } else if (startup.modal.positioningNote) {
        extraBoxEl.style.display = "block";
        extraBoxEl.innerHTML = `
          <p class="modal-callout-title">Positioning &amp; Boundary Note</p>
          <p class="modal-callout-text">${startup.modal.positioningNote}</p>
        `;
      } else {
        extraBoxEl.style.display = "none";
        extraBoxEl.innerHTML = "";
      }
    }

    // Open Modal
    startupModalBackdrop.classList.add("is-open");
    startupModalBackdrop.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";

    setTimeout(() => {
      if (startupModalCloseBtn) startupModalCloseBtn.focus();
    }, 50);
  }

  /**
   * Close Startup Modal
   */
  function closeStartupModal() {
    if (!startupModalBackdrop) return;
    startupModalBackdrop.classList.remove("is-open");
    startupModalBackdrop.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";

    if (lastActiveElement && typeof lastActiveElement.focus === "function") {
      lastActiveElement.focus();
    }
  }

  // Bind Startup Trigger Clicks
  const startupTriggers = document.querySelectorAll("[data-startup-trigger]");
  startupTriggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const sid = trigger.getAttribute("data-startup-trigger");
      if (sid) openStartupModal(sid);
    });

    trigger.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        const sid = trigger.getAttribute("data-startup-trigger");
        if (sid) openStartupModal(sid);
      }
    });
  });

  if (startupModalCloseBtn) {
    startupModalCloseBtn.addEventListener("click", closeStartupModal);
  }

  if (startupModalBackdrop) {
    startupModalBackdrop.addEventListener("click", (e) => {
      if (e.target === startupModalBackdrop) {
        closeStartupModal();
      }
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && startupModalBackdrop && startupModalBackdrop.classList.contains("is-open")) {
      closeStartupModal();
    }
  });

  /* --------------------------------------------------------------------------
     7. SHOW DECK BUTTON HANDLERS (Academic & Business Problems)
     -------------------------------------------------------------------------- */
  const deckButtons = document.querySelectorAll("[data-deck-id]");
  deckButtons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const deckId = btn.getAttribute("data-deck-id");
      if (!deckId || typeof PORTFOLIO_DATA === "undefined") return;

      // Find in academic projects or business problems
      const item =
        PORTFOLIO_DATA.academicProjects.find((p) => p.id === deckId) ||
        PORTFOLIO_DATA.businessProblems.find((p) => p.id === deckId);

      if (item && item.deckUrl) {
        window.open(item.deckUrl, "_blank", "noopener,noreferrer");
      } else {
        // Subtle ripple or toast for Coming Soon
        const originalText = btn.textContent;
        btn.textContent = "URL placeholder configured · Coming Soon";
        setTimeout(() => {
          btn.textContent = originalText;
        }, 2200);
      }
    });
  });
  /* --------------------------------------------------------------------------
     8. RESUME ACTION HANDLER
     -------------------------------------------------------------------------- */
  const resumeBtn = document.getElementById("viewResumeBtn");
  if (resumeBtn) {
    resumeBtn.addEventListener("click", () => {
      if (typeof PORTFOLIO_DATA !== "undefined" && PORTFOLIO_DATA.resume?.fileUrl) {
        window.open(PORTFOLIO_DATA.resume.fileUrl, "_blank", "noopener,noreferrer");
      } else {
        const originalText = resumeBtn.innerHTML;
        resumeBtn.innerHTML = `
          <span>Resume PDF Coming Soon</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="12" cy="12" r="10"/>
            <polyline points="12 6 12 12 16 14"/>
          </svg>
        `;
        setTimeout(() => {
          resumeBtn.innerHTML = originalText;
        }, 2400);
      }
    });
  }

  /* --------------------------------------------------------------------------
     9. CONNECT CHANNELS INTERACTION HANDLER
     -------------------------------------------------------------------------- */
  const connectCards = document.querySelectorAll("[data-connect-id]");
  connectCards.forEach((card) => {
    card.addEventListener("click", (e) => {
      const channelId = card.getAttribute("data-connect-id");
      if (!channelId || typeof PORTFOLIO_DATA === "undefined") return;

      const linkObj = PORTFOLIO_DATA.connectLinks.find((l) => l.id === channelId);
      if (!linkObj) return;

      if (linkObj.url) {
        if (linkObj.url.startsWith("mailto:")) {
          window.location.href = linkObj.url;
        } else {
          window.open(linkObj.url, "_blank", "noopener,noreferrer");
        }
      } else {
        e.preventDefault();
        const handleEl = card.querySelector(".connect-channel-handle");
        if (handleEl) {
          const original = handleEl.textContent;
          handleEl.textContent = "Awaiting link from Hassaan · Placeholder ready";
          handleEl.style.color = "var(--accent-gold)";
          setTimeout(() => {
            handleEl.textContent = original;
            handleEl.style.color = "";
          }, 2400);
        }
      }
    });
  });
})();
