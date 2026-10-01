/* Shared behaviour: theme toggle, mobile nav, active link, reveal, year */
(function () {
  var root = document.documentElement;

  // Theme
  var saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  if (saved === 'light' || saved === 'dark') root.setAttribute('data-theme', saved);

  function currentTheme() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function paintIcon() {
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    var dark = currentTheme() === 'dark';
    btn.innerHTML = dark
      ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
      : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
    btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('#themeToggle');
    if (!btn) return;
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (err) {}
    paintIcon();
  });

  // Mobile menu
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('#menuBtn');
    var links = document.getElementById('navLinks');
    if (btn && links) {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    } else if (links && links.classList.contains('open') && !e.target.closest('#navLinks')) {
      links.classList.remove('open');
    }
  });

  // Active nav link
  function markActive() {
    var path = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('#navLinks a').forEach(function (a) {
      var href = a.getAttribute('href');
      if (href === path || (path === '' && href === 'index.html')) a.setAttribute('aria-current', 'page');
    });
  }

  // Reveal on scroll
  function reveal() {
    var els = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  document.addEventListener('DOMContentLoaded', function () {
    paintIcon();
    markActive();
    reveal();
    var y = document.getElementById('year');
    if (y) y.textContent = new Date().getFullYear();
  });
})();
