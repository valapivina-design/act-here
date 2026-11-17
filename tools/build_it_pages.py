#!/usr/bin/env python3
"""Build the Italian victim-intent cluster under /it/.
Copy rules enforced at build time: no em/en dashes, no smart quotes, no fee-to-release
mechanics, no 'free' claims, no broker names. Fails the build if any rule is broken."""
import os, re, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_de_pages import esc, render_section

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IT = os.path.join(ROOT, "it")
os.makedirs(IT, exist_ok=True)
BASE = "https://act-here.uk/it/"
UPDATED = "Aggiornato novembre 2026"

PAGES = [
 {
  "slug": "truffa-online",
  "card": "Cosa fare subito, a chi rivolgersi e come presentare denuncia.",
  "title": "Truffa online: cosa fare, a chi rivolgersi e come denunciare | Act Here",
  "description": "Truffa online: cosa fare subito, a chi rivolgersi, come presentare denuncia a Polizia Postale o Carabinieri e quali strade esistono per recuperare i soldi.",
  "badge": "Truffa online",
  "h1": "Truffa online: cosa fare e a chi rivolgersi",
  "lead": "Hai pagato per un investimento, un servizio o un acquisto che non esisteva, e ora dall'altra parte non risponde più nessuno. La truffa online è di gran lunga la ricerca più frequente in Italia su questi temi. Conta soprattutto una cosa: quanto in fretta ti muovi, perché i termini bancari sono brevi e le prove si perdono.",
  "sections": [
   ("Primi passi", "Truffa online cosa fare nelle prime 48 ore", [
    ("ul", [
     "Interrompi ogni pagamento verso la controparte e verso chiunque dica di agire per suo conto.",
     "Conserva le prove: schermate del sito e del conto, chat, email, ricevute, IBAN del beneficiario, indirizzi wallet, URL esatti.",
     "Contatta subito la tua banca o l'emittente della carta: richiamo del bonifico e contestazione dell'addebito hanno termini brevi.",
     "Presenta denuncia: mette il fatto agli atti e serve per banca, assicurazione e azione civile.",
     "Fai valutare il caso finché tutte le strade sono ancora aperte.",
    ]),
   ]),
   ("Denuncia", "Truffa online a chi rivolgersi: forze dell'ordine, banca, autorità", [
    ("h3", "Denuncia truffa Polizia Postale"),
    ("p", "La Polizia Postale è il riferimento per i reati informatici. Puoi presentarti in un ufficio oppure usare il portale del Commissariato di P.S. online per la segnalazione e, dove previsto, per avviare la denuncia da formalizzare poi di persona."),
    ("h3", "Denuncia truffa online Carabinieri o Guardia di Finanza"),
    ("p", "La denuncia può essere presentata anche in qualsiasi stazione dei Carabinieri o alla Guardia di Finanza: ha lo stesso valore. Porta con te documento, cronologia dei fatti, dati dei pagamenti e prove salvate su file."),
    ("h3", "Banca e autorità di vigilanza"),
    ("p", "Avvisa per iscritto la banca. Se la controparte si presentava come intermediario finanziario, verifica gli elenchi e gli avvisi di <a href=\"https://www.consob.it\" target=\"_blank\" rel=\"noopener\">CONSOB</a> e Banca d'Italia e segnala il sito."),
   ]),
   ("Profilo penale", "Truffa online reato: cosa prevede il codice penale", [
    ("p", "Truffa online codice penale: il riferimento è l'art. 640 c.p. (truffa) e, per le condotte sui sistemi informatici, l'art. 640-ter c.p. (frode informatica). Di regola la truffa è procedibile a querela, da presentare entro tre mesi dal giorno in cui hai avuto notizia del fatto; nelle ipotesi aggravate si procede d'ufficio."),
    ("p", "La denuncia persegue i responsabili, ma non restituisce da sola il denaro. Per il risarcimento servono la costituzione di parte civile nel processo penale oppure un'azione civile autonoma (art. 2043 c.c.)."),
   ]),
   ("Schemi ricorrenti", "Truffa investimenti online: i casi più cercati", [
    ("p", "La truffa investimenti online segue quasi sempre lo stesso copione: contatto non richiesto, piccolo versamento iniziale, guadagni mostrati a schermo, richiesta di versare di più, prelievo che non arriva."),
    ("ul", [
     "Truffa investimenti 250 euro: il versamento d'ingresso tipico delle piattaforme non autorizzate.",
     "Truffa investimenti oro (o truffa oro): proposte di oro fisico o digitale con rendimento promesso e custodia mai verificabile.",
     "Truffa investimenti bitcoin e truffa investimenti criptovalute: vedi la guida sulla <a href=\"truffa-criptovalute.html\">truffa criptovalute</a>.",
     "Truffa investimenti intelligenza artificiale: finti sistemi automatici che garantirebbero profitti senza rischio.",
    ]),
    ("p", "In tutti i casi di truffa investimenti la verifica decisiva è la stessa: l'operatore compare negli albi ufficiali con lo stesso nome, lo stesso sito e gli stessi contatti?"),
   ]),
  ],
  "faqs": [
   ("Truffa online: cosa fare per prima cosa?", "Interrompi i pagamenti, salva tutte le prove, contatta subito la banca o l'emittente della carta e presenta denuncia. Poi fai valutare il caso: i termini per richiamo e contestazione sono brevi."),
   ("Truffa online, a chi rivolgersi?", "Alla Polizia Postale, ai Carabinieri o alla Guardia di Finanza per la denuncia; alla tua banca per richiamo o contestazione; a CONSOB o Banca d'Italia per la segnalazione se si trattava di servizi finanziari; a un legale per il recupero in sede civile."),
   ("Entro quanto tempo devo presentare denuncia?", "Per la truffa procedibile a querela il termine è di tre mesi da quando hai avuto notizia del fatto. I termini bancari sono più brevi e decorrono dal pagamento, quindi conviene muoversi subito."),
   ("La denuncia mi fa riavere i soldi?", "Non da sola. La denuncia avvia il procedimento penale contro i responsabili. Per il denaro servono le procedure bancarie, la costituzione di parte civile o un'azione civile."),
   ("È possibile recuperare i soldi dopo una truffa online?", "In parte e non sempre. Dipende da come hai pagato e da quanto tempo è passato. Nessuno può garantire il risultato: una valutazione seria ti dice quali strade sono realistiche nel tuo caso."),
  ],
 },
 {
  "slug": "recuperare-soldi-truffa",
  "card": "Bonifico, carta, Postepay, PayPal, cripto: le strade per ogni metodo di pagamento.",
  "title": "Recuperare soldi truffa online: bonifico, carta, Postepay, PayPal | Act Here",
  "description": "Recuperare soldi truffati: richiamo del bonifico, chargeback su carta di credito, Postepay, PayPal, criptovalute e azione civile. Cosa è realistico e in che tempi.",
  "badge": "Recupero fondi",
  "h1": "Recuperare soldi truffati: le strade possibili, metodo per metodo",
  "lead": "La prima domanda dopo una frode è sempre la stessa: posso riavere il mio denaro? La risposta onesta dipende da due fattori: come hai pagato e quanto tempo è passato. Qui trovi le strade che esistono davvero per recuperare soldi truffa online, con i loro limiti.",
  "sections": [
   ("Per metodo di pagamento", "Recuperare soldi truffa online in base a come hai pagato", [
    ("h3", "Recuperare soldi truffa bonifico"),
    ("p", "Chiedi subito alla tua banca il richiamo del bonifico (recall). Funziona solo se la somma è ancora sul conto del beneficiario o se la banca ricevente collabora, quindi contano le ore."),
    ("h3", "Come recuperare soldi truffati con bonifico istantaneo"),
    ("p", "Il bonifico istantaneo è irrevocabile e l'accredito è immediato. Resta la richiesta di richiamo, che dipende dalla banca del beneficiario, e la segnalazione del conto come sospetto insieme alla denuncia."),
    ("h3", "Come recuperare soldi truffati con carta di credito"),
    ("p", "Con la carta puoi chiedere all'emittente la contestazione dell'addebito. Il chargeback truffa segue le regole del circuito, con termini spesso di 120 giorni. Per il chargeback investimento serve documentare che il servizio pagato non è stato reso come descritto."),
    ("h3", "Recuperare soldi truffa Postepay"),
    ("p", "Per operazioni non autorizzate si chiede il disconoscimento; per ricariche eseguite da te verso un truffatore serve un reclamo scritto. Se la risposta non arriva o è negativa, puoi ricorrere all'Arbitro Bancario Finanziario."),
    ("h3", "Recuperare soldi truffa PayPal"),
    ("p", "Apri una contestazione nel Centro risoluzioni entro 180 giorni dal pagamento. La protezione vale per gli acquisti, non per gli invii a familiari e amici."),
    ("h3", "Criptovalute"),
    ("p", "I trasferimenti non sono reversibili, ma restano tracciabili. Per il recupero fondi crypto vedi la guida sulla <a href=\"truffa-criptovalute.html\">truffa criptovalute</a>."),
   ]),
   ("Investimenti", "Recupero fondi investimento: come recuperare soldi dal broker", [
    ("p", "Il recupero fondi trading parte da tre domande: l'intermediario è autorizzato, dove ha sede e come hai versato. Se è autorizzato, presenta reclamo scritto e poi, nei limiti previsti, ricorso all'Arbitro per le Controversie Finanziarie presso la CONSOB. Se non lo è, restano le procedure bancarie e l'azione civile."),
    ("p", "Recuperare soldi truffa trading richiede prove ordinate: contratto o condizioni accettate, estratti del conto di trading, richieste di prelievo e risposte ricevute. Per il recupero fondi truffati l'azione di risarcimento si prescrive di regola in cinque anni (art. 2947 c.c.), dieci per le azioni contrattuali."),
   ]),
   ("Attenzione", "Migliori società di recupero fondi: come valutarle davvero", [
    ("p", "Chi cerca le migliori società di recupero fondi trova di tutto, comprese proposte che replicano la frode una seconda volta. Non esistono classifiche affidabili. Esistono criteri:"),
    ("ul", [
     "Ti hanno contattato loro? Un operatore serio non chiama le vittime.",
     "Promettono il risultato? Nessuno può garantire il recupero.",
     "Sono verificabili? Controlla ragione sociale, sede e, per gli avvocati, l'iscrizione all'albo.",
     "Ti spiegano per iscritto quali passi faranno, prima di iniziare?",
    ]),
   ]),
   ("Se la banca dice no", "Reclamo e Arbitro Bancario Finanziario", [
    ("p", "Il rifiuto della banca riguarda solo il canale bancario. Dopo il reclamo scritto puoi rivolgerti all'Arbitro Bancario Finanziario. Per le operazioni non autorizzate il D.Lgs. 11/2010 prevede la segnalazione senza indugio e comunque entro 13 mesi. Le pretese civili verso i responsabili restano in piedi."),
   ]),
  ],
  "faqs": [
   ("Si possono recuperare i soldi di una truffa online?", "In parte e non sempre. Le possibilità migliori riguardano carta e bonifico se ti muovi subito. Per le criptovalute serve il tracciamento. Nessuno può garantire l'esito."),
   ("Quanto tempo ho per il chargeback?", "Dipende dal circuito della carta: spesso 120 giorni dall'addebito. Chiedi subito all'emittente il termine esatto."),
   ("Il bonifico istantaneo si può annullare?", "No, è irrevocabile. Puoi chiedere il richiamo, che dipende dalla collaborazione della banca del beneficiario, e segnalare subito la frode."),
   ("Come recuperare soldi dal broker se è all'estero?", "Con reclamo scritto, procedure bancarie e, se i fatti lo consentono, azione civile nella giurisdizione competente. La sede e l'autorizzazione dell'intermediario decidono la strada."),
   ("Le società di recupero fondi sono affidabili?", "Alcune sì, molte no. Diffida di chi ti contatta per primo o garantisce il risultato, e verifica sempre l'identità di chi ti assiste."),
  ],
 },
 {
  "slug": "truffa-trading-online",
  "card": "Come riconoscere un broker truffaldino, cosa conservare e a chi rivolgersi.",
  "title": "Truffa trading online: come riconoscerla e recuperare i soldi | Act Here",
  "description": "Truffa trading online: come riconoscere un broker truffaldino, verificare gli elenchi CONSOB, conservare le prove e a chi rivolgersi per recuperare i soldi.",
  "badge": "Truffa trading",
  "h1": "Truffa trading online: riconoscerla e reagire",
  "lead": "La piattaforma mostrava profitti in crescita. Poi hai chiesto di prelevare e sono cominciati i rinvii, le nuove verifiche, il silenzio. La truffa trading online, compresa la truffa forex, usa broker falsi e schermate costruite per sembrare un vero mercato.",
  "sections": [
   ("Il copione", "Come funziona una piattaforma di trading falsa", [
    ("h3", "Truffa trading online 250 euro"),
    ("p", "Si parte quasi sempre da un piccolo versamento, spesso 250 euro, dopo un annuncio o una telefonata. Un consulente personale ti segue e ti mostra subito guadagni."),
    ("h3", "Truffa trading WhatsApp e gruppi di segnali"),
    ("p", "Nella truffa trading WhatsApp o Telegram tutto passa da una chat: segnali, testimonianze di altri membri, inviti a versare di più."),
    ("p", "In una piattaforma di trading falsa i numeri a schermo non corrispondono a operazioni reali: sono valori che il gestore può modificare. Per questo il trading forex truffa si rivela al momento del prelievo."),
   ]),
   ("Verifiche", "Come riconoscere un broker truffaldino", [
    ("ul", [
     "Non compare negli albi ufficiali, oppure usa i dati di un'altra società.",
     "Promette rendimenti certi o senza rischio.",
     "Accetta versamenti solo in criptovalute o su conti esteri che cambiano.",
     "Ti mette fretta e ti scoraggia quando vuoi prelevare.",
    ]),
    ("h3", "Broker truffa CONSOB: dove controllare"),
    ("p", "La CONSOB ordina l'oscuramento dei siti che offrono servizi di investimento senza autorizzazione e ne pubblica l'elenco. È la fonte ufficiale più vicina a una lista broker truffaldini: se il sito è lì, il quadro è chiaro."),
    ("h3", "Broker non regolamentati Italia: perché contano gli albi"),
    ("p", "Con i broker truffaldini e i broker falsi non valgono le tutele previste per gli intermediari autorizzati, come il ricorso all'Arbitro per le Controversie Finanziarie. Controlla nome, sito e contatti direttamente sul registro dell'autorità, non sul sito dell'operatore."),
   ]),
   ("Prove", "Cosa conservare prima che il sito sparisca", [
    ("h3", "App trading falsa screenshot e prove: cosa salvare"),
    ("ul", [
     "Schermate di saldo, operazioni e richieste di prelievo, con data e URL visibili.",
     "Chat ed email con il consulente, compresi numeri e nomi utente.",
     "Ricevute dei versamenti: IBAN del beneficiario, causale, indirizzi wallet e ID delle transazioni.",
     "Nome dell'app, link di download e condizioni che hai accettato.",
    ]),
   ]),
   ("Cosa fare", "Truffa trading online a chi rivolgersi", [
    ("p", "Alla banca o all'emittente della carta per richiamo e contestazione; alle forze dell'ordine per la denuncia; alla CONSOB per la segnalazione del sito. Per il denaro, un avvocato truffa trading valuta le azioni civili possibili: vedi anche la guida su come <a href=\"recuperare-soldi-truffa.html\">recuperare soldi truffati</a>."),
    ("h3", "Truffa trading online responsabilità banca"),
    ("p", "Se l'operazione non era autorizzata da te, la legge pone il rischio in larga parte sulla banca. Se il bonifico l'hai disposto tu, la responsabilità della banca viene valutata caso per caso, in genere davanti all'Arbitro Bancario Finanziario."),
   ]),
  ],
  "faqs": [
   ("Come riconoscere un broker truffaldino in pochi minuti?", "Cerca il nome esatto negli albi CONSOB e negli elenchi dei siti oscurati, confronta sito e contatti con quelli registrati e diffida di rendimenti garantiti e pressioni a versare."),
   ("Truffa trading online reato: quale norma si applica?", "Di regola l'art. 640 c.p. (truffa), a cui possono aggiungersi l'abusivismo finanziario e altri reati. La querela va presentata entro tre mesi dalla notizia del fatto."),
   ("Truffa trading recuperare soldi: è possibile?", "In parte, e dipende da metodo di pagamento e tempi. Carta e bonifico offrono le possibilità migliori se agisci subito. Nessun esito è garantito."),
   ("Esiste una lista di broker truffa?", "La fonte ufficiale è l'elenco CONSOB dei siti oscurati, insieme agli avvisi ai risparmiatori. Un broker truffa può però non comparire ancora: l'assenza dalla lista non è una garanzia."),
   ("Il broker ha sede all'estero: cambia qualcosa?", "Sì. Cambiano autorità competente e giurisdizione. È uno dei primi punti da chiarire in una valutazione del caso."),
  ],
 },
 {
  "slug": "truffa-criptovalute",
  "card": "Bitcoin e cripto: a chi rivolgersi e cosa è realistico recuperare.",
  "title": "Truffa criptovalute: a chi rivolgersi e come recuperare | Act Here",
  "description": "Truffa criptovalute e truffa bitcoin: a chi rivolgersi, come funziona il tracciamento, cosa fare con un prelievo bloccato e quando serve un avvocato esperto.",
  "badge": "Truffa criptovalute",
  "h1": "Truffa criptovalute: a chi rivolgersi e cosa si può recuperare",
  "lead": "Hai inviato bitcoin o stablecoin a una piattaforma o a una persona conosciuta online, e ora il saldo non si può prelevare. Nella truffa criptovalute il trasferimento è definitivo, ma non invisibile: ogni movimento resta su un registro pubblico.",
  "sections": [
   ("Gli schemi", "Truffa bitcoin e truffa investimenti criptovalute: come si presentano", [
    ("ul", [
     "Piattaforme di investimento con rendimenti fissi e saldo visibile solo a schermo.",
     "Contatti nati su social e app di incontri che portano a un investimento guidato: vedi la <a href=\"truffa-romance.html\">truffa romance</a>.",
     "Finti operatori di assistenza che chiedono accesso al wallet o alla frase di recupero.",
     "Token e progetti che scompaiono dopo la raccolta.",
    ]),
   ]),
   ("Primi contatti", "Truffa criptovalute a chi rivolgersi", [
    ("p", "Alle forze dell'ordine per la denuncia, indicando indirizzi wallet e ID delle transazioni. Se hai comprato le cripto con carta o bonifico, anche alla tua banca. Se i fondi sono passati da un exchange, al suo servizio di conformità con il numero di denuncia. Vale lo stesso per chi cerca truffa bitcoin a chi rivolgersi."),
   ]),
   ("Recupero", "Come recuperare criptovalute: cosa è realistico", [
    ("p", "Un'analisi forense della blockchain segue i fondi da un indirizzo all'altro fino al punto in cui vengono convertiti in denaro, di solito un exchange. Lì si concentrano le possibilità: congelamento del conto e richiesta dei dati del titolare, su ordine dell'autorità o del giudice."),
    ("p", "Recuperare criptovalute rubate dipende da tre fattori: rapidità, qualità delle prove e tipo di piattaforma su cui i fondi sono arrivati. Se si disperdono su servizi non collaborativi, le possibilità scendono. Nessuno può garantire il risultato."),
   ]),
   ("Exchange", "Prelievo bloccato su un exchange autorizzato", [
    ("p", "Un prelievo bloccato su una piattaforma autorizzata non è per forza una frode: può dipendere da controlli antiriciclaggio. Chiedi il motivo per iscritto, presenta reclamo formale e verifica che l'operatore sia autorizzato come prestatore di servizi per le cripto-attività secondo il regolamento europeo MiCA."),
   ]),
   ("Assistenza legale", "Quando serve un avvocato criptovalute", [
    ("p", "Un avvocato esperto criptovalute serve quando le somme sono rilevanti, i fondi sono tracciabili fino a un exchange o servono provvedimenti verso soggetti esteri. Chiedi sempre se ha già lavorato con analisi forensi utilizzabili in giudizio."),
   ]),
  ],
  "faqs": [
   ("Come recuperare soldi da criptovalute inviate a un truffatore?", "Con denuncia, tracciamento delle transazioni e richiesta di blocco all'exchange dove i fondi arrivano. È possibile solo in parte dei casi e richiede rapidità."),
   ("Le transazioni in bitcoin si possono annullare?", "No. Sono irreversibili, ma tracciabili: per questo il lavoro si concentra sul punto di conversione in denaro."),
   ("A chi denunciare una truffa bitcoin?", "A Polizia Postale, Carabinieri o Guardia di Finanza, allegando indirizzi wallet, ID delle transazioni e conversazioni."),
   ("Come verifico se un operatore cripto è autorizzato?", "Controlla i registri ufficiali europei e italiani dei prestatori di servizi per le cripto-attività e confronta sito e contatti con quelli registrati."),
   ("Ho comprato le cripto con carta: posso contestare l'addebito?", "Dipende dall'emittente e dal circuito. Vale la pena chiederlo subito, perché i termini sono brevi."),
  ],
 },
 {
  "slug": "avvocato-truffa-online",
  "card": "Quando serve un legale, cosa fa e come scegliere a chi affidarsi.",
  "title": "Avvocato truffa online: quando serve e cosa può fare | Act Here",
  "description": "Avvocato truffa online: querela, costituzione di parte civile, reclami ad ABF e ACF, azione civile. Quando conviene e come scegliere a chi affidarsi.",
  "badge": "Assistenza legale",
  "h1": "Avvocato truffa online: quando serve e cosa può fare",
  "lead": "Dopo la denuncia molti si chiedono se valga la pena coinvolgere un legale. Dipende dall'importo, dal metodo di pagamento e da chi c'è dall'altra parte. Qui trovi cosa fa in concreto un avvocato truffa online e dove si colloca Act Here.",
  "sections": [
   ("Quando", "Avvocato truffa: i casi in cui conviene", [
    ("ul", [
     "La somma è rilevante e la banca ha respinto richiamo o contestazione.",
     "Il pagamento è in criptovalute e i fondi sono tracciabili.",
     "La controparte è identificabile: una società, un intermediario, un conto.",
     "Ci sono più persone danneggiate dalla stessa piattaforma.",
    ]),
   ]),
   ("Cosa fa", "Dalla querela all'azione civile", [
    ("p", "Redige la denuncia-querela in modo completo, segue la costituzione di parte civile, cura i reclami e i ricorsi all'Arbitro Bancario Finanziario o all'Arbitro per le Controversie Finanziarie, e valuta l'azione civile di risarcimento."),
    ("p", "Un avvocato truffa trading o un avvocato criptovalute aggiunge la parte tecnica: verifica delle autorizzazioni, ricostruzione dei flussi, richieste ai soggetti che hanno gestito i pagamenti."),
   ]),
   ("Act Here", "Il nostro ruolo, detto con chiarezza", [
    ("p", "Act Here è uno studio di contenzioso con sede a Londra, nel Regno Unito. Seguiamo controversie finanziarie con elementi internazionali: indagini approfondite sui fatti, valutazione delle pretese civili e, dove i fatti lo consentono, azione in giudizio. Non ci limitiamo a negoziare: siamo pronti ad agire in giudizio."),
    ("p", "Per gli atti davanti all'autorità giudiziaria italiana serve un avvocato iscritto all'albo in Italia. Valutiamo con te quale giurisdizione e quale percorso sono praticabili nel tuo caso."),
   ]),
  ],
  "faqs": [
   ("Serve un avvocato per presentare denuncia?", "No, puoi farlo da solo. Un legale è utile per una querela completa e, soprattutto, per le azioni che riguardano il denaro."),
   ("Quanto costa un avvocato per una truffa online?", "In Act Here la consulenza è gratuita. Dobbiamo prima verificare la tua pretesa e capirne le prospettive e la fattibilità, e questo dipende dal livello delle prove."),
   ("Un avvocato può garantire il recupero dei soldi?", "No. Chi promette il risultato non è affidabile. Si possono valutare le strade realistiche e la loro fattibilità."),
   ("Meglio un avvocato vicino a casa?", "Conta più l'esperienza specifica della distanza: questi casi coinvolgono banche, piattaforme e soggetti esteri e si gestiscono in gran parte a distanza."),
  ],
 },
 {
  "slug": "problemi-prelievo-broker",
  "card": "Broker non paga o prelievo bloccato: cause possibili e passi da fare.",
  "title": "Problemi prelievo broker: perché non paga e cosa fare | Act Here",
  "description": "Problemi prelievo broker: perché il broker trattiene i fondi, come distinguere un ritardo da una frode e cosa fare se il prelievo è bloccato.",
  "badge": "Prelievi bloccati",
  "h1": "Problemi prelievo broker: perché non paga e cosa fare",
  "lead": "Hai chiesto il prelievo e lo stato resta in attesa. Passano i giorni, le risposte cambiano, poi smettono di arrivare. Quando un broker non paga, il modo in cui reagisci nelle prime due settimane pesa molto sul risultato.",
  "sections": [
   ("Le cause", "Perché il mio broker trattiene i fondi?", [
    ("p", "Le cause sono di due tipi. La prima è operativa: verifiche di identità incomplete, controlli antiriciclaggio, tempi della banca. Sono ritardi di giorni, con una spiegazione datata e verificabile."),
    ("p", "La seconda è diversa: il broker non ha mai avuto intenzione di pagare. In questo caso le spiegazioni cambiano a ogni richiesta e compaiono condizioni che non erano nel contratto."),
   ]),
   ("Segnali", "Broker non paga: ritardo o frode?", [
    ("ul", [
     "Un ritardo vero ha una motivazione scritta e una data. Una frode cambia versione ogni volta.",
     "Un intermediario serio risponde ai reclami. Un truffatore ti chiama per convincerti a non prelevare.",
     "Le condizioni valide sono quelle accettate all'apertura del conto, non quelle comparse dopo.",
     "L'intermediario autorizzato compare negli albi con lo stesso sito e gli stessi contatti.",
    ]),
   ]),
   ("Cosa fare", "Prelievo bloccato broker: i passi utili", [
    ("ul", [
     "Chiedi il prelievo e il motivo del blocco per iscritto, e conserva le risposte.",
     "Salva estratti del conto, schermate e conversazioni.",
     "Verifica l'autorizzazione sugli elenchi ufficiali.",
     "Presenta reclamo formale. Se l'intermediario è autorizzato puoi poi ricorrere all'Arbitro per le Controversie Finanziarie.",
     "Contatta la banca per le procedure di richiamo e contestazione e fai valutare il caso.",
    ]),
    ("h3", "Commissioni nascoste prelievo: cosa fare"),
    ("p", "Chiedi per iscritto il riferimento contrattuale, verifica l'intermediario sugli albi ufficiali e fai valutare la documentazione da un legale."),
   ]),
  ],
  "faqs": [
   ("Perché il mio broker trattiene i fondi?", "Può essere un controllo legittimo oppure un rifiuto di pagare. La differenza sta nella spiegazione: scritta, datata e stabile nel primo caso; variabile nel secondo."),
   ("Dopo quanto tempo un prelievo bloccato diventa un problema?", "Quando supera i tempi indicati nelle condizioni e non ricevi una motivazione scritta. Da quel momento conviene presentare reclamo formale."),
   ("Il broker non paga ed è autorizzato: cosa posso fare?", "Reclamo scritto e poi, nei limiti previsti, ricorso all'Arbitro per le Controversie Finanziarie. Resta sempre possibile l'azione davanti al giudice."),
   ("Il broker non è autorizzato: ho ancora possibilità?", "Sì, ma diverse: procedure bancarie, denuncia e azione civile verso i soggetti identificabili. Vedi la guida su come recuperare soldi truffati."),
  ],
 },
 {
  "slug": "truffa-romance",
  "card": "Come funziona il romance scam e cosa fare se hai inviato denaro.",
  "title": "Truffa romance scam: spiegazione, segnali e cosa fare | Act Here",
  "description": "Truffa romance: come funziona il romance scam, quali sono i segnali, cosa prevede la legge e come muoversi per provare a recuperare il denaro inviato.",
  "badge": "Truffa sentimentale",
  "h1": "Truffa romance: come funziona e cosa fare",
  "lead": "Una persona conosciuta online, settimane di messaggi quotidiani, poi una richiesta di aiuto o un'occasione di investimento. La truffa romance, detta anche truffa romantica, colpisce persone di ogni età e livello di istruzione. Non c'è nulla di cui vergognarsi, e muoversi presto fa differenza.",
  "sections": [
   ("Il meccanismo", "Truffa Romance Scam spiegazione: le fasi", [
    ("ul", [
     "Contatto su social, app di incontri o messaggio arrivato per errore.",
     "Costruzione della fiducia: attenzioni costanti, progetti comuni, mai un incontro di persona.",
     "La richiesta: un'emergenza, oppure un investimento da fare insieme.",
     "L'escalation: importi più alti, finché i soldi finiscono o nascono i dubbi.",
    ]),
    ("p", "Nella truffa romantica crypto la richiesta non è un prestito ma un investimento guidato su una piattaforma che mostra guadagni inesistenti. È lo schema descritto nella guida sulla <a href=\"truffa-criptovalute.html\">truffa criptovalute</a>."),
   ]),
   ("Segnali", "Truffa romantica online: come riconoscerla", [
    ("ul", [
     "Rifiuta videochiamate o incontri con motivi sempre nuovi.",
     "Sposta presto la conversazione su un'altra app.",
     "Parla di denaro, investimenti o difficoltà economiche.",
     "Chiede riservatezza verso amici e familiari.",
    ]),
   ]),
   ("La legge", "Truffa romantica reato: cosa dice il codice", [
    ("p", "La truffa romance scam rientra di regola nell'art. 640 c.p. Si procede a querela, da presentare entro tre mesi dalla scoperta. Conserva chat, profili, numeri e ricevute: sono la base della denuncia."),
   ]),
   ("Recupero", "Come recuperare da truffa romance il denaro inviato", [
    ("p", "Le strade sono quelle legate al metodo di pagamento: richiamo del bonifico, contestazione su carta, tracciamento delle criptovalute. Trovi i dettagli nella guida su come <a href=\"recuperare-soldi-truffa.html\">recuperare soldi truffati</a>. Diffida di chi ti contatta dopo la frode offrendo il recupero garantito."),
   ]),
  ],
  "faqs": [
   ("Cos'è il romance scam?", "Una frode in cui una persona finge un legame sentimentale online per ottenere denaro, direttamente o attraverso un falso investimento."),
   ("Come recuperare da truffa romance?", "Blocca i pagamenti, salva le prove, avvisa la banca, presenta denuncia e fai valutare le strade legate al metodo di pagamento. Il recupero è possibile solo in parte dei casi."),
   ("La truffa romantica è un reato anche se ho inviato i soldi volontariamente?", "Sì. Il consenso ottenuto con l'inganno non esclude la truffa."),
   ("Devo dirlo alla mia banca?", "Sì, subito e per iscritto: alcune procedure hanno termini di pochi giorni."),
  ],
 },
]

CHARS_BANNED = "\u2014\u2013\u201e\u201c\u201d\u2018\u2019"
WORDS_BANNED = re.compile(r"sblocc|\btass[ae]\b|svincol|anticip|acconto|caparra", re.I)

def links_strip():
    links = " &middot; ".join(f'<a href="{p["slug"]}.html" style="color:var(--sage-dark)">{esc(p["badge"])}</a>' for p in PAGES)
    return ('<section style="padding:2rem 0;background:var(--off-white)"><div class="article-body" style="max-width:760px;margin:0 auto">'
            f'<p style="color:var(--text-muted);font-size:.95rem">Guide collegate: {links}</p></div></section>')

def faq_html(faqs):
    items = "\n".join(
        f'<div style="border-bottom:1px solid var(--line);padding:1.2rem 0"><h3 style="font-size:1rem;color:var(--navy);margin-bottom:.5rem;font-weight:600">{esc(q)}</h3><p style="color:var(--text-2);font-size:.93rem;line-height:1.75;margin:0">{esc(a)}</p></div>'
        for q, a in faqs)
    return ('<section style="padding:2.5rem 0"><div class="article-body" style="max-width:760px;margin:0 auto">'
            '<h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">Domande frequenti</h2>'
            f'{items}</div></section>')

def head(title, desc, url, schema=None):
    ld = f'\n <script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=1)}\n </script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{esc(title)}</title>
 <meta name="description" content="{esc(desc)}">
 <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
 <link rel="canonical" href="{url}">
 <link rel="alternate" hreflang="it" href="{url}">
 <link rel="alternate" hreflang="x-default" href="{url}">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{esc(title)}">
 <meta property="og:description" content="{esc(desc)}">
 <meta property="og:url" content="{url}">
 <meta property="og:locale" content="it_IT">{ld}
 <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<div id="nav-placeholder"></div>
"""

FOOT = """<div id="footer-placeholder"></div>
<script src="../js/config.js"></script>
<script src="../js/layout.js"></script>
</body>
</html>
"""

CTA = """<section style="padding:3rem 0;background:var(--navy);color:#fff;text-align:center">
 <div style="max-width:640px;margin:0 auto;padding:0 5%">
 <h2 style="font-family:var(--font-serif);color:#fff;font-size:1.9rem;margin-bottom:.8rem">Hai perso denaro? Fai valutare il caso.</h2>
 <p style="color:rgba(255,255,255,.75);margin-bottom:1.5rem">Consulenza gratuita e riservata con il nostro team di contenzioso. Non ci limitiamo a negoziare: siamo pronti ad agire in giudizio.</p>
 <a href="../pages/contact.html" class="btn-primary">Prenota una consulenza gratuita</a>
 </div>
</section>
"""

def render(p):
    url = f"{BASE}{p['slug']}.html"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["description"],
         "isPartOf": {"@type": "WebSite", "name": "Act Here", "url": "https://act-here.uk/"}, "inLanguage": "it"},
        {"@type": "Article", "headline": p["title"], "description": p["description"],
         "author": {"@type": "Organization", "name": "Act Here"},
         "publisher": {"@type": "Organization", "name": "Act Here", "url": "https://act-here.uk/"},
         "dateModified": "2026-11-17", "inLanguage": "it"},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://act-here.uk/"},
            {"@type": "ListItem", "position": 2, "name": "Guide", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": p["badge"], "item": url}]},
    ]}
    body = (f'<div class="breadcrumb"><a href="../index.html">Home</a><span>&#8250;</span><a href="index.html">Guide</a><span>&#8250;</span> {esc(p["badge"])}</div>\n'
            f'<div class="page-hero">\n <div class="hero-badge">{esc(p["badge"])} &middot; {UPDATED}</div>\n <h1>{esc(p["h1"])}</h1>\n <p>{esc(p["lead"])}</p>\n</div>\n'
            + "\n".join(render_section(*s) for s in p["sections"]) + "\n" + links_strip() + "\n" + faq_html(p["faqs"]) + "\n" + CTA)
    return head(p["title"], p["description"], url, schema) + body + FOOT

def render_index():
    cards = "\n".join(
        f'<div style="border:1px solid var(--line);border-radius:8px;padding:1.5rem;background:#fff"><h3 style="font-family:var(--font-serif);font-size:1.1rem;margin-bottom:.5rem"><a href="{p["slug"]}.html" style="color:var(--navy);text-decoration:none">{esc(p["h1"])}</a></h3><p style="color:var(--text-2);font-size:.88rem;line-height:1.65;margin:0">{esc(p["card"])}</p></div>'
        for p in PAGES)
    title = "Truffe online e investimenti: guide in italiano | Act Here"
    desc = "Guide in italiano su truffa online, truffa trading, truffa criptovalute, prelievi bloccati e recupero dei soldi, a cura di uno studio di contenzioso del Regno Unito."
    body = ('<div class="breadcrumb"><a href="../index.html">Home</a><span>&#8250;</span> Guide</div>\n'
            '<div class="page-hero">\n <div class="hero-badge">Italiano</div>\n <h1>Truffe online e investimenti: guide pratiche</h1>\n'
            ' <p>Cosa fare, a chi rivolgersi e quali strade esistono per recuperare il denaro.</p>\n</div>\n'
            '<section style="padding:2.5rem 0"><div style="max-width:1100px;margin:0 auto;padding:0 5%;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem">\n'
            f'{cards}\n</div></section>\n' + CTA)
    return head(title, desc, BASE) + body + FOOT

def main():
    out = {p["slug"] + ".html": render(p) for p in PAGES}
    out["index.html"] = render_index()
    problems = []
    for name, html in out.items():
        bad = sorted(set(c for c in html if c in CHARS_BANNED))
        if bad:
            problems.append(f"{name}: banned characters {bad}")
        hit = WORDS_BANNED.search(html)
        if hit:
            problems.append(f"{name}: banned wording '{hit.group(0)}'")
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            json.loads(m.group(1))
    if problems:
        sys.exit("BUILD FAILED\n" + "\n".join(problems))
    for name, html in out.items():
        with open(os.path.join(IT, name), "w", encoding="utf-8") as f:
            f.write(html)
    print(f"wrote {len(out)} files to it/ (copy rules passed, JSON-LD valid)")

if __name__ == "__main__":
    main()
