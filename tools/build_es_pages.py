#!/usr/bin/env python3
"""Build the Spanish victim-intent cluster under /es/.
Copy rules enforced at build time: no em/en dashes, no smart quotes, no fee-to-release
or pay-first wording, no fee structures, no broker names. Fails the build if a rule is broken."""
import os, re, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_de_pages import esc, render_section

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES = os.path.join(ROOT, "es")
BASE = "https://act-here.uk/es/"
UPDATED = "Actualizado en noviembre de 2026"

FREE = "La consulta es gratuita. Primero tenemos que validar su reclamación y entender sus perspectivas y su viabilidad, y eso depende del nivel de prueba."
FREE_Q = "¿Cuánto cuesta la consulta con Act Here?"
ARCHIVE = '<a href="../reviews/index.html">archivo de análisis</a>'

PAGES = [
 {
  "slug": "estafa-online",
  "card": "Qué hacer en las primeras horas, a quién acudir y cómo denunciar.",
  "title": "Estafa online: qué hacer, a quién acudir y cómo denunciar | Act Here",
  "description": "Estafa online: qué hacer en las primeras horas, a quién acudir, cómo denunciar ante Policía Nacional o Guardia Civil y qué vías existen para recuperar el dinero.",
  "keywords": "estafa online, estafa online que hacer, denunciar estafa online, estafa inversiones, a quien acudir estafa",
  "badge": "Estafa online",
  "h1": "Estafa online: qué hacer y a quién acudir",
  "lead": "Ha pagado por una inversión, un servicio o una compra que no existía, y al otro lado ya no responde nadie. En una estafa online lo que más pesa es la rapidez: los plazos bancarios son cortos y las pruebas se pierden. Esta guía explica qué hacer primero, dónde denunciar y cómo se pasa de la denuncia a la reclamación del dinero.",
  "sections": [
   ("Primeros pasos", "Estafa online: qué hacer en las primeras 48 horas", [
    ("ul", [
     "Deje de enviar dinero a la plataforma y a cualquiera que diga actuar en su nombre.",
     "Guarde las pruebas: capturas de la web y de la cuenta, chats, correos, justificantes, IBAN del beneficiario, direcciones de monedero y las URL exactas.",
     "Llame a su banco o al emisor de la tarjeta: la retrocesión de una transferencia y la devolución de un cargo tienen plazos cortos.",
     "Presente denuncia: deja constancia de los hechos y la necesitará ante el banco, el seguro y en una acción civil.",
     "Cambie las contraseñas y revise los accesos a su banca en línea si compartió datos o instaló alguna aplicación.",
    ]),
   ]),
   ("Denuncia", "Denunciar estafa online: dónde y cómo", [
    ("p", "Para denunciar estafa online puede acudir a una comisaría de la Policía Nacional, a un cuartel de la Guardia Civil o al juzgado de guardia. La denuncia tiene el mismo valor en los tres casos y no exige abogado."),
    ("h3", "Denuncia estafa Policía Nacional"),
    ("p", "La Policía Nacional recibe la denuncia en comisaría y dispone de un canal en línea para determinados hechos, que en algunos casos exige ratificarla después de forma presencial. Lleve su documento de identidad, una cronología, los datos de los pagos y las pruebas en un soporte digital."),
    ("h3", "Denuncia Guardia Civil estafa"),
    ("p", "La Guardia Civil recibe denuncias en sus cuarteles y cuenta con unidades especializadas en delitos telemáticos. Si reside en su demarcación, suele ser la vía más directa."),
    ("h3", "Estafa online: a quién acudir además de la policía"),
    ("p", "El 017 de INCIBE orienta sobre incidentes de ciberseguridad. Si los hechos afectan a una entidad financiera, la CNMV y el Banco de España reciben reclamaciones y comunicaciones. Tenga presente que la denuncia persigue a los responsables, pero no devuelve por sí sola el dinero."),
   ]),
   ("Formas habituales", "Estafa de las inversiones, chiringuito financiero y otras variantes", [
    ("p", "La estafa de las inversiones es la variante que más dinero mueve: promete rentabilidades altas con trading, forex o criptomonedas. La CNMV llama chiringuito financiero a la entidad que ofrece servicios de inversión sin autorización. En Latinoamérica se habla más de fraude de inversiones, pero el esquema es el mismo."),
    ("ul", [
     'Plataformas de inversión y brókeres sin licencia: vea la guía sobre <a href="estafa-trading-broker.html">estafa trading y bróker no regulado</a>.',
     'Monederos, exchanges clonados y grupos de mensajería: vea la guía sobre <a href="estafa-criptomonedas.html">estafa criptomonedas</a>.',
     'Relaciones en línea que terminan en una inversión: vea la guía sobre <a href="estafa-sentimental-criptomonedas.html">estafa sentimental con criptomonedas</a>.',
    ]),
   ]),
   ("Después de denunciar", "De la denuncia a la reclamación del dinero", [
    ("p", "La denuncia abre el proceso penal. En ese proceso puede personarse como acusación particular y reclamar la responsabilidad civil derivada del delito. En paralelo hay que trabajar la vía bancaria, que es la que tiene los plazos más cortos."),
    ("p", 'Para recuperar dinero estafa online conviene ordenar el caso por medio de pago. Lo explicamos paso a paso en la guía para <a href="recuperar-dinero-estafa.html">recuperar dinero estafado</a>.'),
   ]),
  ],
  "faqs": [
   ("Estafa online: ¿qué hacer primero?", "Deje de enviar dinero, guarde todas las pruebas, avise de inmediato a su banco o al emisor de la tarjeta y presente denuncia. Después haga valorar el caso: los plazos de retrocesión y de devolución de cargos son cortos."),
   ("Estafa online: ¿a quién acudir?", "A la Policía Nacional, a la Guardia Civil o al juzgado de guardia para la denuncia, y a su banco para las vías de devolución. El 017 de INCIBE orienta sobre ciberseguridad. Si interviene una entidad financiera, también a la CNMV o al Banco de España."),
   ("¿Cuánto tiempo tengo para denunciar una estafa online?", "La estafa es un delito perseguible durante años, pero los plazos bancarios son mucho más cortos y empiezan a contar desde el pago. Por eso conviene denunciar y avisar al banco de inmediato."),
   ("¿La denuncia me devuelve el dinero?", "No por sí sola. La denuncia inicia el proceso penal contra los responsables. Para el dinero hacen falta las vías bancarias, la personación como acusación particular o una acción civil."),
   ("¿Qué es un chiringuito financiero?", "Es el término que usa la CNMV para las entidades que ofrecen servicios de inversión sin estar autorizadas. La CNMV publica advertencias sobre ellas en su web."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "recuperar-dinero-estafa",
  "card": "Transferencia, tarjeta, Bizum, PayPal y cripto: las vías según el medio de pago.",
  "title": "Recuperar dinero estafa online: tarjeta, Bizum, cripto | Act Here",
  "description": "Recuperar dinero estafado: qué vías existen según el medio de pago. Transferencia, tarjeta, Bizum, PayPal y criptomonedas, con plazos y pasos concretos.",
  "keywords": "recuperar dinero estafa, recuperar dinero estafado, reclamar dinero estafa online",
  "badge": "Recuperar dinero estafado",
  "h1": "Recuperar dinero estafado: las vías según el medio de pago",
  "lead": "Recuperar dinero estafa online no depende de un solo trámite. Depende de cómo pagó, de cuánto tiempo ha pasado y de las pruebas que conserva. Nadie puede garantizar el resultado, pero ordenar el caso por medio de pago permite saber qué vías siguen abiertas.",
  "sections": [
   ("Por medio de pago", "Recuperar dinero estafado según cómo pagó", [
    ("h3", "Recuperar transferencia estafa"),
    ("p", "Avise a su banco de inmediato y pida la retrocesión de la transferencia. Si los fondos siguen en la cuenta de destino, la entidad receptora puede retenerlos. La transferencia inmediata es irrevocable, pero comunicar el fraude cuanto antes sigue siendo decisivo."),
    ("h3", "Recuperar dinero estafa banco: la reclamación"),
    ("p", "Si el banco rechaza su solicitud, presente una reclamación ante su servicio de atención al cliente. Sin respuesta satisfactoria puede acudir al Banco de España. Para las operaciones no autorizadas, el Real Decreto-ley 19/2018 exige comunicarlas sin demora y, como máximo, en 13 meses."),
    ("h3", "Recuperar dinero tarjeta estafa"),
    ("p", "Pida al emisor la devolución del cargo (chargeback). El plazo depende de la red de la tarjeta y suele rondar los 120 días. Solicite el plazo exacto por escrito y aporte la denuncia."),
    ("h3", "Recuperar dinero Bizum estafa"),
    ("p", "Un Bizum entre particulares se abona al instante y no puede anularse desde la aplicación. Contacte con su banco de inmediato, comunique el fraude y aporte la denuncia. Cuanto antes lo haga, más opciones hay de que los fondos sigan localizables."),
    ("h3", "PayPal"),
    ("p", "Abra una disputa en el Centro de resoluciones dentro de los 180 días siguientes al pago. La protección cubre las compras, no los envíos a familiares y amigos."),
    ("h3", "Recuperar criptomonedas estafadas y recuperar bitcoin estafa"),
    ("p", 'Las transacciones quedan registradas en la cadena de bloques y se pueden rastrear hasta la plataforma donde se convierten en dinero. El rastro no devuelve los fondos por sí solo, pero es la base de cualquier reclamación. Lo detallamos en la guía sobre <a href="estafa-criptomonedas.html">estafa criptomonedas</a>.'),
   ]),
   ("Si pagó a un bróker", "Cómo recuperar mi dinero de un bróker", [
    ("p", "Cómo recuperar dinero del bróker depende de si la entidad está autorizada. Con un bróker regulado: reclamación ante su servicio de atención al cliente y, después, ante el supervisor. Con uno no regulado: vías bancarias, denuncia y acción civil contra los responsables identificables."),
    ("h3", "Recuperación de fondos: qué pruebas hacen falta"),
    ("p", "Contrato o condiciones aceptadas, extractos de la cuenta de trading, solicitudes de retiro y respuestas recibidas, justificantes de cada pago y todas las conversaciones."),
    ("h3", "Reembolso inversión: plazos para reclamar"),
    ("p", "En derecho español, la acción por responsabilidad extracontractual prescribe en un año (art. 1968 del Código Civil) y las acciones personales contractuales en cinco (art. 1964). Si la entidad está en otro país, pueden aplicarse otros plazos y otra jurisdicción."),
   ]),
   ("Atención", "Empresas recuperación de fondos estafa: cómo valorarlas", [
    ("p", "Quien busca empresas de recuperación de fondos o los mejores servicios de recuperación encuentra de todo, incluidas ofertas que repiten el fraude por segunda vez. No existen clasificaciones fiables. Existen criterios:"),
    ("ul", [
     "¿Le contactaron ellos? Un profesional serio no llama a las víctimas.",
     "¿Prometen el resultado? Nadie puede garantizar la recuperación.",
     "¿Son verificables? Compruebe razón social, domicilio y, si son abogados, su colegiación.",
     "¿Le explican por escrito qué pasos van a dar antes de empezar?",
    ]),
   ]),
  ],
  "faqs": [
   ("¿Se puede recuperar el dinero de una estafa online?", "En parte y no siempre. Las mejores opciones están en la tarjeta y la transferencia si actúa de inmediato. En criptomonedas hace falta el rastreo. Nadie puede garantizar el resultado."),
   ("¿Cuánto tiempo tengo para reclamar un cargo en la tarjeta?", "Depende de la red de la tarjeta: con frecuencia, 120 días desde el cargo. Pida a su emisor el plazo exacto cuanto antes."),
   ("¿Se puede anular un Bizum enviado a un estafador?", "No desde la aplicación: el abono es inmediato. Lo que sí puede hacer es comunicar el fraude a su banco de inmediato y aportar la denuncia."),
   ("¿Cómo recuperar mi dinero de un bróker que está en el extranjero?", "Con reclamación escrita, vías bancarias y, si los hechos lo permiten, una acción civil en la jurisdicción competente. La sede y la autorización de la entidad determinan el camino."),
   ("¿Son fiables las empresas de recuperación de fondos?", "Algunas sí, muchas no. Desconfíe de quien le contacta primero o garantiza el resultado, y verifique siempre la identidad de quien le asiste."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "estafa-trading-broker",
  "card": "Bróker no regulado, advertencias de la CNMV y cómo reclamar.",
  "title": "Estafa trading y estafa bróker: avisos de la CNMV | Act Here",
  "description": "Estafa trading: cómo funciona, cómo comprobar si un bróker no regulado figura en las advertencias de la CNMV, cómo denunciar y qué vías hay para reclamar.",
  "keywords": "estafa trading, broker no regulado, estafa broker, plataforma trading estafa",
  "badge": "Estafa trading",
  "h1": "Estafa trading y bróker no regulado: cómo actuar",
  "lead": "La estafa trading sigue casi siempre el mismo guion: un primer depósito pequeño, un panel que muestra beneficios y un retiro que nunca llega. Aquí explicamos cómo funciona, qué dice la CNMV sobre las entidades sin licencia y qué pasos dar si ya ha invertido.",
  "sections": [
   ("El esquema", "Estafa trading: cómo funciona paso a paso", [
    ("ul", [
     "El contacto llega por un anuncio, una llamada o un grupo de mensajería. La estafa WhatsApp trading empieza a menudo con un supuesto asesor que comparte señales.",
     "Se pide un primer depósito reducido y se asigna un gestor de cuenta.",
     "La plataforma de trading falsa muestra operaciones ganadoras en forex, índices o criptomonedas. La estafa forex es la versión más antigua de este modelo.",
     "El gestor presiona para aumentar el capital.",
     "Al pedir el retiro aparecen excusas, nuevas condiciones o silencio.",
    ]),
    ("p", "Detrás puede haber un bróker falso que no existe como empresa, un clon que imita a una entidad real o una app de trading falsa distribuida fuera de las tiendas oficiales."),
   ]),
   ("Supervisión", "Bróker no regulado España: qué dice la CNMV", [
    ("p", 'Para prestar servicios de inversión en España hace falta autorización. La CNMV publica advertencias sobre entidades no autorizadas, los llamados chiringuitos financieros. Quien busca "lista brokers estafadores CNMV" encontrará ese listado de entidades advertidas en la web del supervisor. Que una entidad no figure en él no demuestra que sea fiable.'),
    ("h3", "Brókeres no regulados y licencias de otros países"),
    ("p", "Una entidad autorizada en otro país de la Unión Europea puede operar en España con pasaporte europeo y aparece en los registros de la CNMV. Una licencia de fuera de la Unión no basta para captar clientes minoristas en España."),
   ]),
   ("Denuncia", "Denunciar bróker ante CNMV", [
    ("p", "Si la entidad está supervisada, reclame primero ante su servicio de atención al cliente y, sin respuesta satisfactoria, ante el Servicio de Reclamaciones de la CNMV. Si no está autorizada, puede comunicarlo a la CNMV, que valora publicar una advertencia, y debe presentar denuncia ante la Policía Nacional o la Guardia Civil."),
    ("p", "La CNMV no recupera el dinero de los afectados. Para eso están las vías bancarias y judiciales."),
   ]),
   ("Reclamar", "Estafa bróker: recuperar el dinero", [
    ("p", 'Las vías dependen del medio de pago y del tiempo transcurrido. Las reunimos en la guía para <a href="recuperar-dinero-estafa.html">recuperar dinero estafado</a>. Si el problema es que no puede retirar, vea <a href="broker-no-deja-retirar.html">mi bróker no me deja retirar</a>.'),
    ("p", f"Si quiere consultar una plataforma concreta, puede buscarla por nombre en nuestro {ARCHIVE}."),
   ]),
  ],
  "faqs": [
   ("¿Cómo sé si estoy ante una estafa de trading?", "Las señales habituales son la rentabilidad prometida, la presión para depositar más, el contacto por mensajería y un retiro que no se completa. Compruebe siempre la autorización de la entidad en los registros oficiales."),
   ("¿Dónde consulto las advertencias de la CNMV sobre chiringuitos financieros?", "En la web de la CNMV, en el apartado de advertencias sobre entidades no autorizadas. También puede consultar allí el registro de entidades autorizadas."),
   ("¿Puedo denunciar a un bróker ante la CNMV?", "Sí. Si está supervisado, mediante reclamación tras acudir a su servicio de atención al cliente. Si no está autorizado, mediante comunicación a la CNMV, además de la denuncia ante la policía."),
   ("¿Qué hago si el bróker está fuera de España?", "Cambian la autoridad competente y la jurisdicción. Es uno de los primeros puntos que hay que aclarar al valorar el caso."),
   ("¿Puede ayudarme un abogado estafa trading?", "Puede ordenar las pruebas, comprobar autorizaciones, reconstruir los pagos y valorar las vías bancarias y judiciales. Ningún abogado puede garantizar el resultado."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "estafa-criptomonedas",
  "card": "Formas habituales, rastreo de fondos y qué pruebas guardar.",
  "title": "Estafa criptomonedas: qué hacer y cómo reclamar | Act Here",
  "description": "Estafa criptomonedas: plataformas falsas, exchanges clonados y grupos de Instagram o Telegram. Cómo se rastrean los fondos y qué opciones hay para reclamar.",
  "keywords": "estafa criptomonedas, estafa bitcoin, estafa crypto, estafa inversiones cripto",
  "badge": "Estafa criptomonedas",
  "h1": "Estafa criptomonedas: qué hacer y cómo seguir el rastro",
  "lead": "En una estafa criptomonedas el dinero sale de su control en minutos, pero deja un rastro público y permanente. Ese rastro es el punto de partida. Esta guía explica las formas más frecuentes, qué se puede hacer con el rastreo y qué debe conservar desde el primer día.",
  "sections": [
   ("Formas habituales", "Estafa criptomonedas: cómo se presenta", [
    ("ul", [
     "Plataformas de inversión con un panel de beneficios que solo existe en pantalla.",
     "Exchanges clonados que copian el nombre y el diseño de uno real.",
     "Estafa criptomonedas Instagram Telegram: perfiles y grupos que ofrecen señales, gestión de cartera o acceso a una preventa.",
     "Anuncios con famosos generados con inteligencia artificial.",
     'Relaciones en línea que derivan en una inversión: vea la guía sobre <a href="estafa-sentimental-criptomonedas.html">estafa sentimental con criptomonedas</a>.',
    ]),
   ]),
   ("Rastreo", "Recuperar criptomonedas estafadas: qué es posible", [
    ("p", "Cada envío queda registrado en la cadena de bloques. Un análisis forense sigue los fondos desde su monedero hasta la plataforma donde se convierten en dinero. Esas plataformas identifican a sus clientes y pueden colaborar con las autoridades y con los tribunales."),
    ("p", "Recuperar bitcoin estafa no es automático: el rastro muestra adónde fue el dinero, no lo devuelve por sí solo. Sirve para dirigir la denuncia, las solicitudes a las plataformas y, en su caso, una acción civil."),
   ]),
   ("Pruebas", "Qué conservar desde el primer día", [
    ("ul", [
     "Identificadores de cada transacción (TXID) y direcciones de monedero de origen y de destino.",
     "Capturas del panel, del saldo mostrado y de cada solicitud de retiro.",
     "Conversaciones completas, con nombres de usuario y números de teléfono.",
     "Justificantes de la compra de las criptomonedas con tarjeta o transferencia.",
     "La URL exacta de la plataforma y, si la hubo, el archivo de la aplicación instalada.",
    ]),
   ]),
   ("Supervisión", "Proveedores de criptoactivos: cómo comprobarlos", [
    ("p", "Con el reglamento europeo MiCA, los proveedores de servicios de criptoactivos necesitan autorización para operar en la Unión Europea. Compruebe en los registros oficiales si el proveedor figura como autorizado. La CNMV también incluye plataformas de criptoactivos en sus advertencias."),
   ]),
   ("Ayuda legal", "Abogado criptomonedas: cuándo tiene sentido", [
    ("p", 'Un abogado criptomonedas aporta la parte técnica: lectura del rastreo, solicitudes a las plataformas y medidas ante los tribunales. Si busca un abogado experto criptomonedas, compruebe su colegiación y pida que le explique por escrito qué pasos propone. Más detalle en la guía sobre <a href="abogado-estafa-online.html">abogado estafa online</a>.'),
   ]),
  ],
  "faqs": [
   ("¿Se pueden recuperar las criptomonedas estafadas?", "A veces y en parte. Depende de que el rastro lleve a una plataforma identificable y de la rapidez con que se actúe. Nadie puede garantizarlo."),
   ("¿Sirve de algo denunciar una estafa con criptomonedas?", "Sí. La denuncia deja constancia, permite a las autoridades pedir información a las plataformas y es necesaria para las vías bancarias y judiciales."),
   ("Compré las criptomonedas con tarjeta: ¿puedo reclamar al banco?", "Puede comunicar el fraude y pedir la devolución del cargo. El resultado depende del emisor y de las circunstancias de la compra."),
   ("¿Cómo sé si un exchange es un clon?", "Compare el dominio y los datos de contacto con los que figuran en los registros oficiales y en la web auténtica. Un dominio parecido pero distinto es la señal más clara."),
   ("¿Qué es una estafa de criptomonedas por Instagram o Telegram?", "Es la que empieza en un perfil o un grupo que ofrece señales o inversiones y dirige a una plataforma controlada por los propios estafadores."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "broker-no-deja-retirar",
  "card": "Retiro bloqueado o pendiente: cómo distinguir un control de una negativa.",
  "title": "Mi bróker no me deja retirar: qué hacer | Act Here",
  "description": "Mi bróker no me deja retirar dinero: por qué ocurre, cómo distinguir un control legítimo de una negativa a pagar y qué pasos dar con un retiro bloqueado.",
  "keywords": "broker no deja retirar, retiro bloqueado broker, no puedo retirar del broker",
  "badge": "Bróker no deja retirar",
  "h1": "Mi bróker no me deja retirar dinero: pasos a seguir",
  "lead": "Ha pedido el retiro y no llega. Soporte responde con plantillas o no responde. Antes de sacar conclusiones conviene distinguir dos situaciones muy distintas, porque los pasos no son los mismos.",
  "sections": [
   ("Las dos situaciones", "Por qué mi bróker no me deja retirar", [
    ("p", "La primera es un control legítimo: verificación de identidad pendiente, condiciones de un bono aceptado o una incidencia técnica. En ese caso la explicación es escrita, tiene fecha y no cambia."),
    ("p", "La segunda es distinta: el bróker no paga porque nunca tuvo intención de hacerlo. Las explicaciones cambian con cada solicitud y aparecen condiciones que no estaban en el contrato. Es lo que muchos afectados describen como retención de fondos bróker."),
   ]),
   ("Señales", "Retiro bloqueado bróker o retiro pendiente bróker: cómo distinguirlos", [
    ("ul", [
     "Un retiro pendiente tiene un plazo indicado en las condiciones y un estado que avanza.",
     "Un retiro bloqueado no tiene plazo, o el plazo se reinicia cada vez que pregunta.",
     "Si el gestor de cuenta desaparece justo después de la solicitud, es una mala señal.",
     "Si la entidad no figura en los registros oficiales, trate el caso como urgente.",
    ]),
   ]),
   ("Qué hacer", "El bróker me da largas para retirar: pasos concretos", [
    ("ul", [
     "Pida por escrito el motivo del retraso y la fecha prevista.",
     "Guarde extractos de la cuenta, capturas y conversaciones.",
     "Compruebe la autorización de la entidad en los registros oficiales.",
     "Presente una reclamación formal. Si la entidad está supervisada, después puede acudir al supervisor.",
     "Contacte con su banco para las vías de retrocesión y devolución, y haga valorar el caso.",
    ]),
    ("h3", "Comisiones ocultas retiro: qué hacer"),
    ("p", "Pida por escrito la cláusula del contrato en la que se apoyan, compruebe la entidad en los registros oficiales y haga revisar la documentación por un abogado."),
   ]),
   ("Regulado o no", "Problema retiro bróker: por qué importa la licencia", [
    ("p", 'Con una entidad autorizada existen reclamación interna, supervisor y tribunales. Con una no autorizada quedan las vías bancarias, la denuncia y la acción civil contra los responsables identificables. Puede comprobarlo con la guía sobre <a href="como-saber-si-un-broker-es-fiable.html">cómo saber si un bróker es fiable</a>.'),
    ("p", f'Las vías de reclamación están en la guía para <a href="recuperar-dinero-estafa.html">recuperar dinero estafado</a>. Si quiere consultar una plataforma concreta, búsquela por nombre en nuestro {ARCHIVE}.'),
   ]),
  ],
  "faqs": [
   ("¿Por qué mi bróker no me deja retirar?", "Puede ser un control legítimo o una negativa a pagar. La diferencia está en la explicación: escrita, con fecha y estable en el primer caso; cambiante en el segundo."),
   ("Mi bróker no me deja retirar dinero: ¿cuándo es un problema serio?", "Cuando se superan los plazos de las condiciones y no recibe un motivo por escrito. A partir de ahí conviene presentar una reclamación formal."),
   ("El bróker no paga y está autorizado: ¿qué puedo hacer?", "Reclamación escrita ante su servicio de atención al cliente y, después, ante el supervisor. Siempre queda la vía judicial."),
   ("El bróker no está regulado: ¿tengo opciones?", "Sí, pero distintas: vías bancarias, denuncia y acción civil contra los responsables identificables."),
   ("¿Cuánto tarda normalmente un retiro?", "Lo que indiquen las condiciones de la entidad. Un retraso sin explicación escrita es el momento de reclamar."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "abogado-estafa-online",
  "card": "Qué hace un abogado en estos casos y dónde encaja Act Here.",
  "title": "Abogado estafa online: denuncia, reclamación y acción civil | Act Here",
  "description": "Abogado estafa online: qué hace en la denuncia, la acusación particular, las reclamaciones ante supervisores y la acción civil. Cuándo conviene y cómo elegir.",
  "keywords": "abogado estafa online, abogado estafa inversiones, asistencia legal estafa",
  "badge": "Abogado estafa online",
  "h1": "Abogado estafa online: qué hace y cuándo conviene",
  "lead": "Después de la denuncia, muchos afectados se preguntan si merece la pena acudir a un abogado. Depende del importe, del medio de pago y de quién esté al otro lado. Aquí explicamos qué hace en concreto un abogado estafa online y dónde encaja Act Here.",
  "sections": [
   ("Cuándo conviene", "Situaciones en las que tiene sentido", [
    ("ul", [
     "El importe es relevante para su economía.",
     "El banco ha rechazado la retrocesión o la devolución del cargo.",
     "El pago fue en criptomonedas y los fondos son rastreables.",
     "La entidad está en otro país o hay varias sociedades implicadas.",
     "Hay más afectados por la misma plataforma.",
    ]),
   ]),
   ("Qué hace", "El trabajo de un abogado en una estafa online", [
    ("p", "Redacta la denuncia o la querella de forma completa, le representa como acusación particular en el proceso penal, prepara las reclamaciones ante el Banco de España o la CNMV y valora la acción civil de daños."),
    ("p", "Un abogado estafa trading o un abogado criptomonedas añade la parte técnica: comprobación de autorizaciones, reconstrucción de los pagos y solicitudes a las entidades que los tramitaron. Si busca un abogado experto criptomonedas, pida que le explique cómo va a utilizar el rastreo."),
   ]),
   ("Act Here", "Dónde encaja nuestro despacho", [
    ("p", "Act Here es un despacho de litigios con sede en Londres. No somos una agencia de recuperación. Hacemos una investigación a fondo de los hechos y estamos preparados para litigar cuando los hechos lo respaldan. Gestionamos tanto acuerdos como procedimientos judiciales."),
    ("p", "Muchas plataformas operan desde fuera de España, con sociedades y cuentas en varios países. Ahí es donde un despacho de litigios internacional puede aportar. Las actuaciones ante los tribunales españoles requieren un abogado colegiado en España."),
   ]),
   ("Cómo elegir", "Criterios para decidir a quién confiar el caso", [
    ("ul", [
     "Compruebe la colegiación y la identidad del despacho.",
     "Pida por escrito qué pasos propone y por qué.",
     "Desconfíe de quien le contacta tras el fraude ofreciendo una recuperación garantizada.",
     "Pregunte qué pruebas necesita y qué opciones ve como realistas.",
    ]),
   ]),
  ],
  "faqs": [
   ("¿Cuánto cuesta un abogado para una estafa online?", "En Act Here la consulta es gratuita. Primero tenemos que validar su reclamación y entender sus perspectivas y su viabilidad, y eso depende del nivel de prueba."),
   ("¿Un abogado puede garantizar que recuperaré el dinero?", "No. Quien promete el resultado no es fiable. Lo que se puede hacer es valorar las vías realistas y su viabilidad."),
   ("¿Necesito abogado para denunciar una estafa online?", "No. La denuncia puede presentarla usted mismo. Para personarse como acusación particular en el proceso penal sí hacen falta abogado y procurador."),
   ("¿Act Here puede actuar en España?", "Act Here es un despacho de litigios con sede en Londres. Valoramos el caso, las pruebas y la jurisdicción. Las actuaciones ante los tribunales españoles requieren un abogado colegiado en España."),
   ("¿Qué documentos debo preparar antes de la consulta?", "Cronología de los hechos, justificantes de los pagos, conversaciones, capturas de la plataforma y copia de la denuncia si ya la ha presentado."),
  ],
 },
 {
  "slug": "estafa-sentimental-criptomonedas",
  "card": "Pig butchering, apps de citas y vídeos falsos: cómo funciona y qué hacer.",
  "title": "Estafa sentimental criptomonedas y pig butchering | Act Here",
  "description": "Estafa sentimental con criptomonedas: qué es la estafa romance, cómo funciona el pig butchering o matanza del cerdo y qué hacer para denunciar y reclamar.",
  "keywords": "estafa sentimental criptomonedas, estafa romantica crypto, pig butchering",
  "badge": "Estafa sentimental",
  "h1": "Estafa sentimental con criptomonedas: cómo funciona y qué hacer",
  "lead": "La estafa sentimental criptomonedas combina dos cosas: una relación construida durante semanas y una plataforma de inversión falsa. Quien la sufre no ha sido ingenuo. Ha tratado con personas que se dedican a esto de forma profesional.",
  "sections": [
   ("Definición", "Qué es la estafa romance", [
    ("p", "La estafa romance es un fraude en el que alguien finge una relación afectiva para obtener dinero. En su versión actual, la petición no es directa: la otra persona propone invertir juntos en una plataforma que controla."),
   ]),
   ("El método", "Pig butchering: la matanza del cerdo estafa, fase a fase", [
    ("p", 'Los medios en español la llaman "matanza del cerdo estafa" porque la víctima es "engordada" antes del golpe final.'),
    ("ul", [
     "Contacto: un mensaje aparentemente equivocado o una coincidencia en una app de citas.",
     "Confianza: semanas de conversación diaria, sin pedir nada.",
     "Propuesta: la persona muestra sus ganancias y enseña a invertir con una cantidad pequeña.",
     "Aumento: la plataforma muestra beneficios y la víctima invierte cada vez más.",
     "Cierre: el retiro no se completa y el contacto desaparece.",
    ]),
   ]),
   ("Canales", "Estafa Tinder criptomonedas y otros puntos de contacto", [
    ("p", "La estafa Tinder criptomonedas es la más conocida, y de ahí la expresión popular timador Tinder, pero el mismo método se usa en otras apps de citas, en Instagram, en Telegram y en WhatsApp. La conversación suele pasar pronto a una aplicación de mensajería privada."),
    ("h3", "Deepfake estafa inversiones y estafa inteligencia artificial inversiones"),
    ("p", "La inteligencia artificial ha añadido vídeos falsos de personas conocidas recomendando inversiones y videollamadas con el rostro alterado. Un vídeo o una llamada ya no prueban que la persona sea quien dice ser."),
   ]),
   ("Señales", "Cómo reconocerla a tiempo", [
    ("ul", [
     "Nunca hay un encuentro en persona, siempre surge un impedimento.",
     "La inversión se hace en una web o app que usted no conocía.",
     "Le piden discreción con familia, amigos o el banco.",
     "La app de trading falsa se instala desde un enlace y no desde la tienda oficial.",
    ]),
   ]),
   ("Reclamar", "Cómo recuperar dinero de estafa romance", [
    ("p", 'Las vías son las del medio de pago: retrocesión de la transferencia, devolución del cargo de la tarjeta y rastreo de las criptomonedas. Están explicadas en la guía para <a href="recuperar-dinero-estafa.html">recuperar dinero estafado</a>. Desconfíe de quien le contacte después ofreciendo una recuperación garantizada.'),
    ("p", "Corte el contacto, conserve todas las conversaciones sin borrarlas y presente denuncia. Las conversaciones son la prueba principal."),
   ]),
  ],
  "faqs": [
   ("¿Qué es la estafa romance?", "Es un fraude en el que alguien finge una relación afectiva para obtener dinero, hoy casi siempre a través de una supuesta inversión en criptomonedas."),
   ("¿Qué es el pig butchering o matanza del cerdo?", "Es el nombre del método: ganarse la confianza de la víctima durante semanas, llevarla a invertir en una plataforma falsa y desaparecer cuando pide el retiro."),
   ("¿Cómo recuperar dinero de estafa romance?", "Deje de enviar dinero, guarde las pruebas, avise a su banco, presente denuncia y haga valorar las vías según el medio de pago. La recuperación solo es posible en parte de los casos."),
   ("¿Debo seguir hablando con esa persona para obtener pruebas?", "No. Conserve lo que ya tiene y corte el contacto. Seguir la conversación le expone a más presión."),
   ("¿La app de trading que me recomendó puede ser falsa?", "Sí. Si se instaló desde un enlace o no aparece en los registros oficiales, trátela como una app de trading falsa y no introduzca más datos."),
   (FREE_Q, FREE),
  ],
 },
 {
  "slug": "como-saber-si-un-broker-es-fiable",
  "card": "Comprobaciones de licencia, clones y señales de una plataforma falsa.",
  "title": "Cómo saber si un bróker es fiable y está regulado | Act Here",
  "description": "Cómo saber si un bróker es fiable: cómo comprobar si está regulado en los registros de la CNMV, cómo detectar un clon y cómo identificar una plataforma falsa.",
  "keywords": "como saber si un broker es fiable, broker fiable, verificar licencia broker",
  "badge": "Bróker fiable",
  "h1": "Cómo saber si un bróker es fiable: comprobaciones antes de invertir",
  "lead": "Cinco minutos de comprobación evitan la mayoría de los problemas. Esta guía explica cómo saber si un bróker es fiable con fuentes oficiales, sin fiarse de lo que la propia web afirma sobre sí misma.",
  "sections": [
   ("Licencia", "Cómo saber si un bróker está regulado", [
    ("ul", [
     "Localice la razón social exacta y el país de la entidad en el aviso legal de la web.",
     "Busque esa razón social en los registros oficiales de la CNMV.",
     "Compruebe si aparece en las advertencias de la CNMV sobre entidades no autorizadas.",
     "Si dice estar autorizada en otro país europeo, compruébelo en el registro de ese supervisor.",
     "Compare el dominio, el teléfono y el correo de la web con los que constan en el registro.",
    ]),
    ("p", "El último paso es el que detecta los clones: un bróker falso que usa el nombre y el número de registro de una entidad real, pero con otro dominio y otros datos de contacto."),
   ]),
   ("Señales", "Cómo saber si una plataforma de trading es falsa", [
    ("p", "Cómo identificar una plataforma falsa cuando la licencia no está clara: fíjese en el comportamiento, no en el diseño."),
    ("ul", [
     "Promete una rentabilidad fija o garantizada.",
     "El contacto llega por mensajería o por una llamada que usted no pidió.",
     "Hay prisa: una oferta que caduca hoy o un gestor que insiste.",
     "Los pagos van a cuentas de terceros o solo se admiten criptomonedas.",
     "La aplicación se instala desde un enlace: es la señal típica de una app de trading falsa.",
     "No hay domicilio verificable ni razón social.",
    ]),
   ]),
   ("España", "Bróker no regulado España: qué significa en la práctica", [
    ("p", "Con un bróker no regulado no hay supervisor ante el que reclamar ni un procedimiento interno exigible. Los brókeres no regulados que captan clientes en España aparecen con frecuencia en las advertencias de la CNMV, pero muchos cambian de nombre y de dominio antes de ser advertidos."),
   ]),
   ("Si ya ha invertido", "Qué hacer si las comprobaciones fallan", [
    ("p", 'No envíe más dinero, guarde las pruebas y pida el retiro por escrito. Si no llega, siga la guía <a href="broker-no-deja-retirar.html">mi bróker no me deja retirar</a>. Las vías de reclamación están en <a href="recuperar-dinero-estafa.html">recuperar dinero estafado</a>.'),
    ("p", f"Si quiere consultar una plataforma concreta, puede buscarla por nombre en nuestro {ARCHIVE}."),
   ]),
  ],
  "faqs": [
   ("¿Cómo saber si un bróker es fiable?", "Compruebe su razón social en los registros oficiales, revise las advertencias de la CNMV y compare el dominio y los datos de contacto con los del registro."),
   ("¿Cómo saber si un bróker está regulado en España?", "Buscándolo en los registros de la CNMV. Las entidades de otros países europeos que operan con pasaporte también figuran allí."),
   ("¿Cómo saber si una plataforma de trading es falsa?", "Por su comportamiento: rentabilidad garantizada, presión, contacto por mensajería, pagos a terceros y una aplicación que se instala desde un enlace."),
   ("¿Qué es un bróker clon?", "Es un bróker falso que utiliza el nombre y el número de registro de una entidad real. Se detecta comparando el dominio y los datos de contacto con los que constan en el registro oficial."),
   ("¿Una licencia de fuera de Europa es suficiente?", "No para captar clientes minoristas en España. Además, reclamar ante un supervisor lejano es mucho más difícil."),
   (FREE_Q, FREE),
  ],
 },
]

CHARS_BANNED = "\u2014\u2013\u201e\u201c\u201d\u2018\u2019\u00ab\u00bb"
WORDS_BANNED = re.compile(
    r"desbloque|\bimpuestos?\b|\btasas?\b|\bhonorarios?\b|por adelantado|anticip|pago previo|"
    r"comisi[oó]n(es)? (de|para|por) (retir|liber)|liberaci[oó]n de (los )?fondos|\btarifas?\b|\bprecio",
    re.I)

def links_strip():
    links = " &middot; ".join(f'<a href="{p["slug"]}.html" style="color:var(--sage-dark)">{esc(p["badge"])}</a>' for p in PAGES)
    return ('<section style="padding:2rem 0;background:var(--off-white)"><div class="article-body" style="max-width:760px;margin:0 auto">'
            f'<p style="color:var(--text-muted);font-size:.95rem">Guías relacionadas: {links}</p></div></section>')

def faq_html(faqs):
    items = "\n".join(
        f'<div style="border-bottom:1px solid var(--line);padding:1.2rem 0"><h3 style="font-size:1rem;color:var(--navy);margin-bottom:.5rem;font-weight:600">{esc(q)}</h3><p style="color:var(--text-2);font-size:.93rem;line-height:1.75;margin:0">{esc(a)}</p></div>'
        for q, a in faqs)
    return ('<section style="padding:2.5rem 0"><div class="article-body" style="max-width:760px;margin:0 auto">'
            '<h2 style="font-family:var(--font-serif);font-size:1.8rem;color:var(--navy);margin-bottom:1.2rem">Preguntas frecuentes</h2>'
            f'{items}</div></section>')

def head(title, desc, url, schema=None, keywords=""):
    ld = f'\n <script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=1)}\n </script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{esc(title)}</title>
 <meta name="description" content="{esc(desc)}">
 <meta name="keywords" content="{esc(keywords)}">
 <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
 <link rel="canonical" href="{url}">
 <link rel="alternate" hreflang="es" href="{url}">
 <link rel="alternate" hreflang="x-default" href="{url}">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{esc(title)}">
 <meta property="og:description" content="{esc(desc)}">
 <meta property="og:url" content="{url}">
 <meta property="og:locale" content="es_ES">{ld}
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
 <h2 style="font-family:var(--font-serif);color:#fff;font-size:1.9rem;margin-bottom:.8rem">¿Ha perdido dinero? Haga valorar su caso.</h2>
 <p style="color:rgba(255,255,255,.75);margin-bottom:1.5rem">Consulta gratuita y confidencial con nuestro equipo de litigios. No nos limitamos a negociar: estamos preparados para litigar.</p>
 <a href="../pages/contact.html" class="btn-primary">Reserve una consulta gratuita</a>
 </div>
</section>
"""

def render(p):
    url = f"{BASE}{p['slug']}.html"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["description"],
         "isPartOf": {"@type": "WebSite", "name": "Act Here", "url": "https://act-here.uk/"}, "inLanguage": "es"},
        {"@type": "Article", "headline": p["title"], "description": p["description"],
         "author": {"@type": "Organization", "name": "Act Here"},
         "publisher": {"@type": "Organization", "name": "Act Here", "url": "https://act-here.uk/"},
         "dateModified": "2026-11-17", "inLanguage": "es", **({"keywords": p["keywords"]} if p.get("keywords") else {})},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://act-here.uk/"},
            {"@type": "ListItem", "position": 2, "name": "Guías", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": p["badge"], "item": url}]},
    ]}
    body = (f'<div class="breadcrumb"><a href="../index.html">Inicio</a><span>&#8250;</span><a href="index.html">Guías</a><span>&#8250;</span> {esc(p["badge"])}</div>\n'
            f'<div class="page-hero">\n <div class="hero-badge">{esc(p["badge"])} &middot; {UPDATED}</div>\n <h1>{esc(p["h1"])}</h1>\n <p>{esc(p["lead"])}</p>\n</div>\n'
            + "\n".join(render_section(*s) for s in p["sections"]) + "\n" + links_strip() + "\n" + faq_html(p["faqs"]) + "\n" + CTA)
    return head(p["title"], p["description"], url, schema, p.get("keywords", "")) + body + FOOT

def render_index():
    cards = "\n".join(
        f'<div style="border:1px solid var(--line);border-radius:8px;padding:1.5rem;background:#fff"><h3 style="font-family:var(--font-serif);font-size:1.1rem;margin-bottom:.5rem"><a href="{p["slug"]}.html" style="color:var(--navy);text-decoration:none">{esc(p["h1"])}</a></h3><p style="color:var(--text-2);font-size:.88rem;line-height:1.65;margin:0">{esc(p["card"])}</p></div>'
        for p in PAGES)
    title = "Estafas online e inversiones: guías en español | Act Here"
    desc = "Guías en español sobre estafa online, estafa trading, estafa criptomonedas y retiros bloqueados, de un despacho de litigios del Reino Unido."
    body = ('<div class="breadcrumb"><a href="../index.html">Inicio</a><span>&#8250;</span> Guías</div>\n'
            '<div class="page-hero">\n <div class="hero-badge">Español</div>\n <h1>Estafas online e inversiones: guías prácticas</h1>\n'
            ' <p>Qué hacer, a quién acudir y qué vías existen para reclamar el dinero.</p>\n</div>\n'
            '<section style="padding:2.5rem 0"><div style="max-width:1100px;margin:0 auto;padding:0 5%;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem">\n'
            f'{cards}\n</div></section>\n' + CTA)
    return head(title, desc, BASE) + body + FOOT

def main():
    os.makedirs(ES, exist_ok=True)
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
    for p in PAGES:
        if len(p["description"]) > 165:
            problems.append(f"{p['slug']}: description {len(p['description'])} chars")
    if problems:
        sys.exit("BUILD FAILED\n" + "\n".join(problems))
    for name, html in out.items():
        with open(os.path.join(ES, name), "w", encoding="utf-8") as f:
            f.write(html)
    print(f"wrote {len(out)} files to es/ (copy rules passed, JSON-LD valid)")

if __name__ == "__main__":
    main()
