/* ============================================================
   Muhammad Hassaan — behaviors
   intro launch · word-by-word reveals · nav scrolled state ·
   active link highlighting · scroll reveals · count-up stats ·
   project expansion · portrait parallax (desktop) · mobile sheet
   ============================================================ */
(function () {
  'use strict';
  var d = document;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.className = 'js-on';

  /* ---------- intro launch (once per session) ---------- */
  var intro = d.getElementById('intro');
  if (intro) {
    var SKIP = 'mh-intro-done';
    var seen = false;
    try { seen = sessionStorage.getItem(SKIP) === '1'; } catch (e) {}

    var finishIntro = function () {
      intro.classList.add('done');
      try { sessionStorage.setItem(SKIP, '1'); } catch (e) {}
      setTimeout(function () { if (intro.parentNode) intro.parentNode.removeChild(intro); }, 900);
    };

    if (seen || reduced) {
      intro.classList.add('skip');
      finishIntro();
    } else {
      var nameEl = d.getElementById('introName');
      var tag = intro.querySelector('.intro-tag');
      var name = (nameEl.textContent || '').trim();
      nameEl.textContent = '';
      name.split('').forEach(function (ch, i) {
        if (ch === ' ') return;
        var s = d.createElement('span');
        s.className = 'L' + (ch === '·' ? ' mid' : '');
        s.innerHTML = ch;
        s.style.animationDelay = (0.35 + i * 0.05) + 's';
        nameEl.appendChild(s);
      });
      var lastDelay = 0.35 + (name.length - 1) * 0.05;
      var tagDelay = lastDelay + 0.5;
      tag.classList.add('show');
      tag.style.animationDelay = tagDelay + 's';
      setTimeout(finishIntro, (tagDelay + 1.3) * 1000);
    }
  }

  /* ---------- nav scrolled state + progress bar ---------- */
  var nav = d.querySelector('.nav');
  var bar = d.getElementById('progress');
  var onScroll = function () {
    var y = scrollY;
    if (nav) nav.classList.toggle('scrolled', y > 10);
    if (bar) {
      var max = d.documentElement.scrollHeight - innerHeight;
      bar.style.width = (max > 0 ? Math.min(100, Math.max(0, (y / max) * 100)) : 0) + '%';
    }
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- active link highlighting ---------- */
  var links = Array.prototype.slice.call(d.querySelectorAll('.nav-links a[href^="#"]'));
  var sections = links
    .map(function (a) { return d.querySelector(a.getAttribute('href')); })
    .filter(Boolean)
    .sort(function (a, b) { // document order, NOT nav order (nav lists Build before Experience)
      return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
    });

  var onScrollActive = function () {
    var y = scrollY + 140;
    var current = sections.length ? sections[0] : null;
    sections.forEach(function (s) {
      var top = s.getBoundingClientRect().top + scrollY; // robust with any offsetParent
      if (top <= y) current = s;
    });
    links.forEach(function (a) {
      a.classList.toggle('active', !!current && a.getAttribute('href') === '#' + current.id);
    });
  };
  if (sections.length) {
    addEventListener('scroll', onScrollActive, { passive: true });
    onScrollActive();
  }

  /* ---------- reveal on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  d.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  /* ---------- word-by-word headline reveal ---------- */
  d.querySelectorAll('[data-words]').forEach(function (el) {
    var nodes = Array.prototype.slice.call(el.childNodes);
    el.textContent = '';
    nodes.forEach(function (node) {
      if (node.nodeType === 3) { // text node → split into word spans
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { el.appendChild(d.createTextNode(' ')); return; }
          var line = d.createElement('span');
          line.className = 'w-line';
          var w = d.createElement('span');
          w.className = 'w-in';
          w.textContent = part;
          line.appendChild(w);
          el.appendChild(line);
        });
      } else if (node.nodeType === 1) { // keep elements (e.g. .hl) intact
        var wrapEl = d.createElement('span');
        wrapEl.className = 'w-line';
        var inner = d.createElement('span');
        inner.className = 'w-in';
        inner.appendChild(node);
        wrapEl.appendChild(inner);
        el.appendChild(wrapEl);
      }
    });
    var words = el.querySelectorAll('.w-in');
    words.forEach(function (w, i) { w.style.transitionDelay = (i * 0.045) + 's'; });
    var wio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          words.forEach(function (w) { w.classList.add('on'); });
          wio.disconnect();
        }
      });
    }, { threshold: 0.3 });
    wio.observe(el);
  });

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

  /* ---------- project expansion ---------- */
  d.querySelectorAll('.project .p-top').forEach(function (top) {
    top.setAttribute('role', 'button');
    top.setAttribute('tabindex', '0');
    top.setAttribute('aria-expanded', 'false');
    var project = top.closest('.project');
    var toggle = top.querySelector('.p-toggle');
    var setOpen = function (open) {
      project.classList.toggle('expanded', open);
      top.setAttribute('aria-expanded', String(open));
      if (toggle) toggle.textContent = open ? '…less' : '…more';
    };
    top.addEventListener('click', function () { setOpen(!project.classList.contains('expanded')); });
    top.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); setOpen(!project.classList.contains('expanded')); }
    });
  });

  /* ---------- portrait parallax (desktop only, fine pointer) ---------- */
  var portraitWrap = d.getElementById('portraitWrap');
  var desktopMQ = matchMedia('(min-width: 901px)');
  if (portraitWrap && !reduced && matchMedia('(pointer:fine)').matches) {
    var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
    var clearTransform = function () {
      portraitWrap.style.transform = '';
      tx = ty = cx = cy = 0;
    };
    var tick = function () {
      if (!desktopMQ.matches) { clearTransform(); raf = null; return; }
      cx += (tx - cx) * 0.06;
      cy += (ty - cy) * 0.06;
      portraitWrap.style.transform = 'translateY(-6%) translate(' + cx.toFixed(2) + 'px,' + cy.toFixed(2) + 'px)';
      if (Math.abs(tx - cx) > 0.1 || Math.abs(ty - cy) > 0.1) {
        raf = requestAnimationFrame(tick);
      } else {
        raf = null;
      }
    };
    addEventListener('mousemove', function (e) {
      if (!desktopMQ.matches) return;
      tx = (e.clientX / innerWidth - 0.5) * 14;
      ty = (e.clientY / innerHeight - 0.5) * 10;
      if (!raf) raf = requestAnimationFrame(tick);
    }, { passive: true });
    desktopMQ.addEventListener ? desktopMQ.addEventListener('change', clearTransform) : desktopMQ.addListener(clearTransform);
  }

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

  /* ---------- smooth anchors (offset for fixed nav) ---------- */
  d.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var target = d.querySelector(id);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + scrollY - 72;
      scrollTo({ top: top, behavior: reduced ? 'auto' : 'smooth' });
    });
  });
})();
