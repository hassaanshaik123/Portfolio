(() => {
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference;
  try {
    preference = localStorage.getItem("portfolio-theme");
  } catch {}
  if (preference !== "light" && preference !== "dark") preference = null;
  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    window.dispatchEvent(new Event("portfolio-theme-change"));
  }
  apply(preference || (system.matches ? "dark" : "light"));
  window.portfolioTheme = {
    set(theme) {
      preference = theme;
      try {
        localStorage.setItem("portfolio-theme", theme);
      } catch {}
      apply(theme);
    },
  };
  system.addEventListener("change", () => {
    if (!preference) apply(system.matches ? "dark" : "light");
  });
  window.addEventListener("storage", (event) => {
    if (event.key !== "portfolio-theme") return;
    preference = ["light", "dark"].includes(event.newValue) ? event.newValue : null;
    apply(preference || (system.matches ? "dark" : "light"));
  });
})();
