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
        <li><a href="de/krypto-betrug.html">Krypto-Betrug</a></li>
        <li><a href="de/broker-betrug.html">Broker Betrug</a></li>
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

 loadReviewCommentsThenInject();
});

/* Published comments + moderated Formcarry form on review pages. */
function loadReviewCommentsThenInject() {
 const path = window.location.pathname || '';
 if (!/\/reviews\/.+-review\.html$/i.test(path)) return;

 function go() {
  injectPublishedComments();
  injectReviewCommentForm();
 }
 if (window.ACT_HERE_COMMENTS) { go(); return; }
 const existing = document.querySelector('script[data-act-here-comments]');
 if (existing) {
  existing.addEventListener('load', go);
  existing.addEventListener('error', go);
  return;
 }
 const s = document.createElement('script');
 s.src = resolvePath('js/comments.js');
 s.setAttribute('data-act-here-comments', '1');
 s.onload = go;
 s.onerror = go;
 document.head.appendChild(s);
}

function formatCommentDate(iso) {
 try {
  const d = new Date(iso + 'T12:00:00');
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
 } catch (e) { return iso || ''; }
}

function injectPublishedComments() {
 const path = window.location.pathname || '';
 if (!/\/reviews\/.+-review\.html$/i.test(path)) return;
 if (document.getElementById('reviews-grid')) return;

 const file = path.split('/').pop() || '';
 const slug = file.replace(/\.html$/i, '');
 const h1 = document.querySelector('.page-hero h1, h1');
 const company = (h1 ? h1.textContent : slug).replace(/\s*Review\s*$/i, '').trim() || slug;
 const db = window.ACT_HERE_COMMENTS || {};
 const items = db[slug] || [];
 const consultHref = resolvePath('pages/contact.html');

 const block = document.createElement('div');
 block.className = 'reviews-block';
 block.id = 'public-comments';

 let cards = '';
 if (!items.length) {
  cards = '<p class="reviews-empty-soft">No public comments published for this profile yet.</p>';
 } else {
  for (let i = 0; i < items.length; i++) {
   const c = items[i];
   if ((c.name || '').toLowerCase().indexOf('trustpilot') !== -1) continue;
   if ((c.title || '').toLowerCase().indexOf('trustpilot') !== -1) continue;
   const lang = c.lang || 'en';
   cards += '<article class="review-card" lang="' + escapeAttr(lang) + '">' +
    '<div class="review-meta"><time datetime="' + escapeAttr(c.date || '') + '">' + escapeHtml(formatCommentDate(c.date)) + '</time></div>' +
    '<h3 class="review-title">' + escapeHtml(c.title || '') + '</h3>' +
    '<p class="review-body">' + escapeHtml(c.text || '') + '</p>' +
    '<div class="review-author"><div class="avatar">' + escapeHtml(c.initials || '?') + '</div>' +
    '<div class="review-author-text"><strong>' + escapeHtml(c.name || '') + '</strong><span>' + escapeHtml(c.country || '') + '</span></div></div>';
   if (c.support) {
    cards += '<div class="firm-reply" lang="' + escapeAttr(lang) + '">' +
     '<div class="firm-reply-head"><div class="avatar firm">AH</div><div><strong>Act Here</strong><span>Support</span></div></div>' +
     '<p>' + escapeHtml(c.support.text || '') + '</p>' +
     '<a href="' + escapeAttr(consultHref) + '">' + escapeHtml(c.support.ctaLabel || 'Contact us for a consultation →') + '</a></div>';
   }
   cards += '</article>';
  }
 }

 block.innerHTML =
  '<div class="reviews-head">' +
  '<h2>Reviews &amp; What People Are Saying</h2>' +
  '<p class="reviews-lead">Comments from people describing problems with ' + escapeHtml(company) +
  '. Our team may reply when the reported loss appears material and a confidential consultation could help. ' +
  '<a href="#submit-for-review">Submit for review</a> — all new submissions are moderated before publishing.</p>' +
  '</div><div class="reviews-grid" id="reviews-grid">' + cards + '</div>';

 const cta = document.querySelector('section.cta-section');
 const footer = document.querySelector('footer') || document.getElementById('footer-placeholder');
 if (cta) cta.parentNode.insertBefore(block, cta);
 else if (footer) footer.parentNode.insertBefore(block, footer);
 else document.body.appendChild(block);
}

/* Moderated comment form on review pages (Formcarry vb0cjK_9y7T). */
function injectReviewCommentForm() {
 const path = window.location.pathname || '';
 if (!/\/reviews\/.+-review\.html$/i.test(path)) return;
 if (document.getElementById('review-comment-form')) return;

 const file = path.split('/').pop() || '';
 const slug = file.replace(/\.html$/i, '');
 const h1 = document.querySelector('.page-hero h1, h1');
 const company = (h1 ? h1.textContent : slug).replace(/\s*Review\s*$/i, '').trim() || slug;
 const privacyHref = resolvePath('pages/privacy-policy.html');

 const wrap = document.createElement('section');
 wrap.className = 'comment-form-block';
 wrap.id = 'submit-for-review';
 wrap.setAttribute('aria-labelledby', 'comment-form-heading');
 wrap.innerHTML = `
 <h2 id="comment-form-heading">Leave a comment</h2>
 <p class="comment-form-lead">Share your experience with ${escapeHtml(company)}. <strong>All comments are moderated</strong> before anything is published. Email and phone are used only to follow up if needed and are <strong>never published</strong>.</p>
 <form class="comment-form" id="review-comment-form" action="https://formcarry.com/s/vb0cjK_9y7T" method="POST" novalidate>
 <input type="hidden" name="form_type" value="comment">
 <input type="hidden" name="lead_source" value="act-here-review-comment">
 <input type="hidden" name="company" id="comment-company" value="${escapeAttr(company)}">
 <input type="hidden" name="slug" id="comment-slug" value="${escapeAttr(slug)}">
 <input type="hidden" name="page_url" id="comment-page-url" value="">
 <input type="hidden" name="_page" value="comment_${escapeAttr(slug)}">
 <div class="hp" aria-hidden="true">
 <label for="comment-gotcha">Leave blank</label>
 <input type="text" id="comment-gotcha" name="_gotcha" tabindex="-1" autocomplete="off">
 </div>
 <div class="field-row">
 <div class="field">
 <label for="comment-name">Name</label>
 <input type="text" id="comment-name" name="name" required autocomplete="name" placeholder="Your name">
 </div>
 <div class="field">
 <label for="comment-email">Email <span class="hint">(not published)</span></label>
 <input type="email" id="comment-email" name="email" required autocomplete="email" placeholder="you@example.com">
 </div>
 </div>
 <div class="field">
 <label for="comment-phone">Phone <span class="hint">(not published)</span></label>
 <div class="phone-row">
 <select id="comment-country-code" name="country_code" required aria-label="Country code">
 <option value="" selected disabled>Country code</option>
 <option value="+44">+44 UK</option>
 <option value="+1">+1 US/CA</option>
 <option value="+61">+61 AU</option>
 <option value="+353">+353 IE</option>
 <option value="+49">+49 DE</option>
 <option value="+33">+33 FR</option>
 <option value="+31">+31 NL</option>
 <option value="+34">+34 ES</option>
 <option value="+39">+39 IT</option>
 <option value="+48">+48 PL</option>
 <option value="+90">+90 TR</option>
 <option value="+971">+971 AE</option>
 <option value="+65">+65 SG</option>
 <option value="+91">+91 IN</option>
 <option value="+27">+27 ZA</option>
 <option value="+234">+234 NG</option>
 <option value="+64">+64 NZ</option>
 <option value="+46">+46 SE</option>
 <option value="+47">+47 NO</option>
 <option value="+41">+41 CH</option>
 </select>
 <input type="tel" id="comment-phone" name="phone" required autocomplete="tel-national" placeholder="Phone number">
 </div>
 </div>
 <div class="field">
 <label for="comment-subject">Subject</label>
 <input type="text" id="comment-subject" name="subject" required maxlength="160" placeholder="Brief subject line">
 </div>
 <div class="field">
 <label for="comment-body">Comment</label>
 <textarea id="comment-body" name="comment" required maxlength="4000" placeholder="Describe what happened. Include the domain you used if you can."></textarea>
 </div>
 <div class="form-actions">
 <p class="privacy-note">By submitting, you agree we may contact you about this report. We decide which comments go live after review. See our <a href="${privacyHref}">Privacy Policy</a>.</p>
 <button type="submit" class="btn-primary" id="comment-submit">Submit comment</button>
 </div>
 <p class="comment-form-status" id="comment-form-status" role="status" aria-live="polite"></p>
 </form>`;

 const published = document.getElementById('public-comments');
 const cta = document.querySelector('section.cta-section');
 const footer = document.querySelector('footer') || document.getElementById('footer-placeholder');
 if (published && published.nextSibling) published.parentNode.insertBefore(wrap, published.nextSibling);
 else if (published) published.parentNode.appendChild(wrap);
 else if (cta) cta.parentNode.insertBefore(wrap, cta);
 else if (footer) footer.parentNode.insertBefore(wrap, footer);
 else document.body.appendChild(wrap);

 const form = document.getElementById('review-comment-form');
 const urlEl = document.getElementById('comment-page-url');
 if (urlEl) urlEl.value = window.location.href;
 if (!form) return;

 const status = document.getElementById('comment-form-status');
 const btn = document.getElementById('comment-submit');
 const companyEl = document.getElementById('comment-company');
 const slugEl = document.getElementById('comment-slug');
 const companyName = companyEl ? companyEl.value : '';
 const companySlug = slugEl ? slugEl.value : '';

 form.addEventListener('submit', function (e) {
 e.preventDefault();
 if (status) { status.textContent = ''; status.className = 'comment-form-status'; }
 if (!form.checkValidity()) { form.reportValidity(); return; }
 if (btn) btn.disabled = true;
 if (status) status.textContent = 'Sending…';
 fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
 .then(function (res) { return res.json().then(function (data) { return { ok: res.ok, data: data }; }).catch(function () { return { ok: res.ok, data: {} }; }); })
 .then(function (result) {
 const data = result.data || {};
 if (result.ok && (data.code === 200 || data.status === 'success' || !data.code)) {
 if (status) {
 status.className = 'comment-form-status ok';
 status.textContent = 'Thank you. Your comment was received and will be moderated before it appears live.';
 }
 form.reset();
 if (form.elements.form_type) form.elements.form_type.value = 'comment';
 if (form.elements.lead_source) form.elements.lead_source.value = 'act-here-review-comment';
 if (companyEl) companyEl.value = companyName;
 if (slugEl) slugEl.value = companySlug;
 if (urlEl) urlEl.value = window.location.href;
 } else if (status) {
 status.className = 'comment-form-status err';
 status.textContent = (data && data.message) || 'We could not submit that comment. Please try again in a moment.';
 }
 })
 .catch(function () {
 if (status) {
 status.className = 'comment-form-status err';
 status.textContent = 'No response from the form service. Please try again or email hello@act-here.uk.';
 }
 })
 .finally(function () { if (btn) btn.disabled = false; });
 });
}

function escapeHtml(s) {
 return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function escapeAttr(s) {
 return escapeHtml(s).replace(/'/g,'&#39;');
}
