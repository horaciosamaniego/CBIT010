# Semana 6: Del perceptrón a ChatGPT — ¿Qué son los LLMs?

## Guía completa de la sesión

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (2 h cátedra + 1 h laboratorio práctico) |
| **Objetivo central** | Que los estudiantes comprendan — a nivel conceptual, no técnico — cómo funciona un LLM: tokenización, predicción del siguiente token, atención. Y que puedan distinguir entre lo que un LLM parece hacer ("entender") y lo que realmente hace (estadísticas sobre secuencias de texto) |
| **Idea ancla** | Un LLM es la Máquina de Turing más sofisticada que se ha construido — pero sigue siendo una máquina que manipula símbolos según patrones. No "entiende" en el sentido humano. Produce texto plausible, no necesariamente verdadero |
| **Prerrequisito** | Semana 5 (Máquina de Turing, tesis de Church-Turing, lo no computable), Semana 3 (redundancia en el lenguaje, entropía) |
| **Materiales** | Proyector, acceso a internet (para la demo con LLM), computador del docente proyectado, copias del Control 3 |
| **Conexión con semanas previas** | Semana 3: "el español tiene ~60–70% de redundancia" → los LLMs explotan esa redundancia para predecir. Semana 5: "la MT no entiende, sigue reglas" → ¿aplica lo mismo a un LLM? |

---

## PARTE 1: CÁTEDRA (120 minutos)

---

### Bloque A — Apertura: el juego de completar frases (15 min)

**Actividad con el curso entero:**

Proyectar frases incompletas y pedir que las completen en voz alta:

1. *"El pudú es el ciervo más _______ del mundo."* → pequeño
2. *"Las hojas del Nothofagus se caen en _______ ."* → otoño
3. *"El chungungo se alimenta principalmente de _______ ."* → erizos / mariscos
4. *"En Chile, la institución encargada de las áreas protegidas es _______ ."* → CONAF
5. *"Ceci n'est pas une _______ ."* → pipe (si recuerdan la Semana 2)

**Ahora una más difícil:**
6. *"El flavonoide más abundante en la corteza de Drimys winteri es _______ ."* → (silencio)

**Preguntas al curso:**
- *"¿Cómo supieron completar las primeras cinco?"* → Contexto, frecuencia, asociación.
- *"¿Por qué no pudieron con la sexta?"* → No tienen datos sobre ese tema. No está en su "entrenamiento".
- *"Si hubieran leído 10.000 artículos de botánica, ¿podrían?"* → Probablemente sí.

**Revelación:** *"Lo que acaban de hacer — predecir la siguiente palabra usando contexto y frecuencia — es exactamente lo que hace un LLM. La diferencia es que ustedes leyeron miles de textos; un LLM leyó miles de millones."*

---

### Bloque B — Breve historia: del perceptrón al transformer (25 min)

#### La línea temporal (20 min)

Presentar como **cinco generaciones**, no como lista de fechas. Para cada una: qué se inventó, qué podía hacer, y por qué no fue suficiente.

**Generación 1: El perceptrón (1958)**
- Frank Rosenblatt, Cornell.
- Una "neurona" artificial: recibe entradas, las pondera, produce una salida (0 o 1).
- Podía clasificar patrones simples (¿es esta imagen una letra A o una B?).
- **Limitación:** solo funciones lineales. No puede aprender XOR (un problema trivialmente simple).
- 1969: Minsky y Papert publican "Perceptrons" demostrando las limitaciones → "invierno de la IA".

**Generación 2: Redes neuronales multicapa + Backpropagation (1986)**
- Rumelhart, Hinton, Williams.
- Múltiples capas de neuronas → pueden aprender funciones no lineales.
- Backpropagation: algoritmo para ajustar los pesos propagando el error hacia atrás.
- **Limitación:** difíciles de entrenar con muchas capas (el gradiente se desvanece). Datos insuficientes. Computadores lentos.

**Generación 3: Deep Learning (2012)**
- Krizhevsky, Sutskever, Hinton — AlexNet gana ImageNet por un margen enorme.
- Redes profundas (muchas capas) + GPUs + grandes datasets = resultados espectaculares.
- Aplicaciones: reconocimiento de imágenes, voz, traducción.
- **Limitación:** procesamiento secuencial para texto (RNNs, LSTMs). Difícil capturar dependencias a larga distancia.

**Generación 4: El Transformer (2017)**
- Vaswani et al., Google: "Attention Is All You Need".
- Innovación clave: el **mecanismo de atención** — procesa todas las palabras de una oración simultáneamente, no una por una. Cada palabra "mira" a todas las demás para determinar su significado en contexto.
- Permite entrenar modelos masivos en paralelo con GPUs.
- **Consecuencia:** se pueden entrenar modelos con miles de millones de parámetros.

**Generación 5: Los LLMs (2018–presente)**
- GPT (2018), GPT-2 (2019), GPT-3 (2020), GPT-4 (2023), Claude (Anthropic), Llama (Meta), Gemini (Google).
- Transformer + entrenamiento masivo sobre texto de internet + RLHF (alineamiento con humanos).
- Capacidades emergentes: diálogo, razonamiento aparente, generación de código, resumen, traducción.
- **Limitación:** alucinación, sesgo, falta de comprensión real, alto costo energético.

#### El patrón (5 min)

Destacar que cada generación resolvió una limitación de la anterior:
- Perceptrón → multicapa (no linealidad)
- Multicapa → deep learning (profundidad + datos + hardware)
- RNN → transformer (paralelismo + atención)
- Transformer → LLM (escala masiva)

> Cada salto combinó una idea teórica con un avance práctico (datos, hardware, o ambos). La IA no avanza solo por teoría ni solo por fuerza bruta — necesita ambas.

---

### Bloque C — ¿Cómo funciona un LLM? (30 min)

**Nota pedagógica:** No se pretende que entiendan el álgebra lineal detrás de los transformers. El objetivo es una comprensión conceptual que les permita usar y evaluar LLMs con criterio.

#### Paso 1: Tokenización (7 min)

El LLM no trabaja con palabras — trabaja con **tokens**: fragmentos de texto que pueden ser palabras completas, sílabas, o caracteres.

Ejemplo:

| Texto | Tokens |
|---|---|
| "El pudú es un ciervo" | ["El", " pud", "ú", " es", " un", " cier", "vo"] |
| "Conservación" | ["Con", "serv", "ación"] |
| "ChatGPT" | ["Chat", "G", "PT"] |

Un LLM típico tiene un vocabulario de ~50.000–100.000 tokens.

**Conexión con Semana 2:** la tokenización es otro sistema de codificación — como ASCII, pero para fragmentos de texto en vez de caracteres individuales. Y como ASCII, es un acuerdo arbitrario que determina cómo el modelo "ve" el texto.

#### Paso 2: Embeddings — del texto a los vectores (8 min)

Cada token se convierte en un **vector** — una lista de números (típicamente 768 a 12.288 números por token).

**Analogía:** piensen en las coordenadas de un mapa. Valdivia está en (-39.8, -73.2). Esos dos números ubican la ciudad en el espacio. Un embedding hace lo mismo pero en un espacio de miles de dimensiones — ubica cada token en un "mapa semántico" donde palabras con significados similares están cerca.

Ejemplo (simplificado a 2 dimensiones):
- "pudú" y "huemul" estarían **cerca** (ambos son ciervos chilenos)
- "pudú" y "telescopio" estarían **lejos**
- "rey" - "hombre" + "mujer" ≈ "reina" (aritmética de significados)

#### Paso 3: Atención — el ingrediente mágico (8 min)

**El problema:** en la oración *"El pudú que vive en el bosque valdiviano come hojas"*, ¿a qué se refiere "come"? Al pudú, no al bosque. Pero el pudú está lejos en la oración.

**La solución:** el mecanismo de **atención** permite que cada token "mire" a todos los demás tokens de la secuencia y decida cuánta importancia darle a cada uno.

**Analogía ecológica:** imaginen una red trófica. Cada especie está conectada a varias otras con diferentes intensidades. La atención es como una red trófica del texto: cada palabra está conectada a todas las demás, pero con pesos diferentes. "Come" está fuertemente conectado a "pudú" y débilmente a "valdiviano".

#### Paso 4: Predicción del siguiente token (7 min)

Después de procesar toda la entrada a través de muchas capas de atención, el LLM produce una **distribución de probabilidad** sobre todo su vocabulario: ¿cuál es el token más probable que sigue?

Ejemplo: después de procesar "El pudú es el ciervo más", el modelo asigna:
- "pequeño" → 73%
- "chico" → 8%
- "tímido" → 3%
- "grande" → 0.1%
- ... (50.000 opciones más, cada una con una probabilidad)

El modelo **elige uno** (no siempre el más probable — hay algo de aleatoriedad controlada llamada "temperatura").

Luego, agrega ese token a la secuencia y repite. Y repite. Y repite. Token por token, de izquierda a derecha, hasta completar la respuesta.

> **Un LLM no "piensa" una respuesta completa y luego la escribe.** Genera una palabra a la vez, sin saber hacia dónde va. Es como escribir una novela eligiendo cada palabra solo en función de las anteriores — sin conocer el final.

---

### Bloque D — Lo que los LLMs pueden y no pueden hacer (20 min)

#### Lo que hacen bien (5 min)

- Generar texto fluido y coherente
- Resumir documentos
- Traducir idiomas
- Escribir código (con limitaciones)
- Responder preguntas sobre temas de los que "leyeron" mucho durante el entrenamiento
- Reformular, adaptar tono, seguir instrucciones de formato

#### Lo que NO hacen (10 min)

**1. No entienden.** Manipulan patrones estadísticos de texto. No tienen un modelo del mundo, no razonan causalmente, no saben qué significan las palabras.

**2. Alucinan.** Inventan hechos con total confianza. Si les piden una referencia, pueden inventar un paper que no existe, con autores, revista y DOI plausibles.

**Ejemplo en vivo** (si hay internet): pedirle a un LLM que cite papers sobre la ecología del pudú. Verificar si los papers existen.

**3. Tienen sesgos.** Reflejan los sesgos de los datos con los que fueron entrenados. Si la mayoría de los textos de ecología son de ecosistemas templados del hemisferio norte, el modelo "sabe" más sobre eso que sobre bosques valdivianos.

**4. No aprenden de la conversación.** Cada sesión empieza desde cero (con excepciones recientes). No "recuerdan" lo que les dijiste ayer.

**5. No pueden acceder a información en tiempo real** (a menos que tengan herramientas de búsqueda). Su conocimiento tiene una fecha de corte.

#### La distinción clave (5 min)

> **Correlación ≠ Comprensión**

Un LLM sabe que después de "el pudú es el ciervo más" suele venir "pequeño" — porque ha visto ese patrón miles de veces. Pero no sabe qué es un pudú, no ha visto uno, no comprende qué significa "pequeño" en relación a un cuerpo. Produce la respuesta correcta por la razón equivocada (o más precisamente: sin razón, solo patrón).

**Analogía de la habitación china** (John Searle, 1980):
Imaginen a una persona encerrada en una habitación que recibe mensajes en chino, consulta un libro de reglas gigantesco ("si recibes estos caracteres, responde con estos otros"), y envía respuestas perfectas en chino. Desde afuera, parece que habla chino. ¿Entiende chino?

Searle dice que no. Un LLM es esa habitación — a una escala inimaginable.

---

### Bloque E — Implicaciones para la conservación y la ciencia (10 min)

- **Oportunidades:** los LLMs pueden ayudar a redactar informes, resumir literatura, generar código para análisis, traducir documentos técnicos, sugerir hipótesis exploratorias.
- **Riesgos:** si confían sin verificar, pueden citar papers fantasma, aplicar métodos estadísticos incorrectos, o reproducir sesgos del hemisferio norte en contextos del hemisferio sur.
- **La regla de oro:** un LLM es un **asistente**, no un experto. Lo que produce es un **borrador**, no una verdad. Verificar siempre. Citar solo fuentes que han comprobado que existen.

> *"En conservación, una conclusión equivocada basada en una alucinación puede traducirse en una mala política pública. El costo del error no es un ensayo reprobado — puede ser un ecosistema dañado."*

---

### Bloque F — Cierre y puente al laboratorio (5 min)

*"Ahora van a poner a prueba un LLM. Van a hacerle la misma pregunta ecológica de 5 formas diferentes y comparar las respuestas. Van a intentar hacerlo alucinar. Y van a decidir: ¿cuándo confío y cuándo no?"*

---

## PARTE 2: LABORATORIO PRÁCTICO (45 minutos)

## "Interrogando al LLM"

*Nota: esta es la primera sesión con pantallas. Los estudiantes necesitan un celular o computador con acceso a internet y a un LLM gratuito (Claude, ChatGPT, o equivalente).*

---

### Preparación previa (docente)

- Verificar que el acceso a un LLM gratuito funciona desde la red del campus.
- Preparar las 5 preguntas base (proyectar).
- Imprimir hojas de registro (1 por grupo).

---

### Desarrollo de la actividad

#### Fase 1 — El mismo prompt, 5 formas (20 min)

**Pregunta base:** *"¿Cuáles son las principales amenazas para la conservación del bosque valdiviano?"*

Cada grupo (6 grupos) reformula la pregunta de 5 maneras diferentes:

| Versión | Estilo |
|---|---|
| 1 | La pregunta tal cual (directa) |
| 2 | Pidiendo que responda como un experto en ecología |
| 3 | Pidiendo una respuesta para un niño de 10 años |
| 4 | Pidiendo que cite fuentes académicas |
| 5 | Pidiéndola en inglés en vez de español |

**Para cada versión, registrar:**
- El prompt exacto (copiar y pegar)
- Los puntos principales de la respuesta (resumir en 2–3 líneas)
- ¿Hay información que parece incorrecta o sospechosa?
- ¿Las fuentes citadas existen? (verificar al menos una googleándola)

#### Fase 2 — Caza de alucinaciones (15 min)

**Tarea por grupo:** intentar que el LLM produzca una alucinación verificable.

**Estrategias sugeridas:**
- Pedir papers específicos sobre un tema muy nicho (*"¿Puedes darme 3 papers sobre la dieta del monito del monte publicados después de 2020?"*)
- Preguntar por datos numéricos precisos (*"¿Cuántos individuos de huemul quedan en la Región de Los Ríos?"*)
- Inventar un concepto falso y preguntar al LLM como si existiera (*"¿Qué opinas del Índice de Fragmentación de Petersen aplicado a bosques nativos?"* — no existe)

**Registrar:** el prompt, la respuesta, y la verificación (¿era verdad o alucinación?).

#### Fase 3 — Discusión plenaria (10 min)

**Preguntas guía:**

1. *"¿Cambió la respuesta significativamente entre las 5 versiones del prompt?"*
→ Generalmente sí. El prompt importa mucho. Un LLM no tiene una "respuesta correcta" almacenada — genera una nueva cada vez.

2. *"¿Encontraron alucinaciones?"*
→ Casi seguro que sí, especialmente con las citas bibliográficas.

3. *"¿Cuándo confiarían en la respuesta de un LLM y cuándo no?"*
→ Guiar hacia: confiable para ideas generales, resúmenes, borradores. No confiable para datos numéricos específicos, citas, hechos verificables.

4. *"¿Cómo se relaciona esto con lo que vimos en Semanas 3 y 5?"*
→ Semana 3: el LLM explota la redundancia del lenguaje (predice lo probable). Semana 5: sigue reglas (muy complejas), pero no "entiende" — como la MT.

5. *"Si van a usar un LLM en este curso, ¿qué deben hacer siempre?"*
→ Documentar el prompt, verificar la salida, explicar el código en sus palabras. (Recordar la política de IA del curso.)

---

## PARTE 3: CONTROL 3 (15 minutos, individual, con calificación)

*Aplicar al final de la sesión. Sin apuntes ni celular.*

---

### Control 3 — Semana 6
#### Introducción al Análisis de Datos y Programación

**Nombre:** ____________________________  **Fecha:** ____________  **Puntaje:** _____ / 24

*Tiempo: 15 minutos. Sin apuntes ni celular.*

---

**1. (4 puntos)** Nombre las cuatro partes de una Máquina de Turing y explique brevemente la función de cada una.

\[espacio\]

---

**2. (4 puntos)** La tesis de Church-Turing dice que todo lo computable puede ser computado por una MT. ¿Qué implicación práctica tiene esto para los computadores modernos? Explique en 2–3 oraciones.

\[espacio\]

---

**3. (4 puntos)** ¿Qué es el "problema de la detención" (Halting Problem)? ¿Por qué es importante para la informática?

\[espacio\]

---

**4. (4 puntos)** Explique qué significa "predicción del siguiente token" en el contexto de un LLM. ¿Cómo genera texto un LLM?

\[espacio\]

---

**5. (4 puntos)** ¿Qué es una "alucinación" en un LLM? Dé un ejemplo concreto de cómo podría ser problemático en un contexto de conservación de biodiversidad.

\[espacio\]

---

**6. (4 puntos)** Un compañero dice: *"ChatGPT entiende lo que le digo, por eso responde bien."* ¿Está de acuerdo? Argumente su respuesta usando conceptos de las Semanas 5 y 6.

\[espacio\]

---

### Pauta de corrección

| Pregunta | Respuesta esperada | Puntos |
|---|---|---|
| 1 | Cinta (almacenamiento), Cabezal (lee/escribe/mueve), Estados (memoria interna), Tabla de transiciones (programa/instrucciones) — 1 pt por cada componente bien explicado | 4 |
| 2 | Los computadores modernos no pueden resolver más problemas que una MT — solo lo hacen más rápido. Si una MT no puede resolverlo, ningún computador puede. | 4 (2 por la equivalencia, 2 por la implicación) |
| 3 | Es la pregunta de si se puede crear un programa que determine si otro programa terminará o no. Turing demostró que es imposible → hay problemas no computables → hay límites a lo que las máquinas pueden resolver. | 4 (2 por definición, 2 por importancia) |
| 4 | El LLM genera una distribución de probabilidad sobre todos los tokens posibles y elige el más probable (con algo de aleatoriedad). Luego agrega ese token a la secuencia y repite, generando texto palabra por palabra. | 4 (2 por distribución/probabilidad, 2 por el carácter secuencial) |
| 5 | Una alucinación es cuando el LLM genera información falsa con apariencia de verdad (e.g., citar un paper inexistente). En conservación podría llevar a usar datos erróneos, aplicar métodos inadecuados, o tomar decisiones de manejo basadas en información falsa. | 4 (2 por definición, 2 por ejemplo ecológico concreto) |
| 6 | No — un LLM no "entiende" en el sentido humano. Manipula patrones estadísticos (correlaciones) en texto. Produce la respuesta más probable, no la "verdadera". Es como la MT de la Semana 5: sigue reglas sin comprender su significado. Analogía de la habitación china. | 4 (2 por argumento contra la comprensión, 2 por conexión con MT/Semana 5) |

---

## Notas pedagógicas

### Esta es la clase más peligrosa del curso

Peligrosa porque los estudiantes llevan semanas sin pantallas, y hoy abren un LLM por primera vez en el contexto del curso. El riesgo es que se distraigan con la herramienta y pierdan la lección conceptual.

**Estrategia:** la cátedra es ANTES del laboratorio. Cuando abran el LLM, ya tienen el marco conceptual (tokenización, predicción, alucinación) para interpretar lo que ven.

### La actividad de caza de alucinaciones

Es deliberadamente provocadora. Los estudiantes van a sentirse poderosos cuando logran hacer "fallar" al LLM. Esa experiencia es más formativa que cualquier advertencia verbal sobre las limitaciones de la IA.

**Peligro:** algunos pueden concluir "entonces la IA no sirve para nada". Corregir: el hecho de que un martillo pueda lastimar no significa que no sirva para clavar. Es una herramienta — y las herramientas se usan con criterio.

### La analogía de la habitación china

Es la analogía más potente de la clase, pero también la más debatible. Algunos filósofos la rechazan (argumento del sistema: tal vez la habitación completa "entiende" aunque la persona dentro no). No es necesario resolver el debate — basta con plantearlo. Lo importante es que los estudiantes salgan de la clase distinguiendo entre "producir texto correcto" y "comprender".

### Conexión con el resto del curso

| Concepto de esta semana | Dónde se profundiza |
|---|---|
| Tokenización | Semana 8 (strings en Python, split, len) |
| Predicción probabilística | Semana 3 (entropía — el LLM minimiza la sorpresa) |
| Alucinación y verificación | Semana 7 (investigación grupal: verificar fuentes sobre IA en conservación) |
| Política de uso de IA | Semana 8–16 (cada tarea con IA documentada) |
| La habitación china / ¿entiende? | Semana 5 (MT no entiende), Semana 16 (reflexión final) |
