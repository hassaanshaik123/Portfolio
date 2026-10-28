/* ==========================================================================
   Main Interactions — Muhammad Hassaan Portfolio
   ========================================================================== */

(function () {
  "use strict";

  // 1. Project Case Study Data (Strictly factual per user prompt — zero invented stats/claims)
  const PROJECT_DATA = {
    pepperfry: {
      category: "Customer Experience · Business Analysis · Growth Strategy",
      title: "Pepperfry — Customer Experience Improvement",
      summary:
        "A customer experience and business growth analysis focused on addressing post-purchase friction in Pepperfry's customer journey.",
      blocks: [
        {
          heading: "Context",
          body: "We identified a problem in Pepperfry's post-purchase services. This was an area the company appeared to be neglecting, despite many customer complaints falling within that stage of the customer journey."
        },
        {
          heading: "Our Work",
          body: "We highlighted the post-purchase service gap and proposed three structured recommendations that could improve the customer experience and help boost sales."
        },
        {
          heading: "Focus Areas",
          body: "Customer Experience · Post-Purchase Journey Analysis · Business Growth Strategy"
        },
        {
          heading: "Expected Impact (Potential Outcome)",
          body: "Designed to reduce post-purchase friction, strengthen customer trust after checkout, and unlock potential repeat and referral sales growth through improved service reliability."
        }
      ]
    },
    clario: {
      category: "Product Discovery · User Research · EdTech · AI & Text-to-Speech",
      title: "Clario AI — Articles to Regional Audio Notes",
      summary:
        "A product discovery and concept development project designed to make dense written material easier to consume through regional-language audio.",
      blocks: [
        {
          heading: "Context",
          body: "Clario AI is a text-to-speech product concept designed to convert long articles into audio notes in regional languages and explain the content in simple language."
        },
        {
          heading: "Target Users",
          list: ["MBA students", "UPSC aspirants"]
        },
        {
          heading: "Problem Identified",
          body: "The product was conceived around the difficulty these users face in consuming lengthy, dense written information across tight study schedules."
        },
        {
          heading: "Our Approach",
          body: "We identified the core comprehension and time-constraint bottleneck and developed a product concept that makes information easier to consume through simplified, regional-language audio notes."
        }
      ]
    }
  };

  // 2. Project Detail Modal Controller
  const modalBackdrop = document.getElementById("projectModalBackdrop");
  const modalCategory = document.getElementById("modalCategory");
  const modalTitle = document.getElementById("modalTitle");
  const modalSummary = document.getElementById("modalSummary");
  const modalGrid = document.getElementById("modalGrid");
  const modalCloseBtn = document.getElementById("modalCloseBtn");
  let lastFocusedElement = null;

  function openProjectModal(projectId) {
    const data = PROJECT_DATA[projectId];
    if (!data || !modalBackdrop) return;

    lastFocusedElement = document.activeElement;
    modalCategory.textContent = data.category;
    modalTitle.textContent = data.title;
    modalSummary.textContent = data.summary;

    modalGrid.innerHTML = "";
    data.blocks.forEach(function (block) {
      const div = document.createElement("div");
      div.className = "project-modal-block";

      const h4 = document.createElement("h4");
      h4.textContent = block.heading;
      div.appendChild(h4);

      if (block.list) {
        const ul = document.createElement("ul");
        block.list.forEach(function (item) {
          const li = document.createElement("li");
          li.textContent = item;
          ul.appendChild(li);
        });
        div.appendChild(ul);
      } else {
        const p = document.createElement("p");
        p.textContent = block.body;
        div.appendChild(p);
      }

      modalGrid.appendChild(div);
    });

    modalBackdrop.classList.add("is-open");
    modalBackdrop.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    modalCloseBtn.focus();
  }

  function closeProjectModal() {
    if (!modalBackdrop || !modalBackdrop.classList.contains("is-open")) return;
    modalBackdrop.classList.remove("is-open");
    modalBackdrop.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (lastFocusedElement) {
      lastFocusedElement.focus();
    }
  }

  document.querySelectorAll("[data-project-id]").forEach(function (card) {
    card.addEventListener("click", function () {
      openProjectModal(card.getAttribute("data-project-id"));
    });

    card.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        openProjectModal(card.getAttribute("data-project-id"));
      }
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener("click", closeProjectModal);
  }

  if (modalBackdrop) {
    modalBackdrop.addEventListener("click", function (e) {
      if (e.target === modalBackdrop) {
        closeProjectModal();
      }
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeProjectModal();
    }
  });

  // 3. Photos Gallery Placeholder Slideshow Controls
  const photoDots = document.querySelectorAll("[data-photo-slide-btn]");
  const photoSlides = document.querySelectorAll("[data-photo-slide]");

  photoDots.forEach(function (dot) {
    dot.addEventListener("click", function () {
      const targetIndex = dot.getAttribute("data-photo-slide-btn");
      photoDots.forEach(function (d) {
        d.classList.toggle("is-active", d === dot);
        d.setAttribute("aria-selected", d === dot ? "true" : "false");
      });
      photoSlides.forEach(function (slide) {
        slide.classList.toggle(
          "is-active",
          slide.getAttribute("data-photo-slide") === targetIndex
        );
      });
    });
  });

  // 4. Active Section Highlighting in Floating Navigation
  const navLinks = document.querySelectorAll(".nav-link[href^='#']");
  const observedSections = ["work", "about", "experience", "contact"]
    .map(function (id) {
      return document.getElementById(id);
    })
    .filter(Boolean);

  if ("IntersectionObserver" in window && observedSections.length > 0) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            const activeId = entry.target.id;
            navLinks.forEach(function (link) {
              const href = link.getAttribute("href");
              link.classList.toggle("is-active", href === "#" + activeId);
            });
          }
        });
      },
      { rootMargin: "-30% 0px -55% 0px", threshold: 0 }
    );

    observedSections.forEach(function (sec) {
      observer.observe(sec);
    });
  }
})();
