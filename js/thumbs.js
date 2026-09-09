/* Hand-coded SVG diagram thumbnails — injected into [data-thumb] elements.
   Inline SVG so they inherit the page's CSS variables. Static art; motion
   comes from the card hover (scan beam + glow), like omumrania.com. */
(function () {
  'use strict';
  var A = 'var(--accent)', M = 'var(--muted)', F = 'var(--faint)', L = 'var(--line-strong)';
  var MONO = "font-family='ui-monospace,Menlo,Consolas,monospace'";

  var THUMBS = {
    /* Raah.AI — diagnosis funnel: industries → roles → simulation → report */
    funnel: '<svg viewBox="0 0 240 180" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<text x="120" y="18" text-anchor="middle" fill="' + F + '" font-size="8" letter-spacing="2" ' + MONO + '>DIAGNOSE</text>' +
      '<g stroke="' + L + '" stroke-width="1">' +
      '<path d="M40 44 V70 M80 44 V70 M160 44 V70 M200 44 V70"/>' +
      '<path d="M60 92 V110 M180 92 V110"/>' +
      '<path d="M120 132 V150"/></g>' +
      '<g fill="' + A + '" fill-opacity=".12" stroke="' + A + '" stroke-opacity=".5" stroke-width="1">' +
      '<rect x="22" y="30" width="36" height="14" rx="4"/><rect x="62" y="30" width="36" height="14" rx="4"/>' +
      '<rect x="142" y="30" width="36" height="14" rx="4"/><rect x="182" y="30" width="36" height="14" rx="4"/></g>' +
      '<g fill="' + A + '" fill-opacity=".2" stroke="' + A + '" stroke-opacity=".7" stroke-width="1">' +
      '<rect x="42" y="78" width="36" height="14" rx="4"/><rect x="162" y="78" width="36" height="14" rx="4"/></g>' +
      '<rect x="84" y="118" width="72" height="14" rx="4" fill="' + A + '" fill-opacity=".35" stroke="' + A + '" stroke-width="1"/>' +
      '<rect x="70" y="150" width="100" height="16" rx="4" fill="' + A + '" fill-opacity=".55" stroke="' + A + '"/>' +
      '<text x="120" y="161" text-anchor="middle" fill="#0a0a0a" font-size="7.5" font-weight="700" letter-spacing="1.5" ' + MONO + '>REPORT</text>' +
      '<g fill="' + A + '"><circle cx="40" cy="37" r="2"/><circle cx="80" cy="37" r="2"/><circle cx="160" cy="37" r="2"/><circle cx="200" cy="37" r="2"/></g></svg>',

    /* Hustlers' Edge — mentorship flywheel: intention → skill → income loop */
    flywheel: '<svg viewBox="0 0 240 180" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<text x="120" y="18" text-anchor="middle" fill="' + F + '" font-size="8" letter-spacing="2" ' + MONO + '>MENTORSHIP LOOP</text>' +
      '<circle cx="120" cy="102" r="52" stroke="' + L + '" stroke-width="1" stroke-dasharray="3 4"/>' +
      '<circle cx="120" cy="102" r="52" stroke="' + A + '" stroke-opacity=".6" stroke-width="1.4" stroke-dasharray="70 260" stroke-linecap="round"/>' +
      '<g fill="' + A + '" fill-opacity=".14" stroke="' + A + '" stroke-opacity=".6">' +
      '<circle cx="120" cy="50" r="13"/><circle cx="172" cy="102" r="13"/><circle cx="120" cy="154" r="13"/><circle cx="68" cy="102" r="13"/></g>' +
      '<g fill="' + A + '" font-size="7.5" font-weight="600" ' + MONO + '>' +
      '<text x="120" y="53" text-anchor="middle">LEARN</text><text x="172" y="105" text-anchor="middle">BUILD</text>' +
      '<text x="120" y="157" text-anchor="middle">EARN</text><text x="68" y="105" text-anchor="middle">MENTOR</text></g>' +
      '<path d="M164 66 l7 4 -4 7" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path d="M164 138 l7 -4 -4 -7" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path d="M76 138 l-7 -4 4 -7" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path d="M76 66 l-7 4 4 7" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<circle cx="120" cy="102" r="17" fill="#0a0a0a" stroke="' + A + '" stroke-opacity=".5"/>' +
      '<text x="120" y="105" text-anchor="middle" fill="' + A + '" font-size="8" font-weight="700" ' + MONO + '>200+</text></svg>',

    /* NexClip — growth curve: 0 → 13K followers, views spike */
    growth: '<svg viewBox="0 0 240 180" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<text x="120" y="18" text-anchor="middle" fill="' + F + '" font-size="8" letter-spacing="2" ' + MONO + '>AUDIENCE CURVE</text>' +
      '<g stroke="' + L + '" stroke-width="1">' +
      '<line x1="30" y1="150" x2="216" y2="150"/><line x1="30" y1="150" x2="30" y2="34"/>' +
      '<line x1="30" y1="121" x2="216" y2="121" stroke-dasharray="2 5"/>' +
      '<line x1="30" y1="92" x2="216" y2="92" stroke-dasharray="2 5"/>' +
      '<line x1="30" y1="63" x2="216" y2="63" stroke-dasharray="2 5"/></g>' +
      '<path d="M30 148 C70 147 96 144 118 128 C140 112 158 78 178 48 L206 40" stroke="' + A + '" stroke-width="2" stroke-linecap="round"/>' +
      '<path d="M30 148 C70 147 96 144 118 128 C140 112 158 78 178 48 L206 40 L206 150 L30 150 Z" fill="' + A + '" fill-opacity=".07"/>' +
      '<g fill="' + A + '"><circle cx="30" cy="148" r="2.5"/><circle cx="118" cy="128" r="2.5"/><circle cx="178" cy="48" r="2.5"/><circle cx="206" cy="40" r="3.5" stroke="#0a0a0a" stroke-width="1"/></g>' +
      '<text x="208" y="30" text-anchor="end" fill="' + A + '" font-size="9" font-weight="700" ' + MONO + '>13K+</text>' +
      '<text x="34" y="166" fill="' + F + '" font-size="7" ' + MONO + '>M0</text>' +
      '<text x="206" y="166" text-anchor="end" fill="' + F + '" font-size="7" ' + MONO + '>M10 · 19M VIEWS</text></svg>',

    /* E-Cell — org/ecosystem chart: founding president hub */
    network: '<svg viewBox="0 0 240 180" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<text x="120" y="18" text-anchor="middle" fill="' + F + '" font-size="8" letter-spacing="2" ' + MONO + '>ECOSYSTEM MAP</text>' +
      '<g stroke="' + L + '" stroke-width="1">' +
      '<line x1="120" y1="96" x2="52" y2="52"/><line x1="120" y1="96" x2="188" y2="52"/>' +
      '<line x1="120" y1="96" x2="52" y2="140"/><line x1="120" y1="96" x2="188" y2="140"/>' +
      '<line x1="52" y1="52" x2="52" y2="140" stroke-dasharray="2 4"/><line x1="188" y1="52" x2="188" y2="140" stroke-dasharray="2 4"/></g>' +
      '<g fill="' + A + '" fill-opacity=".15" stroke="' + A + '" stroke-opacity=".55">' +
      '<circle cx="52" cy="52" r="11"/><circle cx="188" cy="52" r="11"/><circle cx="52" cy="140" r="11"/><circle cx="188" cy="140" r="11"/></g>' +
      '<circle cx="120" cy="96" r="15" fill="' + A + '" fill-opacity=".85"/>' +
      '<text x="120" y="99" text-anchor="middle" fill="#0a0a0a" font-size="7.5" font-weight="800" ' + MONO + '>E-CELL</text>' +
      '<g fill="' + A + '" font-size="6.5" ' + MONO + '>' +
      '<text x="52" y="32" text-anchor="middle">EVENTS</text><text x="188" y="32" text-anchor="middle">STARTUPS</text>' +
      '<text x="52" y="163" text-anchor="middle">MEMBERS</text><text x="188" y="163" text-anchor="middle">FUNDING</text></g>' +
      '<text x="120" y="128" text-anchor="middle" fill="' + M + '" font-size="7" ' + MONO + '>110+ STUDENTS · ₹6L SEED</text></svg>',

    /* In-page Raah.AI flow diagram (case study figure) */
    raahflow: '<svg viewBox="0 0 640 240" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<g stroke="' + L + '" stroke-width="1"><path d="M118 60 H176 M118 120 H176 M118 180 H176 M238 120 H296 M418 120 H476"/></g>' +
      '<g stroke="' + A + '" stroke-opacity=".55" fill="' + A + '" fill-opacity=".1">' +
      '<rect x="18" y="38" width="100" height="34" rx="8"/><rect x="18" y="103" width="100" height="34" rx="8"/>' +
      '<rect x="18" y="168" width="100" height="34" rx="8"/></g>' +
      '<rect x="176" y="92" width="62" height="56" rx="10" fill="' + A + '" fill-opacity=".25" stroke="' + A + '" stroke-opacity=".8"/>' +
      '<g stroke="' + A + '" stroke-opacity=".6" fill="none">' +
      '<rect x="296" y="38" width="122" height="44" rx="8"/><rect x="296" y="98" width="122" height="44" rx="8"/>' +
      '<rect x="296" y="158" width="122" height="44" rx="8"/></g>' +
      '<rect x="476" y="92" width="146" height="56" rx="10" fill="' + A + '" fill-opacity=".55"/>' +
      '<g fill="' + A + '" font-size="11" font-weight="600" ' + MONO + '>' +
      '<text x="68" y="59" text-anchor="middle">EDUCATION</text><text x="68" y="124" text-anchor="middle">INTERESTS</text>' +
      '<text x="68" y="189" text-anchor="middle">APTITUDE</text>' +
      '<text x="207" y="124" text-anchor="middle">MATCH</text>' +
      '<text x="357" y="64" text-anchor="middle">4 INDUSTRIES</text>' +
      '<text x="357" y="124" text-anchor="middle">4 ROLES</text>' +
      '<text x="357" y="184" text-anchor="middle">SIMULATION</text>' +
      '<text x="549" y="124" text-anchor="middle">REPORT</text></g>' +
      '<path d="M330 84 l8 -8 8 8" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path d="M330 154 l8 -8 8 8" stroke="' + A + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',

    /* In-page HE funnel (case study figure) */
    hefunnel: '<svg viewBox="0 0 640 240" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<g font-size="11" font-weight="600" ' + MONO + '>' +
      '<rect x="70" y="30" width="500" height="40" rx="9" fill="' + A + '" fill-opacity=".1" stroke="' + A + '" stroke-opacity=".45"/>' +
      '<text x="320" y="54" text-anchor="middle" fill="' + A + '">200+ MEMBERS · REFERRAL-LED ACQUISITION</text>' +
      '<rect x="120" y="90" width="400" height="40" rx="9" fill="' + A + '" fill-opacity=".2" stroke="' + A + '" stroke-opacity=".6"/>' +
      '<text x="320" y="114" text-anchor="middle" fill="' + A + '">STRUCTURED MENTORSHIP ECOSYSTEM</text>' +
      '<rect x="170" y="150" width="300" height="40" rx="9" fill="' + A + '" fill-opacity=".35" stroke="' + A + '" stroke-opacity=".75"/>' +
      '<text x="320" y="174" text-anchor="middle" fill="' + A + '">70% MEMBERS × ₹50K+ REVENUE</text>' +
      '<rect x="220" y="200" width="200" height="30" rx="9" fill="' + A + '" fill-opacity=".6"/>' +
      '<text x="320" y="219" text-anchor="middle" fill="#0a0a0a" font-weight="800">₹6L SEED ENABLED</text></g></svg>',

    /* In-page NexClip timeline (case study figure) */
    nextrack: '<svg viewBox="0 0 640 240" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<g stroke="' + L + '" stroke-width="1"><line x1="40" y1="180" x2="600" y2="180"/></g>' +
      '<g fill="' + A + '" fill-opacity=".25" stroke="' + A + '" stroke-opacity=".5">' +
      '<rect x="70" y="150" width="34" height="30" rx="4"/><rect x="120" y="132" width="34" height="48" rx="4"/>' +
      '<rect x="170" y="140" width="34" height="40" rx="4"/><rect x="220" y="104" width="34" height="76" rx="4"/>' +
      '<rect x="270" y="118" width="34" height="62" rx="4"/><rect x="320" y="80" width="34" height="100" rx="4"/>' +
      '<rect x="370" y="56" width="34" height="124" rx="4"/><rect x="420" y="70" width="34" height="110" rx="4"/></g>' +
      '<g fill="' + A + '">' +
      '<rect x="470" y="30" width="34" height="150" rx="4" fill-opacity=".85"/>' +
      '<rect x="520" y="20" width="34" height="160" rx="4" fill-opacity=".85"/></g>' +
      '<g fill="' + F + '" font-size="9" ' + MONO + '>' +
      '<text x="87" y="198" text-anchor="middle">M1</text><text x="187" y="198" text-anchor="middle">M3</text>' +
      '<text x="287" y="198" text-anchor="middle">M5</text><text x="387" y="198" text-anchor="middle">M7</text>' +
      '<text x="487" y="198" text-anchor="middle">M9</text><text x="587" y="198" text-anchor="end">M10</text></g>' +
      '<text x="537" y="14" text-anchor="end" fill="' + A + '" font-size="11" font-weight="700" ' + MONO + '>19M+ VIEWS</text>' +
      '<text x="40" y="14" fill="' + F + '" font-size="9" letter-spacing="2" ' + MONO + '>MONTHLY ORGANIC VIEWS</text></svg>'
  };

  document.querySelectorAll('[data-thumb]').forEach(function (el) {
    var key = el.getAttribute('data-thumb');
    if (THUMBS[key]) el.innerHTML = THUMBS[key];
  });
})();
