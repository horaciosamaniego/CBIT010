---
marp: false
theme: gaia
paginate: true
size: 16:9
style: |
  :root {
    /* --- THEME COLORS --- */
    --color-bg:      #091926;
    --color-elime:    #DEFF9A; /* Primary Highlight (Electric Lime) */
    --color-accent:   #5DD9E8; /* Secondary Highlight (Cyan) */
    --color-mid:      #00B4CC; /* UI Accents (Teal) */
    --color-dark:     #495f71; /* Faded UI */
    --color-light:    #6199ac; /* Sub-headings */
    --color-muted:    #7CA9BA; /* Low-priority text */
    --color-white:    #e1ebee; /* Body text */
    --color-warn:     #E05B3A; /* Error/Alerts */
    --font-head:      'Georgia', serif;
    --font-body:      'Trebuchet MS', sans-serif;
  }

  /* --- Base Slide Styles --- */
  section {
    font-family: var(--font-body);
    font-size: 32px;
    line-height: 1.45;
    padding: 40px 60px;
    background-color: var(--color-bg);
    color: var(--color-white);
  }

  /* --- Links (Accessibility Fix) --- */
  section a {
    color: var(--color-accent);
    text-decoration: underline;
    text-underline-offset: 6px;
    text-decoration-thickness: 3px;
    font-weight: bold;
  }

  /* --- Typography --- */
  section h1, section h2, section h3 { 
    font-family: var(--font-head); 
    margin-top: 0;
  }
  
  section h1 { 
    color: var(--color-elime); 
    font-size: 1.7em; 
    border-bottom: 4px solid var(--color-mid); 
    padding-bottom: 8px; 
    margin-bottom: 20px; 
  }
  
  /* H2 pop: Cyan on Navy provides high luminance */
  section h2 { 
    color: var(--color-accent); 
    font-size: 1.3em; 
    margin-bottom: 12px; 
    font-weight: 700;
  }
  
  section h3 { 
    color: var(--color-light); 
    font-size: 1.1em; 
  }

  section strong { 
      color: var(--color-elime); 
      font-weight: 800; 
      }
  section em { 
      color: var(--color-muted); 
      }

  /* --- Layout & Lists --- */
  section li { margin-bottom: 8px; }
  section ul, section ol { margin: 8px 0 12px 30px; }
  section p { margin-bottom: 12px; }

  /* --- Slide Variant: LEAD (Heavy Title Slide) --- */
  section.lead {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 12px solid var(--color-mid);
  }
  section.lead h1 { color: var(--color-elime); font-size: 2.4em; border-bottom: none; }
  section.lead h2 { color: var(--color-accent); font-size: 1.4em; font-style: italic; }
  section.lead p { color: var(--color-white); opacity: 0.8; }

  /* --- Slide Variant: INVERT (Light Mode Toggle) --- */
  section.invert {
    background-color: var(--color-white);
    color: var(--color-bg);
  }
  section.invert h1 { color: var(--color-bg); border-bottom-color: var(--color-mid); }
  section.invert h2 { color: var(--color-dark); }
  section.invert strong { color: var(--color-warn); }
  section.invert a { color: var(--color-mid); }

  /* --- Slide Variant: PREGUNTA (Quiz/Prompt) --- */
  section.pregunta {
    background-color: var(--color-mid);
    color: var(--color-bg);
    text-align: center;
    justify-content: center;
  }
  section.pregunta h1 { 
    color: var(--color-elime); 
    border-bottom: none; 
    font-size: 1.6em; 
    }
  section.pregunta h2 { 
    color: var(--color-bg); 
    border-bottom: none; 
    font-size: 1.4em; 
    }
  section.pregunta p { 
    font-weight: bold; 
    font-size: 1.2em; 
    }

  /* --- Slide Variant: LAB (Activity) --- */
  section.lab {
    border-left: 15px solid var(--color-warn);
  }
  section.lab h1 { color: var(--color-warn); border-bottom-color: var(--color-dark); }
  section.lab h2 { color: var(--color-accent); }

  /* --- Tables (Dark Mode Optimized) --- */
  table { font-size: 0.8em; width: 100%; border-collapse: collapse; margin: 15px 0; }
  thead th { background-color: var(--color-dark); color: var(--color-elime); padding: 10px; text-align: left; }
  td { padding: 10px; border: 1px solid var(--color-dark); }
  tbody tr:nth-child(even) td { background-color: rgba(255,255,255,0.05); }

  /* --- Blocks & Code --- */
  blockquote {
    background-color: rgba(255,255,255,0.05);
    border-left: 6px solid var(--color-elime);
    padding: 15px 25px;
    font-style: italic;
    color: var(--color-accent);
  }
  
  pre { 
    background-color: #000; 
    border: 1px solid var(--color-dark); 
    padding: 15px; 
    border-radius: 6px;
    color: var(--color-accent);
  }
  
  code { 
    background-color: var(--color-dark); 
    color: var(--color-elime); 
    padding: 2px 6px; 
    border-radius: 4px;
    font-family: 'Consolas', monospace;
  }

  /* --- UI Elements --- */
  /*.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 15px; }*/
  
  .cols {
    display: grid;
    gap: 24px;
    margin-top: 0.6em;
    color: var(--color-dark);
  }
  .cols-2 {
    grid-template-columns: 1fr 1fr;
  }
  .cols-60-40 {
    grid-template-columns: 3fr 2fr;
  }
  .cols-40-60 {
    grid-template-columns: 2fr 3fr;
  }



  .card {
    background: rgba(255,255,255,0.95);
    border-radius: 10px;
    padding: 20px;
    border-top: 6px solid var(--color-accent);
    color: var(--color-bg);
  }
  .card h3 { color: var(--color-mid); margin-bottom: 5px; }
  .card p, .card li { color: var(--color-bg); font-size: 0.85em; }
  .card.warn { border-top-color: var(--color-warn); }

  .state-badge { 
    background-color: var(--color-elime); 
    color: var(--color-bg); 
    padding: 4px 12px; 
    border-radius: 20px; 
    font-size: 0.7em; 
    font-weight: bold; 
    vertical-align: middle;
  }

footer: "Semana 06 · Del perceptrón a ChatGPT · Horacio Samaniego (*horaciosamaniego@uach.cl*)"
---
<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->


<div>

![w:900px](./figs/words.jpeg)

</div>

---
<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Del perceptrón a ChatGPT
## ¿Qué son los LLMs?


*Introducción al Análisis de Datos y Programación*


*Laboratorio de Ecoinformática*
*Instituto de Conservación, Biodiversidad y Territorio - Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

<!-- _class: pregunta -->

# Completen la frase:

## "El pudú es el ciervo más _______ del mundo."

---

<!-- _class: pregunta -->

# Y esta:

## "El flavonoide más abundante en la corteza de Drimys winteri es _______ ."

<!-- (...silencio?) -->

---

# ¿Cómo supieron la primera y no la segunda?


<div class="cols">

La primera: la han leído o escuchado *muuchas* de veces. El **Contexto + frecuencia** les permiten predecir y completar la frase.

<div>

![w:470px](https%3A%2F%2Fi.redd.it%2Fuw7d3ql5ql1d1.jpeg)

</div>
</div>

---

# ¿Cómo supieron la primera y no la segunda?


Para la segunda: no tienen datos. No están "entrenados" - ¡aún!

> Usando el contexto y la frecuencia pueden **predecir la siguiente palabra**  — esto es exactamente lo que hace un LLM. La diferencia es que ustedes han oído y leído miles de textos. Un LLM leyó **miles de millones**.

---

# Hoja de ruta

1. 📜 **Breve historia:** perceptrón → transformers → LLMs
2. 🧠 **¿Cómo funciona?** Tokens, embeddings, atención, predicción
3. ⚠️ **Lo que pueden y no pueden hacer**
4. 🌿 **Implicaciones para la conservación**
5. 🧪 **Laboratorio:** interrogando al LLM
6. 📝 **Control 3**

---

<!-- _class: invert -->

# Breve historia de la IA
## Cinco generaciones en 66 años

---
<!-- _footer: "" -->

# Gen 1 · El perceptrón (1958)

<div class="card">

![w:570px](https://as.cornell.edu/sites/default/files/styles/6_4_large/public/inline-article-images/rosenblatt600.jpg) ![w:470px](https://upload.wikimedia.org/wikipedia/commons/1/13/Mark_I_Perceptron%2C_Figure_2_of_operator%27s_manual.png) 

Mark I Perceptron de Rosenblatt (la máquina física con cables y fotodetectores)
</div>

---

# Gen 1 · El perceptrón (1958)

- Frank Rosenblatt, Cornell. Una "neurona" artificial.
- Recibe entradas, las pondera, produce 0 o 1.
- Podía clasificar patrones simples (¿A o B?).
- **Limitación:** solo funciones lineales. No puede aprender XOR.
- 1969: Minsky y Papert demuestran las limitaciones → **"invierno de la IA"**.

<div>

![w:300px](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoW37n2MxdUfEx048uCoZDPcpgAet6r_YTfAroFmQ7WiBLfXV527WjM818-CtG0g4udUWDdhBbb_buAwq-ZADRMkj35jK53egisAGbIOSwVJTEgRYVPKWkf4d3ZJkOE_if8BcNu-E3NTNOIUNnhI4lF8xzkiYl3A6j2ChBZMr-MqBqs1XaPHH6irfnKA/w512-h258-rw/Perceptron%20with%20bias.png)

</div>


---

# Gen 2 · Redes multicapa + Backpropagation (1986)
<!--
<div class="img-placeholder">
📎 IMAGEN: Diagrama de una red neuronal multicapa (nodos en capas, conexiones ponderadas). Buscar: "multilayer neural network diagram" o "backpropagation network schematic". Simple, con 3 capas visibles.
</div>
-->
![bg w:90% right:30%](https://miro.medium.com/v2/resize:fit:720/format:webp/0*16VII9o-kkiRWwlx)

- Rumelhart, Hinton, Williams.
- Múltiples capas → pueden aprender funciones no lineales.
- **Backpropagation:** ajustar los pesos propagando el error hacia atrás.
- **Limitación:** difícil entrenar muchas capas. Datos y computadores insuficientes.

---

# Gen 3 · Deep Learning (2012)


<div class="cols">
<div class="card" >

![w:350px](./figs/Imagenet_err.png)
</div>

- AlexNet (Krizhevsky, Sutskever, Hinton) gana ImageNet por un margen enorme.
- Redes **profundas** (muchas capas) + **GPUs** + **grandes datasets** = resultados espectaculares.

</div>
</div>

<!--
<div class="img-placeholder">
📎 IMAGEN: La gráfica de error en ImageNet (2010–2017) que muestra la caída dramática del error con la llegada de deep learning en 2012. O una demo de reconocimiento de imágenes (foto → "gato: 97%"). Buscar: "ImageNet error rate graph deep learning" — imagen icónica.
</div>
-->
- **Limitación:** para texto, procesamiento secuencial (una palabra a la vez). Difícil capturar relaciones a larga distancia.

---

# Gen 4 · El Transformer (2017)

**"Attention Is All You Need"** — Vaswani et al., Google.

Innovación clave: el **mecanismo de atención**.

- Procesa todas las palabras **simultáneamente** (no una por una)
- Cada palabra "mira" a todas las demás para determinar su significado en contexto
- Permite entrenar en paralelo con GPUs → modelos masivos

<!--
<div class="img-placeholder">
📎 IMAGEN: Diagrama simplificado del mecanismo de atención — una oración donde cada palabra tiene flechas de diferente grosor hacia las demás (grosor = peso de atención). Ejemplo: "El pudú que vive en el bosque come hojas" con flecha gruesa de "come" hacia "pudú" y flecha fina hacia "bosque". Buscar: "attention mechanism visualization sentence" o "self-attention diagram NLP".
</div>
-->
---

<style scoped> {font-size:27px; }</style>


# Gen 5 · Los LLMs (2018–presente)

Transformer + **entrenamiento masivo** sobre texto de internet + **alineamiento** con humanos

- GPT (2018), GPT-2 (2019), GPT-3 (2020), GPT-4 (2023)
- Claude (Anthropic), Llama (Meta), Gemini (Google)
- Capacidades emergentes: diálogo, código, resumen, traducción, "razonamiento"

**Escala:**

| Modelo | Parámetros | Datos de entrenamiento |
|---|---|---|
| GPT-2 (2019) | 1.500 millones | ~40 GB de texto |
| GPT-3 (2020) | 175.000 millones | ~570 GB |
| GPT-4 (2023) | ~1.800.000 millones (est.) | ~13 TB (est.) |

---

# El patrón de cada generación

Cada salto combinó una **idea teórica** con un **avance práctico**:

| Generación | Idea | Avance práctico |
|---|---|---|
| Perceptrón → multicapa | No linealidad | — |
| Multicapa → deep learning | Profundidad | GPUs + datos masivos |
| RNN → transformer | Atención (paralelismo) | Hardware paralelo |
| Transformer → LLM | Escala | Internet completo como dataset |

> La IA no avanza solo por teoría ni solo por fuerza bruta. Necesita **ambas**.

---

<!-- _class: invert -->

# ¿Cómo funciona un LLM?
## Cuatro pasos

---
<style scoped> {font-size:27px; }</style>

# Paso 1 · Tokenización

Un LLM no trabaja con palabras — trabaja con **tokens** (fragmentos de texto):

| Texto | Tokens |
|---|---|
| "El pudú es un ciervo" | ["El", " pud", "ú", " es", " un", " cier", "vo"] |
| "Conservación" | ["Con", "serv", "ación"] |

Un LLM típico tiene un vocabulario de **~50.000–100.000 tokens**.

> **Conexión Semana 2:** la tokenización es otro sistema de codificación — como ASCII, pero para fragmentos de texto. Y como ASCII, es un acuerdo arbitrario.

---

# Paso 2 · Embeddings: del texto a los números

Cada token se convierte en un **vector** — una lista de cientos o miles de números.

**Analogía:** coordenadas en un mapa. Valdivia = (-39.8, -73.2). Dos números ubican la ciudad. Un embedding hace lo mismo en miles de dimensiones — ubica cada token en un **"mapa semántico"**.

- "pudú" y "huemul" → **cerca** (ambos ciervos chilenos)
- "pudú" y "telescopio" → **lejos**
- "rey" - "hombre" + "mujer" ≈ "reina" (aritmética de significados)

<!-- <div class="img-placeholder">
📎 IMAGEN: Diagrama 2D de word embeddings — puntos etiquetados con palabras, donde las semánticas cercanas forman clusters (animales juntos, plantas juntas, etc.). Buscar: "word2vec embeddings visualization 2D" o "word embedding semantic map". La versión de TensorFlow Projector es interactiva y visualmente impactante.
</div> -->

---
<style scoped> {font-size:27px; }</style>

# Paso 3 · Atención: cada palabra mira a todas las demás

**Problema:** *"El pudú que vive en el bosque valdiviano come hojas"*
¿A qué se refiere "come"? Al pudú, no al bosque. Pero el pudú está **lejos** en la oración.

**Solución:** el mecanismo de **atención** permite que cada token "mire" a todos los demás y decida cuánta importancia darle.

> **Analogía ecológica:** piensen en una red trófica. Cada especie está conectada a varias otras con diferentes intensidades. La atención es una red trófica del texto — "come" está fuertemente conectado a "pudú" y débilmente a "valdiviano".

---
<style scoped> {font-size:27px; }</style>

# Paso 4 · Predicción del siguiente token

Después de procesar la entrada, el LLM produce una **distribución de probabilidad** sobre todo su vocabulario:

*Después de "El pudú es el ciervo más":*

| Token | Probabilidad |
|---|---|
| "pequeño" | 73% |
| "chico" | 8% |
| "tímido" | 3% |
| "grande" | 0.1% |
| ... (50.000 opciones más) | ... |

Elige uno. Lo agrega a la secuencia. **Repite.** Token por token, de izquierda a derecha.

---

<!-- _class: pregunta -->

# Un LLM no "piensa" una respuesta completa y luego la escribe.

# Genera una palabra a la vez, sin saber hacia dónde va.

Es como escribir una novela eligiendo cada palabra solo en función de las anteriores — sin conocer el final.

---

<!-- _class: invert -->

# Lo que los LLMs pueden y no pueden hacer

---

# ✅ Lo que hacen bien

- Generar texto fluido y coherente
- Resumir documentos
- Traducir idiomas
- Escribir código (con limitaciones)
- Responder preguntas sobre temas frecuentes en su entrenamiento
- Reformular, adaptar tono, seguir instrucciones de formato

---
<style scoped> {font-size:27px; }</style>

# ❌ Lo que NO hacen

**1. No entienden.** Manipulan patrones estadísticos. No tienen modelo del mundo.

**2. Alucinan.** Inventan hechos con total confianza. Papers inexistentes, datos falsos, DOIs fabricados.

**3. Tienen sesgos.** Reflejan los sesgos de sus datos de entrenamiento. Si la mayoría de textos de ecología son del hemisferio norte, el modelo "sabe" más sobre eso que sobre bosques valdivianos.

**4. No aprenden de la conversación.** Cada sesión empieza desde cero (con excepciones recientes).

**5. No acceden a información en tiempo real** (a menos que tengan herramientas de búsqueda).

---

# La distinción clave

## Correlación ≠ Comprensión

Un LLM sabe que después de "el pudú es el ciervo más" suele venir "pequeño" — porque ha visto ese patrón miles de veces.

Pero **no sabe qué es un pudú**. No ha visto uno. No comprende "pequeño" en relación a un cuerpo.

> Produce la respuesta correcta **por la razón equivocada** — o más precisamente, sin razón. Solo patrón.

---
<style scoped> {font-size:28px; }</style>


# La razón: La habitación china (Searle, 1980)

<div class="cols">

![w:550px](./figs/searl.png)


- *Desde afuera*: respuestas perfectas en chino.
- *Desde dentro*: solo reglas mecánicas. Ninguna comprensión.

</div>

<!--
<div class="img-placeholder">
📎 IMAGEN: Diagrama de la "Chinese Room" de Searle — una persona encerrada en una habitación recibe mensajes en chino por una ranura, consulta un libro de reglas gigante, y envía respuestas perfectas en chino. Desde afuera parece que habla chino. ¿Entiende? Buscar: "Searle Chinese Room diagram" o "Chinese Room thought experiment illustration".
</div>
-->

Un LLM es esa habitación — a una **escala inimaginable**.

> ¿Entiende? Searle dice que no. El debate sigue abierto. Pero la distinción importa para saber **cuándo confiar**.

---

<!-- _class: invert -->

# Implicaciones para la conservación

---

# Oportunidades

- Redactar borradores de informes
- Resumir literatura científica rápidamente
- Generar código para análisis de datos
- Traducir documentos técnicos
- Sugerir hipótesis exploratorias
- Diseñar protocolos de muestreo (como punto de partida)

---
<style scoped> {font-size:28px; }</style>


# Riesgos

- Citar **papers que no existen**
- Dar datos numéricos **inventados** con apariencia de precisión
- Aplicar métodos estadísticos **incorrectos** sin advertirlo
- Reproducir sesgos (más conocimiento sobre ecosistemas boreales que australes)
- Generar una falsa sensación de autoridad

> *"En conservación, una conclusión equivocada basada en una alucinación puede traducirse en una mala política pública. El costo del error no es un ensayo reprobado — puede ser un ecosistema dañado."*

---
<style scoped> {font-size:28px; }</style>

# La regla de oro

Un LLM es un **asistente**, no un experto.

Lo que produce es un **borrador**, no una verdad.

**Siempre:**
1. Verificar datos y fuentes
2. Documentar los prompts usados
3. Explicar en sus propias palabras
4. No delegar el juicio crítico

> La Semana 7 lanzan la investigación grupal sobre IA y conservación. Todo lo de hoy aplica directamente.

---

<!-- _class: lead -->

# 🧪 Laboratorio práctico
## "Interrogando al LLM"

*Primera sesión con pantallas. Van a poner a prueba lo que acaban de aprender.*

---

<!-- _class: lab -->
<style scoped> {font-size:28px; }</style>

# Fase 1 · El mismo prompt, 5 formas (20 min)

**Pregunta base:** *"¿Cuáles son las principales amenazas para la conservación del bosque valdiviano?"*

| Versión | Estilo del prompt |
|---|---|
| 1 | Pregunta directa |
| 2 | "Responde como un experto en ecología" |
| 3 | "Explícalo para un niño de 10 años" |
| 4 | "Cita fuentes académicas" |
| 5 | La misma pregunta **en inglés** |

**Registrar:** prompt exacto, puntos principales, información sospechosa, ¿las fuentes citadas existen?

---
<style scoped> {font-size:28px; }</style>

<!-- _class: lab -->

# Fase 2 · Caza de alucinaciones (15 min)

**Tarea:** intenten que el LLM produzca una **alucinación verificable**.

**Estrategias:**
- Pedir papers específicos sobre un tema nicho: *"3 papers sobre la dieta del monito del monte post-2020"*
- Preguntar datos numéricos precisos: *"¿Cuántos individuos de huemul quedan en Los Ríos?"*
- Inventar un concepto falso: *"¿Qué opinas del Índice de Fragmentación de Petersen?"* (no existe)

**Registrar:** prompt, respuesta, verificación (¿verdad o alucinación?).

💬 *¿Lograron hacerlo alucinar? ¿Qué tan difícil fue?*

---

<!-- _class: invert -->

# Discusión plenaria

---

<!-- _class: pregunta -->

# ¿Cambió la respuesta entre las 5 versiones del prompt?

Generalmente sí — y a veces mucho. El prompt importa tanto como la pregunta. Un LLM no tiene una "respuesta correcta" almacenada — genera una nueva cada vez.

---

<!-- _class: pregunta -->

# ¿Encontraron alucinaciones?

Casi seguro que sí, especialmente con las citas. ¿Cómo lo verificaron? ¿Cuánto tardaron?

---

<!-- _class: pregunta -->

# ¿Cuándo confiarían en un LLM y cuándo no?

Confiable: ideas generales, resúmenes, borradores, reformulación.
No confiable: datos numéricos específicos, citas, hechos verificables, decisiones críticas.

---

<!-- _class: pregunta -->

# ¿Cómo se conecta con las Semanas 3 y 5?

Semana 3: el LLM explota la **redundancia** del lenguaje — predice lo probable.
Semana 5: sigue reglas (muy complejas), pero no **entiende** — como la MT.

---

# Lo que aprendimos hoy

- Los LLMs son producto de 66 años de desarrollo: perceptrón → redes → deep learning → transformers → escala
- Funcionan prediciendo **el siguiente token** usando patrones estadísticos
- **No entienden** — producen texto plausible, no necesariamente verdadero
- **Alucinan** — inventan hechos con confianza
- Son **herramientas poderosas** si se usan con criterio y verificación
- En conservación, el costo de confiar ciegamente puede ser alto

---

# Próxima semana

## Semana 7 · IA y Conservación: síntesis e investigación grupal

Lanzan el trabajo grupal de investigación (2000 palabras + presentación oral).

**Temas posibles:** cámaras trampa con IA, monitoreo acústico, clasificación satelital, IA para priorización, ética de la IA en territorios indígenas...

*Todo lo que aprendieron en las Semanas 1–6 les da el marco para evaluar críticamente estas tecnologías.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 6 · Del perceptrón a ChatGPT: ¿Qué son los LLMs?*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 📝 Control 3
## Máquina de Turing + Fundamentos de LLMs

*15 minutos · Individual · Sin apuntes ni celular*
