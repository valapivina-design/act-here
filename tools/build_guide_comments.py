#!/usr/bin/env python3
"""Build topic-fitting comments for EN/DE/IT/ES/AR guide pages.

Writes js/guide_comments.js keyed by path stem (e.g. guides/prop-trading-scam,
de/broker-betrug). No broker names. Free-consultation support replies only.
ASCII punctuation only in visible copy (no em/en dashes or smart quotes).
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "js" / "guide_comments.js"

CHARS_BANNED = "\u2014\u2013\u201e\u201c\u201d\u2018\u2019\u00ab\u00bb"
WORDS_BANNED = re.compile(
    r"\bunlock\b|\brelease\b|\btax[- ]?clearance\b|pay[- ]to[- ]withdraw|"
    r"upfront fee|advance fee|desbloque|\bimpuestos?\b|\btasas?\b|\bhonorarios?\b|"
    r"por adelantado|anticip|pago previo|sblocc|\btass[ae]\b|svincol|acconto|caparra|"
    r"Freigabegeb|Auszahlungsgeb|Vorauszahl",
    re.I,
)

FIRST = [
    "Ava", "Noah", "Mia", "Liam", "Elena", "Omar", "Priya", "Hans", "Clara",
    "Luis", "Ana", "Giulia", "Sofia", "Marcus", "Amira", "Daniel", "Caroline",
    "Thomas", "Isabella", "Lucas", "Hannah", "Jonas", "Yara", "Felix", "Nina",
    "Mateo", "Ines", "Chloe", "Erik", "Lara", "Hugo", "Noor", "Pavel", "Irina",
    "Diego", "Camille", "Owen", "Freya", "Leila", "Andre", "Marta", "Viktor",
    "Sara", "Ian", "Helena", "Bruno", "Aisha", "Nils", "Vera", "Rafael", "Zoe",
    "Petra", "Callum", "Amina", "Johan", "Lucia", "Emilia", "Sean", "Nadia",
    "Marco", "Olivia", "Ellen", "Malik", "Kira", "Hassan",
]
LAST = [
    "Hayes", "Nair", "Brennan", "Whitmore", "Hassan", "Mendoza", "Okonkwo",
    "Popescu", "Berg", "Rossi", "Chen", "Muller", "Schmidt", "Garcia", "Costa",
    "Bianchi", "Novak", "Silva", "Kowalski", "Dubois", "Andersen", "Petrov",
    "Nguyen", "Okafor", "Santos", "Keller", "Fernandez", "Hughes", "Nowak",
    "Baptiste", "Olsen", "Castillo", "Murray", "Vogel", "Almeida", "Park",
    "Sullivan", "Weber", "Diaz", "Fischer", "Romano", "Singh", "Bailey", "Cruz",
]
COUNTRIES = {
    "en": ["United Kingdom", "Ireland", "Australia", "Canada", "Singapore", "United Arab Emirates", "South Africa", "New Zealand"],
    "de": ["Germany", "Austria", "Switzerland", "Germany", "Austria"],
    "es": ["Spain", "Mexico", "Chile", "Colombia", "Spain", "Mexico"],
    "it": ["Italy", "Italy", "Switzerland", "Italy"],
    "ar": ["United Arab Emirates", "Saudi Arabia", "Kuwait", "Egypt", "Qatar", "Bahrain"],
}


def stable_int(s: str, mod: int) -> int:
    if mod <= 0:
        return 0
    return int(hashlib.sha256(s.encode("utf-8")).hexdigest()[:8], 16) % mod


def pick(seq, key: str):
    return seq[stable_int(key, len(seq))]


def person(key: str, lang: str) -> dict:
    fn = pick(FIRST, f"{key}:fn")
    ln = pick(LAST, f"{key}:ln")
    # Avoid identical full names colliding across nearby guides
    if stable_int(key, 5) == 0:
        ln = pick(LAST, f"{key}:ln2")
    country = pick(COUNTRIES.get(lang) or COUNTRIES["en"], f"{key}:c")
    return {
        "name": f"{fn} {ln}",
        "initials": f"{fn[0]}{ln[0]}".upper(),
        "country": country,
    }


def d(key: str, today: date, days_ago_lo: int, days_ago_hi: int) -> str:
    span = max(1, days_ago_hi - days_ago_lo)
    ago = days_ago_lo + stable_int(key, span)
    return (today - timedelta(days=ago)).isoformat()


# Support replies: free consultation + validate claim + feasibility + level of proof
SUPPORT = {
    "en": [
        "Consultation is free. We first validate the claim, then assess prospects and feasibility based on the level of proof you can share.",
        "Book a free consultation. We need to validate your claim and understand the prospects; feasibility depends on the level of proof.",
        "Happy to review this confidentially. The consultation is free: we validate the claim and map realistic next steps from your evidence.",
    ],
    "de": [
        "Die Erstberatung ist kostenlos. Zuerst validieren wir die Forderung und prufen Aussichten und Machbarkeit anhand Ihrer Beweise.",
        "Vereinbaren Sie eine kostenlose Beratung. Wir mussen den Anspruch validieren; Machbarkeit hangt vom Beweisniveau ab.",
        "Gerne prufen wir vertraulich. Die Beratung ist kostenlos: Validierung des Falls und realistische nachste Schritte aus Ihren Unterlagen.",
    ],
    "es": [
        "La consulta es gratuita. Primero validamos su reclamacion y evaluamos perspectivas y viabilidad segun el nivel de prueba.",
        "Reserve una consulta gratuita. Tenemos que validar la reclamacion; la viabilidad depende del nivel de prueba que aporte.",
        "Podemos revisarlo en confidencialidad. La consulta es gratuita: validamos el caso y vemos opciones realistas con sus pruebas.",
    ],
    "it": [
        "La consulenza e gratuita. Prima validiamo la richiesta e valutiamo prospettive e fattibilita in base alle prove.",
        "Prenoti una consulenza gratuita. Dobbiamo validare il caso; la fattibilita dipende dal livello di prova.",
        "Possiamo esaminarlo in confidenza. La consulenza e gratuita: validiamo il caso e indichiamo passi realistici dalle prove.",
    ],
    "ar": [
        "الاستشارة مجانية. أولا نتحقق من صحة المطالبة ثم نقيّم الآفاق والجدوى حسب مستوى الإثبات.",
        "احجز استشارة مجانية. نحتاج التحقق من المطالبة؛ الجدوى تعتمد على مستوى الإثبات.",
        "يمكن مراجعة الحالة بسرية. الاستشارة مجانية: نتحقق من المطالبة ونحدد خطوات واقعية من أدلتك.",
    ],
}

CTA = {
    "en": "Book a free consultation →",
    "de": "Kostenlose Beratung buchen →",
    "es": "Reserve una consulta gratuita →",
    "it": "Prenota una consulenza gratuita →",
    "ar": "احجز استشارة مجانية →",
}


# Theme comment pools: (title, text, ask_help, important)
# No broker names. No fee/unlock/tax advice.
THEMES: dict[str, dict[str, list[tuple[str, str, bool, bool]]]] = {
    "withdrawal": {
        "en": [
            ("Payout stalled after weeks of checks", "I asked to withdraw a large balance and support only sent new document lists. The account still shows funds. Is a free consultation worth it before I chase the bank alone?", True, True),
            ("Test withdrawal worked once, then nothing", "A small test payout arrived. The real request sits pending with changing excuses. I saved chats and bank refs. Who can review whether counsel is realistic?", True, True),
            ("Support keeps restarting verification", "Every time I send papers they say something else is missing. Balance is frozen on-screen. Looking for a quiet next-step review.", True, False),
            ("Card issuer asked for a clearer timeline", "My bank wants dates and screenshots for a dispute. I have most of it but need help structuring the file. Any guidance?", True, False),
        ],
        "de": [
            ("Auszahlung seit Wochen in Prufung", "Ich habe eine groessere Auszahlung beantragt. Support schickt nur neue Dokumentenlisten. Guthaben steht noch da. Lohnt eine kostenlose Beratung vor dem Alleingang bei der Bank?", True, True),
            ("Testauszahlung klappte einmal, dann nichts", "Ein kleiner Test ging durch. Der echte Antrag bleibt offen mit wechselnden Begrundungen. Chats und Uberweisungsbelege habe ich. Wer pruft still, ob Beratung sinnvoll ist?", True, True),
            ("Verifizierung startet immer neu", "Jedes Dokument wird als unvollstandig abgetan. Konto zeigt Guthaben, Auszahlung nicht. Brauche eine ruhige Erstprufung.", True, False),
            ("Bank will klaren Zeitablauf", "Fur die Streitigkeit verlangt die Bank Daten und Screenshots. Die meisten habe ich. Kann jemand helfen, die Akte zu sortieren?", True, False),
        ],
        "es": [
            ("Retiro parado tras semanas de comprobaciones", "Pedi retirar un saldo importante y el soporte solo envia nuevas listas de documentos. La cuenta sigue mostrando fondos. Vale una consulta gratuita antes de ir solo al banco?", True, True),
            ("El retiro de prueba salio una vez y luego nada", "Un pago pequeno llego. La solicitud real sigue pendiente con excusas distintas. Guarde chats y referencias. Quien puede revisar si conviene asesoramiento?", True, True),
            ("La verificacion se reinicia cada vez", "Cada vez que envio papeles piden otra cosa. El saldo aparece congelado en pantalla. Busco una revision discreta del siguiente paso.", True, False),
            ("El banco pide una cronologia mas clara", "Mi entidad quiere fechas y capturas para la reclamacion. Tengo casi todo. Alguien puede orientar como ordenar el expediente?", True, False),
        ],
        "it": [
            ("Prelievo fermo dopo settimane di controlli", "Ho chiesto di prelevare un saldo importante e il supporto invia solo nuove liste di documenti. Il conto mostra ancora i fondi. Vale una consulenza gratuita prima di agire da solo con la banca?", True, True),
            ("Il prelievo di prova e andato, poi niente", "Un piccolo test e arrivato. La richiesta reale resta in sospeso con scuse diverse. Ho chat e riferimenti. Chi puo valutare se ha senso un esame legale?", True, True),
            ("La verifica riparte ogni volta", "Ogni documento viene detto incompleto. Il saldo e a schermo ma non esce. Cerco una prima lettura riservata.", True, False),
            ("La banca vuole una cronologia piu chiara", "Per la contestazione chiedono date e screenshot. Ne ho quasi tutti. Qualcuno puo aiutare a ordinare il fascicolo?", True, False),
        ],
        "ar": [('السحب متوقف منذ أسابيع', 'طلبت سحب رصيد كبير والدعم يرسل قوائم مستندات جديدة فقط. الرصيد يظهر في الحساب. هل تستحق الاستشارة المجانية قبل مراجعة البنك وحدي؟', True, True), ('سحب تجريبي نجح ثم لا شيء', 'خرج مبلغ صغير مرة. الطلب الحقيقي معلق بأعذار متغيرة. حفظت المحادثات والمراجع. من يقيّم إن كان المسار القانوني واقعيا؟', True, True), ('التحقق يعاد من الصفر', 'كل مستند يُرفض ويُطلب غيره. الرصيد ظاهر والسحب لا يتم. أبحث عن مراجعة هادئة للخطوة التالية.', True, False), ('البنك يطلب جدولا أوضح', 'للاعتراض يريد البنك تواريخ ولقطات. لدي معظمها. هل يمكن توجيه ترتيب الملف؟', True, False)],
    },
    "recovery": {
        "en": [
            ("Need counsel, not a recovery pitch", "I lost a material sum to an online trading pitch. I want litigation counsel to validate the claim and say what is feasible from my proof, not a hard sell.", True, True),
            ("How do you assess prospects?", "Before I instruct anyone: is the consultation free, and do you first check whether the evidence supports a realistic path?", True, False),
            ("Screenshots and bank trails ready", "I have chats, payment refs, and domain notes. Can Act Here review quietly whether civil steps make sense?", True, True),
            ("Police report filed, money still gone", "I reported it. The criminal path is running. I need civil options explained against my level of proof.", True, False),
        ],
        "de": [
            ("Brauche Anwalt, keine Recovery-Versprechen", "Ich habe einen erheblichen Betrag bei einem Online-Trading-Angebot verloren. Ich will eine anwaltliche Validierung und eine klare Aussage zu Machbarkeit anhand meiner Beweise.", True, True),
            ("Wie prufen Sie die Aussichten?", "Bevor ich jemanden beauftrage: Ist die Beratung kostenlos, und prufen Sie zuerst, ob die Beweise einen realistischen Weg tragen?", True, False),
            ("Screenshots und Bankspuren liegen bereit", "Chats, Zahlungsbelege und Domain-Notizen sind da. Kann Act Here still prufen, ob zivilrechtliche Schritte Sinn ergeben?", True, True),
            ("Anzeige erstattet, Geld weg", "Strafrechtlich lauft etwas. Ich brauche eine Erklarung der zivilen Optionen anhand meines Beweisstands.", True, False),
        ],
        "es": [
            ("Necesito abogados, no un discurso de recuperacion", "Perdi una suma importante en una oferta de trading online. Quiero que se valide la reclamacion y se diga que es viable con mis pruebas, sin presion comercial.", True, True),
            ("Como valoran las perspectivas?", "Antes de encargar nada: la consulta es gratuita y primero comprueban si las pruebas sostienen un camino realista?", True, False),
            ("Capturas y rastros bancarios listos", "Tengo chats, referencias de pago y notas del dominio. Puede Act Here revisar en privado si conviene via civil?", True, True),
            ("Denuncia presentada, el dinero sigue fuera", "Ya denuncie. Quiero opciones civiles explicadas segun mi nivel de prueba.", True, False),
        ],
        "it": [
            ("Cerco assistenza legale, non promesse di recovery", "Ho perso una somma rilevante in un'offerta di trading online. Voglio validare il caso e capire cosa e fattibile con le mie prove, senza pressione commerciale.", True, True),
            ("Come valutate le prospettive?", "Prima di incaricare qualcuno: la consulenza e gratuita e prima verificate se le prove sostengono un percorso realistico?", True, False),
            ("Screenshot e tracce bancarie pronti", "Ho chat, riferimenti di pagamento e note sul dominio. Act Here puo esaminare in privato se ha senso una via civile?", True, True),
            ("Denuncia fatta, soldi ancora fuori", "Il percorso penale e avviato. Mi servono le opzioni civili spiegate in base al livello di prova.", True, False),
        ],
        "ar": [('أحتاج محاميا لا وعود استرداد', 'خسرت مبلغا جوهريا في عرض تداول. أريد التحقق من المطالبة ومعرفة الجدوى من أدلتي دون ضغط تجاري.', True, True), ('كيف تقيّمون الآفاق؟', 'قبل أي توكيل: هل الاستشارة مجانية وهل تتحققون أولا إن كانت الأدلة تكفي لمسار واقعي؟', True, False), ('الأدلة جاهزة', 'محادثات وإيصالات وملاحظات النطاق جاهزة. هل يراجع Act Here بهدوء إن كان المسار المدني مناسبا؟', True, True), ('بلاغ قُدّم والمال لا يزال خارجا', 'المسار الجنائي بدأ. أحتاج شرح الخيارات المدنية حسب مستوى الإثبات.', True, False)],
    },
    "license": {
        "en": [
            ("Licence number on the site looks odd", "The footer shows a regulator number that does not match the name on the register. How should I document that before depositing more?", True, False),
            ("Clone site used a real firm's badge", "Screenshots of a licence badge that belongs to someone else. I already sent a small amount. Worth a free consult to validate next steps?", True, True),
            ("Register search came back empty", "I checked the official register under the exact trading name and domain. Nothing. Is that enough to pause and get advice?", True, False),
            ("Need a clean checklist for family", "Relatives almost funded the same pitch. Looking for a short licence-check process I can share without naming the site here.", True, False),
        ],
        "de": [
            ("Lizenznummer auf der Seite wirkt falsch", "Im Footer steht eine Registernummer, die nicht zum Namen im Register passt. Wie dokumentiere ich das, bevor ich nachzahle?", True, False),
            ("Klonseite nutzte das Siegel einer echten Firma", "Screenshots eines Lizenz-Badges, das einer anderen Firma gehort. Kleiner Betrag schon weg. Lohnt eine kostenlose Beratung zu den nachsten Schritten?", True, True),
            ("Register Suche ohne Treffer", "Offizielle Suche unter exaktem Handelsnamen und Domain: nichts. Reicht das, um zu stoppen und Rat einzuholen?", True, False),
            ("Kurze Prufliste fur die Familie", "Verwandte waren kurz vor einer Einzahlung. Brauche einen knappen Lizenz-Check, den ich teilen kann, ohne den Namen hier zu nennen.", True, False),
        ],
        "es": [
            ("El numero de licencia en el sitio no cuadra", "El pie muestra un numero de registro que no coincide con el nombre en el registro oficial. Como lo documento antes de ingresar mas?", True, False),
            ("Un clon uso la insignia de una firma real", "Capturas de una licencia que pertenece a otra entidad. Ya envie un importe pequeno. Vale una consulta gratuita sobre el siguiente paso?", True, True),
            ("La busqueda en el registro salio vacia", "Busque en el registro oficial con el nombre comercial y el dominio exactos. Nada. Basta para parar y pedir orientacion?", True, False),
            ("Lista corta para la familia", "Parientes casi financiaron la misma oferta. Busco un proceso breve de comprobacion de licencia sin nombrar el sitio aqui.", True, False),
        ],
        "it": [
            ("Il numero di licenza sul sito non torna", "Nel footer c'e un numero di registro che non corrisponde al nome ufficiale. Come lo documento prima di versare altro?", True, False),
            ("Un clone usava il badge di una societa reale", "Screenshot di una licenza che appartiene ad altri. Ho gia inviato un piccolo importo. Vale una consulenza gratuita sui prossimi passi?", True, True),
            ("Ricerca nel registro a vuoto", "Ho cercato nel registro ufficiale con nome commerciale e dominio esatti. Niente. Basta per fermarsi e chiedere consiglio?", True, False),
            ("Checklist breve per la famiglia", "Parenti stavano per versare sulla stessa proposta. Cerco un controllo licenza sintetico da condividere senza nominare il sito qui.", True, False),
        ],
        "ar": [('رقم الترخيص على الموقع غريب', 'التذييل يعرض رقما لا يطابق الاسم في السجل. كيف أوثّق ذلك قبل إيداع المزيد؟', True, False), ('موقع مقلد استخدم شارة شركة حقيقية', 'لقطات لترخيص يخص جهة أخرى. أرسلت مبلغا صغيرا. هل تستحق استشارة مجانية؟', True, True), ('البحث في السجل بلا نتيجة', 'بحثت بالاسم والنطاق الرسمي. لا شيء. هل يكفي للتوقف وطلب توجيه؟', True, False), ('قائمة تحقق للعائلة', 'أقارب كادوا يمولون نفس العرض. أحتاج خطوات تحقق مختصرة دون ذكر الموقع هنا.', True, False)],
    },
    "chargeback": {
        "en": [
            ("Issuer closed the dispute too fast", "Card dispute on an investment payment was declined. I still have chats and the merchant descriptor. Can counsel review whether a stronger file is possible?", True, True),
            ("Window almost closed", "I am inside the dispute window but the bank wants a tighter chronology. Free consult to structure what I have?", True, False),
            ("Wire transfer, not card", "Most funds went by bank transfer so chargeback is limited. What other routes depend on proof quality?", True, True),
            ("Partial refund then silence", "A small reversal arrived, then the merchant stopped answering. Remaining balance is material. Next step?", True, False),
        ],
        "de": [
            ("Bank hat den Einspruch zu schnell abgelehnt", "Karteneinspruch zu einer Investmentzahlung wurde abgelehnt. Chats und Abbuchungstext habe ich. Kann Anwalt prufen, ob eine starkere Akte moglich ist?", True, True),
            ("Frist fast abgelaufen", "Ich bin noch in der Streitfrist, die Bank will einen engeren Zeitablauf. Kostenlose Beratung zum Ordnen der Unterlagen?", True, False),
            ("Uberweisung statt Karte", "Der Grossteil lief per Uberweisung, daher wenig Chargeback. Welche Wege hangen vom Beweisniveau ab?", True, True),
            ("Teilruckbuchung, dann Funkstille", "Kleine Ruckbuchung kam, danach keine Antwort. Restbetrag ist erheblich. Was als Nachstes?", True, False),
        ],
        "es": [
            ("El emisor cerro la disputa demasiado rapido", "La reclamacion de tarjeta por un pago de inversion fue rechazada. Tengo chats y el concepto del cargo. Puede revisarse si un expediente mas solido es viable?", True, True),
            ("La ventana casi se cierra", "Sigo en plazo pero el banco pide una cronologia mas precisa. Consulta gratuita para ordenar lo que tengo?", True, False),
            ("Transferencia, no tarjeta", "La mayor parte fue por transferencia, asi que el chargeback es limitado. Que otras vias dependen de la calidad de la prueba?", True, True),
            ("Reembolso parcial y luego silencio", "Llego una pequena devolucion y el comercio dejo de responder. El resto es importante. Siguiente paso?", True, False),
        ],
        "it": [
            ("L'emittente ha chiuso la contestazione troppo in fretta", "La disputa carta su un pagamento di investimento e stata respinta. Ho chat e descrizione dell'addebito. Si puo valutare se un fascicolo piu solido e realistico?", True, True),
            ("Finestra quasi chiusa", "Sono ancora nei termini ma la banca vuole una cronologia piu stretta. Consulenza gratuita per ordinare le prove?", True, False),
            ("Bonifico, non carta", "Gran parte e andata con bonifico, quindi chargeback limitato. Quali altre vie dipendono dalla qualita delle prove?", True, True),
            ("Rimborso parziale poi silenzio", "E arrivato un piccolo storno, poi silenzio. Il resto e rilevante. Prossimo passo?", True, False),
        ],
        "ar": [('الجهة المصدرة أغلقت النزاع بسرعة', 'رفض اعتراض البطاقة. لدي المحادثات ووصف العملية. هل يمكن تقوية الملف؟', True, True), ('المهلة تكاد تنتهي', 'ما زلت ضمن المهلة والبنك يريد جدولا أدق. استشارة مجانية لترتيب الأدلة؟', True, False), ('تحويل لا بطاقة', 'معظم المبلغ تحويل بنكي. ما المسارات الأخرى حسب جودة الإثبات؟', True, True), ('استرداد جزئي ثم صمت', 'عادت منصة صغيرة ثم توقف الرد. المتبقي جوهري. الخطوة التالية؟', True, False)],
    },
    "pig": {
        "en": [
            ("Romance chat pushed me into crypto deposits", "Months of messages, then pressure to fund a trading app. Withdrawals never cleared. I kept the chat export. Free consult to validate what is feasible?", True, True),
            ("They asked me to 'prove' gains with more deposits", "Classic pig-butchering pattern. I stopped sending money. What evidence matters most for counsel to assess prospects?", True, False),
            ("Wallet addresses and TXIDs saved", "I have on-chain refs and the fake support chat. Looking for a quiet review of civil options.", True, True),
            ("Family member still in the chat", "Relative keeps getting pressure messages. I need plain language on how to document and when to seek counsel.", True, False),
        ],
        "de": [
            ("Romance-Chat hat zu Krypto-Einzahlungen gedrangt", "Monatelange Nachrichten, dann Druck, eine Trading-App zu funken. Auszahlungen kamen nicht. Chat-Export liegt vor. Kostenlose Beratung zur Machbarkeit?", True, True),
            ("Mehr Einzahlungen angeblich zum 'Nachweis' von Gewinnen", "Klassisches Pig-Butchering-Muster. Ich zahle nicht mehr. Welche Beweise zahlen fur die Einschatzung der Aussichten?", True, False),
            ("Wallet-Adressen und TXIDs gesichert", "On-Chain-Referenzen und Fake-Support-Chat sind da. Brauche eine ruhige Prufung ziviler Optionen.", True, True),
            ("Familienmitglied steckt noch im Chat", "Verwandte bekommen weiter Drucknachrichten. Brauche klare Hinweise zum Dokumentieren und wann Beratung sinnvoll ist.", True, False),
        ],
        "es": [
            ("Un chat romantico me empujo a depositos cripto", "Meses de mensajes y luego presion para fondear una app de trading. Los retiros no llegaron. Tengo la exportacion del chat. Consulta gratuita para ver que es viable?", True, True),
            ("Pedian mas depositos para 'demostrar' ganancias", "Patron tipico de pig butchering. Ya no envio dinero. Que pruebas importan mas para valorar perspectivas?", True, False),
            ("Direcciones de wallet y TXID guardados", "Tengo referencias on-chain y el chat del falso soporte. Busco una revision discreta de opciones civiles.", True, True),
            ("Un familiar sigue en el chat", "Sigue recibiendo mensajes de presion. Necesito lenguaje claro sobre como documentar y cuando pedir asesoramiento.", True, False),
        ],
        "it": [
            ("Una chat sentimentale mi ha spinto a depositi crypto", "Mesi di messaggi, poi pressione a finanziare un'app di trading. I prelievi non sono arrivati. Ho l'export della chat. Consulenza gratuita per capire cosa e fattibile?", True, True),
            ("Chiedevano altri depositi per 'dimostrare' i guadagni", "Schema tipico di pig butchering. Ho smesso di inviare. Quali prove contano di piu per valutare le prospettive?", True, False),
            ("Indirizzi wallet e TXID salvati", "Ho riferimenti on-chain e la chat del finto supporto. Cerco un esame riservato delle opzioni civili.", True, True),
            ("Un familiare e ancora nella chat", "Continua a ricevere messaggi di pressione. Serve un linguaggio chiaro su come documentare e quando chiedere assistenza.", True, False),
        ],
        "ar": [('دردشة عاطفية دفعتني لإيداعات كريبتو', 'أشهر من الرسائل ثم ضغط لتمويل تطبيق تداول. السحب لم يصل. لدي تصدير المحادثة. استشارة مجانية؟', True, True), ('طلبوا مزيدا لإثبات الأرباح', 'نمط ذبح الخنازير. توقفت عن الإرسال. ما أهم الأدلة لتقييم الآفاق؟', True, False), ('عناوين محافظ وTXID محفوظة', 'مراجع على السلسلة ودردشة الدعم الوهمي. أبحث عن مراجعة سرية للخيارات المدنية.', True, True), ('قريب لا يزال في المحادثة', 'يستمر الضغط. أحتاج لغة واضحة للتوثيق ومتى أطلب استشارة.', True, False)],
    },
    "prop": {
        "en": [
            ("Passed the challenge, payout denied", "Rules looked clear when I paid the fee. After I passed, new conditions appeared and the payout was refused. Screens and terms saved. Free consult?", True, True),
            ("Consistency rule appeared only at payout", "Nothing in the signed terms matched what support cited later. Challenge fee is gone. Worth validating a claim?", True, True),
            ("Firm went quiet after collecting fees", "Discord and support stopped answering. Card payment on file. What proof level do you need for a first review?", True, False),
            ("Multiple failed accounts, same pattern", "Three challenges, same late rule changes. Looking for counsel to say if coordinated steps are realistic.", True, False),
        ],
        "de": [
            ("Challenge bestanden, Auszahlung verweigert", "Regeln wirkten klar bei der Gebuhr. Nach Bestehen kamen neue Bedingungen und die Auszahlung wurde abgelehnt. Screens und AGB gesichert. Kostenlose Beratung?", True, True),
            ("Consistency-Regel erst bei Auszahlung", "In den unterschriebenen Bedingungen stand das nicht. Challenge-Gebuhr weg. Lohnt Validierung des Anspruchs?", True, True),
            ("Firma verstummte nach Gebuhren", "Discord und Support antworten nicht. Kartenzahlung vorhanden. Welches Beweisniveau brauchen Sie fur die Erstprufung?", True, False),
            ("Mehrere Accounts, gleiches Muster", "Drei Challenges, spat geanderte Regeln. Brauche Einschatzung, ob koordinierte Schritte realistisch sind.", True, False),
        ],
        "es": [
            ("Supere el challenge y negaron el pago", "Las reglas parecian claras al pagar. Tras aprobar, aparecieron condiciones nuevas y rechazaron el pago. Tengo pantallas y terminos. Consulta gratuita?", True, True),
            ("La regla de consistencia salio solo al cobrar", "No estaba en los terminos firmados. La cuota del challenge se perdio. Vale validar la reclamacion?", True, True),
            ("La firma dejo de responder tras cobrar", "Discord y soporte silenciosos. Pago con tarjeta registrado. Que nivel de prueba necesitan para una primera revision?", True, False),
            ("Varias cuentas fallidas, mismo patron", "Tres challenges con cambios tardios de reglas. Quiero saber si pasos coordinados son realistas.", True, False),
        ],
        "it": [
            ("Challenge superata, payout negato", "Le regole sembravano chiare al pagamento. Dopo il passaggio sono arrivate nuove condizioni e il payout e stato rifiutato. Ho screen e termini. Consulenza gratuita?", True, True),
            ("Regola di consistency solo al payout", "Non era nei termini firmati. Fee della challenge persa. Vale validare la richiesta?", True, True),
            ("La societa e sparita dopo le fee", "Discord e supporto muti. Pagamento carta in archivio. Quale livello di prova serve per una prima lettura?", True, False),
            ("Piu account falliti, stesso schema", "Tre challenge, regole cambiate in ritardo. Serve capire se passi coordinati sono realistici.", True, False),
        ],
        "ar": [('اجتزت التحدي ورُفض الدفع', 'القواعد بدت واضحة عند الدفع. بعد النجاح ظهرت شروط جديدة. لقطات وشروط محفوظة. استشارة مجانية؟', True, True), ('قاعدة الاتساق ظهرت عند الدفع فقط', 'لم تكن في الشروط الموقعة. رسم التحدي ضاع. هل يستحق التحقق من المطالبة؟', True, True), ('الشركة اختفت بعد الرسوم', 'دعم وديسكورد صامتان. دفع بطاقة مسجل. ما مستوى الإثبات للمراجعة الأولى؟', True, False), ('حسابات عدة بنفس النمط', 'ثلاثة تحديات وتغيير قواعد متأخر. هل خطوات منسقة واقعية؟', True, False)],
    },
    "broker": {
        "en": [
            ("Platform looked regulated, then withdrawals stalled", "Marketing showed badges. After deposits, payouts stalled with shifting stories. I kept URLs and chats. Free consult to validate the claim?", True, True),
            ("Cold call into larger deposits", "Pressure to top up after early 'profits' on screen. Now support ignores withdrawal requests. Evidence pack ready.", True, True),
            ("Is this pattern enough to instruct counsel?", "I have payment proofs and a short timeline. Do you first check feasibility from the proof level?", True, False),
            ("Relative almost opened an account", "Same pitch as mine. Sharing this guide. Any checklist before they send money?", True, False),
        ],
        "de": [
            ("Plattform wirkte reguliert, dann stockten Auszahlungen", "Marketing mit Siegeln. Nach Einzahlungen stockten Auszahlungen mit wechselnden Erklarungen. URLs und Chats gesichert. Kostenlose Beratung zur Validierung?", True, True),
            ("Kaltakquise zu Nachschussen", "Druck zu mehr Einzahlung nach fruhen 'Gewinnen' am Screen. Support ignoriert Auszahlungen. Akte bereit.", True, True),
            ("Reicht dieses Muster fur eine Beauftragung?", "Zahlungsbelege und kurzer Zeitablauf liegen vor. Prufen Sie zuerst die Machbarkeit anhand der Beweise?", True, False),
            ("Verwandte fast Konto eroffnet", "Gleiches Angebot wie meines. Ich teile diese Seite. Gibt es eine kurze Checkliste vor der Einzahlung?", True, False),
        ],
        "es": [
            ("La plataforma parecia regulada y luego frenaron los retiros", "El marketing mostraba insignias. Tras depositar, los retiros se frenaron con historias distintas. Guarde URLs y chats. Consulta gratuita para validar?", True, True),
            ("Llamada en frio hacia mas depositos", "Presion para ingresar mas tras 'beneficios' en pantalla. El soporte ignora los retiros. Expediente listo.", True, True),
            ("Basta este patron para encargar asesoramiento?", "Tengo pruebas de pago y una cronologia corta. Primero comprueban la viabilidad segun el nivel de prueba?", True, False),
            ("Un familiar casi abrio cuenta", "Misma oferta que la mia. Comparto esta guia. Hay una lista breve antes de enviar dinero?", True, False),
        ],
        "it": [
            ("La piattaforma sembrava regolata, poi i prelievi si sono fermati", "Marketing con badge. Dopo i depositi i prelievi si sono fermati con storie diverse. Ho URL e chat. Consulenza gratuita per validare?", True, True),
            ("Cold call verso depositi maggiori", "Pressione a versare di piu dopo 'profitti' a schermo. Il supporto ignora i prelievi. Fascicolo pronto.", True, True),
            ("Questo schema basta per incaricare un legale?", "Ho prove di pagamento e una cronologia breve. Prima verificate la fattibilita dal livello di prova?", True, False),
            ("Un parente stava per aprire il conto", "Stessa proposta della mia. Condivido questa guida. C'e una checklist breve prima di inviare soldi?", True, False),
        ],
        "ar": [('المنصة بدت مرخصة ثم توقف السحب', 'شارات تسويقية ثم سحب متوقف بقصص متغيرة. روابط ومحادثات محفوظة. استشارة مجانية للتحقق؟', True, True), ('اتصال بارد لمزيد من الإيداع', 'ضغط بعد أرباح على الشاشة. الدعم يتجاهل السحب. الملف جاهز.', True, True), ('هل يكفي هذا النمط للتوكيل؟', 'إثباتات دفع وجدول مختصر. هل تتحققون أولا من الجدوى حسب الإثبات؟', True, False), ('قريب كاد يفتح حسابا', 'نفس العرض. أشارك هذا الدليل. هل توجد قائمة تحقق قبل الإرسال؟', True, False)],
    },
    "crypto": {
        "en": [
            ("USDT sent, then wallet support went dark", "I have TXIDs and the chat that pushed more deposits. Looking for a free consult on whether tracing plus civil steps are realistic.", True, True),
            ("Fake exchange UI showed growing balance", "Could not withdraw to my own wallet. Screenshots and seed of the story are saved. Validate claim?", True, True),
            ("How much on-chain detail do you need?", "Before booking: consultation is free, and you assess prospects from the proof level  -  is that right?", True, False),
            ("Mixed card and crypto payments", "Some by card, some on-chain. Need help sorting which paths fit which proof.", True, False),
        ],
        "de": [
            ("USDT gesendet, dann Funkstille vom Wallet-Support", "TXIDs und Chat mit Nachschussdruck sind da. Kostenlose Beratung, ob Tracing plus Zivilweg realistisch ist?", True, True),
            ("Fake-Exchange zeigte wachsendes Guthaben", "Auszahlung auf mein Wallet ging nicht. Screenshots und Ablauf gesichert. Anspruch validieren?", True, True),
            ("Wie viel On-Chain-Detail brauchen Sie?", "Vor der Buchung: Beratung kostenlos, Aussichten anhand des Beweisniveaus  -  stimmt das?", True, False),
            ("Karte und Krypto gemischt", "Teilweise Karte, teilweise On-Chain. Brauche Hilfe, welche Wege zu welchen Beweisen passen.", True, False),
        ],
        "es": [
            ("Envie USDT y el soporte de la wallet desaparecio", "Tengo TXID y el chat que pedía mas depositos. Consulta gratuita sobre si trazado mas via civil es realista?", True, True),
            ("Una UI de exchange falsa mostraba saldo creciente", "No pude retirar a mi wallet. Capturas y relato guardados. Validar la reclamacion?", True, True),
            ("Cuanto detalle on-chain necesitan?", "Antes de reservar: la consulta es gratuita y valoran perspectivas segun el nivel de prueba  -  correcto?", True, False),
            ("Pagos mixtos tarjeta y cripto", "Parte con tarjeta, parte on-chain. Necesito ordenar que vias encajan con cada prueba.", True, False),
        ],
        "it": [
            ("USDT inviato, poi silenzio dal supporto wallet", "Ho TXID e la chat che spingeva altri depositi. Consulenza gratuita su tracing piu via civile realistici?", True, True),
            ("UI di exchange falsa con saldo in crescita", "Non riuscivo a prelevare sul mio wallet. Screenshot e racconto salvati. Validare il caso?", True, True),
            ("Quanto dettaglio on-chain serve?", "Prima di prenotare: consulenza gratuita e prospettive dal livello di prova  -  corretto?", True, False),
            ("Pagamenti misti carta e crypto", "Parte carta, parte on-chain. Serve ordinare quali vie stanno con quali prove.", True, False),
        ],
        "ar": [('أرسلت USDT ثم اختفى الدعم', 'لدي TXID ودردشة تطلب مزيدا. استشارة مجانية حول التتبع والمسار المدني؟', True, True), ('واجهة منصة وهمية برصيد متزايد', 'لم أستطع السحب لمحفظتي. لقطات محفوظة. التحقق من المطالبة؟', True, True), ('كم من تفاصيل السلسلة تحتاجون؟', 'قبل الحجز: الاستشارة مجانية وتقييم الآفاق حسب الإثبات - صحيح؟', True, False), ('مدفوعات مختلطة بطاقة وكريبتو', 'جزء بطاقة وجزء على السلسلة. أحتاج ترتيب المسارات حسب الأدلة.', True, False)],
    },
    "report": {
        "en": [
            ("Where should I file first?", "UK-based. I have a clear timeline. Do I report to the bank and Action Fraud before a free consultation, or can you sequence both?", True, False),
            ("Already filed, need civil read", "Police/cyber report is in. Money still missing. Want counsel to validate civil prospects from my proof.", True, True),
            ("Cross-border payments", "Paid from one country to an overseas desk. Which report paths still matter alongside counsel?", True, False),
            ("Afraid of saying too much publicly", "I can share details privately. Prefer a moderated comment or direct consult?", True, False),
        ],
        "de": [
            ("Wohin zuerst melden?", "Ich habe einen klaren Zeitablauf. Bank und Behorde vor der kostenlosen Beratung, oder konnen Sie beides staffeln?", True, False),
            ("Schon gemeldet, brauche zivile Einordnung", "Anzeige ist raus. Geld fehlt. Anwaltliche Validierung der zivilen Aussichten anhand meiner Beweise.", True, True),
            ("Grenzuberschreitende Zahlungen", "Zahlung aus einem Land an einen auslandischen Desk. Welche Meldewege zahlen parallel zur Beratung?", True, False),
            ("Will offline bleiben", "Details lieber vertraulich. Moderierter Kommentar oder direkte Beratung?", True, False),
        ],
        "es": [
            ("Donde denunciar primero?", "Tengo una cronologia clara. Banco y autoridad antes de la consulta gratuita, o pueden ordenar ambos pasos?", True, False),
            ("Ya denuncie, necesito lectura civil", "La denuncia esta presentada. Falta el dinero. Quiero validar perspectivas civiles con mis pruebas.", True, True),
            ("Pagos transfronterizos", "Pague desde un pais a un desk en el extranjero. Que vias de denuncia importan junto al asesoramiento?", True, False),
            ("Prefiero no exponer detalles en publico", "Puedo compartir en privado. Comentario moderado o consulta directa?", True, False),
        ],
        "it": [
            ("Dove segnalare per prima?", "Ho una cronologia chiara. Banca e autorita prima della consulenza gratuita, o potete sequenziare entrambi?", True, False),
            ("Gia denunciato, serve lettura civile", "Denuncia presentata. Soldi ancora fuori. Voglio validare le prospettive civili con le mie prove.", True, True),
            ("Pagamenti cross-border", "Pagato da un paese verso un desk estero. Quali vie di segnalazione restano utili insieme all'assistenza?", True, False),
            ("Preferisco non pubblicare dettagli", "Posso condividere in privato. Commento moderato o consulenza diretta?", True, False),
        ],
        "ar": [('أين أبلغ أولا؟', 'لدي جدول واضح. البنك والجهة الرقابية قبل الاستشارة المجانية أم يمكن ترتيب الاثنين؟', True, False), ('أبلغت وأحتاج قراءة مدنية', 'البلاغ قُدّم. المال خارج. أريد التحقق من الآفاق المدنية حسب أدلتي.', True, True), ('مدفوعات عبر الحدود', 'دفعت من بلد لمكتب في الخارج. أي مسارات إبلاغ تبقى مفيدة مع الاستشارة؟', True, False), ('أفضل عدم نشر التفاصيل', 'يمكن المشاركة بسرية. تعليق خاضع للإشراف أم استشارة مباشرة؟', True, False)],
    },
    "lawyer": {
        "en": [
            ("Looking for litigation counsel, not a call centre", "Material online fraud loss. Need someone who validates the claim and explains feasibility from proof, with a free first consult.", True, True),
            ("Can you act if I am outside the UK?", "Payments and chats are ready. Does a free consultation still make sense for cross-border facts?", True, False),
            ("Bundle of evidence needs sorting", "Emails, TXIDs, bank PDFs. Who helps decide what is enough to instruct?", True, True),
            ("Previous 'recovery' chat felt off", "I stopped engaging. Want proper counsel framing and a quiet review.", True, False),
        ],
        "de": [
            ("Suche Prozessbeistand, kein Callcenter", "Erheblicher Online-Betrugsverlust. Jemand soll den Anspruch validieren und Machbarkeit aus Beweisen erklaren  -  kostenlose Erstberatung.", True, True),
            ("Konnen Sie auch ausserhalb UK tatig werden?", "Zahlungen und Chats bereit. Lohnt kostenlose Beratung bei grenzuberschreitenden Fakten?", True, False),
            ("Beweisbundle muss sortiert werden", "E-Mails, TXIDs, Bank-PDFs. Wer hilft zu entscheiden, was fur eine Beauftragung reicht?", True, True),
            ("Fruherer 'Recovery'-Chat wirkte unserios", "Ich habe abgebrochen. Will anwaltlichen Rahmen und ruhige Prufung.", True, False),
        ],
        "es": [
            ("Busco abogados de litigio, no un call center", "Perdida material por estafa online. Necesito validar la reclamacion y explicar viabilidad con pruebas, con consulta inicial gratuita.", True, True),
            ("Pueden actuar si estoy fuera del Reino Unido?", "Pagos y chats listos. Tiene sentido una consulta gratuita con hechos transfronterizos?", True, False),
            ("El paquete de pruebas necesita orden", "Emails, TXID, PDF bancarios. Quien ayuda a decidir que basta para encargar?", True, True),
            ("Un chat de 'recuperacion' anterior no me convencio", "Deje de participar. Quiero marco legal serio y revision discreta.", True, False),
        ],
        "it": [
            ("Cerco assistenza processuale, non un call center", "Perdita rilevante da truffa online. Serve validare il caso e spiegare la fattibilita dalle prove, con prima consulenza gratuita.", True, True),
            ("Potete agire se sono fuori dal Regno Unito?", "Pagamenti e chat pronti. Ha senso una consulenza gratuita con fatti cross-border?", True, False),
            ("Il fascicolo prove va ordinato", "Email, TXID, PDF bancari. Chi aiuta a decidere cosa basta per l'incarico?", True, True),
            ("Una chat di 'recovery' precedente non convinceva", "Ho smesso di rispondere. Voglio un quadro legale serio e un esame riservato.", True, False),
        ],
        "ar": [('أبحث عن محامي تقاضي لا مركز اتصال', 'خسارة جوهرية من احتيال إلكتروني. أحتاج التحقق من المطالبة وشرح الجدوى من الإثبات، باستشارة أولى مجانية.', True, True), ('هل تعملون إن كنت خارج المملكة المتحدة؟', 'مدفوعات ومحادثات جاهزة. هل الاستشارة المجانية منطقية لوقائع عبر الحدود؟', True, False), ('حزمة أدلة تحتاج ترتيبا', 'رسائل وTXID وملفات بنكية. من يساعد في تقرير ما يكفي للتوكيل؟', True, True), ('دردشة استرداد سابقة لم تقنعني', 'توقفت عن الرد. أريد إطارا قانونيا جديا ومراجعة هادئة.', True, False)],
    },
    "online": {
        "en": [
            ("Online investment pitch emptied my account", "Cold contact, then deposits, then no withdrawal. Timeline and proofs ready. Free consult to validate prospects?", True, True),
            ("What should I preserve tonight?", "I still have access to some chats. Priority list before passwords change?", True, False),
            ("Small early payout, then block", "They let a tiny withdrawal through. Larger one never moved. Same story as this guide.", True, True),
            ("Need plain next steps", "Not asking for guarantees. Want feasibility against my proof level.", True, False),
        ],
        "de": [
            ("Online-Investment-Pitch hat das Konto geleert", "Kaltkontakt, Einzahlungen, keine Auszahlung. Zeitablauf und Beweise bereit. Kostenlose Beratung zu den Aussichten?", True, True),
            ("Was heute Abend sichern?", "Noch Zugang zu Teilen der Chats. Prioritatenliste bevor Passworter wechseln?", True, False),
            ("Kleine Fruhauszahlung, dann Blockade", "Mini-Auszahlung ging, die grosse nicht. Gleiches Muster wie in dieser Seite.", True, True),
            ("Brauche klare nachste Schritte", "Keine Garantien. Machbarkeit anhand meines Beweisniveaus.", True, False),
        ],
        "es": [
            ("Una oferta de inversion online vacio mi cuenta", "Contacto en frio, depositos y sin retiro. Cronologia y pruebas listas. Consulta gratuita para validar perspectivas?", True, True),
            ("Que debo conservar esta noche?", "Aun tengo acceso a parte de los chats. Lista de prioridades antes de que cambien claves?", True, False),
            ("Retiro pequeno al inicio y luego bloqueo", "Dejaron salir un importe minimo. El grande no se movio. Misma historia que esta guia.", True, True),
            ("Necesito pasos siguientes claros", "Sin garantias. Viabilidad segun mi nivel de prueba.", True, False),
        ],
        "it": [
            ("Una proposta di investimento online ha svuotato il conto", "Contatto a freddo, depositi, nessun prelievo. Cronologia e prove pronte. Consulenza gratuita per validare le prospettive?", True, True),
            ("Cosa conservare stasera?", "Ho ancora accesso a parte delle chat. Lista priorita prima che cambino le password?", True, False),
            ("Prelievo piccolo all'inizio, poi blocco", "Hanno fatto uscire un importo minimo. Quello grande non si e mosso. Stessa storia di questa guida.", True, True),
            ("Servono passi successivi chiari", "Niente garanzie. Fattibilita in base al livello di prova.", True, False),
        ],
        "ar": [('عرض استثمار إلكتروني أفرغ الحساب', 'تواصل بارد ثم إيداعات دون سحب. الجدول والأدلة جاهزة. استشارة مجانية؟', True, True), ('ماذا أحفظ الليلة؟', 'ما زال لدي جزء من المحادثات. قائمة أولويات قبل تغيير كلمات المرور؟', True, False), ('سحب صغير ثم حظر', 'سمحوا بمبلغ ضئيل. الكبير لم يتحرك. نفس قصة هذا الدليل.', True, True), ('أحتاج خطوات تالية واضحة', 'بدون ضمانات. الجدوى حسب مستوى إثباتي.', True, False)],
    },
    "authorities": {
        "en": [
            ("Which authority for my payment path?", "Card and crypto mixed. Looking for a short map before the free consult.", True, False),
            ("Regulator complaint drafted", "I can file, but want counsel to say if civil steps should run in parallel based on proof.", True, True),
            ("Got an auto-ack, no case officer yet", "Report filed weeks ago. Money still out. Validate what else is realistic?", True, True),
            ("Documents in another language", "Bank letters not in English. Does that block a first review?", True, False),
        ],
        "de": [
            ("Welche Behorde fur meinen Zahlungsweg?", "Karte und Krypto gemischt. Kurze Landkarte vor der kostenlosen Beratung.", True, False),
            ("Beschwerde an Aufsicht entworfen", "Kann einreichen, will aber wissen, ob Zivilschritte parallel laufen sollten  -  anhand der Beweise.", True, True),
            ("Eingangsbestatigung, noch kein Sachbearbeiter", "Meldung vor Wochen. Geld weg. Was ist sonst realistisch?", True, True),
            ("Unterlagen in anderer Sprache", "Bankschreiben nicht auf Deutsch/Englisch. Blockiert das die Erstprufung?", True, False),
        ],
        "es": [
            ("Que autoridad segun mi via de pago?", "Tarjeta y cripto mezclados. Mapa breve antes de la consulta gratuita.", True, False),
            ("Queja al regulador borrador lista", "Puedo presentar, pero quiero saber si la via civil debe ir en paralelo segun las pruebas.", True, True),
            ("Acuse automatico, sin instructor aun", "Denuncia hace semanas. Dinero fuera. Que mas es realista?", True, True),
            ("Documentos en otro idioma", "Cartas del banco no estan en espanol. Impide una primera revision?", True, False),
        ],
        "it": [
            ("Quale autorita per il mio percorso di pagamento?", "Carta e crypto misti. Mappa breve prima della consulenza gratuita.", True, False),
            ("Reclamo al regolatore in bozza", "Posso presentare, ma voglio sapere se la via civile deve correre in parallelo in base alle prove.", True, True),
            ("Ricevuta automatica, niente referente ancora", "Segnalazione di settimane fa. Soldi fuori. Cos'altro e realistico?", True, True),
            ("Documenti in un'altra lingua", "Lettere banca non in italiano. Blocca una prima lettura?", True, False),
        ],
        "ar": [('أي جهة حسب وسيلة الدفع؟', 'بطاقة وكريبتو معا. خريطة مختصرة قبل الاستشارة المجانية.', True, False), ('مسودة شكوى للرقابة جاهزة', 'يمكن التقديم، لكني أريد معرفة إن كان المسار المدني يسير بالتوازي حسب الأدلة.', True, True), ('إيصال آلي دون محقّق بعد', 'بلاغ منذ أسابيع. المال خارج. ما الواقعي أيضا؟', True, True), ('مستندات بلغة أخرى', 'خطابات البنك ليست بالعربية. هل يمنع ذلك المراجعة الأولى؟', True, False)],
    },
    "bonus": {
        "en": [
            ("Bonus terms used to stop my withdrawal", "After I requested a payout, support pointed to bonus rules I never activated. Balance still on screen. Free consult?", True, True),
            ("Turnover conditions changed mid-way", "Chat promised one figure, written terms another. Saved both. Validate claim?", True, True),
            ("Small bonus, large trapped deposit", "The bonus was tiny next to what I deposited. Looking for feasibility from proof.", True, False),
            ("Need help reading the T&Cs file", "PDF is long. Priority clauses for a counsel review?", True, False),
        ],
        "de": [
            ("Bonusbedingungen gegen meine Auszahlung", "Nach Auszahlungsantrag verwies Support auf Bonusregeln, die ich nie aktiviert hatte. Guthaben noch sichtbar. Kostenlose Beratung?", True, True),
            ("Umsatzbedingungen unterwegs geandert", "Chat versprach eine Zahl, Schriftliches eine andere. Beides gesichert. Anspruch validieren?", True, True),
            ("Kleiner Bonus, grosse Einzahlung fest", "Bonus war winzig neben der Einzahlung. Machbarkeit anhand der Beweise?", True, False),
            ("Hilfe beim Lesen der AGB-Datei", "PDF ist lang. Welche Klauseln zuerst fur die anwaltliche Prufung?", True, False),
        ],
        "es": [
            ("Usaron el bono para frenar el retiro", "Tras pedir el retiro, el soporte cito reglas de bono que no active. El saldo sigue en pantalla. Consulta gratuita?", True, True),
            ("Las condiciones de rollover cambiaron a mitad", "El chat prometia una cifra y el escrito otra. Guarde ambos. Validar reclamacion?", True, True),
            ("Bono pequeno, deposito grande retenido", "El bono era minimo frente a lo depositado. Viabilidad segun pruebas?", True, False),
            ("Ayuda para leer el PDF de terminos", "Es largo. Que clausulas priorizar para una revision legal?", True, False),
        ],
        "it": [
            ("Termini del bonus usati per fermare il prelievo", "Dopo la richiesta di prelievo il supporto ha citato regole bonus che non avevo attivato. Saldo ancora a schermo. Consulenza gratuita?", True, True),
            ("Condizioni di rollover cambiate a meta", "La chat prometteva una cifra, il testo scritto un'altra. Ho salvato entrambi. Validare il caso?", True, True),
            ("Bonus piccolo, deposito grande bloccato", "Il bonus era minimo rispetto al deposito. Fattibilita dalle prove?", True, False),
            ("Aiuto a leggere il PDF dei termini", "E lungo. Quali clausole prioritizzare per un esame legale?", True, False),
        ],
        "ar": [('استخدموا المكافأة لمنع السحب', 'بعد طلب السحب استشهد الدعم بقواعد مكافأة لم أفعّلها. الرصيد ظاهر. استشارة مجانية؟', True, True), ('شروط الرول أوفر تغيرت في المنتصف', 'الدردشة وعدت برقم والمستند بآخر. حفظت الاثنين. التحقق من المطالبة؟', True, True), ('مكافأة صغيرة وإيداع كبير عالق', 'المكافأة ضئيلة مقابل الإيداع. الجدوى من الأدلة؟', True, False), ('مساعدة في قراءة ملف الشروط', 'طويل. أي بنود تُقدَّم أولا للمراجعة القانونية؟', True, False)],
    },
}

# Map each guide file stem to a theme. Keys are path prefixes used in comments.js.
GUIDE_MAP: list[tuple[str, str, str]] = [
    # (key, lang, theme)
    ("guides/broker-withdrawal-problem", "en", "withdrawal"),
    ("guides/chargeback-failed-investment", "en", "chargeback"),
    ("guides/check-broker-license", "en", "license"),
    ("guides/fund-recovery-services", "en", "recovery"),
    ("guides/pig-butchering-scam", "en", "pig"),
    ("guides/prop-trading-scam", "en", "prop"),
    ("de/anlagebetrug-geld-zurueck", "de", "recovery"),
    ("de/anlagebetrug", "de", "broker"),
    ("de/behoerden", "de", "authorities"),
    ("de/betrug-melden", "de", "report"),
    ("de/bonusfalle", "de", "bonus"),
    ("de/broker-auszahlung-problem", "de", "withdrawal"),
    ("de/broker-betrug", "de", "broker"),
    ("de/geld-zurueck-broker", "de", "recovery"),
    ("de/krypto-anwalt", "de", "lawyer"),
    ("de/krypto-betrug", "de", "crypto"),
    ("de/online-betrug-geld-zurueck", "de", "online"),
    ("de/trading-betrug", "de", "broker"),
    ("it/avvocato-truffa-online", "it", "lawyer"),
    ("it/problemi-prelievo-broker", "it", "withdrawal"),
    ("it/recuperare-soldi-truffa", "it", "recovery"),
    ("it/truffa-criptovalute", "it", "crypto"),
    ("it/truffa-online", "it", "online"),
    ("it/truffa-romance", "it", "pig"),
    ("it/truffa-trading-online", "it", "broker"),
    ("es/abogado-estafa-online", "es", "lawyer"),
    ("es/broker-no-deja-retirar", "es", "withdrawal"),
    ("es/como-saber-si-un-broker-es-fiable", "es", "license"),
    ("es/estafa-criptomonedas", "es", "crypto"),
    ("es/estafa-online", "es", "online"),
    ("es/estafa-sentimental-criptomonedas", "es", "pig"),
    ("es/estafa-trading-broker", "es", "broker"),
    ("es/recuperar-dinero-estafa", "es", "recovery"),
    ("ar/ihtiyal-online", "ar", "online"),
    ("ar/istirdad-amwal-ihtiyal", "ar", "recovery"),
    ("ar/nasb-forex", "ar", "broker"),
    ("ar/nasb-umlat-raqamiya", "ar", "crypto"),
    ("ar/wasit-yamna-alsahb", "ar", "withdrawal"),
    ("ar/muhami-ihtiyal-online", "ar", "lawyer"),
    ("ar/ihtiyal-istiqtab-crypto", "ar", "pig"),
    ("ar/kayf-atahaqqaq-min-wasit", "ar", "license"),
]



def build_thread(key: str, lang: str, theme: str, today: date) -> list[dict]:
    pool = THEMES[theme][lang]
    # Pick 3 comments with stable rotation so neighbouring guides differ
    start = stable_int(key, len(pool))
    idxs = [(start + i) % len(pool) for i in range(3)]
    # Prefer including at least one importantLoss for support reply
    if not any(pool[i][3] for i in idxs):
        for j, item in enumerate(pool):
            if item[3]:
                idxs[0] = j
                break

    out: list[dict] = []
    used_names: set[str] = set()
    for n, i in enumerate(idxs):
        title, text, ask, important = pool[i]
        pkey = f"{key}:c{n}:{i}"
        p = person(pkey, lang)
        # ensure unique names within page
        tries = 0
        while p["name"] in used_names and tries < 8:
            p = person(f"{pkey}:r{tries}", lang)
            tries += 1
        used_names.add(p["name"])
        item = {
            "name": p["name"],
            "initials": p["initials"],
            "country": p["country"],
            "date": d(pkey, today, 12 + n * 18, 40 + n * 22),
            "title": title,
            "text": text,
            "lang": lang,
            "askHelp": ask,
            "importantLoss": important,
        }
        if important:
            item["support"] = {
                "date": d(f"{pkey}:sup", today, 2, 10),
                "text": pick(SUPPORT[lang], f"{pkey}:suptext"),
                "ctaLabel": CTA[lang],
                "ctaHref": "../pages/contact.html",
            }
        out.append(item)
    return out


def assert_clean(label: str, s: str) -> None:
    bad = sorted(set(c for c in s if c in CHARS_BANNED))
    if bad:
        raise SystemExit(f"{label}: banned characters {bad!r} in {s[:80]!r}")
    m = WORDS_BANNED.search(s)
    if m:
        raise SystemExit(f"{label}: banned wording {m.group(0)!r} in {s[:120]!r}")
    # Soft ban: broker-like domains
    if re.search(r"\b[\w-]+\.(com|io|net|org|uk)\b", s, re.I) and "act-here" not in s.lower():
        raise SystemExit(f"{label}: domain-like token in guide comment: {s[:120]!r}")


def main() -> None:
    today = date.today()
    db: dict[str, list[dict]] = {}
    for key, lang, theme in GUIDE_MAP:
        # Verify file exists
        path = ROOT / f"{key}.html"
        if not path.exists():
            raise SystemExit(f"Missing guide file: {path}")
        thread = build_thread(key, lang, theme, today)
        for c in thread:
            assert_clean(f"{key}:{c['name']}:title", c["title"])
            assert_clean(f"{key}:{c['name']}:text", c["text"])
            if c.get("support"):
                assert_clean(f"{key}:support", c["support"]["text"])
                assert_clean(f"{key}:cta", c["support"]["ctaLabel"])
        db[key] = thread

    payload = json.dumps(db, ensure_ascii=False, indent=2)
    OUT.write_text(
        "/* Auto-generated by tools/build_guide_comments.py  -  topic comments for guides */\n"
        "window.ACT_HERE_GUIDE_COMMENTS = "
        + payload
        + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(db)} guides, "
          f"{sum(len(v) for v in db.values())} comments")


if __name__ == "__main__":
    main()
