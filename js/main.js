/**
 * Muhammad Hassaan — Personal Portfolio
 * Interactions:
 *  1. Smooth in-page anchor navigation & active section highlight
 *  2. Interactive top crimson orb portrait reveal (#heroOrbStage)
 *  3. Interactive 3D Flip & Pop-Out Project Flashcards (Pepperfry & Clario AI)
 *  4. Interactive HTML5 Canvas Halftone/Pixel Portrait Reveal (#portraitCanvas)
 *  5. Gallery slide switcher & scroll entrance reveals
 */

(function () {
  "use strict";

  /* --------------------------------------------------------------------------
     1. Project Flashcard Data (Strictly Factual — No Invented Metrics/Claims)
     -------------------------------------------------------------------------- */
  const PROJECTS = {
    pepperfry: {
      category: "Customer Experience · Business Analysis · Growth Strategy",
      title: "Pepperfry — Customer Experience Improvement",
      image: "assets/pepperfry.png",
      imageAlt: "Pepperfry — Customer Experience Improvement visual",
      summary:
        "A customer experience and business growth project examining post-purchase service friction and its connection to customer retention and sales potential.",
      details: [
        {
          label: "01 / Context",
          body: "We identified a problem in Pepperfry's post-purchase services. This was an area the company appeared to be neglecting, despite many customer complaints falling within that stage of the customer journey."
        },
        {
          label: "02 / Problem Stage",
          body: "Customer complaints were concentrated in the post-purchase stage of the journey, signaling an underserved operational and customer-experience gap."
        },
        {
          label: "03 / Our Work",
          body: "We highlighted the problem and proposed three recommendations that could improve the customer experience and help boost sales."
        },
        {
          label: "04 / Expected Impact (Potential Outcome)",
          body: "Framed as a customer experience and business growth opportunity: resolving post-purchase friction has the potential to strengthen customer trust, improve satisfaction, and support stronger sales outcomes."
        }
      ]
    },
    clario: {
      category: "Product Discovery · User Research · EdTech · AI and Text-to-Speech",
      title: "Clario AI — Articles to Regional Audio Notes",
      image: "assets/clario.png",
      imageAlt: "Clario AI — Articles to Regional Audio Notes visual",
      summary:
        "A product discovery and development concept demonstrating problem identification and solution thinking around long-form reading fatigue.",
      details: [
        {
          label: "01 / Product Concept",
          body: "Clario AI is a text-to-speech product concept designed to convert long articles into audio notes in regional languages and explain the content in simple language."
        },
        {
          label: "02 / Target Users",
          body: "Designed specifically for MBA students and UPSC aspirants who regularly work through dense, high-volume reading material."
        },
        {
          label: "03 / Core Problem",
          body: "The product was conceived around the difficulty these users face in consuming lengthy written information efficiently."
        },
        {
          label: "04 / Our Approach",
          body: "We identified the problem and developed a product concept that makes information easier to consume through regional-language audio and simplified explanations."
        }
      ]
    }
  };

  /* --------------------------------------------------------------------------
     2. Smooth Scroll Navigation, Slide-Down After Hero & Active Link Highlight
     -------------------------------------------------------------------------- */
  const navWrapper = document.querySelector(".nav-wrapper");
  const heroSection = document.getElementById("hero");

  function updateNavVisibility() {
    if (!navWrapper || !heroSection) return;
    const heroRect = heroSection.getBoundingClientRect();
    // Slide down the navigation bar once the user reaches the end of the hero section
    const pastHero = heroRect.bottom <= 180;
    navWrapper.classList.toggle("is-visible", pastHero);
  }

  window.addEventListener("scroll", updateNavVisibility, { passive: true });
  window.addEventListener("resize", updateNavVisibility, { passive: true });
  updateNavVisibility();

  const navLinks = document.querySelectorAll('.nav-link[href^="#"], .nav-logo[href^="#"]');

  navLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      const targetId = link.getAttribute("href");
      if (!targetId || targetId === "#") return;
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        event.preventDefault();
        targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
        history.replaceState(null, "", targetId);
      }
    });
  });

  const sections = ["work", "about", "experience", "contact"]
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length > 0) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const activeHash = `#${entry.target.id}`;
            document.querySelectorAll(".nav-link").forEach((navItem) => {
              navItem.classList.toggle(
                "is-active",
                navItem.getAttribute("href") === activeHash
              );
            });
          }
        });
      },
      { rootMargin: "-35% 0px -50% 0px", threshold: 0 }
    );

    sections.forEach((section) => observer.observe(section));
  }

  /* --------------------------------------------------------------------------
     3. Entrance Reveal Observer (.reveal-up)
     -------------------------------------------------------------------------- */
  const revealItems = document.querySelectorAll(".reveal-up");
  if ("IntersectionObserver" in window && revealItems.length > 0) {
    const revealObserver = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );

    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  /* --------------------------------------------------------------------------
     4. Hero Top Crimson Orb Toggle (Touch & Keyboard Accessibility)
     -------------------------------------------------------------------------- */
  const heroOrbStage = document.getElementById("heroOrbStage");
  if (heroOrbStage) {
    heroOrbStage.addEventListener("click", () => {
      heroOrbStage.classList.toggle("is-expanded");
    });
    heroOrbStage.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        heroOrbStage.classList.toggle("is-expanded");
      }
    });
  }

  /* --------------------------------------------------------------------------
     5. Interactive 3D Flip & Pop-Out Flashcards (Pepperfry & Clario AI)
     -------------------------------------------------------------------------- */
  const modalBackdrop = document.getElementById("flashcardModalBackdrop");
  const popoutCard3D = document.getElementById("popoutCard3D");
  const popoutFlipBtn = document.getElementById("popoutFlipBtn");
  const popoutFlipLabel = document.getElementById("popoutFlipLabel");
  const popoutCloseBtn = document.getElementById("popoutCloseBtn");
  const popoutImage = document.getElementById("popoutImage");
  const popoutCategory = document.getElementById("popoutCategory");
  const popoutTitle = document.getElementById("popoutTitle");
  const popoutSummary = document.getElementById("popoutSummary");
  const popoutGrid = document.getElementById("popoutGrid");

  let lastFocusedFlashcard = null;
  let flipTimer = null;

  function updatePopoutFlipLabel(isFlippedToBack) {
    if (!popoutFlipLabel) return;
    popoutFlipLabel.textContent = isFlippedToBack
      ? "Flip to front photo"
      : "Turn up flashcard details";
  }

  function openPopoutFlashcard(projectId, triggerElement) {
    const project = PROJECTS[projectId];
    if (!project || !modalBackdrop || !popoutCard3D) return;

    lastFocusedFlashcard = triggerElement || document.activeElement;

    // Also flip the inline flashcard so the user sees the 3D rotation immediately
    const inlineCard = document.querySelector(`.flashcard-3d[data-flashcard-id="${projectId}"]`);
    if (inlineCard) {
      inlineCard.classList.add("is-flipped");
      inlineCard.setAttribute("aria-expanded", "true");
    }

    // Populate front & back faces of the popped-out 3D flashcard
    if (popoutImage) {
      popoutImage.src = project.image;
      popoutImage.alt = project.imageAlt;
    }
    popoutCategory.textContent = project.category;
    popoutTitle.textContent = project.title;
    popoutSummary.textContent = project.summary;

    popoutGrid.innerHTML = project.details
      .map(
        (item) => `
        <div class="popout-detail-item">
          <p class="popout-detail-label">${item.label}</p>
          <p class="popout-detail-body">${item.body}</p>
        </div>
      `
      )
      .join("");

    // Start the popped-out card on the front photo face, then animate the 3D flip!
    popoutCard3D.classList.remove("is-flipped");
    updatePopoutFlipLabel(false);

    modalBackdrop.classList.add("is-open");
    modalBackdrop.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";

    if (flipTimer) clearTimeout(flipTimer);
    flipTimer = setTimeout(() => {
      popoutCard3D.classList.add("is-flipped");
      updatePopoutFlipLabel(true);
    }, 110);

    if (popoutCloseBtn) {
      popoutCloseBtn.focus();
    }
  }

  function togglePopoutCardFlip() {
    if (!popoutCard3D) return;
    const isNowFlipped = popoutCard3D.classList.toggle("is-flipped");
    updatePopoutFlipLabel(isNowFlipped);
  }

  function closePopoutFlashcard() {
    if (!modalBackdrop) return;
    if (flipTimer) clearTimeout(flipTimer);

    modalBackdrop.classList.remove("is-open");
    modalBackdrop.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";

    // Reset inline flashcards back to front photo face smoothly when modal closes
    document.querySelectorAll(".flashcard-3d.is-flipped").forEach((card) => {
      card.classList.remove("is-flipped");
      card.setAttribute("aria-expanded", "false");
    });

    if (lastFocusedFlashcard && typeof lastFocusedFlashcard.focus === "function") {
      lastFocusedFlashcard.focus();
    }
  }

  // Bind click & keyboard events on the 3D flashcards
  document.querySelectorAll(".flashcard-3d[data-flashcard-id]").forEach((flashcard) => {
    const projectId = flashcard.getAttribute("data-flashcard-id");

    flashcard.addEventListener("click", () => {
      openPopoutFlashcard(projectId, flashcard);
    });

    flashcard.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openPopoutFlashcard(projectId, flashcard);
      }
    });
  });

  // Bind click on the left-column circular action buttons
  document.querySelectorAll("[data-trigger-flashcard]").forEach((btn) => {
    const projectId = btn.getAttribute("data-trigger-flashcard");
    btn.addEventListener("click", () => {
      openPopoutFlashcard(projectId, btn);
    });
  });

  if (popoutFlipBtn) {
    popoutFlipBtn.addEventListener("click", (event) => {
      event.stopPropagation();
      togglePopoutCardFlip();
    });
  }

  if (popoutCard3D) {
    popoutCard3D.addEventListener("click", () => {
      togglePopoutCardFlip();
    });
  }

  if (popoutCloseBtn) {
    popoutCloseBtn.addEventListener("click", closePopoutFlashcard);
  }

  if (modalBackdrop) {
    modalBackdrop.addEventListener("click", (event) => {
      if (event.target === modalBackdrop) {
        closePopoutFlashcard();
      }
    });
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && modalBackdrop && modalBackdrop.classList.contains("is-open")) {
      closePopoutFlashcard();
    }
  });

  /* --------------------------------------------------------------------------
     6. Interactive HTML5 Canvas Halftone/Pixel Portrait Reveal (#portraitCanvas)
        Matches dharmeshnayak.com's blockSize/revealRadius/ease/raggedness effect
     -------------------------------------------------------------------------- */
  const portraitCard = document.getElementById("aboutPortraitCard");
  const portraitCanvas = document.getElementById("portraitCanvas");
  const portraitSource = document.getElementById("aboutPortraitSource");

  if (portraitCard && portraitCanvas && portraitSource) {
    const ctx = portraitCanvas.getContext("2d");
    const offscreen = document.createElement("canvas");
    const offCtx = offscreen.getContext("2d", { willReadFrequently: true });

    const BLOCK_SIZE = 5;
    const REVEAL_RADIUS = 155;
    const EASE_IN = 0.22;
    const EASE_OUT = 0.035;
    const RAGGEDNESS = 0.36;

    let width = 0;
    let height = 0;
    let cols = 0;
    let rows = 0;
    let cellWeights = null;
    let cellJitter = null;
    let cellLums = null;
    let pointerX = -9999;
    let pointerY = -9999;
    let isPointerInside = false;
    let rafId = null;
    let imageReady = false;

    function buildGrid() {
      const rect = portraitCard.getBoundingClientRect();
      width = Math.max(1, Math.round(rect.width));
      height = Math.max(1, Math.round(rect.height));

      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      portraitCanvas.width = width * dpr;
      portraitCanvas.height = height * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      offscreen.width = width;
      offscreen.height = height;

      // Draw cover-fitted source portrait onto offscreen canvas
      const imgW = portraitSource.naturalWidth || 768;
      const imgH = portraitSource.naturalHeight || 1024;
      const scale = Math.max(width / imgW, height / imgH);
      const drawW = imgW * scale;
      const drawH = imgH * scale;
      const offsetX = (width - drawW) * 0.5;
      const offsetY = (height - drawH) * 0.15;

      offCtx.clearRect(0, 0, width, height);
      offCtx.drawImage(portraitSource, offsetX, offsetY, drawW, drawH);

      const imgData = offCtx.getImageData(0, 0, width, height).data;

      cols = Math.ceil(width / BLOCK_SIZE);
      rows = Math.ceil(height / BLOCK_SIZE);
      const total = cols * rows;

      cellWeights = new Float32Array(total);
      cellJitter = new Float32Array(total);
      cellLums = new Uint8Array(total);

      for (let r = 0; r < rows; r++) {
        const py = Math.min(height - 1, r * BLOCK_SIZE + (BLOCK_SIZE >> 1));
        for (let c = 0; c < cols; c++) {
          const px = Math.min(width - 1, c * BLOCK_SIZE + (BLOCK_SIZE >> 1));
          const idx = (py * width + px) * 4;
          const red = imgData[idx];
          const green = imgData[idx + 1];
          const blue = imgData[idx + 2];

          // Perceived luminance with subtle contrast curve for editorial dark bento feel
          let lum = Math.round(0.299 * red + 0.587 * green + 0.114 * blue);
          lum = Math.max(12, Math.min(235, Math.round((lum - 115) * 1.18 + 95)));

          const cellIdx = r * cols + c;
          cellLums[cellIdx] = lum;
          // Deterministic organic jitter per cell
          const seed = Math.sin(c * 12.9898 + r * 78.233) * 43758.5453;
          cellJitter[cellIdx] = (seed - Math.floor(seed) - 0.5) * 2 * RAGGEDNESS;
        }
      }

      renderFrame();
    }

    function renderFrame() {
      if (!imageReady || !cellWeights) return;

      let anyActive = false;

      // 1. Base layer: draw the dark monochrome pixelated/halftone portrait
      ctx.fillStyle = "#101010";
      ctx.fillRect(0, 0, width, height);

      for (let r = 0; r < rows; r++) {
        const y = r * BLOCK_SIZE;
        const cy = y + BLOCK_SIZE * 0.5;
        for (let c = 0; c < cols; c++) {
          const x = c * BLOCK_SIZE;
          const cx = x + BLOCK_SIZE * 0.5;
          const i = r * cols + c;

          let target = 0;
          if (isPointerInside) {
            const dx = cx - pointerX;
            const dy = cy - pointerY;
            const dist = Math.sqrt(dx * dx + dy * dy);
            const effectiveRadius = REVEAL_RADIUS * (1 + cellJitter[i]);
            if (dist < effectiveRadius) {
              target = Math.min(1, Math.max(0, 1 - Math.pow(dist / effectiveRadius, 2.2)));
            }
          }

          const current = cellWeights[i];
          const next =
            target > current
              ? current + (target - current) * EASE_IN
              : current + (target - current) * EASE_OUT;

          cellWeights[i] = next < 0.004 ? 0 : next;
          if (cellWeights[i] > 0.004 || isPointerInside) {
            anyActive = true;
          }

          // Monochrome halftone dot/block size modulated by luminance
          const lum = cellLums[i];
          const shade = Math.round(lum * 0.72);
          ctx.fillStyle = `rgb(${shade}, ${shade}, ${Math.min(255, shade + 4)})`;
          ctx.fillRect(x, y, BLOCK_SIZE - 1, BLOCK_SIZE - 1);

          // Overlay full-color source block where revealed by cursor
          if (cellWeights[i] > 0.01) {
            ctx.save();
            ctx.globalAlpha = Math.min(1, cellWeights[i]);
            ctx.drawImage(
              offscreen,
              x,
              y,
              BLOCK_SIZE,
              BLOCK_SIZE,
              x,
              y,
              BLOCK_SIZE,
              BLOCK_SIZE
            );
            ctx.restore();
          }
        }
      }

      if (anyActive) {
        rafId = requestAnimationFrame(renderFrame);
      } else {
        rafId = null;
      }
    }

    function startLoop() {
      if (!rafId) {
        rafId = requestAnimationFrame(renderFrame);
      }
    }

    function updatePointer(clientX, clientY) {
      const rect = portraitCard.getBoundingClientRect();
      pointerX = clientX - rect.left;
      pointerY = clientY - rect.top;
      isPointerInside = true;
      startLoop();
    }

    portraitCard.addEventListener("mousemove", (event) => {
      updatePointer(event.clientX, event.clientY);
    });

    portraitCard.addEventListener("mouseleave", () => {
      isPointerInside = false;
      startLoop();
    });

    portraitCard.addEventListener(
      "touchmove",
      (event) => {
        if (event.touches && event.touches[0]) {
          updatePointer(event.touches[0].clientX, event.touches[0].clientY);
        }
      },
      { passive: true }
    );

    portraitCard.addEventListener("touchend", () => {
      isPointerInside = false;
      startLoop();
    });

    function initPortraitCanvas() {
      imageReady = true;
      buildGrid();
    }

    if (portraitSource.complete && portraitSource.naturalWidth > 0) {
      initPortraitCanvas();
    } else {
      portraitSource.addEventListener("load", initPortraitCanvas);
    }

    window.addEventListener("resize", () => {
      if (imageReady) {
        buildGrid();
      }
    });
  }

  /* --------------------------------------------------------------------------
     7. Personal Gallery — Photos Slide Switcher
     -------------------------------------------------------------------------- */
  const photoSlideButtons = document.querySelectorAll("[data-photo-slide-btn]");
  const photoSlides = document.querySelectorAll("[data-photo-slide]");

  if (photoSlideButtons.length > 0 && photoSlides.length > 0) {
    photoSlideButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetIndex = btn.getAttribute("data-photo-slide-btn");

        photoSlideButtons.forEach((b) => {
          const isMatch = b.getAttribute("data-photo-slide-btn") === targetIndex;
          b.classList.toggle("is-active", isMatch);
          b.setAttribute("aria-selected", isMatch ? "true" : "false");
        });

        photoSlides.forEach((slide) => {
          const isMatch = slide.getAttribute("data-photo-slide") === targetIndex;
          slide.classList.toggle("is-active", isMatch);
        });
      });
    });
  }
})();
