/* ============================================================
   Muhammad Hassaan — v4 behaviors
   theme toggle → nav scroll state → mobile sheet → progress →
   reveal on scroll → count-up stats → FAQ exclusivity → anchors
   ============================================================ */
(function () {
  'use strict';
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var d = document;

  /* ---------- theme toggle (remembers visitor choice) ---------- */
  var KEY = 'mh-theme';
  var root = d.documentElement;
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
  else root.setAttribute('data-theme', 'light'); // milky white by default

  d.querySelectorAll('.theme-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  });

  /* ---------- nav scrolled state + progress bar ---------- */
  var nav = d.querySelector('.nav');
  var bar = d.getElementById('progress');
  var onScroll = function () {
    var y = scrollY;
    if (nav) nav.classList.toggle('scrolled', y > 10);
    if (bar) {
      var max = d.documentElement.scrollHeight - innerHeight;
      bar.style.width = (max > 0 ? (y / max) * 100 : 0) + '%';
    }
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- mobile sheet ---------- */
  var burger = d.querySelector('.burger');
  var sheet = d.getElementById('sheet');
  if (burger && sheet) {
    burger.addEventListener('click', function () {
      var open = sheet.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
      d.documentElement.style.overflow = open ? 'hidden' : '';
    });
    sheet.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        sheet.classList.remove('open');
        burger.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        d.documentElement.style.overflow = '';
      });
    });
  }

  /* ---------- reveal on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  d.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  /* ---------- count-up stats ---------- */
  var easeOut = function (t) { return 1 - Math.pow(1 - t, 3); };
  var fmt = function (el, v) {
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    el.innerHTML = prefix + v + (suffix ? '<b>' + suffix + '</b>' : '');
  };
  var animateCount = function (el) {
    var target = parseFloat(el.getAttribute('data-count') || '0');
    if (reduced) { fmt(el, target); return; }
    var dur = 1500, t0 = null;
    var step = function (ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      fmt(el, Math.round(easeOut(p) * target));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  var cio = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); }
    });
  }, { threshold: 0.4 });
  d.querySelectorAll('[data-count]').forEach(function (el) { cio.observe(el); });

  /* ---------- FAQ: close others when one opens ---------- */
  var faqs = d.querySelectorAll('.faq details');
  faqs.forEach(function (det) {
    det.addEventListener('toggle', function () {
      if (det.open) faqs.forEach(function (o) { if (o !== det) o.open = false; });
    });
  });

  /* ---------- expandable project cards: one open at a time ---------- */
  var pds = d.querySelectorAll('.pdetail');
  pds.forEach(function (det) {
    det.addEventListener('toggle', function () {
      if (det.open) pds.forEach(function (o) { if (o !== det) o.open = false; });
    });
  });

  /* ---------- smooth anchors (offset for floating pill) ---------- */
  d.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var target = d.querySelector(id);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + scrollY - 86;
      scrollTo({ top: top, behavior: reduced ? 'auto' : 'smooth' });
    });
  });
})();
