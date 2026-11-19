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
 <li><a href="guides/index.html">Guides</a></li>
 <li><a href="blog/index.html">Insights</a></li>
 <li><a href="pages/contact.html" class="nav-cta">Free Consultation</a></li>
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
 <a href="guides/index.html">Guides</a>
 <a href="blog/index.html">Insights</a>
 <a href="pages/faq.html">FAQ</a>
 <a href="pages/privacy-policy.html">Privacy Policy</a>
 <a href="pages/terms-of-service.html">Terms of Service</a>
 <a href="pages/cookie-policy.html">Cookie Policy</a>
 <a href="pages/disclaimer.html">Disclaimer</a>
 <a href="pages/contact.html" class="mobile-cta">Free Consultation</a>
 </nav>
</div>`;

const FOOTER_HTML = `
<footer>
 <div class="footer-grid">
 <div class="footer-brand">
 <a href="index.html" class="nav-logo">Act<span>Here</span></a>
 <p>United Kingdom litigation counsel for commercial, consumer, and complex dispute matters. Clear strategy. Free consultation. Disciplined advocacy.</p>
 <p class="footer-address">25 Cabot Square<br>London, E14 4QZ</p>
 <div class="footer-badge">UK Litigation · Free Consultation</div>
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
        <li><a href="it/index.html">Italiano</a></li>
        <li><a href="es/index.html">Español</a></li>
        <li><a href="ar/index.html">العربية</a></li>
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

 loadPageCommentsThenInject();
});

/* Comment UI copy by page language (guides + reviews). */
const COMMENT_UI = {
 en: {
  heading: 'Comments & What Readers Are Saying',
  leadReview: 'Comments from people describing problems with {topic}. Our team may reply when the reported loss appears material and a confidential consultation could help. <a href="#submit-for-review">Submit for review</a> - all new submissions are moderated before publishing.',
  leadGuide: 'Comments from readers facing issues like those in this guide. Our team may reply when the reported loss appears material and a confidential consultation could help. <a href="#submit-for-review">Submit for review</a> - all new submissions are moderated before publishing.',
  empty: 'No public comments published for this page yet.',
  formHeading: 'Leave a comment',
  formLeadReview: 'Share your experience with {topic}. <strong>All comments are moderated</strong> before anything is published. Email and phone are used only to follow up if needed and are <strong>never published</strong>.',
  formLeadGuide: 'Share your experience related to this guide. <strong>All comments are moderated</strong> before anything is published. Email and phone are used only to follow up if needed and are <strong>never published</strong>. Do not name brokers here if you prefer privacy - you can share details in the free consultation.',
  name: 'Name',
  email: 'Email',
  phone: 'Phone',
  notPublished: '(not published)',
  subject: 'Subject',
  comment: 'Comment',
  namePh: 'Your name',
  emailPh: 'you@example.com',
  phonePh: 'Phone number',
  subjectPh: 'Brief subject line',
  bodyPh: 'Describe what happened. Include dates and how you paid if you can.',
  countryCode: 'Country code',
  privacy: 'By submitting, you agree we may contact you about this report. We decide which comments go live after review. See our <a href="{privacy}">Privacy Policy</a>.',
  submit: 'Submit comment',
  sending: 'Sending…',
  thanks: 'Thank you. Your comment was received and will be moderated before it appears live.',
  errSubmit: 'We could not submit that comment. Please try again in a moment.',
  errNetwork: 'No response from the form service. Please try again or email hello@act-here.uk.',
  supportRole: 'Support',
  ctaFallback: 'Book a free consultation →',
  gotcha: 'Leave blank'
 },
 de: {
  heading: 'Kommentare & Stimmen von Betroffenen',
  leadReview: 'Kommentare zu Problemen mit {topic}. Unser Team antwortet, wenn der gemeldete Schaden erheblich wirkt und eine vertrauliche Beratung helfen kann. <a href="#submit-for-review">Zur Prufung einreichen</a> - neue Beitrage werden vor der Veroffentlichung moderiert.',
  leadGuide: 'Kommentare von Lesern mit ahnlichen Situationen wie in diesem Ratgeber. Unser Team antwortet bei erheblichem Schaden und wenn eine vertrauliche Beratung helfen kann. <a href="#submit-for-review">Zur Prufung einreichen</a> - neue Beitrage werden vor der Veroffentlichung moderiert.',
  empty: 'Noch keine offentlichen Kommentare zu dieser Seite.',
  formHeading: 'Kommentar hinterlassen',
  formLeadReview: 'Schildern Sie Ihre Erfahrung mit {topic}. <strong>Alle Kommentare werden moderiert</strong>, bevor etwas erscheint. E-Mail und Telefon dienen nur der Ruckfrage und werden <strong>nicht veroeffentlicht</strong>.',
  formLeadGuide: 'Schildern Sie Ihre Erfahrung zu diesem Thema. <strong>Alle Kommentare werden moderiert</strong>. E-Mail und Telefon dienen nur der Ruckfrage und werden <strong>nicht veroeffentlicht</strong>. Broker-Namen konnen Sie in der kostenlosen Beratung nennen.',
  name: 'Name',
  email: 'E-Mail',
  phone: 'Telefon',
  notPublished: '(nicht oeffentlich)',
  subject: 'Betreff',
  comment: 'Kommentar',
  namePh: 'Ihr Name',
  emailPh: 'sie@beispiel.de',
  phonePh: 'Telefonnummer',
  subjectPh: 'Kurzer Betreff',
  bodyPh: 'Beschreiben Sie, was passiert ist. Daten und Zahlungsweg helfen.',
  countryCode: 'Landesvorwahl',
  privacy: 'Mit dem Absenden stimmen Sie zu, dass wir Sie zu diesem Bericht kontaktieren konnen. Wir entscheiden, welche Kommentare freigeschaltet werden. Siehe <a href="{privacy}">Datenschutz</a>.',
  submit: 'Kommentar senden',
  sending: 'Wird gesendet…',
  thanks: 'Danke. Ihr Kommentar ist eingegangen und wird vor der Freischaltung gepruft.',
  errSubmit: 'Kommentar konnte nicht gesendet werden. Bitte versuchen Sie es erneut.',
  errNetwork: 'Keine Antwort vom Formular-Dienst. Bitte erneut versuchen oder hello@act-here.uk schreiben.',
  supportRole: 'Support',
  ctaFallback: 'Kostenlose Beratung buchen →',
  gotcha: 'Leer lassen'
 },
 es: {
  heading: 'Comentarios y lo que dicen los lectores',
  leadReview: 'Comentarios sobre problemas con {topic}. Nuestro equipo puede responder cuando la perdida parece material y una consulta confidencial puede ayudar. <a href="#submit-for-review">Enviar para revision</a> - las nuevas entradas se moderan antes de publicarse.',
  leadGuide: 'Comentarios de lectores con situaciones como las de esta guia. Nuestro equipo puede responder cuando la perdida parece material y una consulta confidencial puede ayudar. <a href="#submit-for-review">Enviar para revision</a> - las nuevas entradas se moderan antes de publicarse.',
  empty: 'Aun no hay comentarios publicos en esta pagina.',
  formHeading: 'Deje un comentario',
  formLeadReview: 'Comparta su experiencia con {topic}. <strong>Todos los comentarios se moderan</strong> antes de publicarse. Email y telefono solo para seguimiento y <strong>nunca se publican</strong>.',
  formLeadGuide: 'Comparta su experiencia sobre este tema. <strong>Todos los comentarios se moderan</strong>. Email y telefono solo para seguimiento y <strong>nunca se publican</strong>. Puede dar el nombre del broker en la consulta gratuita.',
  name: 'Nombre',
  email: 'Email',
  phone: 'Telefono',
  notPublished: '(no se publica)',
  subject: 'Asunto',
  comment: 'Comentario',
  namePh: 'Su nombre',
  emailPh: 'usted@ejemplo.com',
  phonePh: 'Numero de telefono',
  subjectPh: 'Asunto breve',
  bodyPh: 'Describa lo ocurrido. Fechas y forma de pago ayudan.',
  countryCode: 'Codigo de pais',
  privacy: 'Al enviar, acepta que podamos contactarle sobre este informe. Decidimos que comentarios se publican. Vea nuestra <a href="{privacy}">Politica de privacidad</a>.',
  submit: 'Enviar comentario',
  sending: 'Enviando…',
  thanks: 'Gracias. Su comentario se recibio y se moderara antes de publicarse.',
  errSubmit: 'No pudimos enviar el comentario. Intentelo de nuevo en un momento.',
  errNetwork: 'Sin respuesta del servicio del formulario. Intentelo de nuevo o escriba a hello@act-here.uk.',
  supportRole: 'Soporte',
  ctaFallback: 'Reserve una consulta gratuita →',
  gotcha: 'Dejar en blanco'
 },
 it: {
  heading: 'Commenti e voci dei lettori',
  leadReview: 'Commenti su problemi con {topic}. Il team puo rispondere quando la perdita appare rilevante e una consulenza riservata puo aiutare. <a href="#submit-for-review">Invia per revisione</a> - i nuovi contributi sono moderati prima della pubblicazione.',
  leadGuide: 'Commenti di lettori con situazioni simili a questa guida. Il team puo rispondere quando la perdita appare rilevante e una consulenza riservata puo aiutare. <a href="#submit-for-review">Invia per revisione</a> - i nuovi contributi sono moderati prima della pubblicazione.',
  empty: 'Ancora nessun commento pubblico su questa pagina.',
  formHeading: 'Lascia un commento',
  formLeadReview: 'Condivida la sua esperienza con {topic}. <strong>Tutti i commenti sono moderati</strong> prima della pubblicazione. Email e telefono servono solo per il follow-up e <strong>non vengono pubblicati</strong>.',
  formLeadGuide: 'Condivida la sua esperienza su questo tema. <strong>Tutti i commenti sono moderati</strong>. Email e telefono solo per follow-up e <strong>non pubblicati</strong>. Puo indicare il broker nella consulenza gratuita.',
  name: 'Nome',
  email: 'Email',
  phone: 'Telefono',
  notPublished: '(non pubblicato)',
  subject: 'Oggetto',
  comment: 'Commento',
  namePh: 'Il suo nome',
  emailPh: 'lei@esempio.it',
  phonePh: 'Numero di telefono',
  subjectPh: 'Oggetto breve',
  bodyPh: 'Descriva cosa e successo. Date e metodo di pagamento aiutano.',
  countryCode: 'Prefisso paese',
  privacy: 'Inviando, accetta che possiamo contattarla su questa segnalazione. Decidiamo quali commenti pubblicare. Veda la <a href="{privacy}">Privacy Policy</a>.',
  submit: 'Invia commento',
  sending: 'Invio…',
  thanks: 'Grazie. Il commento e stato ricevuto e sara moderato prima di andare online.',
  errSubmit: 'Non siamo riusciti a inviare il commento. Riprovi tra poco.',
  errNetwork: 'Nessuna risposta dal servizio form. Riprovi o scriva a hello@act-here.uk.',
  supportRole: 'Supporto',
  ctaFallback: 'Prenota una consulenza gratuita →',
  gotcha: 'Lasciare vuoto'
 },
 ar: {
  heading: 'التعليقات وآراء القراء',
  leadReview: 'تعليقات حول مشكلات متعلقة بـ {topic}. قد يرد فريقنا عندما يبدو الضرر جوهريا ويمكن أن تفيد استشارة سرية. <a href="#submit-for-review">أرسل للمراجعة</a> - تخضع التعليقات الجديدة للإشراف قبل النشر.',
  leadGuide: 'تعليقات من قراء يواجهون مواقف مشابهة لهذا الدليل. قد يرد فريقنا عندما يبدو الضرر جوهريا ويمكن أن تفيد استشارة سرية. <a href="#submit-for-review">أرسل للمراجعة</a> - تخضع التعليقات الجديدة للإشراف قبل النشر.',
  empty: 'لا توجد تعليقات عامة على هذه الصفحة بعد.',
  formHeading: 'اترك تعليقا',
  formLeadReview: 'شارك تجربتك مع {topic}. <strong>جميع التعليقات تخضع للإشراف</strong> قبل النشر. البريد والهاتف للمتابعة فقط و<strong>لا يُنشران</strong>.',
  formLeadGuide: 'شارك تجربتك حول هذا الموضوع. <strong>جميع التعليقات تخضع للإشراف</strong>. البريد والهاتف للمتابعة فقط و<strong>لا يُنشران</strong>. يمكنك ذكر اسم الوسيط في الاستشارة المجانية.',
  name: 'الاسم',
  email: 'البريد الإلكتروني',
  phone: 'الهاتف',
  notPublished: '(لا يُنشر)',
  subject: 'الموضوع',
  comment: 'التعليق',
  namePh: 'اسمك',
  emailPh: 'you@example.com',
  phonePh: 'رقم الهاتف',
  subjectPh: 'موضوع مختصر',
  bodyPh: 'صف ما حدث. التواريخ وطريقة الدفع تساعد.',
  countryCode: 'رمز الدولة',
  privacy: 'بإرسال النموذج توافق على أن نتواصل معك بشأن هذا البلاغ. نقرر أي التعليقات تُنشر. راجع <a href="{privacy}">سياسة الخصوصية</a>.',
  submit: 'إرسال التعليق',
  sending: 'جاري الإرسال…',
  thanks: 'شكرا. استلمنا تعليقك وسيُراجع قبل النشر.',
  errSubmit: 'تعذر إرسال التعليق. حاول مرة أخرى بعد قليل.',
  errNetwork: 'لا رد من خدمة النموذج. حاول مرة أخرى أو راسل hello@act-here.uk.',
  supportRole: 'الدعم',
  ctaFallback: 'احجز استشارة مجانية →',
  gotcha: 'اتركه فارغا'
 }
};

function getCommentPageContext() {
 const path = window.location.pathname || '';
 const file = (path.split('/').pop() || '').replace(/\.html$/i, '');
 if (/\/reviews\/.+-review\.html$/i.test(path)) {
  const h1 = document.querySelector('.page-hero h1, h1');
  const topic = (h1 ? h1.textContent : file).replace(/\s*Review\s*$/i, '').trim() || file;
  return { kind: 'review', slug: file, dbKey: file, lang: 'en', topic: topic, leadSource: 'act-here-review-comment' };
 }
 // Guide pages: /guides/*.html, /de|it|es|ar/*.html (exclude index)
 const m = path.match(/\/(guides|de|it|es|ar)\/([^/]+)\.html$/i);
 if (!m) return null;
 const folder = m[1].toLowerCase();
 const stem = m[2];
 if (/^index$/i.test(stem)) return null;
 const lang = folder === 'guides' ? 'en' : folder;
 const h1 = document.querySelector('.page-hero h1, h1');
 const topic = (h1 ? h1.textContent : stem).trim() || stem;
 return {
  kind: 'guide',
  slug: stem,
  dbKey: folder + '/' + stem,
  lang: lang,
  topic: topic,
  leadSource: 'act-here-guide-comment'
 };
}

function loadPageCommentsThenInject() {
 const ctx = getCommentPageContext();
 if (!ctx) return;

 function go() {
  injectPublishedComments(ctx);
  injectPageCommentForm(ctx);
 }

 if (ctx.kind === 'review') {
  if (window.ACT_HERE_COMMENTS) { go(); return; }
  loadCommentScript('js/comments.js', 'data-act-here-comments', go);
  return;
 }
 if (window.ACT_HERE_GUIDE_COMMENTS) { go(); return; }
 loadCommentScript('js/guide_comments.js', 'data-act-here-guide-comments', go);
}

function loadCommentScript(src, attr, go) {
 const existing = document.querySelector('script[' + attr + ']');
 if (existing) {
  existing.addEventListener('load', go);
  existing.addEventListener('error', go);
  return;
 }
 const s = document.createElement('script');
 s.src = resolvePath(src);
 s.setAttribute(attr, '1');
 s.onload = go;
 s.onerror = go;
 document.head.appendChild(s);
}

function formatCommentDate(iso, lang) {
 try {
  const d = new Date(iso + 'T12:00:00');
  const loc = lang === 'de' ? 'de-DE' : lang === 'es' ? 'es-ES' : lang === 'it' ? 'it-IT' : lang === 'ar' ? 'ar' : 'en-GB';
  return d.toLocaleDateString(loc, { day: 'numeric', month: 'short', year: 'numeric' });
 } catch (e) { return iso || ''; }
}

function injectPublishedComments(ctx) {
 if (!ctx) ctx = getCommentPageContext();
 if (!ctx) return;
 if (document.getElementById('reviews-grid')) return;

 const ui = COMMENT_UI[ctx.lang] || COMMENT_UI.en;
 const db = ctx.kind === 'guide'
  ? (window.ACT_HERE_GUIDE_COMMENTS || {})
  : (window.ACT_HERE_COMMENTS || {});
 const items = db[ctx.dbKey] || [];
 const consultHref = resolvePath('pages/contact.html');

 const block = document.createElement('div');
 block.className = 'reviews-block';
 block.id = 'public-comments';

 let cards = '';
 if (!items.length) {
  cards = '<p class="reviews-empty-soft">' + escapeHtml(ui.empty) + '</p>';
 } else {
  for (let i = 0; i < items.length; i++) {
   const c = items[i];
   if ((c.name || '').toLowerCase().indexOf('trustpilot') !== -1) continue;
   if ((c.title || '').toLowerCase().indexOf('trustpilot') !== -1) continue;
   const lang = c.lang || ctx.lang || 'en';
   cards += '<article class="review-card" lang="' + escapeAttr(lang) + '">' +
    '<div class="review-meta"><time datetime="' + escapeAttr(c.date || '') + '">' + escapeHtml(formatCommentDate(c.date, ctx.lang)) + '</time></div>' +
    '<h3 class="review-title">' + escapeHtml(c.title || '') + '</h3>' +
    '<p class="review-body">' + escapeHtml(c.text || '') + '</p>' +
    '<div class="review-author"><div class="avatar">' + escapeHtml(c.initials || '?') + '</div>' +
    '<div class="review-author-text"><strong>' + escapeHtml(c.name || '') + '</strong><span>' + escapeHtml(c.country || '') + '</span></div></div>';
   if (c.support) {
    const cta = c.support.ctaLabel || ui.ctaFallback;
    cards += '<div class="firm-reply" lang="' + escapeAttr(lang) + '">' +
     '<div class="firm-reply-head"><div class="avatar firm">AH</div><div><strong>Act Here</strong><span>' + escapeHtml(ui.supportRole) + '</span></div></div>' +
     '<p>' + escapeHtml(c.support.text || '') + '</p>' +
     '<a href="' + escapeAttr(consultHref) + '">' + escapeHtml(cta) + '</a></div>';
   }
   cards += '</article>';
  }
 }

 const leadTpl = ctx.kind === 'guide' ? ui.leadGuide : ui.leadReview;
 const lead = leadTpl.replace(/\{topic\}/g, escapeHtml(ctx.topic));

 block.innerHTML =
  '<div class="reviews-head">' +
  '<h2>' + escapeHtml(ui.heading) + '</h2>' +
  '<p class="reviews-lead">' + lead + '</p>' +
  '</div><div class="reviews-grid" id="reviews-grid">' + cards + '</div>';

 const cta = document.querySelector('section.cta-section');
 const footer = document.querySelector('footer') || document.getElementById('footer-placeholder');
 // Guide pages often put the navy CTA before the footer without .cta-section
 const navyCta = document.querySelector('section[style*="background:var(--navy)"]');
 const insertBefore = cta || navyCta || footer;
 if (insertBefore && insertBefore.parentNode) insertBefore.parentNode.insertBefore(block, insertBefore);
 else document.body.appendChild(block);
}

/* Moderated comment form (Formcarry vb0cjK_9y7T) on review + guide pages. */
function injectPageCommentForm(ctx) {
 if (!ctx) ctx = getCommentPageContext();
 if (!ctx) return;
 if (document.getElementById('review-comment-form')) return;

 const ui = COMMENT_UI[ctx.lang] || COMMENT_UI.en;
 const privacyHref = resolvePath('pages/privacy-policy.html');
 const formLeadTpl = ctx.kind === 'guide' ? ui.formLeadGuide : ui.formLeadReview;
 const formLead = formLeadTpl.replace(/\{topic\}/g, escapeHtml(ctx.topic));
 const privacy = ui.privacy.replace(/\{privacy\}/g, escapeAttr(privacyHref));

 const wrap = document.createElement('section');
 wrap.className = 'comment-form-block';
 wrap.id = 'submit-for-review';
 wrap.setAttribute('aria-labelledby', 'comment-form-heading');
 wrap.innerHTML = `
 <h2 id="comment-form-heading">${escapeHtml(ui.formHeading)}</h2>
 <p class="comment-form-lead">${formLead}</p>
 <form class="comment-form" id="review-comment-form" action="https://formcarry.com/s/vb0cjK_9y7T" method="POST" novalidate>
 <input type="hidden" name="form_type" value="comment">
 <input type="hidden" name="lead_source" value="${escapeAttr(ctx.leadSource)}">
 <input type="hidden" name="company" id="comment-company" value="${escapeAttr(ctx.topic)}">
 <input type="hidden" name="slug" id="comment-slug" value="${escapeAttr(ctx.dbKey)}">
 <input type="hidden" name="page_url" id="comment-page-url" value="">
 <input type="hidden" name="_page" value="comment_${escapeAttr(ctx.dbKey)}">
 <div class="hp" aria-hidden="true">
 <label for="comment-gotcha">${escapeHtml(ui.gotcha)}</label>
 <input type="text" id="comment-gotcha" name="_gotcha" tabindex="-1" autocomplete="off">
 </div>
 <div class="field-row">
 <div class="field">
 <label for="comment-name">${escapeHtml(ui.name)}</label>
 <input type="text" id="comment-name" name="name" required autocomplete="name" placeholder="${escapeAttr(ui.namePh)}">
 </div>
 <div class="field">
 <label for="comment-email">${escapeHtml(ui.email)} <span class="hint">${escapeHtml(ui.notPublished)}</span></label>
 <input type="email" id="comment-email" name="email" required autocomplete="email" placeholder="${escapeAttr(ui.emailPh)}">
 </div>
 </div>
 <div class="field">
 <label for="comment-phone">${escapeHtml(ui.phone)} <span class="hint">${escapeHtml(ui.notPublished)}</span></label>
 <div class="phone-row">
 <select id="comment-country-code" name="country_code" required aria-label="${escapeAttr(ui.countryCode)}">
 <option value="" selected disabled>${escapeHtml(ui.countryCode)}</option>
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
 <input type="tel" id="comment-phone" name="phone" required autocomplete="tel-national" placeholder="${escapeAttr(ui.phonePh)}">
 </div>
 </div>
 <div class="field">
 <label for="comment-subject">${escapeHtml(ui.subject)}</label>
 <input type="text" id="comment-subject" name="subject" required maxlength="160" placeholder="${escapeAttr(ui.subjectPh)}">
 </div>
 <div class="field">
 <label for="comment-body">${escapeHtml(ui.comment)}</label>
 <textarea id="comment-body" name="comment" required maxlength="4000" placeholder="${escapeAttr(ui.bodyPh)}"></textarea>
 </div>
 <div class="form-actions">
 <p class="privacy-note">${privacy}</p>
 <button type="submit" class="btn-primary" id="comment-submit">${escapeHtml(ui.submit)}</button>
 </div>
 <p class="comment-form-status" id="comment-form-status" role="status" aria-live="polite"></p>
 </form>`;

 const published = document.getElementById('public-comments');
 const cta = document.querySelector('section.cta-section');
 const navyCta = document.querySelector('section[style*="background:var(--navy)"]');
 const footer = document.querySelector('footer') || document.getElementById('footer-placeholder');
 if (published && published.nextSibling) published.parentNode.insertBefore(wrap, published.nextSibling);
 else if (published) published.parentNode.appendChild(wrap);
 else if (cta) cta.parentNode.insertBefore(wrap, cta);
 else if (navyCta) navyCta.parentNode.insertBefore(wrap, navyCta);
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
 const leadSource = ctx.leadSource;

 form.addEventListener('submit', function (e) {
 e.preventDefault();
 if (status) { status.textContent = ''; status.className = 'comment-form-status'; }
 if (!form.checkValidity()) { form.reportValidity(); return; }
 if (btn) btn.disabled = true;
 if (status) status.textContent = ui.sending;
 fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
 .then(function (res) { return res.json().then(function (data) { return { ok: res.ok, data: data }; }).catch(function () { return { ok: res.ok, data: {} }; }); })
 .then(function (result) {
 const data = result.data || {};
 if (result.ok && (data.code === 200 || data.status === 'success' || !data.code)) {
 if (status) {
 status.className = 'comment-form-status ok';
 status.textContent = ui.thanks;
 }
 form.reset();
 if (form.elements.form_type) form.elements.form_type.value = 'comment';
 if (form.elements.lead_source) form.elements.lead_source.value = leadSource;
 if (companyEl) companyEl.value = companyName;
 if (slugEl) slugEl.value = companySlug;
 if (urlEl) urlEl.value = window.location.href;
 } else if (status) {
 status.className = 'comment-form-status err';
 status.textContent = (data && data.message) || ui.errSubmit;
 }
 })
 .catch(function () {
 if (status) {
 status.className = 'comment-form-status err';
 status.textContent = ui.errNetwork;
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
