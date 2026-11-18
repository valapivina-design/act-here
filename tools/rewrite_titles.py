#!/usr/bin/env python3
"""
Rewrite review titles to:
  <Brand> Review - Complaints, Warnings & How to Report | Act Here
Updates og:title and schema headline/name to match. Leaves H1/verdict body as-is.
Idempotent: skips pages already on the target title.
"""
import os, re, json, html as htmlmod, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEWS = os.path.join(ROOT, "reviews")

TITLE_SUFFIX = " | Act Here"

def brand_from_h1(html_text):
    m = re.search(r"<h1>([^<]+?) Review</h1>", html_text)
    if not m:
        return None
    return m.group(1).strip()

def make_title(brand):
    # Title pattern requested: {Brand} Review - Complaints, Warnings & How to Report
    return f"{brand} Review - Complaints, Warnings & How to Report" + TITLE_SUFFIX

def esc(s):
    return htmlmod.escape(s, quote=True)

def rewrite(path):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    brand = brand_from_h1(src)
    if not brand:
        # Fallback: brand from "X Review — Is X a Scam?" H1
        m = re.search(r"<h1>([^<]+?) Review(?:\s*[—\-].*?)?</h1>", src)
        if m:
            brand = m.group(1).strip()
        else:
            return "skip-nobrand"
    new_title = make_title(brand)
    # Keep existing H1/verdict structure; only title/og/schema follow the complaints pattern
    new_h1 = None
    og_title = new_title
    mtitle = re.search(r"<title>([^<]*)</title>", src)
    if mtitle and htmlmod.unescape(mtitle.group(1)) == new_title:
        return "skip-already"

    out = src

    # 1. <title>
    out = re.sub(r"<title>[^<]*</title>", f"<title>{esc(new_title)}</title>", out, count=1)

    # 2. og:title
    out = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{esc(og_title)}">',
        out, count=1,
    )

    # 3. JSON-LD headline / WebPage name (headline fields referencing old title pattern)
    # Replace "headline":"<Brand> Review: Complaints & How to Report" style
    headline_json = json.dumps(og_title, ensure_ascii=False)
    out = re.sub(
        r'"headline":"[^"]*"',
        lambda _: f'"headline":{headline_json}',
        out, count=1,
    )
    # WebPage "name"
    out = re.sub(
        r'("name":")[^"]*(Review[^"]*)(")',
        lambda m: m.group(1) + og_title.replace('"', '\\"') + m.group(3),
        out, count=1,
    )

    # 4. Inject "Do these 4 things today" before FAQ if missing.
    if "do these 4 things today" not in out.lower():
        four_things = f"""
 <h2>If {brand} has your money: do these 4 things today</h2>
 <ul class="checklist">
 <li><strong>Stop sending money.</strong> Do not make any further payments to the platform or to anyone claiming to act on its behalf.</li>
 <li><strong>Screenshot everything.</strong> Dashboard, balances, chats, emails, receipts, wallet addresses, the exact URLs you used. Do it now, while you still have access to the account.</li>
 <li><strong>Call your bank today.</strong> Card payments and bank transfers can sometimes be recalled. The window closes permanently, and it closes fast.</li>
 <li><strong>Then speak to litigation counsel.</strong> Act Here conducts deep-dive discovery and is prepared to litigate where the facts support it. The earlier the evidence is reviewed, the more options remain open. <a href="../pages/contact.html">Book a free consultation</a>.</li>
 </ul>
"""
        # Insert before FAQ heading
        m = re.search(r'(<h2 id="faq">)', out)
        if m:
            out = out[:m.start()] + four_things + out[m.start():]
        else:
            m = re.search(r"<h2>Frequently Asked Questions</h2>", out)
            if m:
                out = out[:m.start()] + four_things + out[m.start():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    return "ok"

def main():
    files = sorted(
        f for f in os.listdir(REVIEWS)
        if f.endswith("-review.html") and f != "index.html"
    )
    ok = skipped = nobrand = 0
    for fname in files:
        r = rewrite(os.path.join(REVIEWS, fname))
        if r == "ok":
            ok += 1
        elif r == "skip-already":
            skipped += 1
        else:
            nobrand += 1
    print(f"rewritten={ok} skipped={skipped} nobrand={nobrand}")

if __name__ == "__main__":
    main()
