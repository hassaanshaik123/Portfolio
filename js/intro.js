(() => {
  if ((location.hash && location.hash !== "#home") || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const root = document.documentElement;
  root.classList.add("intro-pending");
  let overlay;
  let frame;
  let finished = false;
  function finish() {
    if (finished) return;
    finished = true;
    cancelAnimationFrame(frame);
    root.classList.remove("intro-pending");
    window.dispatchEvent(new Event("portfolio-intro-complete"));
    overlay?.classList.add("intro-leaving");
    setTimeout(() => overlay?.remove(), 450);
  }
  // Always release the page, even if the animation cannot start.
  const safety = setTimeout(finish, 7000);
  document.addEventListener("DOMContentLoaded", () => {
    if (finished) return;
    overlay = document.createElement("div");
    overlay.className = "intro-loader";
    overlay.innerHTML = `
      <div class="intro-content">
        <span class="intro-brand">HASSAAN<span>.</span></span>
        <div class="intro-scene" aria-hidden="true">
          <div class="morphing-square"></div>
        </div>
        <div class="intro-readout"><span class="intro-message">Loading portfolio</span><span class="intro-percent">0<span>%</span></span></div>
        <div class="intro-track" role="progressbar" aria-label="Opening portfolio" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span></span></div>
        <p class="sr-only" role="status">Opening Hassaan’s portfolio.</p>
      </div>`;
    document.body.prepend(overlay);
    const bar = overlay.querySelector(".intro-track");
    const fill = bar.firstElementChild;
    const percent = overlay.querySelector(".intro-percent");
    const message = overlay.querySelector(".intro-message");
    const start = performance.now();
    let lastPercent = -1;
    function draw(now) {
      if (finished) return;
      const elapsed = Math.min((now - start) / 1000, 5.5);
      const progress = elapsed / 5.5;
      const value = Math.floor(progress * 100);
      if (value !== lastPercent) {
        percent.innerHTML = `${value}<span>%</span>`;
        bar.setAttribute("aria-valuenow", value);
        fill.style.transform = `scaleX(${progress})`;
        lastPercent = value;
      }
      message.textContent = progress < 0.95 ? "Loading portfolio" : "Let’s get started";
      if (progress < 1) frame = requestAnimationFrame(draw);
      else {
        clearTimeout(safety);
        setTimeout(finish, 150);
      }
    }
    frame = requestAnimationFrame(draw);
  }, { once: true });
})();
