/* ============================================================
   Muhammad Hassaan — shared behaviors
   intro → cursor → dropdown → mobile sheet → progress →
   smooth scroll → rotator → stepper → count-up → reveal
   ============================================================ */
(function () {
  'use strict';
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = matchMedia('(pointer: fine)').matches;
  var d = document;

  /* ---------- intro overlay ---------- */
  var intro = d.getElementById('intro');
  if (intro && !reduced) {
    var INTRO_MS = 2600;          // must match the data-intro-duration you set
    intro.style.transitionDuration = '1s';
    var play = function () {
      intro.classList.add('play');                    // words rise + photo pops
      setTimeout(function () { intro.classList.add('done'); }, INTRO_MS - 1000);
    };
    // start after fonts load so the headline measures correctly
    if (d.readyState === 'complete') setTimeout(play, 150);
    else addEventListener('load', function () { setTimeout(play, 150); });

    // block scrolling while the curtain is up
    d.documentElement.style.overflow = 'hidden';
    setTimeout(function () { d.documentElement.style.overflow = ''; }, INTRO_MS);

    // hero entrance choreography starts as the curtain lifts
    var hero = d.querySelector('.hero');
    if (hero) setTimeout(function () { hero.classList.add('stagger'); }, INTRO_MS - 500);
  } else if (intro) {
    intro.style.display = 'none';
    var hero2 = d.querySelector('.hero');
    if (hero2) hero2.classList.add('stagger');
  }

  /* ---------- custom cursor with contextual labels ---------- */
  if (fine && !reduced) {
    d.documentElement.classList.add('has-cursor');
    var dot = d.getElementById('cursor-dot');
    var ring = d.getElementById('cursor-ring');
    if (dot && ring) {
      var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
      var labelEl = d.querySelector('.cursor-text');

      addEventListener('mousemove', function (e) {
        mx = e.clientX; my = e.clientY;
        dot.style.transform = 'translate(' + mx + 'px,' + my + 'px)';
      }, { passive: true });

      (function loop() {
        rx += (mx - rx) * 0.16;
        ry += (my - ry) * 0.16;
        ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px)';
        requestAnimationFrame(loop);
      })();

      // generic grow targets
      d.querySelectorAll('a, button, .pill, .steps li').forEach(function (el) {
        el.addEventListener('mouseenter', function () { ring.classList.add('big'); });
        el.addEventListener('mouseleave', function () { ring.classList.remove('big'); });
      });

      // contextual labels — exactly like omumrania.com (VIEW / READ)
      var LABELS = [
        { sel: '.cs-row', label: 'VIEW' },
        { sel: '.blog-row', label: 'READ' },
        { sel: '.tile', label: 'READ' },
        { sel: '.portrait', label: 'HELLO' },
      ];
      LABELS.forEach(function (cfg) {
        d.querySelectorAll(cfg.sel).forEach(function (el) {
          el.addEventListener('mouseenter', function () {
            ring.classList.add('label');
            ring.classList.remove('big');
            if (labelEl) labelEl.textContent = cfg.label;
          });
          el.addEventListener('mouseleave', function () {
            ring.classList.remove('label');
          });
        });
      });
    }
  }

  /* ---------- WORK dropdown ---------- */
  var btn = d.querySelector('.drop-btn');
  var menu = d.getElementById('work-menu');
  if (btn && menu) {
    var close = function () {
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    };
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
    });
    d.addEventListener('click', function (e) {
      if (menu.classList.contains('open') && !menu.contains(e.target)) close();
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', close);
    });
  }

  /* ---------- mobile sheet ---------- */
  var burger = d.querySelector('.burger');
  var sheet = d.getElementById('sheet');
  if (burger && sheet) {
    burger.addEventListener('click', function () {
      var open = sheet.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
    });
    sheet.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        sheet.classList.remove('open');
        burger.classList.remove('open');
      });
    });
  }

  /* ---------- scroll progress ---------- */
  var bar = d.getElementById('progress');
  if (bar) {
    var prog = function () {
      var h = d.documentElement.scrollHeight - innerHeight;
      bar.style.width = (h > 0 ? (scrollY / h) * 100 : 0) + '%';
    };
    addEventListener('scroll', prog, { passive: true });
    prog();
  }

  /* ---------- inert smooth-scroll physics (Lenis-style) ---------- */
  var targetY = scrollY, currentY = scrollY;
  if (!reduced) {
    addEventListener('wheel', function (e) {
      if (e.ctrlKey) return;
      e.preventDefault();
      var max = d.documentElement.scrollHeight - innerHeight;
      targetY = Math.max(0, Math.min(max, targetY + e.deltaY));
    }, { passive: false });
    addEventListener('scroll', function () {
      if (Math.abs(scrollY - currentY) > 2) { currentY = targetY = scrollY; }
    }, { passive: true });
    (function raf() {
      currentY += (targetY - currentY) * 0.09;
      if (Math.abs(targetY - currentY) < 0.5) currentY = targetY;
      scrollTo(0, currentY);
      requestAnimationFrame(raf);
    })();
  }

  /* ---------- anchor clicks respect physics ---------- */
  d.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var el = d.querySelector(a.getAttribute('href'));
      if (!el) return;
      e.preventDefault();
      if (!reduced) targetY = el.offsetTop - 80;
      else el.scrollIntoView({ behavior: 'smooth' });
    });
  });

  /* ---------- rotating hero word ---------- */
  var words = d.querySelectorAll('.rot');
  if (words.length) {
    var wi = 0;
    setInterval(function () {
      words[wi].classList.remove('on');
      wi = (wi + 1) % words.length;
      words[wi].classList.add('on');
    }, 2000);
  }

  /* ---------- Raah.AI flow stepper ---------- */
  var steps = d.querySelectorAll('.steps li');
  if (steps.length) {
    var si = 0;
    setInterval(function () {
      steps.forEach(function (s, i) { s.classList.toggle('active', i === si); });
      si = (si + 1) % steps.length;
    }, 1400);
  }

  /* ---------- count-up stats ---------- */
  function countUp(el) {
    var end = parseFloat(el.dataset.count), pre = el.dataset.prefix || '', suf = el.dataset.suffix || '';
    var t0 = performance.now(), dur = 1300;
    (function tick(t) {
      var p = Math.min(1, (t - t0) / dur);
      el.textContent = pre + Math.round(end * (1 - Math.pow(1 - p, 3))) + suf;
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }

  /* ---------- reveal on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      en.target.querySelectorAll('[data-count]').forEach(function (c, i) {
        setTimeout(function () { countUp(c); }, i * 150);
      });
      io.unobserve(en.target);
    });
  }, { threshold: 0.12 });
  d.querySelectorAll('.reveal').forEach(function (el, i) {
    el.style.transitionDelay = (i % 4) * 60 + 'ms';
    io.observe(el);
  });
})();
