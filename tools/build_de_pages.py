#!/usr/bin/env python3
"""Build rich German victim-intent pages under /de/. Native German copy, full JSON-LD, FAQ in German."""
import os, json, html as htmlmod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DE = os.path.join(ROOT, "de")

PAGES = [
    {
        "slug": "krypto-anwalt",
        "title": "Krypto Anwalt: Geld zurück nach Krypto-Betrug – Deutschlandweit | Act Here",
        "description": "Krypto Anwalt gesucht? Bei Krypto-Betrug, blockierten Auszahlungen und Fake-Brokern: blockchainforensik, Rückbuchung und zivilrechtliche Durchsetzung. Kostenlose Ersteinschätzung.",
        "keywords": "krypto anwalt, anwalt krypto betrug, rechtsanwalt kryptowährung, krypto anwalt münchen, krypto anwalt berlin, krypto anwalt köln, krypto anwalt hamburg, krypto anwalt frankfurt, krypto anwalt stuttgart, krypto anwalt in der nähe, krypto betrug anwalt, bitcoin anwalt, anwalt crypto scam",
        "badge": "Rechtsanwalt für Krypto-Betrug · Aktualisiert November 2026",
        "h1": "Krypto Anwalt: Ihr Anwalt bei Krypto-Betrug und Scam",
        "lead": "Sie haben bei einem Krypto-Investment Geld verloren – durch einen Fake-Broker, eine betrügerische Trading-Plattform oder einen Romance-Scam? Ein auf Krypto-Betrug spezialisierter Anwalt kann mehr erreichen als eine Strafanzeige allein: Blockchainforensik, Rückbuchungen über Banken und Börsen sowie zivilrechtliche Ansprüche. Act Here prüft Ihren Fall kostenlos und unverbindlich.",
        "sections": [
            ("Wann Sie einen Krypto Anwalt brauchen", "Typische Fälle, in denen Betroffene zu uns kommen", [
                ("ul", [
                    "Auszahlung blockiert: Die Plattform verweigert die Auszahlung Ihrer Gewinne oder Ihres Guthabens – mit immer neuen Begründungen.",
                    "Fake-Broker oder Scam-Plattform: Das angebliche Investment existierte nie; die Website ist inzwischen offline oder der Support schweigt.",
                    "Romance Scam / Pig Butchering: Eine Online-Bekanntschaft hat Sie über Wochen in ein Krypto-Investment gelockt.",
                    "Erbe oder Wallet-Zugang: Angehörige haben keinen Zugriff auf Wallets oder Börsenkonten eines Verstorbenen.",
                    "Konto gesperrt bei einer echten Börse: Ihr Konto bei einer regulierten Exchange wurde ohne nachvollziehbaren Grund eingefroren.",
                ]),
            ]),
            ("Was ein Krypto Anwalt tatsächlich bewirkt", "Die drei Hebel: Blockchainforensik, Banken, Zivilrecht", [
                ("h3", "Blockchainforensik und Wallet-Tracing"),
                ("p", "Jede Bitcoin- oder USDT-Transaktion ist öffentlich und dauerhaft nachvollziehbar. Unsere Ermittler verfolgen den Weg Ihrer Coins von Ihrer Wallet über die Adressen der Täter bis zu der Börse, an der diese zu Bargeld machen. Genau dort setzt der Hebel an: Börsen sperren Konten und kooperieren mit Ermittlungsbehörden, wenn ihnen eine gerichtsverwertbare Beweisakte vorliegt."),
                ("h3", "Rückbuchung und Chargeback über Ihre Bank"),
                ("p", "Wenn Sie per Kreditkarte oder Überweisung eingezahlt haben – auch zum Kauf von Kryptowährung, die Sie dann weitergeleitet haben – kommt eine Rückbuchung in Betracht. Die Fristen sind kurz: Bei Kreditkarten in der Regel 120 Tage. Je früher Sie handeln, desto besser stehen die Chancen."),
                ("h3", "Zivilrechtliche Ansprüche und Klage"),
                ("p", "Eine Strafanzeige genügt selten, um Ihr Geld zurückzubekommen – die Staatsanwaltschaft verfolgt Täter, nicht Ihre Rückzahlung. Zivilrechtlich prüfen wir Ansprüche aus Betrug (§ 823 Abs. 2 BGB i.V.m. § 263 StGB), Vertrag und ungerechtfertigter Bereicherung. Act Here verhandelt nicht nur: Wir sind bereit, Ihren Fall vor Gericht zu bringen."),
            ]),
            ("Krypto Anwalt in Ihrer Stadt", "Deutschlandweit tätig: München, Berlin, Köln, Hamburg, Frankfurt und mehr", [
                ("p", "Betroffene suchen häufig einen Krypto Anwalt in München, Berlin, Köln, Hamburg, Frankfurt am Main, Stuttgart oder Düsseldorf – also einen Anwalt in der Nähe. Krypto-Betrug ist jedoch ein grenzüberschreitendes Delikt: Die Täter sitzen im Ausland, die Beweise liegen auf der Blockchain, und die entscheidenden Schritte (Tracing, Auskunftsersuchen an Börsen, Rückbuchungen) erfolgen digital. Act Here betreut Mandate deutschlandweit und international – unabhängig von Ihrem Wohnort."),
                ("p", "Wichtiger als die Postleitzahl ist die Spezialisierung: Fragen Sie jeden Anwalt, ob er bereits Blockchain-Tracing in gerichtsverwertbarer Form erstellt und mit Krypto-Börsen zusammengearbeitet hat."),
                ("p", "Betroffene, die Krypto Betrug melden oder Krypto Betrug erkennen wollen, finden die Schritt-für-Schritt-Anleitung in unserem Ratgeber zu <a href=\"krypto-betrug.html\">Krypto-Betrug</a>. Dort erklären wir auch, wie Sie nach Krypto Betrug Geld zurück sichern und welche Krypto Betrug Hilfe realistisch ist. Wer nach einem Krypto Scam Anwalt sucht, sollte denselben Maßstab anlegen: Tracing-Kompetenz statt Versprechen."),
            ]),
            ("Erste Schritte", "Was Sie sofort tun sollten – bevor Spuren verwischen", [
                ("ul", [
                    "Leisten Sie keine weiteren Zahlungen an die Plattform oder an Personen, die in ihrem Namen auftreten.",
                    "Sichern Sie alle Beweise: Screenshots von Konto und Guthaben, Chats, E-Mails, Überweisungsbelege, Wallet-Adressen und die exakten URLs der Plattform.",
                    "Kontaktieren Sie noch heute Ihre Bank: Überweisungen lassen sich teilweise zurückrufen, Kreditkartenzahlungen reklamieren.",
                    "Erstatten Sie Strafanzeige bei der Polizei oder der Online-Wache Ihres Bundeslandes – sie schadet nicht, ersetzt aber keine zivilrechtliche Strategie.",
                    "Lassen Sie Ihren Fall kostenlos einschätzen: Wir sagen Ihnen ehrlich, was realistisch verfolgbar ist und was nicht.",
                ]),
            ]),
        ],
        "faqs": [
            ("Was kostet ein Krypto Anwalt?", "Die Ersteinschätzung Ihres Falls ist bei Act Here kostenlos und unverbindlich. Sie dient dazu, Ihren Anspruch zu prüfen: was passiert ist, welche Beweise vorliegen und welche Wege realistisch sind. Alles Weitere wird vor Beginn schriftlich mit Ihnen vereinbart."),
            ("Kann ein Anwalt mein Geld bei Krypto-Betrug zurückholen?", "Teilweise – und ehrlicherweise nicht immer. Die besten Chancen bestehen bei Kartenzahlungen und Banküberweisungen innerhalb der Rückbuchungsfristen sowie bei Krypto-Zahlungen, die zu einer regulierten Börse geführt haben. Kein seriöser Anwalt garantiert eine Rückzahlung. Wir sagen Ihnen nach der kostenlosen Ersteinschätzung, welche Wege in Ihrem Fall realistisch sind."),
            ("Lohnt sich ein Anwalt auch bei kleineren Beträgen?", "Ab etwa 1.000 Euro Schaden ist eine professionelle Einschätzung sinnvoll, schon wegen der Rückbuchungsfristen bei Banken. Bei fünfstelligen Beträgen ist anwaltliche Vertretung fast immer wirtschaftlich sinnvoll. Bei sehr kleinen Beträgen kann die Strafanzeige plus Rückbuchung über die eigene Bank ausreichen."),
            ("Strafanzeige oder Anwalt – was ist besser?", "Beides, aber mit unterschiedlichem Ziel: Die Strafanzeige richtet sich gegen die Täter und kostet nichts, führt aber selten zur Rückzahlung. Der Anwalt verfolgt Ihr Geld: Rückbuchung, Tracing, zivilrechtliche Ansprüche. Wer sein Geld zurückwill, braucht die zivilrechtliche Spur."),
            ("Gibt es einen Krypto Anwalt in meiner Nähe?", "Act Here betreut Krypto-Betrugsmandate deutschlandweit – München, Berlin, Köln, Hamburg, Frankfurt, Stuttgart, Düsseldorf und überall sonst. Krypto-Fälle werden ohnehin digital bearbeitet: Tracing, Börsen-Anfragen und Bankwege sind ortsunabhängig. Entscheidend ist Spezialisierung, nicht Entfernung."),
            ("Wie erkenne ich einen unseriösen „Krypto-Anwalt“ oder Recovery-Dienst?", "Zwei Warnsignale: Er kontaktiert Sie unaufgefordert (seriöse Kanzleien rufen keine Opfer an) und er garantiert die Rückzahlung. Prüfen Sie die Kanzleiregistrierung und lassen Sie sich schriftlich erklären, welche konkreten Schritte geplant sind."),
        ],
    },
    {
        "slug": "anlagebetrug-geld-zurueck",
        "title": "Anlagebetrug: Geld zurück – So holen Sie Ihr Investment zurück (2026) | Act Here",
        "description": "Anlagebetrug: Geld zurück ist möglich – über Rückbuchung, Chargeback, Krypto-Tracing und Zivilklage. Was Betroffene jetzt tun müssen. Kostenlose Ersteinschätzung.",
        "keywords": "anlagebetrug geld zurück, anlagebetrug was tun, anlagebetrug anzeigen, anlagebetrug anwalt, anlagebetrug melden, anlagebetrug erkennen, geld zurück nach anlagebetrug, investmentbetrug geld zurück, anlagebetrug hilfe, anlagebetrug stgb § 263",
        "badge": "Anlagebetrug · Aktualisiert November 2026",
        "h1": "Anlagebetrug: Geld zurück – Ihre realistischen Optionen",
        "lead": "Sie haben in eine Anlage investiert, die es nie gab – und die Auszahlung wird verweigert oder die Plattform ist verschwunden. Anlagebetrug (§ 263 StGB) ist die häufigste Anlagestraftat Deutschlands; der Schaden geht jährlich in die Milliarden. Die entscheidende Frage ist nicht, ob Sie betrogen wurden, sondern wie schnell Sie jetzt handeln: Rückbuchungsfristen laufen in Wochen ab, Krypto-Spuren kühlen täglich ab.",
        "sections": [
            ("Sofortmaßnahmen", "Anlagebetrug: Was tun in den ersten 72 Stunden", [
                ("ul", [
                    "Keine weiteren Zahlungen an die Plattform oder an Personen, die in ihrem Namen auftreten.",
                    "Beweise sichern: Screenshots des Kontos und der angezeigten Gewinne, alle Chats und E-Mails, Überweisungsbelege, Transaktions-IDs, Wallet-Adressen, die exakten URLs. Plattformen gehen über Nacht offline.",
                    "Bank kontaktieren: Überweisungen lassen sich teilweise zurückholen, Kreditkartenzahlungen reklamieren (Chargeback, meist 120 Tage Frist).",
                    "Strafanzeige erstatten: bei jeder Polizeidienststelle oder der Online-Wache Ihres Bundeslandes. Sie dokumentiert den Fall, ersetzt aber keine Rückholung.",
                    "Fall professionell einschätzen lassen, solange alle Wege offen sind.",
                ]),
            ]),
            ("Die Rückhol-Wege", "Anlagebetrug: Geld zurück über vier Wege", [
                ("h3", "1. Rückbuchung und Überweisungsrückruf"),
                ("p", "Bei SEPA-Überweisungen kann die eigene Bank unter Umständen einen Rückruf einleiten – innerhalb weniger Tage nach der Überweisung. Bei Kreditkartenzahlungen greift das Chargeback-Verfahren: „Leistung nicht wie beschrieben“ oder Betrug. Die Frist beträgt üblicherweise 120 Tage ab Belastung – danach ist der Bankweg endgültig geschlossen."),
                ("h3", "2. Krypto-Tracing bis zur Auszahlungsbörse"),
                ("p", "Wer in Bitcoin, USDT oder Ethereum gezahlt hat, hinterlässt eine unlöschbare Spur. Unsere Blockchainforensik verfolgt die Coins bis zu der Börse, an der die Täter in Euro auszahlen. Mit einer gerichtsverwertbaren Beweisakte lassen sich Konten sperren und Auskünfte über die Kontoinhaber erwirken – der stärkste Hebel bei Krypto-Anlagebetrug."),
                ("h3", "3. Zivilklage und Schadensersatz"),
                ("p", "Zivilrechtlich kommen Ansprüche aus § 823 Abs. 2 BGB i.V.m. § 263 StGB (Betrug), Vertragsrecht und ungerechtfertigter Bereicherung (§ 812 BGB) in Betracht. Die Verjährung beträgt in der Regel drei Jahre, bei Betrug oft deutlich länger. Act Here verhandelt nicht nur – wir bereiten Fälle so vor, dass sie vor Gericht Bestand haben."),
                ("h3", "4. Gemeinsames Vorgehen mit weiteren Geschädigten"),
                ("p", "Bei Plattformen mit vielen Opfern ändert ein gebündeltes Vorgehen die Ökonomie: geteilte Ermittlungskosten, gemeinsame Beweislage und deutlich mehr Druck auf Banken, Zahlungsdienstleister und Behörden."),
            ]),
            ("Erkennungsmerkmale", "Anlagebetrug erkennen: Die sieben Warnsignale", [
                ("ul", [
                    "Unaufgeforderte Kontaktaufnahme – per Telefon, WhatsApp, Telegram, E-Mail oder Werbeanzeige mit Prominenten.",
                    "Garantierte hohe Renditen ohne Verlustrisiko („10–20 % pro Monat, sicher“).",
                    "Zeitdruck: „Nur heute“, „letzte Plätze“, „sofort einzahlen, sonst verfällt der Bonus“.",
                    "Kleine Test-Auszahlungen am Anfang, um Vertrauen aufzubauen – danach blockieren größere Auszahlungen.",
                    "Immer neue Bedingungen und Begründungen, sobald Sie eine Auszahlung beantragen.",
                    "Keine oder gefälschte Regulierung: Lizenznummern, die auf keinem offiziellen Register (BaFin, FCA, CySEC) existieren oder einer anderen Firma gehören.",
                    "Zahlung nur in Kryptowährung oder auf ausländische Konten wechselnder Empfänger.",
                ]),
                ("p", "Prüfen Sie jeden Anbieter vor der Einzahlung im <a href=\"https://www.bafin.de\" target=\"_blank\" rel=\"noopener\">BaFin-Unternehmensregister</a> und in der BaFin-Warnliste. Fehlt der Eintrag oder steht die Firma auf der Warnliste, ist der Fall klar."),
            ]),
        ],
        "faqs": [
            ("Kann ich mein Geld nach Anlagebetrug zurückbekommen?", "Teilweise ja. Die besten Chancen haben Kartenzahlungen und Banküberweisungen innerhalb der Rückbuchungsfristen (bei Kreditkarten ca. 120 Tage) sowie Krypto-Zahlungen, die forensisch bis zu einer regulierten Börse verfolgt werden können. Kein seriöser Berater garantiert die Rückzahlung – wir sagen Ihnen nach der kostenlosen Ersteinschätzung, was in Ihrem Fall realistisch ist."),
            ("Anlagebetrug: was tun als Erstes?", "Keine weiteren Zahlungen leisten, alle Beweise sichern (Screenshots, Chats, Belege, Wallet-Adressen), sofort die eigene Bank kontaktieren und den Fall prüfen lassen. Die Rückbuchungsfristen laufen ab dem Tag der Zahlung – jede Woche Verzögerung schließt Optionen."),
            ("Wo kann ich Anlagebetrug melden bzw. anzeigen?", "Strafanzeige ist bei jeder Polizeidienststelle und online über die Onlinewache Ihres Bundeslandes möglich. Zusätzlich sollten Sie den Fall der BaFin melden, wenn sich die Plattform als Finanzdienstleister ausgegeben hat, und Ihre Bank informieren. Für die Rückholung des Geldes ist jedoch der zivilrechtliche Weg entscheidend."),
            ("Was bringt eine Strafanzeige bei Anlagebetrug?", "Sie dokumentiert den Fall und kann die Täter strafrechtlich verfolgen – Ihr Geld bekommen Sie dadurch aber meist nicht zurück. Die Staatsanwaltschaft verfolgt Straftäter, nicht Ihre Rückzahlung. Für die Rückholung brauchen Sie Rückbuchung, Tracing und zivilrechtliche Ansprüche."),
            ("Wie lange dauert es, Geld nach Anlagebetrug zurückzuholen?", "Rückbuchungen über die Bank: Tage bis wenige Wochen. Krypto-Tracing bis zur Beweisakte: mehrere Wochen. Zivilrechtliche Durchsetzung: Monate, je nach Erreichbarkeit der Gegenseite. Entscheidend ist der frühe Start – Spuren verwischen und Fristen laufen."),
            ("Verjähren meine Ansprüche?", "Zivilrechtliche Ansprüche verjähren meist in drei Jahren (ab Kenntnis des Betrugs), bei vorsätzlichem Betrug können längere Fristen gelten. Bankfristen sind viel kürzer: Chargeback ca. 120 Tage, Überweisungsrückruf nur wenige Tage. Deshalb gilt: sofort handeln, Verjährung später prüfen."),
            ("Lohnt sich ein Anwalt bei Anlagebetrug?", "Bei vier- bis fünfstelligen Schäden fast immer. Die Ersteinschätzung bei Act Here ist kostenlos; wir sagen Ihnen offen, ob sich Rückbuchung, Tracing oder eine Klage in Ihrem Fall wirtschaftlich lohnt – und wenn nicht, sagen wir das auch."),
        ],
    },
    {
        "slug": "trading-betrug",
        "title": "Trading Betrug: Erkennen, melden & Geld zurück (2026) | Act Here",
        "description": "Trading Betrug erkennen: Fake-Broker, manipulierte Plattformen, blockierte Auszahlungen. Was tun, wo melden und wie Sie Ihr Geld zurückholen. Kostenlose Ersteinschätzung.",
        "keywords": "trading betrug, trading betrug was tun, trading betrug melden, trading betrug anwalt, trading betrug geld zurück, online trading betrug, trading betrugsmasche, fake broker erkennen, trading plattform betrug, cfd betrug, forex betrug",
        "badge": "Trading-Betrug · Aktualisiert November 2026",
        "h1": "Trading Betrug: So erkennen Sie ihn – und so handeln Sie richtig",
        "lead": "Die Plattform zeigte steigende Kurse und satte Gewinne – doch als Sie auszahlen wollten, begannen die Probleme: neue Bedingungen, endlose Verifizierung, Funkstille. Trading-Betrug über gefälschte Broker und manipulierte Plattformen ist eine der größten Betrugsmaschen Europas. Hier erfahren Sie, wie Sie ihn erkennen, wo Sie ihn melden und welche Wege Ihr Geld tatsächlich zurückholen können.",
        "sections": [
            ("Das Schema", "Wie Trading-Betrug funktioniert: Das Drehbuch der Täter", [
                ("p", "Fast jeder Trading-Betrug folgt demselben Drehbuch: Werbung oder ein Anruf mit einem „Geheimtipp“, eine professionell wirkende Plattform, ein persönlicher „Kontomanager“, kleine Anfangsgewinne – und dann die Sperrung der Auszahlung, sobald größere Beträge im Spiel sind. Die angezeigten Gewinne existieren nur auf dem Bildschirm: Die Plattform ist keine echte Handelsumgebung, sondern eine Kulisse, deren Zahlen der Betreiber frei bearbeiten kann."),
                ("ul", [
                    "Kontaktaufnahme: Werbeanzeige mit Promis, Cold Call, WhatsApp- oder Telegram-Nachricht – oft beginnt es mit einer „Verwechslung“.",
                    "Vertrauensphase: Ein freundlicher Kontomanager, schnelle kleine Gewinne, oft eine funktionierende erste Test-Auszahlung.",
                    "Eskalation: Druck zu höheren Einzahlungen – Boni, „VIP-Status“, angebliche Sonderkonditionen.",
                    "Blockade: Bei der Auszahlung folgen Verifizierungsschleifen, wechselnde Begründungen und schließlich Funkstille oder Kontosperrung.",
                ]),
            ]),
            ("Warnsignale", "Trading-Betrug erkennen: Der 60-Sekunden-Check", [
                ("ul", [
                    "Kein Eintrag im BaFin-Unternehmensregister oder in der Warnliste der BaFin / FCA / CySEC.",
                    "Lizenznummer gehört einer anderen, echten Firma (Clone-Firm) – Domain, Telefonnummer oder E-Mail weichen vom Registereintrag ab.",
                    "Einzahlung nur per Krypto oder auf wechselnde ausländische Konten möglich.",
                    "Garantierte Gewinne, „kein Risiko“, Renditen von 10 % und mehr pro Monat.",
                    "Wechselnde Begründungen und neue Bedingungen, sobald Sie auszahlen wollen.",
                    "Der „Berater“ ruft genau dann an, wenn Sie auszahlen wollen – und versucht, Sie davon abzubringen.",
                ]),
            ]),
            ("Handlungsoptionen", "Trading Betrug: Was tun, wenn das Geld festhängt", [
                ("h3", "Sofort: Bank und Beweise"),
                ("p", "Kontaktieren Sie sofort Ihre Bank: Kreditkartenzahlungen können per Chargeback reklamiert werden (Frist ca. 120 Tage), SEPA-Überweisungen lassen sich in den ersten Tagen teilweise zurückrufen. Sichern Sie parallel alles: Kontoauszüge, Screenshots der Plattform, Chats mit dem Kontomanager, E-Mails, Wallet-Adressen, die exakten URLs."),
                ("h3", "Melden: Polizei, BaFin und Verbraucherzentrale"),
                ("p", "Erstatten Sie Strafanzeige (jede Dienststelle oder Onlinewache Ihres Bundeslandes) und melden Sie die Plattform der BaFin – Ihre Meldung kann eine offizielle Warnung auslösen und andere schützen. Wichtig zu wissen: Die Anzeige verfolgt die Täter, nicht Ihre Rückzahlung."),
                ("h3", "Geld zurück: Rückbuchung, Tracing, Zivilklage"),
                ("p", "Für die Rückholung gibt es drei realistische Wege: Chargeback/Rückbuchung über die Bank, Blockchain-Tracing bei Krypto-Zahlungen bis zur Auszahlungsbörse und zivilrechtliche Ansprüche aus Betrug und Vertrag. Act Here kombiniert alle drei und bereitet die Beweislage gerichtsfest auf – wir verhandeln nicht nur, wir sind bereit zu klagen."),
            ]),
        ],
        "faqs": [
            ("Trading Betrug: was tun, wenn die Auszahlung blockiert wird?", "Keine weiteren Zahlungen leisten. Alle Beweise sichern, sofort die Bank wegen Rückbuchung kontaktieren (Chargeback-Frist ca. 120 Tage), Strafanzeige erstatten und den Fall kostenlos einschätzen lassen. Je schneller Sie handeln, desto mehr Wege stehen offen."),
            ("Wo kann ich einen Trading-Betrug melden?", "Strafanzeige: bei jeder Polizeidienststelle oder online über die Onlinewache Ihres Bundeslandes. Zusätzlich: Meldung an die BaFin (wenn die Plattform Finanzdienstleistungen anbot) und an Ihre Bank. Die Meldung schützt andere – für Ihr Geld ist der zivilrechtliche Weg entscheidend."),
            ("Woran erkenne ich einen Fake-Broker?", "Am fehlenden BaFin-Registereintrag, an Lizenznummern, die zu anderen Firmen gehören, an Krypto-Einzahlungen als einzigem Zahlungsweg, an garantierten Renditen und an Geldforderungen vor der Auszahlung. Prüfen Sie jeden Anbieter im offiziellen Register – nicht über die Website des Brokers selbst."),
            ("Kann ich Geld von einer betrügerischen Trading-Plattform zurückholen?", "Teilweise. Kreditkartenzahlungen: Chargeback innerhalb von ca. 120 Tagen. Banküberweisungen: Rückruf in den ersten Tagen. Krypto-Zahlungen: forensisches Tracing bis zur Auszahlungsbörse. Danach: zivilrechtliche Ansprüche. Eine Garantie gibt es nicht – wohl aber klare realistische Einschätzungen."),
            ("Lohnt sich ein Anwalt bei Trading-Betrug?", "Bei Schäden ab etwa 1.000 Euro ist eine Einschätzung sinnvoll, schon wegen der kurzen Bankfristen. Bei größeren Beträgen ist anwaltliche Vertretung meist wirtschaftlich geboten. Die Ersteinschätzung bei Act Here ist kostenlos und unverbindlich."),
        ],
    },
    {
        "slug": "online-betrug-geld-zurueck",
        "title": "Online Betrug: Geld zurück – alle Wege nach Internet-Betrug (2026) | Act Here",
        "description": "Online Betrug: Geld zurückfordern nach Investment-, Krypto- oder Shopping-Betrug. Rückbuchung, Chargeback, Anzeige und zivilrechtliche Wege – Schritt für Schritt erklärt.",
        "keywords": "online betrug geld zurück, online betrug geld zurückfordern, internet betrug geld zurück, online betrug anzeige, online betrug was tun, online banking betrug geld zurück, cyberbetrug geld zurück, betrug im internet melden, online betrug hilfe",
        "badge": "Online-Betrug · Aktualisiert November 2026",
        "h1": "Online Betrug: Geld zurück – Ihre Wege Schritt für Schritt",
        "lead": "Ob Investmentplattform, Fake-Shop, Krypto-Scam oder Identitätsdiebstahl: Wer online betrogen wurde, steht vor denselben Fragen – bekomme ich mein Geld zurück, wo melde ich das, und was muss ich zuerst tun? Die Antwort hängt vor allem von zwei Dingen ab: wie Sie gezahlt haben und wie schnell Sie jetzt handeln. Dieser Leitfaden führt Sie durch alle realistischen Wege.",
        "sections": [
            ("Erste Hilfe", "Online-Betrug: Die ersten vier Schritte", [
                ("ul", [
                    "Zahlungen stoppen: Keine weiteren Überweisungen an die Gegenseite – und falls das Konto angegriffen wurde: Bankkarten und Online-Banking sofort sperren lassen.",
                    "Beweise sichern: Screenshots von Plattform, Bestellungen, Chats und Kontoständen; Überweisungsbelege, Transaktions-IDs, E-Mails mit vollständigem Header, die exakten URLs.",
                    "Bank kontaktieren: Überweisungsrückruf (nur in den ersten Tagen), Kreditkarten-Chargeback (ca. 120 Tage), Lastschriftwiderruf (8 Wochen bei autorisierten, 13 Monate bei nicht autorisierten Lastschriften).",
                    "Anzeige erstatten: Online über die Onlinewache Ihres Bundeslandes oder bei jeder Polizeidienststelle – kostenlos und in wenigen Minuten erledigt.",
                ]),
            ]),
            ("Nach Zahlungsart", "Geld zurück je nachdem, wie Sie gezahlt haben", [
                ("h3", "Kreditkarte: Chargeback"),
                ("p", "Das stärkste Instrument: „Leistung nicht erbracht / nicht wie beschrieben“ oder Betrug. Frist meist 120 Tage ab Belastung, bei manchen Anbietern bis zu 540 Tage. Reichen Sie Belege und die Kommunikation mit dem Händler gleich mit ein – unvollständige Anträge scheitern sonst an Formalien."),
                ("h3", "SEPA-Überweisung: Rückruf und Empfängerbank"),
                ("p", "Eine abgeschickte Überweisung kann die eigene Bank nur in den ersten Tagen zurückrufen. Danach bleibt der Weg über die Empfängerbank: Mit einer Betrugsanzeige und Belegen kann diese den Empfänger zur Rücküberweisung auffordern und das Konto intern markieren. Bei Online-Banking-Betrug durch Dritte (Phishing, Kontohack) gelten die Regeln der §§ 675u ff. BGB: Die Bank trägt grundsätzlich das Risiko nicht autorisierter Vorgänge."),
                ("h3", "Kryptowährung: Tracing statt Rückbuchung"),
                ("p", "Krypto-Transfers sind technisch unumkehrbar – aber nicht unsichtbar. Unsere Blockchainforensik verfolgt Bitcoin, USDT und Ethereum bis zu der Börse, an der die Täter in Fiat auszahlen. Dort setzen Sperrung und Auskunftsersuchen an. Die Spur kühlt mit jeder Woche ab – Zeit ist der entscheidende Faktor."),
                ("h3", "PayPal, Klarna & Co."),
                ("p", "PayPal-Käuferschutz (180 Tage), Klarna-Käuferschutz und ähnliche Programme funktionieren bei Warenkäufen gut, bei „Friends & Family“-Zahlungen und Geldtransfers dagegen praktisch nicht. Prüfen Sie, ob die Zahlung als Warendienst oder als Freunde-Zahlung lief."),
            ]),
            ("Strafanzeige richtig stellen", "Online-Betrug anzeigen: so geht es", [
                ("p", "Die Onlinewache Ihres Bundeslandes führt Sie in etwa 15 Minuten durch die Anzeige. Halten Sie bereit: Ihre Personalien, den Ablauf in Stichpunkten, alle Zahlungsdaten (IBAN, Empfänger, Beträge, Daten), die URLs und Benutzernamen der Täter sowie die gesicherten Beweise als Dateien. Sie erhalten ein Aktenzeichen – wichtig für Bank, Versicherung und spätere zivilrechtliche Schritte."),
                ("p", "Bedenken Sie: Die Strafanzeige verfolgt die Täter. Für Ihr Geld brauchen Sie parallel den zivilrechtlichen Weg – Schadensersatzansprüche aus § 823 Abs. 2 BGB i.V.m. § 263 StGB, Rückforderung und gegebenenfalls Klage."),
            ]),
            ("Professionelle Hilfe", "Wann sich Act Here einschaltet", [
                ("p", "Bei kleinen Beträgen und klarer Zahlungsspur reichen Bank und Anzeige oft aus. Sobald es um vier- bis fünfstellige Schäden geht, Krypto im Spiel ist oder die Bank die Rückbuchung abgelehnt hat, ändert sich die Lage: Dann entscheiden Beweisqualität und Geschwindigkeit. Act Here führt Blockchain-Tracing durch, koordiniert Rückbuchungen, baut die gerichtsfeste Beweisakte und setzt Ihre Ansprüche durch – notfalls vor Gericht. Die Ersteinschätzung ist kostenlos."),
            ]),
        ],
        "faqs": [
            ("Kann ich Geld nach Online-Betrug zurückbekommen?", "In vielen Fällen zumindest teilweise. Entscheidend sind Zahlungsart und Geschwindigkeit: Kreditkarte (Chargeback, ca. 120 Tage), Lastschrift (8 Wochen Widerruf), Überweisung (Rückruf in den ersten Tagen), Krypto (forensisches Tracing). Je früher Sie handeln, desto mehr Wege stehen offen."),
            ("Online-Betrug: wo anzeigen?", "Bei jeder Polizeidienststelle oder bequem online über die Onlinewache Ihres Bundeslandes. Halten Sie Zahlungsdaten, URLs und Beweise bereit; Sie erhalten ein Aktenzeichen für Bank und weitere Schritte. Zusätzlich empfiehlt sich die Meldung an Ihre Bank und – bei Finanzplattformen – an die BaFin."),
            ("Die Bank lehnt meine Rückbuchung ab – was nun?", "Eine Ablehnung der Bank ist nicht das Ende: Sie betrifft nur den bankinternen Weg. Zivilrechtliche Ansprüche gegen die Empfänger bleiben bestehen, ebenso die forensische Verfolgung der Zahlungsströme. Gerade nach abgelehnten Chargebacks lohnt eine professionelle Prüfung der Ablehnungsgründe – sie sind nicht immer zutreffend."),
            ("Gilt das auch bei Phishing und Online-Banking-Betrug?", "Ja, sogar mit guter Rechtslage: Bei nicht autorisierten Zahlungsvorgängen trägt nach §§ 675u ff. BGB grundsätzlich die Bank das Risiko – Sie müssen sich allenfalls grobe Fahrlässigkeit vorhalten lassen. Melden Sie den Vorgang sofort, lassen Sie die Konten sperren und verlangen Sie schriftlich die Erstattung."),
            ("Wie lange habe ich Zeit, den Betrug zu melden?", "Für die Strafanzeige gibt es keine Frist (Verjährung des Betrugs: meist 5 Jahre). Kritisch sind die Bankfristen: Chargeback ca. 120 Tage, Lastschriftwiderruf 8 Wochen, Überweisungsrückruf wenige Tage. Zivilansprüche verjähren in der Regel nach 3 Jahren ab Kenntnis."),
            ("Was kostet die Hilfe durch Act Here?", "Die Ersteinschätzung Ihres Falls ist kostenlos und unverbindlich. Sie dient dazu, Ihren Anspruch zu prüfen: was passiert ist, welche Beweise vorliegen und welche Wege realistisch sind. Alles Weitere wird vor Beginn schriftlich mit Ihnen vereinbart."),
        ],
    },
]

def esc(s):
    return htmlmod.escape(s, quote=True)

def render_section(kicker, h2, blocks):
    out = ['<section style="padding:2.5rem 0;border-bottom:1px solid var(--line)"><div class="article-body" style="max-width:760px;margin:0 auto">']
    out.append(f'<span style="display:block;font-size:.72rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:.6rem">{esc(kicker)}</span>')
    out.append(f'<h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">{esc(h2)}</h2>')
    for kind, content in blocks:
        if kind == "p":
            out.append(f"<p>{content}</p>")
        elif kind == "h3":
            out.append(f'<h3 style="font-size:1.05rem;color:var(--sage-dark);margin:1.6rem 0 .6rem;font-weight:600">{esc(content)}</h3>')
        elif kind == "ul":
            out.append('<ul style="list-style:none;margin:1rem 0 1.5rem;padding:0">' + "".join(
                f'<li style="padding:.5rem 0;display:flex;gap:.7rem;color:var(--text-2);font-size:.95rem;line-height:1.7"><span style="color:var(--sage-dark);font-weight:700;flex-shrink:0">&#10003;</span><span>{item}</span></li>'
                for item in content
            ) + "</ul>")
    out.append("</div></section>")
    return "\n".join(out)

def render_faq(faqs):
    items = "\n".join(
        f'<div style="border-bottom:1px solid var(--line);padding:1.2rem 0"><h3 style="font-size:1rem;color:var(--navy);margin-bottom:.5rem;font-weight:600">{esc(q)}</h3><p style="color:var(--text-2);font-size:.93rem;line-height:1.75;margin:0">{a}</p></div>'
        for q, a in faqs
    )
    return ('<section style="padding:2.5rem 0"><div class="article-body" style="max-width:760px;margin:0 auto">'
            '<span style="display:block;font-size:.72rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:.6rem">FAQ</span>'
            '<h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">Häufige Fragen</h2>'
            f'{items}</div></section>')

def build_schema(p):
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": f"https://act-here.uk/de/{p['slug']}.html#webpage",
             "url": f"https://act-here.uk/de/{p['slug']}.html", "name": p["title"],
             "description": p["description"],
             "isPartOf": {"@type": "WebSite", "name": "Act Here", "url": "https://act-here.uk/"},
             "inLanguage": "de"},
            {"@type": "Article", "headline": p["title"], "description": p["description"],
             "author": {"@type": "Organization", "name": "Act Here"},
             "publisher": {"@type": "Organization", "name": "Act Here", "url": "https://act-here.uk/"},
             "dateModified": "2026-11-17", "inLanguage": "de", "keywords": p["keywords"]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faqs"]]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://act-here.uk/"},
                {"@type": "ListItem", "position": 2, "name": "Ratgeber", "item": "https://act-here.uk/de/"},
                {"@type": "ListItem", "position": 3, "name": p["h1"].split(":")[0], "item": f"https://act-here.uk/de/{p['slug']}.html"}]},
        ],
    }

DE_INTERNAL_LINKS = (
    '<section style="padding:2rem 0;background:var(--off-white)"><div class="article-body" style="max-width:760px;margin:0 auto">'
    '<p style="color:var(--text-muted);font-size:.95rem">Verwandte Ratgeber: '
    '<a href="anlagebetrug.html" style="color:var(--sage-dark)">Anlagebetrug</a> &middot; '
    '<a href="krypto-betrug.html" style="color:var(--sage-dark)">Krypto-Betrug</a> &middot; '
    '<a href="broker-betrug.html" style="color:var(--sage-dark)">Broker-Betrug</a> &middot; '
    '<a href="geld-zurueck-broker.html" style="color:var(--sage-dark)">Geld zurück vom Broker</a> &middot; '
    '<a href="betrug-melden.html" style="color:var(--sage-dark)">Betrug melden</a> &middot; '
    '<a href="broker-auszahlung-problem.html" style="color:var(--sage-dark)">Broker-Auszahlungsproblem</a>'
    '</p></div></section>'
)

def render(p):
    sections_html = "\n".join(render_section(*s) for s in p["sections"])
    faq_html = render_faq(p["faqs"])
    schema_json = json.dumps(build_schema(p), ensure_ascii=False, indent=1)
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{esc(p['title'])}</title>
 <meta name="description" content="{esc(p['description'])}">
 <meta name="keywords" content="{esc(p['keywords'])}">
 <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
 <link rel="canonical" href="https://act-here.uk/de/{p['slug']}.html">
 <link rel="alternate" hreflang="de" href="https://act-here.uk/de/{p['slug']}.html">
 <link rel="alternate" hreflang="x-default" href="https://act-here.uk/de/{p['slug']}.html">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{esc(p['title'])}">
 <meta property="og:description" content="{esc(p['description'])}">
 <meta property="og:url" content="https://act-here.uk/de/{p['slug']}.html">
 <meta property="og:locale" content="de_DE">
 <script type="application/ld+json">
{schema_json}
 </script>
 <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<div id="nav-placeholder"></div>
<div class="breadcrumb"><a href="../index.html">Home</a><span>&#8250;</span><a href="index.html">Ratgeber</a><span>&#8250;</span> {esc(p['h1'].split(':')[0])}</div>
<div class="page-hero">
 <div class="hero-badge">{esc(p['badge'])}</div>
 <h1>{esc(p['h1'])}</h1>
 <p>{esc(p['lead'])}</p>
</div>
{sections_html}
{DE_INTERNAL_LINKS}
{faq_html}
<section style="padding:3rem 0;background:var(--navy);color:#fff;text-align:center">
 <div style="max-width:640px;margin:0 auto;padding:0 5%">
 <h2 style="font-family:var(--font-serif);color:#fff;font-size:1.9rem;margin-bottom:.8rem">Geld verloren? Wir pr&uuml;fen Ihren Fall.</h2>
 <p style="color:rgba(255,255,255,.75);margin-bottom:1.5rem">Kostenlose, vertrauliche Ersteinsch&auml;tzung durch unser Litigation-Team. Wir verhandeln nicht nur &ndash; wir sind bereit zu klagen.</p>
 <a href="../pages/contact.html" class="btn-primary">Kostenlose Ersteinsch&auml;tzung</a>
 </div>
</section>
<div id="footer-placeholder"></div>
<script src="../js/config.js"></script>
<script src="../js/layout.js"></script>
</body>
</html>
"""

def main():
    for p in PAGES:
        path = os.path.join(DE, p["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(p))
        print("wrote", path)

if __name__ == "__main__":
    main()
