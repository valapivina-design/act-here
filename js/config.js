/* ═══════════════════════════════════════════════════════════════
 ACT-HERE.COM, THIRD-PARTY INTEGRATIONS CONFIG
 ═══════════════════════════════════════════════════════════════

 HOW TO USE THIS FILE:
 1. Fill in your API keys and IDs below
 2. This file is already loaded on every page via layout.js
 3. Never commit real keys to a public git repo
 ─────────────────────────────────────────────────────────────── */

const ACT_HERE_CONFIG = {

 /* ───────────────────────────────────────────────────
 FORMCARRY, Contact Form Submissions
 https://formcarry.com/
 ───────────────────────────────────────────────────
 Steps to activate:
 1. Sign up at formcarry.com
 2. Create a new form → copy the Form ID from the URL
 e.g. https://formcarry.com/f/YOUR_FORM_ID_HERE
 3. Paste your Form ID below
 4. Each <form> on the site will automatically POST to Formcarry
 5. Optional: set up email notifications + spam filter in your Formcarry dashboard
 */
 formcarry: {
 enabled: false, // ← set to true once you add your ID
 formId: "YOUR_FORMCARRY_FORM_ID_HERE", // ← paste your Formcarry form ID here
 endpoint: "https://formcarry.com/s/", // do not change

 // Which forms to connect (matches the id= attribute on each <form>)
 // Leave as-is, all forms with data-formcarry on them will be wired up
 successMessage: "Thank you, a solicitor will contact you within 1 business day.",
 errorMessage: "Something went wrong. Please email us directly at hello@act-here.uk",
 },


 /* ───────────────────────────────────────────────────
 TAWK.TO, Live Chat Widget
 https://tawk.to/
 ───────────────────────────────────────────────────
 Steps to activate:
 1. Sign up at tawk.to (free)
 2. Create a property for act-here.uk
 3. Go to Administration → Chat Widget → Direct Chat Link
 You'll see a snippet like:
 s1.src='https://embed.tawk.to/PROPERTY_ID/WIDGET_ID';
 4. Copy BOTH the Property ID and Widget ID below
 5. Set enabled: true
 */
 tawkto: {
 enabled: false, // ← set to true once you add your IDs
 propertyId: "YOUR_TAWKTO_PROPERTY_ID", // ← e.g. "64abc123def456"
 widgetId: "YOUR_TAWKTO_WIDGET_ID", // ← e.g. "1hxyz7890" (usually "default" or a hash)

 // Pages where chat should be HIDDEN (e.g. blog pages where it's distracting)
 // Use partial path matches
 hideOnPages: [],

 // Custom greeting shown to visitors
 // Configure this in your tawk.to dashboard under Triggers instead
 },


 /* ───────────────────────────────────────────────────
 OPTIONAL: GOOGLE ANALYTICS 4
 https://analytics.google.com/
 ───────────────────────────────────────────────────
 */
 ga4: {
 enabled: false,
 measurementId: "G-XXXXXXXXXX", // ← e.g. "G-ABC123DEF4"
 },


 /* ───────────────────────────────────────────────────
 OPTIONAL: MICROSOFT CLARITY (free heatmaps)
 https://clarity.microsoft.com/
 ───────────────────────────────────────────────────
 */
 clarity: {
 enabled: false,
 projectId: "YOUR_CLARITY_PROJECT_ID", // ← 10-char ID from Clarity dashboard
 },


 /* ───────────────────────────────────────────────────
 OPTIONAL: INDEXNOW (Bing fast indexing)
 https://www.indexnow.org/
 ───────────────────────────────────────────────────
 Steps:
 1. Generate a key at indexnow.org
 2. Upload a text file named <key>.txt to your domain root
 containing just the key on one line
 3. Paste the key below, layout.js will auto-submit
 new pages to Bing on each visit
 */
 indexNow: {
 enabled: false,
 key: "YOUR_INDEXNOW_KEY_HERE", // ← 32-128 char hex key
 host: "act-here.uk",
 },

};


/* ═══════════════════════════════════════════════════════════════
 RUNTIME, DO NOT EDIT BELOW THIS LINE
 (Reads config above and activates each service automatically)
═══════════════════════════════════════════════════════════════ */

(function initIntegrations() {

 /* ── FORMCARRY ── */
 if (ACT_HERE_CONFIG.formcarry.enabled && ACT_HERE_CONFIG.formcarry.formId !== "YOUR_FORMCARRY_FORM_ID_HERE") {
 document.addEventListener("DOMContentLoaded", () => {
 const cfg = ACT_HERE_CONFIG.formcarry;
 const endpoint = cfg.endpoint + cfg.formId;

 document.querySelectorAll("form[data-formcarry], form.contact-form.story-form").forEach(form => {

 // Give the form an action if it doesn't have one
 if (!form.action || form.action === window.location.href) {
 form.setAttribute("action", endpoint);
 form.setAttribute("method", "POST");
 form.setAttribute("enctype", "application/x-www-form-urlencoded");
 }

 form.addEventListener("submit", async function (e) {
 e.preventDefault();

 const submitBtn = form.querySelector("[type=submit], button.btn-primary");
 const originalText = submitBtn ? submitBtn.textContent : "";
 if (submitBtn) {
 submitBtn.textContent = "Sending…";
 submitBtn.disabled = true;
 }

 try {
 const data = new FormData(form);
 // Add page source so you can see where leads came from in Formcarry
 data.append("_source_page", window.location.href);

 const res = await fetch(endpoint, {
 method: "POST",
 body: data,
 headers: { "Accept": "application/json" },
 });

 if (res.ok) {
 showFormFeedback(form, cfg.successMessage, "success");
 form.reset();
 } else {
 showFormFeedback(form, cfg.errorMessage, "error");
 }
 } catch (err) {
 showFormFeedback(form, cfg.errorMessage, "error");
 } finally {
 if (submitBtn) {
 submitBtn.textContent = originalText;
 submitBtn.disabled = false;
 }
 }
 });
 });
 });
 }


 /* ── TAWK.TO ── */
 if (ACT_HERE_CONFIG.tawkto.enabled &&
 ACT_HERE_CONFIG.tawkto.propertyId !== "YOUR_TAWKTO_PROPERTY_ID") {
 const t = ACT_HERE_CONFIG.tawkto;

 // Check if this page should hide the widget
 const currentPath = window.location.pathname;
 const shouldHide = t.hideOnPages.some(p => currentPath.includes(p));

 if (!shouldHide) {
 var Tawk_API = Tawk_API || {};
 var Tawk_LoadStart = new Date();
 (function () {
 var s1 = document.createElement("script");
 var s0 = document.getElementsByTagName("script")[0];
 s1.async = true;
 s1.src = "https://embed.tawk.to/" + t.propertyId + "/" + t.widgetId;
 s1.charset = "UTF-8";
 s1.setAttribute("crossorigin", "*");
 s0.parentNode.insertBefore(s1, s0);
 })();
 }
 }


 /* ── GOOGLE ANALYTICS 4 ── */
 if (ACT_HERE_CONFIG.ga4.enabled &&
 ACT_HERE_CONFIG.ga4.measurementId !== "G-XXXXXXXXXX") {
 const mid = ACT_HERE_CONFIG.ga4.measurementId;
 const s = document.createElement("script");
 s.async = true;
 s.src = "https://www.googletagmanager.com/gtag/js?id=" + mid;
 document.head.appendChild(s);
 window.dataLayer = window.dataLayer || [];
 function gtag() { dataLayer.push(arguments); }
 gtag("js", new Date());
 gtag("config", mid);
 }


 /* ── MICROSOFT CLARITY ── */
 if (ACT_HERE_CONFIG.clarity.enabled &&
 ACT_HERE_CONFIG.clarity.projectId !== "YOUR_CLARITY_PROJECT_ID") {
 (function (c, l, a, r, i, t, y) {
 c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
 t = l.createElement(r); t.async = 1;
 t.src = "https://www.clarity.ms/tag/" + i;
 y = l.getElementsByTagName(r)[0];
 y.parentNode.insertBefore(t, y);
 })(window, document, "clarity", "script", ACT_HERE_CONFIG.clarity.projectId);
 }

})();


/* ── UTILITY: show inline form feedback ── */
function showFormFeedback(form, message, type) {
 // Remove any existing feedback
 const existing = form.parentElement.querySelector(".form-feedback");
 if (existing) existing.remove();

 const div = document.createElement("div");
 div.className = "form-feedback";
 div.textContent = message;
 div.style.cssText = [
 "margin-top: 1rem",
 "padding: 0.75rem 1.1rem",
 "border-radius: 8px",
 "font-size: 0.85rem",
 "font-family: 'Syne', sans-serif",
 type === "success"
 ? "background: rgba(39,174,96,0.08); border: 1px solid rgba(39,174,96,0.22); color: #27ae60;"
 : "background: rgba(192,57,43,0.08); border: 1px solid rgba(192,57,43,0.22); color: #e74c3c;",
 ].join(";");

 form.parentElement.appendChild(div);
 setTimeout(() => div.remove(), 8000);
}
