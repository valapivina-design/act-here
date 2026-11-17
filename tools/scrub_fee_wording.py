#!/usr/bin/env python3
"""Remove pay-to-withdraw / release-fee / tax-before-withdrawal wording from review pages.

Each edit is a (old, new) substring pair applied file-wide, in every escaping the
text can appear in (visible HTML, attribute, JSON-LD). Direct quotes are trimmed
with an ellipsis rather than reworded.
"""
import glob
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REV = ROOT / "reviews"

ESC_FEE = "and escalating fee demands."

# slug -> list of (old, new)
EDITS = {
    "aixaminer": [(", then being asked to pay 'gas fee top-ups' or 'network priority fees' to expedite processing. After paying, the status resets to pending.", ", with the status repeatedly resetting to pending.")],
    "algobi": [("'system maintenance,' 'verification requirements,' or escalating fee demands.", "'system maintenance' or 'verification requirements.'")],
    "alpinalimted": [("Victims report being asked to pay 'verification fees,' 'tax clearance' charges, and 'processing costs' before withdrawals.", "Victims report that withdrawal requests are not completed.")],
    "apexvault": [
        ("including fake 'security audits,' 'compliance checks,' and escalating fee demands.", "including fake 'security audits' and 'compliance checks.'"),
        ("they are told their accounts require 'verification upgrades' that cost additional money.", "they are told their accounts require 'verification upgrades.'"),
    ],
    "assetcrest": [("with fake 'compliance fees' and 'tax clearance' demands.", "with shifting 'compliance' conditions.")],
    "torroso": [("with fake 'compliance fees' and 'tax clearance' demands.", "with shifting 'compliance' conditions.")],
    "athensmarkets": [("through fake 'compliance checks' and escalating fee demands.", "through fake 'compliance checks.'")],
    "azethio": [
        (" asking me to pay commission fees and taxes from an external account.", " ..."),
        (" pending external commission and tax payments.", "."),
    ],
    "bemine-cloud": [("Users describe being asked for 'maintenance fees,' 'upgrade charges,' and 'blockchain synchronisation' payments, each fee revealing another required fee behind it.", "Users describe a series of new requirements, each one revealing another behind it.")],
    "bituigg-exchange": [
        ("were sent under unlock promises and", "were sent and"),
        ("Account lockouts triggered a $5,320 restore fee, then another $5,000 credit-standing demand.", "The account was then locked and the funds were not returned."),
        ("Restore Then Credit Fees", "Account Locked, Funds Not Returned"),
        ("BBB: locked out and charged $5320 to restore the account. Then told credit rating was too low and I needed another $5000.", "BBB: locked out ... Then told credit rating was too low ..."),
    ],
    "blue-chip-growth-fund": [
        (", paid Bitinvests fees, and recovered nothing.", " and recovered nothing."),
        (", paying numerous fees without recovery.", ", without any recovery."),
        ("into Bitinvests recovery fees.", "into a Bitinvests recovery pitch."),
    ],
    "bluechip-usa": [("Multiple users report that after paying initial compliance fees, additional requirements appear, insurance bonds, AML verification deposits, and processing fees. Each payment unlocks a new demand rather than releasing actual funds.", "Multiple users report that each time one requirement is met, additional requirements appear, and funds are not released.")],
    "btduex": [("including fake 'security verifications' " + ESC_FEE, "including fake 'security verifications.'")],
    "ev-capital": [("including fake 'security verifications' " + ESC_FEE, "including fake 'security verifications.'")],
    "zenstox": [("including fake 'security verifications' " + ESC_FEE, "including fake 'security verifications.'")],
    "bullprofitsfx": [("are blocked by escalating fee requirements.", "are blocked.")],
    "bxbmarket": [("including fake 'security audits' " + ESC_FEE, "including fake 'security audits.'")],
    "capitaltradingia": [("met with demands for 'AI processing fees,' 'verification charges,' and 'tax clearance' payments. After paying these fees, users report that new fees appear.", "met with a series of new requirements.")],
    "chobes": [("after withdrawal access required further payments that never released funds.", "after withdrawals were never released.")],
    "crypto-clear": [
        ("Has anyone else paid the £305 and then been asked to pay another £254 to the us government to release my funds help is it a scam Yes I paid the £305 and also got asked to pay the £254 to the government and I still haven't paid it as I don't trust it at all.. johnathon just keeps asking for more and more money", "... help is it a scam ... I don't trust it at all.."),
    ],
    "cryptonow": [("Victims describe being asked to pay 'network confirmation fees,' 'wallet verification charges,' and 'tax clearance' costs before any withdrawal can be processed. After paying these fees, the platform either demands more or ceases communication entirely.", "Victims describe a series of new requirements before any withdrawal can be processed. The platform then either adds more or ceases communication entirely.")],
    "dogecloudmine": [
        ("or additional fee requirements.", "or additional requirements."),
        ("met with demands for 'gas fees,' 'blockchain confirmation charges,' or 'account verification' payments. Users who pay these additional charges report that their accounts are subsequently closed without explanation.", "met with 'blockchain confirmation' or 'account verification' demands. Users report that their accounts are subsequently closed without explanation."),
    ],
    "dz-alliance": [
        (", then insisted he first pay a $30,000 tax with external funds, not from his account balance.", " ..."),
        ("fake bonuses, and tax demands that blocked withdrawals.", "fake bonuses, and blocked withdrawals."),
        (", then a $30,000 tax that had to be paid from external funds before any withdrawal.", ", and withdrawals that never followed."),
        ("Fake $300k Bonus Then Tax", "Fake $300k Bonus, No Withdrawal"),
    ],
    "eagleeye-trading": [
        (", then a demand for more external cash to repay before any withdrawal.", ", with no withdrawal allowed."),
        ("They refused to take the loan out of CBT winnings and demanded I put MORE money in to pay off the loan.", "They refused to take the loan out of CBT winnings ..."),
    ],
    "elite-trading": [("identity verification that never completes, minimum trading volume requirements that reset, and compliance fees that multiply.", "identity verification that never completes and minimum trading volume requirements that reset.")],
    "exbo-invest": [("the platform demands tax payments, compliance fees, or verification deposits before releasing funds.", "the platform adds new conditions and does not release funds.")],
    "exclusivesky-investment-guild": [
        (" When I tell Exclusivesky they recommend paying the withdrawal fee.", ""),
        ("Handlers still recommend paying the exchange fee, which victims read as proof the guild and exchange work together.", "Victims read the handlers' responses as proof the guild and exchange work together."),
    ],
    "fetch-frieth-logistics": [
        ("Unexpected Release Fee Pattern", "Parcel Fraud Pattern"),
        ("fake logistics desks demand customs or release payments for packages the victim never ordered.", "fake logistics desks contact victims about packages they never ordered."),
    ],
    "fintrixmarkets": [("including fake 'compliance fees' and 'tax clearance' demands.", "including shifting 'compliance' conditions.")],
    "fivenot-10": [("that blocked withdrawals and demanded more deposits to retrieve funds.", "that blocked withdrawals.")],
    "fx-pec": [("demands for additional documentation, fees, and verification steps", "demands for additional documentation and verification steps")],
    "gold-trader-mo": [
        ("VIP deposit schemes, and extra fees before withdrawal.", "VIP deposit schemes, and blocked withdrawals."),
        ('Several users describe being asked to pay additional "commission", "gas", or activation fees before a withdrawal of supposed profits, a classic escalation pattern.', "Several users describe new conditions being added before a withdrawal of supposed profits, a classic escalation pattern."),
        ("Extra Fee Before Withdrawal", "New Conditions Before Withdrawal"),
        (" Once you deposit with them, they keeping asking for more money for account activation, commission etc.", " ..."),
    ],
    "heleket": [("and refunds that take weeks or require extra network fees before release.", "and refunds that take weeks.")],
    "hellobit": [
        ("are blocked by escalating fee demands described as tax clearance, compliance verification, or insurance bonds.", "are blocked by an escalating series of new conditions."),
        ("tax fee demands before withdrawals,", "blocked withdrawals,"),
    ],
    "hm-treasury": [("or ask for fees via messaging apps.", "or contact them via messaging apps.")],
    "iodefi": [
        ("that freezes withdrawals and demands large payments to unlock affiliate or reinvested balances.", "that freezes withdrawals on affiliate or reinvested balances."),
        ("Operators allegedly admitted an error then still required $25,000 payments to unlock, with a second identical demand after the first transfer cleared. That pattern matches advance-deposit mining frauds rather than a regulated mining host.", "Operators allegedly admitted an error but still did not release the balance. That pattern matches mining frauds rather than a regulated mining host."),
        ("Pay to Unlock After Their Error", "Balance Frozen After Their Error"),
    ],
    "lexo-exchange": [
        (" When it is time to withdraw they require an additional fee. After the fee is paid they refuse to release the funds. I paid a $579,000 fee yet they have not released my profits.", " ... they have not released my profits."),
        ("and large wire fees that never release withdrawals.", "and withdrawals that are never released."),
        ("Fee Paid, Profits Not Released", "Profits Not Released"),
    ],
    "ligocu-betfandecs": [("with fake 'compliance checks' " + ESC_FEE, "with fake 'compliance checks.'")],
    "segofinance": [("with fake 'compliance checks' " + ESC_FEE, "with fake 'compliance checks.'")],
    "lst-alliance-trading": [
        ("I paid profit fees and still could not withdraw because IPX locked funds claiming a further tax must be paid from outside the account.", "I ... still could not withdraw because IPX locked funds ..."),
        ("Profit Fee Then Tax Wall", "Funds Locked at Withdrawal"),
        ("Separate filings describe profit fees, LST tokens, cascading ICOs, then tax demands from the exchange.", "Separate filings describe LST tokens, cascading ICOs, then blocked withdrawals at the exchange."),
    ],
    "metaquotes": [("and asking for wallet access or fees should", "and asking for wallet access should")],
    "n5-nextleap": [
        (" they said I had to pay a 2% Asset management fee of $98,870.", " ..."),
        (", then a 2% fee near $98,870 with a loan story requiring $10,000 external cash.", " that could not be withdrawn."),
        ("paper balances then demand large external asset-management fees before withdrawal.", "paper balances that cannot be withdrawn."),
        ("Multi-Million Screen, External Fee", "Multi-Million Screen, No Withdrawal"),
        ("Borrowed Fee Then Silence", "Money Sent, Then Silence"),
        ("BBB: Next leap would let me borrow most of it if I paid $10000 from external funds. Once I paid that $10000 they took my money and disappeared.", "BBB: ... they took my money and disappeared."),
    ],
    "nextproptrader": [("Separate high-loss processing-fee stories", "Separate high-loss stories")],
    "polywex": [
        ("Never send further funds to 'unlock' a balance; document and instruct counsel instead.", "Document everything and instruct counsel."),
        ("and Reddit reports of users being asked for an extra deposit before they can withdraw earnings.", "and Reddit reports of users unable to withdraw earnings."),
        ("Reddit threads describe a cash-out demand for an additional deposit before release of balances.", "Reddit threads describe balances that could not be cashed out."),
        ("Extra Deposit Before Withdraw", "Earnings Could Not Be Withdrawn"),
        (", and they say I need to deposit $150 to withdraw the money I've earned there.", " ..."),
    ],
    "prime-holdings": [
        (" she was told she had to pay over 8k in taxes before it could be released.", " ..."),
        (", then an $8,000+ tax was demanded to release funds.", ", but the funds were not released."),
        ("then demands large tax payments before withdrawal,", "then blocks withdrawal,"),
        ("Tax Before Withdrawal", "Withdrawal Blocked"),
    ],
    "profit-trade": [("are blocked by escalating fee demands.", "are blocked.")],
    "valterox": [("are blocked by escalating fee demands.", "are blocked.")],
    "qberx-capital": [("withdrawal holds, unclear regulation, and pressure to deposit more before release.", "withdrawal holds and unclear regulation.")],
    "saovex": [("that repeatedly demanded fresh deposits for verification, wallet checks, and tier upgrades before any withdrawal.", "that repeatedly added verification, wallet-check, and tier-upgrade conditions before any withdrawal.")],
    "smartstp": [("through fake 'compliance checks' and escalating fee requirements.", "through fake 'compliance checks.'")],
    "starpronto": [(" Do not send further capital to release a locked Athena or Slogem balance.", "")],
    "t15-mining": [("escalating clearance demands", "shifting withdrawal conditions")],
    "tapbit": [("Every time I tried to withdraw, they keep asking me to make more deposit. They threatened me that if I don't make the deposit within certain time, they said all my credits will be affected.", "Every time I tried to withdraw ... they said all my credits will be affected.")],
    "usdpick": [("withdrawals, rewards that stay pending, and claims that deposits or upgrades were required before cash-out.", "withdrawals and rewards that stay pending.")],
    "wallethatch": [
        (" They are charging you before!!", " ..."),
        (" and then they send you an email asking for tracing fees and legal fees before they refund you.", " ..."),
        ("Recovery businesses that request payment before funds are returned are a common secondary-scam pattern. Legitimate counsel typically explains fees in a clear engagement letter and explains fees only in a clear engagement letter with regulated counsel.", "Recovery businesses whose service does not match what they advertise are a common secondary-scam pattern. Check that any adviser is regulated before instructing them."),
        ("Fees After No-Win-No-Fee Pitch", "Service Did Not Match the Pitch"),
        (", then later demands tracing fees and legal fees before any refund.", ", but does not operate that way."),
    ],
    "weisero": [("Victims report being asked to pay 'verification fees,' 'tax clearance' charges, and 'processing costs' before withdrawals, fees that multiply indefinitely.", "Victims report that withdrawal requests are met with a series of new requirements.")],
}

# Wording repeated on many pages; applied wherever it occurs.
GLOBAL = [
    ("When I tried to take out money I was told I owed compliance fees.", "When I tried to take out money the withdrawal was refused."),
    ("I was told I needed to pay a tax clearance fee first. After paying, another fee appeared.", "the request was blocked."),
    ('Any contact after a withdrawal dispute, especially offering to "release" your funds for a fee, is almost certainly part of an escalating fraud.', "Treat any unsolicited contact after a withdrawal dispute with caution."),
]

VARIANTS = [
    lambda t: t,
    lambda t: t.replace('"', "&quot;"),
    lambda t: t.replace("'", "&#x27;"),
    lambda t: t.replace("'", "&#39;"),
    lambda t: t.replace('"', "&quot;").replace("'", "&#x27;"),
    lambda t: t.replace('"', '\\"'),
    lambda t: t.replace("&", "&amp;"),
]


def apply(s, old, new):
    total = 0
    seen = set()
    for v in VARIANTS:
        o, n = v(old), v(new)
        if o in seen:
            continue
        seen.add(o)
        k = s.count(o)
        if k:
            s = s.replace(o, n)
            total += k
    return s, total


def main():
    missing = []
    changed = 0
    for path in sorted(REV.glob("*.html")):
        slug = path.name.replace("-review.html", "").replace(".html", "")
        s0 = s = path.read_text(encoding="utf-8")
        for old, new in GLOBAL:
            s, _ = apply(s, old, new)
        for old, new in EDITS.get(slug, []):
            s, k = apply(s, old, new)
            if not k:
                missing.append((slug, old[:70]))
        if s != s0:
            for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
                json.loads(block)
            path.write_text(s, encoding="utf-8")
            changed += 1
    unknown = [k for k in EDITS if not (REV / f"{k}-review.html").exists() and not (REV / f"{k}.html").exists()]
    print(f"changed {changed} files")
    if unknown:
        print("unknown slugs:", unknown)
    if missing:
        print("edits that matched nothing:")
        for m in missing:
            print("  ", m)
    if unknown or missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
