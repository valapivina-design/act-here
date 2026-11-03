/* ═══════════════════════════════════════════
 ACT HERE, act-here.uk: Layout Injector
 UK Litigation Counsel
 ═══════════════════════════════════════════ */

const NAV_HTML = `
<nav id="main-nav">
 <a href="index.html" class="nav-logo">Act<span>Here</span></a>
 <ul class="nav-links">
 <li><a href="index.html">Home</a></li>
 <li class="nav-dropdown">
 <button type="button" class="nav-drop-btn" aria-expanded="false" aria-haspopup="true">Firm ▾</button>
 <ul class="nav-drop-menu">
 <li><a href="pages/about.html">About Us</a></li>
 <li><a href="pages/contact.html">Contact</a></li>
 <li><a href="pages/faq.html">FAQ</a></li>
 <li><a href="pages/privacy-policy.html">Privacy Policy</a></li>
 <li><a href="pages/terms-of-service.html">Terms of Service</a></li>
 <li><a href="pages/cookie-policy.html">Cookie Policy</a></li>
 <li><a href="pages/disclaimer.html">Disclaimer</a></li>
 </ul>
 </li>
 <li><a href="pages/investment-fraud.html">Practice Areas</a></li>
 <li><a href="reviews/index.html">Case Reviews</a></li>
 <li><a href="blog/index.html">Insights</a></li>
 <li><a href="pages/contact.html" class="nav-cta">Book Consultation</a></li>
 </ul>
 <div class="nav-hamburger" id="hamburger">
 <span></span><span></span><span></span>
 </div>
</nav>
<div class="mobile-overlay" id="mobile-overlay">
 <button class="mobile-close" id="mobile-close">✕</button>
 <nav class="mobile-nav">
 <a href="index.html">Home</a>
 <a href="pages/about.html">About Us</a>
 <a href="pages/investment-fraud.html">Practice Areas</a>
 <a href="pages/scam-types.html">Matters We Handle</a>
 <a href="reviews/index.html">Case Reviews</a>
 <a href="blog/index.html">Insights</a>
 <a href="pages/faq.html">FAQ</a>
 <a href="pages/privacy-policy.html">Privacy Policy</a>
 <a href="pages/terms-of-service.html">Terms of Service</a>
 <a href="pages/cookie-policy.html">Cookie Policy</a>
 <a href="pages/disclaimer.html">Disclaimer</a>
 <a href="pages/contact.html" class="mobile-cta">Book Consultation</a>
 </nav>
</div>`;

const FOOTER_HTML = `
<footer>
 <div class="footer-grid">
 <div class="footer-brand">
 <a href="index.html" class="nav-logo">Act<span>Here</span></a>
 <p>United Kingdom litigation counsel for commercial, consumer, and complex dispute matters. Clear strategy. Transparent fees. Disciplined advocacy.</p>
 <p class="footer-address">25 Cabot Square<br>London, E14 4QZ</p>
 <div class="footer-badge">UK Litigation · Transparent Fees · Consultation Available</div>
 <div class="footer-social" aria-label="Social links">
 <a href="#" aria-label="LinkedIn">in</a>
 <a href="#" aria-label="Facebook">f</a>
 <a href="#" aria-label="Instagram">ig</a>
 <a href="#" aria-label="YouTube">yt</a>
 </div>
 </div>
 <div class="footer-col">
 <h4>Practice</h4>
 <ul>
 <li><a href="pages/investment-fraud.html">Commercial Litigation</a></li>
 <li><a href="pages/crypto-scams.html">Financial Disputes</a></li>
 <li><a href="pages/romance-scams.html">Consumer Claims</a></li>
 <li><a href="pages/timeshare-exit.html">Contract Exit Counsel</a></li>
 <li><a href="pages/pig-butchering-scam.html">Investment Disputes</a></li>
 <li><a href="reviews/index.html">Case Reviews</a></li>
 </ul>
 </div>
 <div class="footer-col">
 <h4>Resources</h4>
 <ul>
 <li><a href="blog/index.html">Legal Insights</a></li>
 <li><a href="pages/how-to-report-a-scam.html">How to Instruct Us</a></li>
 <li><a href="pages/report-a-scam.html">Start a Matter</a></li>
 <li><a href="pages/faq.html">FAQ</a></li>
 <li><a href="pages/about.html">About Us</a></li>
 <li><a href="pages/contact.html">Contact</a></li>
 </ul>
 </div>
 <div class="footer-col">
 <h4>Legal</h4>
 <ul>
 <li><a href="pages/privacy-policy.html">Privacy Policy</a></li>
 <li><a href="pages/terms-of-service.html">Terms of Service</a></li>
 <li><a href="pages/cookie-policy.html">Cookie Policy</a></li>
 <li><a href="pages/disclaimer.html">Disclaimer</a></li>
 <li><a href="de/index.html">Deutsch</a></li>
 </ul>
 </div>
 </div>
 <div class="footer-bottom">
 <p>© 2025 Act Here · act-here.uk · 25 Cabot Square, London, E14 4QZ · Solicitor advertising. Prior results do not guarantee a similar outcome.</p>
 <p class="footer-legal-links">
 <a href="pages/privacy-policy.html">Privacy Policy</a>
 <span>·</span>
 <a href="pages/terms-of-service.html">Terms of Service</a>
 <span>·</span>
 <a href="pages/cookie-policy.html">Cookie Policy</a>
 <span>·</span>
 <a href="pages/disclaimer.html">Disclaimer</a>
 <span>·</span>
 <a href="mailto:hello@act-here.uk">hello@act-here.uk</a>
 </p>
 </div>
</footer>`;

/* ─── PATH RESOLVER (works from any subfolder depth) ─── */
function resolvePath(href) {
 const depth = (window.location.pathname.match(/\//g) || []).length - 1;
 if (depth <= 0) return href;
 return '../'.repeat(depth) + href;
}

function resolveNav(html) {
 return html.replace(/href="([^"#]+)"/g, (match, p1) => {
 if (p1.startsWith('http') || p1.startsWith('mailto:') || p1.startsWith('#') || p1 === '#') return match;
 return `href="${resolvePath(p1)}"`;
 });
}

document.addEventListener('DOMContentLoaded', () => {
 const navEl = document.getElementById('nav-placeholder');
 const footerEl = document.getElementById('footer-placeholder');
 if (navEl) navEl.outerHTML = resolveNav(NAV_HTML);
 if (footerEl) footerEl.outerHTML = resolveNav(FOOTER_HTML);

 const nav = document.getElementById('main-nav');
 if (nav) {
 const onHero = !!document.querySelector('.law-hero');
 const onScroll = () => {
 const scrolled = window.scrollY > 40;
 nav.classList.toggle('scrolled', scrolled || !onHero);
 };
 window.addEventListener('scroll', onScroll, { passive: true });
 onScroll();
 }

 // Dropdown
 document.querySelectorAll('.nav-dropdown').forEach(drop => {
 const btn = drop.querySelector('.nav-drop-btn');
 btn?.addEventListener('click', (e) => {
 e.stopPropagation();
 const open = drop.classList.toggle('open');
 btn.setAttribute('aria-expanded', open ? 'true' : 'false');
 document.querySelectorAll('.nav-dropdown.open').forEach(other => {
 if (other !== drop) {
 other.classList.remove('open');
 other.querySelector('.nav-drop-btn')?.setAttribute('aria-expanded', 'false');
 }
 });
 });
 });
 document.addEventListener('click', () => {
 document.querySelectorAll('.nav-dropdown.open').forEach(drop => {
 drop.classList.remove('open');
 drop.querySelector('.nav-drop-btn')?.setAttribute('aria-expanded', 'false');
 });
 });

 const hamburger = document.getElementById('hamburger');
 const overlay = document.getElementById('mobile-overlay');
 const closeBtn = document.getElementById('mobile-close');
 if (hamburger && overlay) {
 hamburger.addEventListener('click', () => overlay.classList.add('open'));
 closeBtn?.addEventListener('click', () => overlay.classList.remove('open'));
 overlay.querySelectorAll('a').forEach(a =>
 a.addEventListener('click', () => overlay.classList.remove('open'))
 );
 }

 const reveals = document.querySelectorAll('.reveal');
 if (reveals.length) {
 const io = new IntersectionObserver((entries) => {
 entries.forEach(e => {
 if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
 });
 }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
 reveals.forEach(el => io.observe(el));
 }

 document.querySelectorAll('.faq-question').forEach(q => {
 q.addEventListener('click', () => {
 const item = q.closest('.faq-item');
 const wasOpen = item.classList.contains('open');
 document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
 if (!wasOpen) item.classList.add('open');
 });
 });

 document.querySelectorAll('form[data-fraudshield], form[data-acthere]').forEach(form => {
 form.addEventListener('submit', e => {
 e.preventDefault();
 const btn = form.querySelector('[type=submit]');
 btn.textContent = 'Received, we will respond within 1 business day';
 btn.disabled = true;
 btn.style.opacity = '0.7';
 });
 });
});
