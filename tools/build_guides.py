#!/usr/bin/env python3
"""Build victim-intent guides under /guides/."""
import os, json, html as htmlmod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES = os.path.join(ROOT, "guides")
os.makedirs(GUIDES, exist_ok=True)

SITE = "Act Here"
BASE = "https://act-here.uk/guides/"

# Each guide: slug, title (SERP), meta_description, hero_kicker, hero_h1, hero_lead, sections [(kicker, h2, [paragraphs or list of (html,)])], faqs [(q, a)], related_reviews [(slug, anchor)]
GUIDES_DATA = [
    {
        "slug": "prop-trading-scam",
        "title": "Prop Trading Scam: How Fake Prop Firms Steal Challenge Fees | Act Here",
        "description": "Failed your prop firm challenge right before payout? Rules changed after you passed? How prop trading scams work — and what UK litigation can do about it.",
        "keywords": "prop trading scam, prop firm scam, prop firm payout denied, challenge fee scam, funded account denied, prop trading fraud",
        "kicker": "Prop firm fraud · Updated November 2026",
        "h1": "Prop Trading Scam: How Fake Prop Firms Steal Challenge Fees",
        "lead": "You paid $99 for a 100k challenge. Passed phase one. Phase two failed at 9.7% profit with one day left — or the firm reset your account, denied your payout, or simply vanished. Prop trading scams are the fastest-growing fraud category we see at Act Here, and the playbook is nearly identical across firms.",
        "sections": [
            ("Red flags", "How a prop firm scam actually works", [
                ("p", "Legitimate prop firms make money when traders pass and trade profitably. Scam prop firms make money when traders fail — so the entire business model is to sell you a challenge, then engineer your failure."),
                ("ul", [
                    "The 'consistency rule' that appears only after you request a payout — a rule that wasn't in the terms you signed.",
                    "A 'news trading' violation announced at payout time for trades placed days earlier, when no news calendar was ever provided.",
                    "IP-address / VPN excuses: 'you traded from two locations' used to void a passed challenge, even though the trader travelled.",
                    "Slippage and spread spikes during the final hours of a challenge phase, pushing you over the daily drawdown limit.",
                    "The firm disappears after collecting thousands of challenge fees — domain goes dark, support stops responding, Discord deleted.",
                ]),
            ]),
            ("Behind the scenes", "Why 'prop trading scam' searches spike every month", [
                ("p", "The prop firm industry exploded after 2022. A small number of real firms built multi-year track records and published payout proof. But hundreds of clones launched with the same website template, the same 'challenge' mechanics, and no underlying brokerage. When the operator has no live capital at risk, your challenge fee is pure revenue."),
                ("p", "The giveaway: a real prop firm profits from your success; a scam prop firm profits from your failure. If the firm's terms give it unlimited discretion to fail you — 'we may void any account at our sole discretion' — that's the entire business model in one clause."),
            ]),
            ("Your options", "Failed challenge or denied payout: the three routes that still work", [
                ("h3", "Card chargeback on the challenge fee"),
                ("p", "Most prop firm fees are paid by card. If the firm changed its rules after you paid, refused a documented payout, or went dark, you may have a chargeback claim under 'services not as described'. The window is typically 120 days from the charge — file it now, not next month."),
                ("h3", "Civil claim for breach of contract"),
                ("p", "The 'challenge' is a contract: you paid a fee, the firm promised a funded account on specific terms. If it denied your payout while you met every written rule, that is breach. UK small-claims and county-court routes are usable for amounts under £10,000; larger claims need litigation counsel."),
                ("h3", "Regulatory complaint + class action"),
                ("p", "Most prop firms are unregulated, but the FCA has begun treating some as collective investment schemes. A coordinated complaint with dozens of victims creates the paper trail that forces payment processors to cut the firm off. Act Here coordinates multi-victim litigation where the facts support it."),
            ]),
            ("Sort your situation", "Legit prop firm or scam: how to tell them apart", [
                ("ul", [
                    "A real firm publishes its payout history and processes payouts on a fixed schedule. A scam firm invents a new reason every time.",
                    "A real firm's rules don't change after you sign. A scam firm adds 'consistency' or 'news trading' rules retroactively.",
                    "A real firm has a multi-year track record on Trustpilot with verified payouts. A scam firm has hundreds of 'paid for challenge, never got funded' reviews.",
                    "A real firm answers tickets in order. A scam firm's 'account manager' calls you the moment you request a payout — to talk you out of it.",
                ]),
            ]),
        ],
        "faqs": [
            ("Is prop trading a scam?", "No — real prop firms exist and pay out, and a small number of established firms have multi-year payout records. But the industry is saturated with clones that sell challenges with no intention of funding anyone. The test: does the firm publish verifiable payout proof, and does its rulebook stay fixed after you sign?"),
            ("My prop firm denied my payout after I passed. Is that legal?", "Usually not. The 'challenge' is a contract: you paid a fee, the firm promised a funded account on specific written terms. If you met every written rule and the firm still denied payout, that is breach of contract. Retroactive 'consistency' or 'news trading' rules added after the fact are very hard for the firm to defend in court."),
            ("Can I get my challenge fee back?", "Sometimes. Card chargebacks work when the firm changed its terms after you paid or refused a documented payout — file within 120 days. For larger losses (multiple challenges, denied funded-account payouts), civil litigation or a coordinated multi-victim claim is usually the realistic route."),
            ("How do I report a prop trading scam?", "Contact your bank or card issuer immediately and file a chargeback if applicable. Report to Action Fraud (UK), the FTC (US), and your national regulator. Preserve every screenshot, email, Discord message, and the exact terms you signed. For material losses, book a free consultation with UK litigation counsel."),
        ],
        "related": [],
    },
    {
        "slug": "broker-withdrawal-problem",
        "title": "Broker Withdrawal Problem? Why Your Payout Is Stalled — and How to Unblock It | Act Here",
        "description": "You clicked 'withdraw' and the status flipped to 'pending' — for weeks. Why brokers stall payouts, how to tell slow from scam, and what still works.",
        "keywords": "broker withdrawal problem, broker not paying out, withdrawal pending broker, cannot withdraw from broker, broker payout stalled",
        "kicker": "Withdrawal problems · Updated November 2026",
        "h1": "Broker Withdrawal Problem? Why Your Payout Is Stalled — and How to Unblock It",
        "lead": "You click 'withdraw', the status flips to 'pending' — and nothing happens for days. Then weeks. Then support stops answering. A broker withdrawal problem is the single most common first symptom of investment fraud, and the way you respond in the next 14 days often decides whether the money comes back.",
        "sections": [
            ("Red flags", "How a broker holds your funds hostage", [
                ("ul", [
                    "The bonus trap: a 'welcome bonus' was added without you asking — and the broker now claims it voids your right to withdraw your own deposit.",
                    "New conditions that appear only when you ask to withdraw, and that were never in the terms you accepted when you deposited.",
                    "A fake app or web trader that shows profits on screen but routes nothing to any real market — the balance is a number the operator can edit.",
                    "Endless verification loops: documents accepted yesterday are 'insufficient' today, and each resubmission restarts the clock.",
                    "The account manager who was your best friend while you deposited and now answers every withdrawal request with a bigger investment pitch.",
                ]),
            ]),
            ("Behind the block", "Why is my broker not paying out? Two very different causes", [
                ("p", "Not every delayed payout is fraud. Legitimate brokers can stall when markets are volatile, when their banking partner reviews a large transfer, or when your own verification is incomplete. Those delays are measured in days, come with a clear paper trail, and survive a direct question to support."),
                ("p", "Malicious blocks work differently. The broker is not short of liquidity — it simply never intended to pay. Withdrawal requests trigger a retention script: new conditions, new documents, trades you are told not to close. The purpose is to keep your money on the platform until you give up."),
                ("p", "The practical test: a real operational delay explains itself in verifiable detail. A fraudulent block changes its story every time you ask."),
            ]),
            ("Your options", "Withdrawal blocked: the three routes that still work", [
                ("h3", "Chargeback and bank recall"),
                ("p", "If you funded by card or bank transfer, your bank may be able to reverse the transaction — but chargeback windows close in weeks, not months. Gather your deposit receipts, the broker's withdrawal refusals in writing, and file immediately. This is usually the fastest route for card-funded deposits."),
                ("h3", "Crypto tracing"),
                ("p", "If you paid in Bitcoin or USDT, the transfer is permanent but not invisible: every coin moves on a public ledger and typically ends at an exchange where it is converted to cash. A forensic trace that reaches the cash-out exchange is what forces action."),
                ("h3", "Regulatory complaint — and professional help"),
                ("p", "Report the broker to the financial regulator of the country it claims to operate from; a regulator warning can freeze its accounts. For significant amounts, a specialist fund-recovery investigation combines all three routes and builds the documented, court-usable evidence file that banks and exchanges respond to."),
            ]),
        ],
        "faqs": [
            ("Why has my withdrawal been pending for weeks?", "The pattern matters more than the delay. One dated explanation plus a trackable transfer usually means an operational queue. Shifting excuses, new documents and new conditions each time you ask mean the broker is running a retention script. Treat a withdrawal pending for weeks with changing explanations as a fraud event."),
            ("What should I do first when a broker will not pay out?", "Put the withdrawal request and every refusal in writing, save the account statements and chat logs, and check the firm on the official regulator register. Then ask your bank or card issuer about dispute options, and have the matter assessed by litigation counsel while every route is still open."),
            ("Is my money gone if the broker won't pay?", "Not necessarily. Card and bank transfers can sometimes be reversed within the dispute window, and crypto payments leave a permanent public trail. The odds drop every week — which is why the first move is to preserve evidence and ask for a professional assessment while every route is still open."),
        ],
        "related": [],
    },
    {
        "slug": "chargeback-failed-investment",
        "title": "Chargeback Failed Investment? Bank, Court & Tracing Options | Act Here",
        "description": "Your bank said no — or the chargeback window already closed. What still works when a chargeback on a failed investment is denied or too late.",
        "keywords": "chargeback failed investment, investment chargeback, credit card chargeback scam, dispute investment payment",
        "kicker": "Chargeback options · Updated November 2026",
        "h1": "Chargeback Failed Investment? Bank, Court & Tracing Options",
        "lead": "Your bank said no. Or the 120-day window closed while you were still hoping the broker would pay. A failed chargeback feels like the end of the road — but in UK investment-fraud litigation, it is often just the beginning.",
        "sections": [
            ("Why chargebacks fail", "The four reasons banks deny investment-fraud chargebacks", [
                ("ul", [
                    "Authorised push payment: you sent the money yourself, so the bank treats it as your choice — even if you were defrauded into sending it.",
                    "The window closed: card chargebacks typically must be filed within 120 days of the transaction, and most victims wait far longer.",
                    "'Services as described': the broker points to a trading dashboard and claims you received what you paid for — access to a platform.",
                    "Crypto payments: chargebacks don't exist on-chain, and banks treat crypto purchases as final.",
                ]),
            ]),
            ("What still works", "Three routes after a failed chargeback", [
                ("h3", "Civil claim for fraud or breach of contract"),
                ("p", "A chargeback is a banking remedy. A civil claim is a legal one. If the broker made false promises, changed its terms after you paid, or denied a documented withdrawal, you have a claim in contract and tort — regardless of what the bank decided. UK county-court and High Court routes are available depending on amount."),
                ("h3", "Crypto tracing to the cash-out exchange"),
                ("p", "Even if you paid in crypto, the trail is not lost. Every transaction is on a public ledger, and the operator must eventually convert to fiat at an exchange. A forensic trace that identifies the cash-out exchange is what forces that exchange to freeze accounts and cooperate with law enforcement."),
                ("h3", "Multi-victim coordination"),
                ("p", "One victim is a dispute. Fifty victims is a fraud pattern. Act Here coordinates claims across multiple victims of the same platform, which changes the economics of litigation and the attention of regulators."),
            ]),
        ],
        "faqs": [
            ("My bank denied my chargeback. Do I have any other options?", "Yes. A chargeback is only a banking remedy, not a legal one. You can still sue the broker for fraud or breach of contract, trace crypto payments to the cash-out exchange, and join a coordinated multi-victim claim. The bank's 'no' does not end the case."),
            ("How long do I have to sue after a failed investment?", "In England and Wales, contract and tort claims typically have a 6-year limitation period from the date of the breach or the date you discovered the fraud. Evidence quality matters more than time — the sooner you preserve screenshots and communications, the stronger the claim."),
            ("Can I chargeback a crypto payment?", "Not on-chain. But if you bought the crypto with a card specifically to send to the scammer, some banks will consider a chargeback on the card purchase itself. The stronger route is forensic tracing to the exchange where the operator cashes out."),
        ],
        "related": [],
    },
    {
        "slug": "check-broker-license",
        "title": "Check Broker License: FCA, CySEC, ASIC & SEC Step by Step | Act Here",
        "description": "How to verify a broker's licence on the official FCA, CySEC, ASIC and SEC registers — and the clone-firm tricks that look identical to a real licence.",
        "keywords": "check broker license, how to verify broker licence, is broker regulated, fake broker licence, broker register check",
        "kicker": "Broker verification · Updated November 2026",
        "h1": "Check Broker License: FCA, CySEC, ASIC & SEC Step by Step",
        "lead": "The broker's website shows an FCA registration number. You Google it — it exists. But the number belongs to a completely different company, and the 'broker' is a clone. Licence verification is the single most-skipped step before depositing, and the single most-faked element of a scam platform.",
        "sections": [
            ("The official registers", "Where to verify a broker licence — the only sources that matter", [
                ("ul", [
                    "FCA Register (UK): register.fca.org.uk — search the exact company name, not the trading name.",
                    "CySEC (Cyprus/EU): cysec.gov.cy — the dominant regulator for EU forex and CFD brokers.",
                    "ASIC Connect (Australia): connectonline.asic.gov.au — search ABN and company name.",
                    "SEC EDGAR + FINRA BrokerCheck (US): sec.gov/edgar and brokercheck.finra.org.",
                    "CFTC / NFA (US derivatives): cftc.gov and nfa.futures.org.",
                ]),
            ]),
            ("The clone trick", "How scam brokers fake a licence — and how to catch it", [
                ("p", "Clone firms copy the name, registration number and branding of a real, licensed firm. The licence is real — but it belongs to someone else. The catch: the clone's website URL, phone number and email domain differ from the licensed firm's official records by even one character."),
                ("p", "The three-step check: (1) Find the licence number on the broker's site. (2) Search it on the official regulator's register — not via Google, directly. (3) Compare the registered website, phone and address on the regulator's record with the site you are actually on. If any detail differs, it is a clone."),
            ]),
            ("Red flags", "Licence claims that are always fake", [
                ("ul", [
                    "A licence from 'FINAEU', 'CARFIS', or another regulator that does not exist — the only real Canadian SRO is CIRO; the only real UK regulator is the FCA.",
                    "A registration number that returns no result on the official register, or a result for a different company.",
                    "A 'licence' that is only a PDF on the broker's own website, with no verifiable record on the regulator's public register.",
                    "A regulator badge image that doesn't link to a live record on the regulator's website.",
                ]),
            ]),
        ],
        "faqs": [
            ("How do I check if a broker is FCA regulated?", "Go directly to register.fca.org.uk and search the exact company name — not the trading name, and not via Google. The FCA register shows the firm's authorised status, its registered website, and its approved activities. If the website you are on differs from the registered website, it is a clone firm."),
            ("Is a CySEC licence as good as an FCA licence?", "No. CySEC is a real regulator but a lighter one — no meaningful compensation scheme and weaker escalation if the operator digs in. An FCA licence comes with FSCS protection up to £85,000 and a much stricter conduct regime. Treat CySEC-licensed brokers with more caution, and size your deposits accordingly."),
            ("What if the broker's licence number doesn't exist?", "That is a definitive red flag. Either the broker is unregulated and lying, or it is a clone using a fabricated number. Do not deposit. Report the site to the FCA's clone-firm warning list and to Action Fraud."),
        ],
        "related": [],
    },
    {
        "slug": "pig-butchering-scam",
        "title": "Pig Butchering Scam Explained: The Romance Scam Crypto Fraud | Act Here",
        "description": "They messaged you on WhatsApp, built trust for weeks, then introduced a 'trading platform'. How pig butchering scams work — and what UK litigation can recover.",
        "keywords": "pig butchering scam, romance crypto scam, pig butchering crypto, crypto romance fraud, pig butchering what to do",
        "kicker": "Romance + crypto fraud · Updated November 2026",
        "h1": "Pig Butchering Scam Explained: The Romance Scam Crypto Fraud",
        "lead": "They messaged you by 'mistake' on WhatsApp or Telegram. Weeks of friendly chat. Then a casual mention of a trading platform where they 'made 40% last month'. You deposited a little, watched fake profits grow, deposited more — and now the platform won't let you withdraw, and the person who introduced you has vanished.",
        "sections": [
            ("The script", "How pig butchering actually works", [
                ("p", "The name comes from the Chinese 'sha zhu pan' — fattening the pig before slaughter. The scammer (often a victim of trafficking themselves, working from a compound in Southeast Asia) spends weeks or months building emotional trust. The 'trading platform' is a fake: your deposits go straight to the operator, and the profits on screen are numbers they can edit."),
                ("ul", [
                    "The initial contact is always 'accidental': a wrong number, a wrong WhatsApp group, a mistaken Telegram add.",
                    "The relationship builds slowly — weeks of daily chat before money is ever mentioned.",
                    "The platform is introduced casually, as a favour: 'I'll teach you, but don't tell anyone.'",
                    "Early withdrawals work — a deliberate trust-building move. The big deposits come after.",
                    "The end is always the same: the withdrawal never arrives, the explanations keep changing, and then there is silence.",
                ]),
            ]),
            ("The money trail", "Where your money actually went", [
                ("p", "Your 'trading account' was never real. The deposits went to the operator's wallets or bank accounts, then through mixers or exchanges to cash out. The platform you logged into was a website showing numbers the operator controlled. There were no trades, no profits, and no market."),
                ("p", "The good news: every crypto transaction is on a public ledger, and every fiat transfer left a bank record. A forensic trace that follows the money to the cash-out exchange is what forces action — exchanges freeze accounts and cooperate with law enforcement when presented with a court-ready evidence file."),
            ]),
            ("Your options", "What still works after a pig butchering scam", [
                ("h3", "Crypto tracing"),
                ("p", "If you paid in USDT, BTC or ETH, the trail is permanent. Our forensic team follows the money from your wallet through the operator's addresses to the exchange where they cash out — the point where law enforcement and courts can act."),
                ("h3", "Bank recall and chargeback"),
                ("p", "If any deposit was made by card or bank transfer (even to buy the crypto you then sent), the bank may be able to recall it. The window closes fast — typically 120 days for card chargebacks."),
                ("h3", "Civil claim + criminal referral"),
                ("p", "A coordinated civil claim against the operators (when identifiable) plus a criminal referral to Action Fraud and the NCA creates the pressure that recovers funds. Act Here handles both tracks."),
            ]),
        ],
        "faqs": [
            ("Is pig butchering a scam?", "Yes — it is one of the largest fraud categories in the world, responsible for billions in losses. The 'trading platform' is always fake, the 'profits' are numbers the operator edits, and the person who introduced you is part of the operation (often a trafficking victim working under duress)."),
            ("Can I recover money from a pig butchering scam?", "Sometimes. Crypto tracing to the cash-out exchange is the strongest route when you paid in crypto. Card and bank recalls work for fiat deposits within the dispute window. No honest investigator guarantees recovery — what we can give you is a documented, court-usable trail."),
            ("Why did the platform let me withdraw small amounts at first?", "That is the trust-building phase. The operator lets early withdrawals succeed so you will deposit larger amounts. The block comes only when you try to withdraw a significant balance."),
        ],
        "related": [],
    },
    {
        "slug": "fund-recovery-services",
        "title": "Fund Recovery Services: How to Get Money Back From a Scam Broker | Act Here",
        "description": "Most 'fund recovery' companies are scams themselves. How to tell a real recovery service from a recovery scam — and what legitimate routes actually work.",
        "keywords": "fund recovery services, investment recovery, scam recovery counsel, recover money from broker scam",
        "kicker": "Recovery scams · Updated November 2026",
        "h1": "Fund Recovery Services: How to Get Money Back From a Scam Broker",
        "lead": "You lost money to a scam broker. Then a 'fund recovery specialist' contacts you — they found you through the same scam's victim list — and guarantees to get your money back. This is often the second scam, and it can be run by the same people as the first.",
        "sections": [
            ("The recovery scam", "How fake fund recovery services work", [
                ("ul", [
                    "They contact you — you never contacted them. Real recovery firms don't cold-call victims.",
                    "They guarantee recovery, or quote a success rate above 90%. No honest investigator guarantees anything.",
                    "They claim to have 'inside contacts' at banks or regulators, or to have 'already located' your funds.",
                    "They pressure you to act immediately, before you have time to verify them.",
                ]),
            ]),
            ("What real recovery looks like", "The legitimate routes that actually work", [
                ("h3", "Card chargeback and bank recall"),
                ("p", "The fastest legitimate route for card-funded deposits. Your bank reverses the transaction under 'services not as described' or fraud rules. The window is typically 120 days from the charge — file it immediately."),
                ("h3", "Crypto tracing"),
                ("p", "A forensic blockchain trace follows your payment from your wallet through the operator's addresses to the exchange where they cash out. Exchanges freeze accounts and cooperate when presented with a court-ready evidence file. This is the strongest route for crypto payments."),
                ("h3", "Civil litigation"),
                ("p", "A UK civil claim for fraud or breach of contract is available for up to 6 years. For amounts over £10,000, litigation counsel is the realistic route. For multi-victim platforms, coordinated claims change the economics and the regulator's attention."),
            ]),
            ("How to verify a recovery service", "The three checks before you instruct anyone", [
                ("ul", [
                    "Did they contact you, or did you contact them? Real firms don't cold-call.",
                    "Do they guarantee recovery? No honest investigator does — the answer should be 'we assess, then we tell you what's realistic'.",
                    "Can you verify their company registration, their litigation counsel's SRA number, and their physical office? Check Companies House and the SRA register directly.",
                ]),
            ]),
        ],
        "faqs": [
            ("Are fund recovery services legitimate?", "Some are — but the industry is saturated with scams. The test: did they contact you (red flag), do they guarantee recovery (red flag), and can you verify their company registration and litigation counsel independently (essential). Act Here is UK litigation counsel — we don't cold-call, and we don't guarantee outcomes."),
            ("How much does fund recovery cost?", "The consultation is free. We first need to validate your claim and understand its prospects and feasibility, and that depends on the level of proof."),
            ("Can I get my money back from a scam broker?", "Sometimes. The realistic routes are card chargeback (within 120 days), bank recall (within days), crypto tracing (permanent trail), and civil litigation (6-year limitation). The odds drop every week — which is why the first move is to preserve evidence and get a professional assessment while every route is still open."),
        ],
        "related": [],
    },
]

def render_section(kicker, h2, blocks):
    out = [f'<section style="padding:2.5rem 0;border-bottom:1px solid var(--line)"><div class="article-body" style="max-width:760px;margin:0 auto">']
    out.append(f'<span style="display:block;font-size:.72rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:.6rem">{htmlmod.escape(kicker)}</span>')
    out.append(f'<h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">{htmlmod.escape(h2)}</h2>')
    for kind, content in blocks:
        if kind == "p":
            out.append(f"<p>{content}</p>")
        elif kind == "h3":
            out.append(f'<h3 style="font-size:1.05rem;color:var(--sage-dark);margin:1.6rem 0 .6rem;font-weight:600">{htmlmod.escape(content)}</h3>')
        elif kind == "ul":
            out.append('<ul style="list-style:none;margin:1rem 0 1.5rem;padding:0">' + "".join(
                f'<li style="padding:.5rem 0;display:flex;gap:.7rem;color:var(--text-2);font-size:.95rem;line-height:1.7"><span style="color:var(--sage-dark);font-weight:700;flex-shrink:0">&#10003;</span><span>{item}</span></li>'
                for item in content
            ) + "</ul>")
    out.append("</div></section>")
    return "\n".join(out)

def render_faq(faqs):
    items = "\n".join(
        f'<div style="border-bottom:1px solid var(--line);padding:1.2rem 0"><h3 style="font-size:1rem;color:var(--navy);margin-bottom:.5rem;font-weight:600">{htmlmod.escape(q)}</h3><p style="color:var(--text-2);font-size:.93rem;line-height:1.75;margin:0">{a}</p></div>'
        for q, a in faqs
    )
    return f'<section style="padding:2.5rem 0"><div class="article-body" style="max-width:760px;margin:0 auto"><span style="display:block;font-size:.72rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:.6rem">FAQ</span><h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">Frequently asked questions</h2>{items}</div></section>'

def build_faq_schema(slug, faqs, title, description, keywords=""):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"https://act-here.uk/guides/{slug}.html#webpage",
                "url": f"https://act-here.uk/guides/{slug}.html",
                "name": title,
                "description": description,
                "isPartOf": {"@type": "WebSite", "name": "Act Here", "url": "https://act-here.uk/"},
                "inLanguage": "en-GB",
            },
            {
                "@type": "Article",
                "headline": title,
                "description": description,
                "author": {"@type": "Organization", "name": "Act Here"},
                "publisher": {"@type": "Organization", "name": "Act Here", "url": "https://act-here.uk/"},
                "dateModified": "2026-11-16",
                "inLanguage": "en-GB",
                **({"keywords": keywords} if keywords else {}),
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in faqs
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://act-here.uk/"},
                    {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://act-here.uk/guides/"},
                    {"@type": "ListItem", "position": 3, "name": title.split(":")[0], "item": f"https://act-here.uk/guides/{slug}.html"},
                ],
            },
        ],
    }

def render_guide(g):
    slug = g["slug"]
    sections_html = "\n".join(render_section(*s) for s in g["sections"])
    faq_html = render_faq(g["faqs"])
    schema = build_faq_schema(slug, g["faqs"], g["title"], g["description"], g.get("keywords", ""))
    schema_json = json.dumps(schema, ensure_ascii=False, indent=1)
    # No broker names on guides: point readers at the searchable review archive instead.
    related_html = '<section style="padding:2rem 0;background:var(--off-white)"><div class="article-body" style="max-width:760px;margin:0 auto"><p style="color:var(--text-muted);font-size:.95rem">Looking for a specific platform? <a href="../reviews/index.html" style="color:var(--sage-dark)">Search our broker review archive</a> — we publish complaint assessments of trading platforms, prop firms and their payout records.</p></div></section>'
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{htmlmod.escape(g['title'])}</title>
 <meta name="description" content="{htmlmod.escape(g['description'])}">
 <meta name="keywords" content="{htmlmod.escape(g.get('keywords', ''))}">
 <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
 <link rel="canonical" href="https://act-here.uk/guides/{slug}.html">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{htmlmod.escape(g['title'])}">
 <meta property="og:description" content="{htmlmod.escape(g['description'])}">
 <meta property="og:url" content="https://act-here.uk/guides/{slug}.html">
 <script type="application/ld+json">
{schema_json}
 </script>
 <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<div id="nav-placeholder"></div>
<div class="breadcrumb"><a href="../index.html">Home</a><span>&#8250;</span><a href="index.html">Guides</a><span>&#8250;</span> {htmlmod.escape(g['h1'].split(':')[0])}</div>
<div class="page-hero">
 <div class="hero-badge">{htmlmod.escape(g['kicker'])}</div>
 <h1>{htmlmod.escape(g['h1'])}</h1>
 <p>{htmlmod.escape(g['lead'])}</p>
</div>
{sections_html}
{related_html}
{faq_html}
<section style="padding:3rem 0;background:var(--navy);color:#fff;text-align:center">
 <div style="max-width:640px;margin:0 auto;padding:0 5%">
 <h2 style="font-family:var(--font-serif);color:#fff;font-size:1.9rem;margin-bottom:.8rem">Lost money to this scam?</h2>
 <p style="color:rgba(255,255,255,.75);margin-bottom:1.5rem">Our UK litigation team can assess your options for free. We don't just negotiate; we are prepared to litigate.</p>
 <a href="../pages/contact.html" class="btn-primary">Book a free consultation</a>
 </div>
</section>
<div id="footer-placeholder"></div>
<script src="../js/config.js"></script>
<script src="../js/layout.js"></script>
</body>
</html>
"""
    return html

def render_index():
    cards = "\n".join(
        f'<div style="border:1px solid var(--line);border-radius:8px;padding:1.5rem;background:#fff"><h3 style="font-family:var(--font-serif);font-size:1.1rem;color:var(--navy);margin-bottom:.5rem"><a href="{g["slug"]}.html" style="color:var(--navy);text-decoration:none">{htmlmod.escape(g["h1"])}</a></h3><p style="color:var(--text-2);font-size:.88rem;line-height:1.65;margin:0">{htmlmod.escape(g["description"][:140])}...</p></div>'
        for g in GUIDES_DATA
    )
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Guides: How to Recover Money From Investment Fraud | Act Here</title>
 <meta name="description" content="Step-by-step guides on broker withdrawal problems, chargebacks, prop trading scams, pig butchering, and fund recovery — from UK litigation counsel.">
 <link rel="canonical" href="https://act-here.uk/guides/">
 <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<div id="nav-placeholder"></div>
<div class="breadcrumb"><a href="../index.html">Home</a><span>&#8250;</span> Guides</div>
<div class="page-hero">
 <div class="hero-badge">Victim-Intent Guides</div>
 <h1>How to Recover Money From Investment Fraud</h1>
 <p>Practical guides for victims of broker fraud, prop trading scams, pig butchering, and withdrawal blocks — written by UK litigation counsel.</p>
</div>
<section style="padding:2.5rem 0">
 <div style="max-width:1100px;margin:0 auto;padding:0 5%;display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1.5rem">
{cards}
 </div>
</section>
<div id="footer-placeholder"></div>
<script src="../js/config.js"></script>
<script src="../js/layout.js"></script>
</body>
</html>
"""

def main():
    for g in GUIDES_DATA:
        path = os.path.join(GUIDES, g["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_guide(g))
        print("wrote", path)
    with open(os.path.join(GUIDES, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    print("wrote", os.path.join(GUIDES, "index.html"))

if __name__ == "__main__":
    main()
