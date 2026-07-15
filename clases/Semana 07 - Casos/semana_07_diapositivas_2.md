---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  section {
    font-size: 22px; line-height: 1.45; padding: 40px 50px;
    background: #FAFAFA; color: #222;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  }
  section h1 { color: #1B4332; font-size: 1.6em; border-bottom: 3px solid #B2DFDB; padding-bottom: 6px; margin-bottom: 16px; }
  section h2 { color: #2E5E4E; font-size: 1.25em; margin-bottom: 12px; }
  section h3 { color: #40916C; font-size: 1.05em; }
  section strong { color: #1B4332; }
  section em { color: #555; }
  section li { margin-bottom: 4px; }
  section ul, section ol { margin: 6px 0 10px 20px; }
  section p { margin-bottom: 8px; }
  section.lead {
    background: #1B4332; color: #E8F5E9;
    text-align: center; display: flex; flex-direction: column; justify-content: center;
  }
  section.lead h1 { color: #fff; font-size: 2em; border-bottom: none; margin-bottom: 8px; }
  section.lead h2 { color: #A5D6A7; font-weight: 400; font-size: 1.3em; }
  section.lead p, section.lead em { color: #81C784; font-size: 0.85em; }
  section.invert {
    background: #2E5E4E; color: #E8F5E9;
    display: flex; flex-direction: column; justify-content: center; text-align: center;
  }
  section.invert h1 { color: #fff; border-bottom: 3px solid rgba(255,255,255,0.3); font-size: 1.8em; }
  section.invert h2 { color: #A5D6A7; font-size: 1.2em; }
  section.invert h3 { color: #81C784; }
  section.pregunta {
    background: #E8F5E9; color: #1B4332;
    text-align: center; display: flex; flex-direction: column; justify-content: center;
  }
  section.pregunta h1 { font-size: 1.4em; border-bottom: none; color: #1B4332; margin-bottom: 12px; }
  section.pregunta p, section.pregunta em { color: #2E5E4E; font-size: 0.95em; }
  section.caso {
    background: #FFF8E1; color: #333; border-top: 4px solid #F9A825;
  }
  section.caso h1 { color: #E65100; border-bottom: 3px solid #FFE0B2; font-size: 1.4em; }
  section.caso h2 { color: #BF360C; font-size: 1.15em; }
  section.etica {
    background: #FCE4EC; color: #333; border-top: 4px solid #E91E63;
  }
  section.etica h1 { color: #880E4F; border-bottom: 3px solid #F8BBD0; font-size: 1.4em; }
  section.etica h2 { color: #AD1457; font-size: 1.15em; }
  section.lab {
    background: #E3F2FD; color: #333; border-top: 4px solid #1976D2;
  }
  section.lab h1 { color: #0D47A1; border-bottom: 3px solid #BBDEFB; font-size: 1.4em; }
  section.lab h2 { color: #1565C0; font-size: 1.15em; }
  table { font-size: 0.78em; width: 100%; border-collapse: collapse; margin: 8px 0; }
  thead th { background: #2E5E4E; color: #fff; padding: 5px 8px; text-align: left; font-weight: 600; }
  td { padding: 4px 8px; border: 1px solid #ccc; vertical-align: top; }
  tbody tr:nth-child(even) td { background: #F0F7F4; }
  section.caso thead th { background: #E65100; }
  section.caso tbody tr:nth-child(even) td { background: #FFF3E0; }
  section.lab thead th { background: #1565C0; }
  section.lab tbody tr:nth-child(even) td { background: #E3F2FD; }
  blockquote {
    background: #E8F5E9; border-left: 4px solid #2E7D32;
    padding: 10px 16px; margin: 10px 0; font-size: 0.95em; border-radius: 3px;
    color: #1B4332;
  }
  blockquote p { margin: 0; color: #1B4332; }
  blockquote strong { color: #1B4332; }
  section.invert blockquote { background: rgba(255,255,255,0.15); border-left-color: #A5D6A7; color: #fff; }
  section.invert blockquote p, section.invert blockquote strong { color: #fff; }
  section.lead blockquote { background: rgba(255,255,255,0.15); border-left-color: #A5D6A7; color: #fff; }
  section.lead blockquote p, section.lead blockquote strong { color: #fff; }
  section.etica blockquote { background: #FCE4EC; border-left-color: #E91E63; color: #880E4F; }
  section.etica blockquote p { color: #880E4F; }
  pre { font-size: 0.72em; background: #f5f5f5; border-left: 3px solid #40916C; padding: 10px 14px; }
  code { font-size: 0.85em; background: #E8F5E9; padding: 1px 5px; border-radius: 3px; }
  section::after { color: #999; font-size: 0.65em; }
  .img-placeholder {
    background: #E8F5E9; border: 2px dashed #40916C; border-radius: 8px;
    padding: 14px; text-align: center; color: #2E5E4E; font-style: italic;
    font-size: 0.7em; margin: 8px 0;
  }

footer: "Semana 07 · IA y Conservación"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# IA y Conservación
## Síntesis e investigación grupal

*Semana 7 · Cierre de la Sección 1*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

<!-- _class: pregunta -->

# ¿Han usado alguna app que use IA para identificar especies?

*iNaturalist? Merlin? PlantNet?*

*Abran una ahora — muéstrenle una foto de un animal o planta. ¿La identifica bien?*

---

# Detrás de la identificación

Cada vez que iNaturalist dice *"esto parece un Dromiciops gliroides"*:

- Una **red neuronal** analiza los píxeles de la foto (**Sem. 2**: RGB = números)
- Los compara con millones de imágenes etiquetadas (**Sem. 6**: patrones estadísticos)
- Produce una probabilidad (**Sem. 3**: predicción basada en frecuencia)

La red **no "ve"** al monito del monte. Opera sobre números.

<div class="img-placeholder">
📎 IMAGEN: Screenshot de iNaturalist o Merlin identificando una especie chilena (pudú, chucao, monito del monte). Hacer un screenshot en el momento con el celular del docente y proyectarlo.
</div>

---

# Hoja de ruta

1. 📊 **El estado del campo:** la escala de la IA en conservación hoy
2. 🔬 **Seis aplicaciones** concretas
3. ⚖️ **Dimensiones éticas**
4. 🗺️ **El mapa conceptual** de la Sección 1
5. 📋 **Lanzamiento del trabajo de investigación**
6. 🔧 **Taller:** formar grupos, elegir temas, definir preguntas

---

<!-- _class: invert -->

# El estado del campo
## ¿Cuánto ha crecido la IA en conservación?

---

# Los números

- Weinstein (2018) revisó **187 aplicaciones** de visión computacional en ecología animal — organizadas en **descripción**, **conteo** e **identidad**.
- En 2025, la plataforma **Conservation AI** (Fergus et al., 2024) ha procesado más de **30 millones de imágenes**, identificado **9 millones de animales** de **88 especies**, en **900+ proyectos** globales.
- Precisión de los mejores modelos regionales: **mAP > 0.96** (donde 1.0 es perfecto).
- Pero: la precisión varía de **~38%** (mamíferos de bosque tropical) a **~99%** (peces en condiciones controladas).

> El campo ha pasado de preguntar *"¿puede la IA detectar fauna?"* a *"¿puede hacerlo con la precisión, ética y especificidad regional necesarias para cambiar la conservación?"*

---

# El cuello de botella ha cambiado

| Época | Problema principal |
|---|---|
| ~2000 | **Recolectar** datos (pocas cámaras, drones caros) |
| ~2018 | **Analizar** datos (675K imágenes en iNaturalist; 1,2M en Zooniverse — imposibles de revisar a mano) |
| ~2025 | **Generalizar** (modelos de sabana no funcionan en bosque valdiviano) y **confiar** (¿los sesgos del modelo afectan decisiones de conservación?) |

*Para cada caso que veremos hoy, pregúntense: ¿qué datos usa? ¿Qué modelo? ¿Dónde puede fallar? ¿Quién se beneficia y quién podría perjudicarse?*

---

<!-- _class: invert -->

# Seis aplicaciones de IA en conservación

---

<!-- _class: caso -->

# Caso 1 · Cámaras trampa + Clasificación automática

**¿Qué hace?** Clasifica automáticamente miles de fotos de cámaras trampa: ¿qué especie aparece?

**¿Cómo?** CNNs, YOLO, SSD o Faster R-CNN (Obisa et al., 2025) entrenadas con miles de fotos etiquetadas por especie.

<div class="img-placeholder">
📎 IMAGEN: Foto de cámara trampa con un animal (idealmente fauna chilena — pudú, puma, zorro). Alternativa: usar una de las imágenes de detección del Apéndice A de Fergus et al. (2024) — elefante, cebra o jirafa con bounding box.
</div>

**Ejemplo:** **Conservation AI** (Fergus et al., 2024) — 30M imágenes, 88 especies, mAP@0.5 de **0.974** para su modelo de África Subsahariana (29 especies). Modelos ajustados por sitio durante ~1 año (*"situated learning"*).

**Limitación:** CNN entrenada en sabana africana funciona **mal** en bosque valdiviano. Cada nuevo ecosistema necesita su propio dataset etiquetado — y el etiquetado sigue siendo manual y costoso.

---

<!-- _class: caso -->

# Caso 2 · Monitoreo acústico

**¿Qué hace?** Graba sonido 24/7 y detecta automáticamente qué especies están vocalizando.

**¿Cómo?** Sonido → **espectrograma** (imagen de frecuencia × tiempo) → CNN clasifica la imagen.

<div class="img-placeholder">
📎 IMAGEN: Un espectrograma de un canto de ave (idealmente chucao o chercán) junto a una foto de un AudioMoth. Buscar: "bird song spectrogram BirdNET" o "AudioMoth field deployment". Si tienen datos propios, generar un espectrograma con Audacity o Raven.
</div>

**Ejemplo:** **BirdNET** (Cornell) — 6.000+ especies. En Chile: monitoreo en parques nacionales.

**Limitación:** Funciona mal con especies silenciosas, ambientes ruidosos (viento, ríos), o cantos no representados en el dataset.

---

<!-- _class: caso -->

# Caso 3 · Teledetección y uso de suelo

**¿Qué hace?** Clasifica imágenes satelitales: bosque nativo, plantación, pradera, urbano, agua...

**¿Cómo?** Cada píxel tiene valores en múltiples bandas espectrales. Un clasificador asigna categorías por "firma espectral".

<div class="img-placeholder">
📎 IMAGEN: Imagen satelital de la región de Los Ríos mostrando una clasificación de uso de suelo (bosque nativo en verde, plantaciones en verde claro, urbano en gris). Buscar en Copernicus Browser, o usar mapas de cambio de uso de suelo de CONAF/UACh (Echeverría et al.).
</div>

**Ejemplo:** Mapa de cambio de uso de suelo de Chile (CONAF / UACh) — Landsat + clasificación supervisada.

**Limitación:** La clasificación es tan buena como los **datos de entrenamiento en terreno**. Nubes = ruido (**Sem. 3**). Resolución Landsat (30m) no distingue árboles individuales.

---

<!-- _class: caso -->

# Caso 4 · Modelos de distribución de especies

**¿Qué hace?** Predice dónde es probable encontrar una especie, basándose en clima, topografía, vegetación.

**¿Cómo?** Modelos como MaxEnt reciben registros de presencia + capas ambientales → aprenden la relación → proyectan a otras áreas o escenarios futuros.

<div class="img-placeholder">
📎 IMAGEN: Mapa de distribución potencial de una especie chilena (huemul, pudú, o araucaria) bajo escenario actual y bajo cambio climático. Buscar: "species distribution model Chile climate change map" o usar figuras de papers publicados (con cita).
</div>

**Ejemplo:** Distribución del huemul bajo cambio climático en Patagonia.

**Limitación:** Correlación ≠ causalidad (**Sem. 6**). El modelo no sabe que el área predicha está llena de ganado o que no hay conectividad.

---

<!-- _class: caso -->

# Caso 5 · Predicción de caza furtiva + Detección en tiempo real

**¿Qué hace?** Dos enfoques: (1) predecir dónde ocurrirá caza furtiva → optimizar patrullajes. (2) Detectar intrusos en tiempo real → alertar guardaparques.

**¿Cómo?** **PAWS** aprende modelos de comportamiento de cazadores a partir de datos históricos y sugiere rutas de patrullaje. **TrailGuard AI** (Resolve + Intel) usa IA en el dispositivo para detectar humanos/vehículos y enviar alertas instantáneas (Nandutu et al., 2023).

<div class="img-placeholder">
📎 IMAGEN: Mapa de riesgo de caza furtiva con celdas coloreadas (rojo = alto riesgo, verde = bajo). Buscar: "PAWS poaching prediction map" o "anti-poaching AI heat map".
</div>

**Ejemplo:** Conservation AI (Fergus et al., 2024) logró **condenas y sentencias de cárcel** gracias a detecciones en tiempo real — en Uganda (pangolines) y UK (tejones). Una cámara robada siguió transmitiendo sin que los cazadores lo supieran.

**Limitación:** Sesgo de observación — se registran más incidentes donde hay más patrullajes → sesgo idéntico a la **detección imperfecta** (**Sem. 3**).

---

<!-- _class: etica -->

# Caso 6 · Dimensiones éticas

Nandutu et al. (2023): *"La integración de la ética de la IA en los sistemas de conservación ha recibido poca atención."* La mayoría de las herramientas se enfocan en precisión técnica sin un marco ético explícito.

---

<!-- _class: etica -->

# Soberanía de datos

¿Quién es **dueño** de los datos de biodiversidad recopilados en territorio indígena? ¿Quién decide cómo se usan?

En Sudáfrica, GBIF exige licenciamiento; el Endangered Wildlife Trust requiere respeto por embargos. Pero no todos los países tienen estas protecciones (Nandutu et al., 2023).

<div class="img-placeholder">
📎 IMAGEN: Foto de comunidad indígena en territorio del sur de Chile (Mapuche, Huilliche), o mapa de territorios indígenas superpuesto con áreas protegidas. Buscar: "pueblos originarios sur Chile territorio" o "indigenous territory protected areas overlap Chile". Usar con respeto y contexto.
</div>

---

<!-- _class: etica -->

# Ciber-caza furtiva

Un riesgo emergente: cazadores furtivos **hackean etiquetas GPS** y roban datos geoespaciales para rastrear y matar animales (Nandutu et al., 2023).

La transparencia que beneficia a la ciencia — datos abiertos, ubicaciones en tiempo real — puede convertirse en **arma contra la fauna**.

> La misma tecnología que protege puede ser usada para dañar. La seguridad de los datos no es un detalle técnico — es una cuestión de vida o muerte para las especies.

---

<!-- _class: etica -->

# Sesgo algorítmico en priorización

Si Marxan o Zonation optimizan biodiversidad **sin considerar derechos territoriales** de comunidades locales...

¿Están haciendo conservación o **colonialismo verde**?

Fergus et al. (2024) identifican múltiples tipos de sesgo: de **datos** (muestras no representativas), **algorítmico** (diseño del modelo), **cultural** (prioridades de conservación del Norte Global), **temporal** (modelos desactualizados) y de **presentación** (cómo se interpretan los resultados).

> La IA no es neutra. Toda herramienta incorpora los valores de quien la diseña y los sesgos de los datos que la alimentan.

---

<!-- _class: etica -->

# Vigilancia y privacidad

Cámaras trampa y sensores acústicos diseñados para detectar fauna **también pueden monitorear personas**.

En Sudáfrica, el uso de drones dentro de parques nacionales está **prohibido** sin autorización (Nandutu et al., 2023). Los collares GPS pueden alterar el comportamiento animal.

¿Quién controla esos datos? ¿Quién tiene acceso? ¿Hay consentimiento?

> Evaluar los aspectos éticos de una herramienta de IA es **tan importante** como evaluar su precisión técnica.

---

<!-- _class: invert -->

# El mapa de la Sección 1
## Todo conecta

---

# Siete semanas, un marco de pensamiento

| Semana | Concepto | Aplicación en IA y conservación |
|---|---|---|
| 1 | Instrucciones precisas | Los algoritmos de clasificación son instrucciones para máquinas |
| 2 | Codificación binaria | Píxeles, espectrogramas, tokens: todo son números |
| 3 | Entropía, redundancia | Diversidad, compresión, detección imperfecta como ruido |
| 4 | Algoritmos, complejidad | Optimización de reservas: Marxan es un algoritmo |
| 5 | Máquina de Turing | Límites de la predicción: no todo es computable |
| 6 | LLMs, alucinación | Sesgos, verificación, confianza crítica |
| **7** | **Síntesis** | **Evaluar críticamente la IA en conservación** |

---

<!-- _class: pregunta -->

# No les pedimos que aprendieran estas cosas por separado.

# Les pedimos que construyeran un **marco de pensamiento**.

# Ahora lo van a aplicar.

---

<!-- _class: invert -->

# El trabajo de investigación grupal
## 2000 palabras + presentación oral

---

# Los entregables

**1. Informe escrito (2000 palabras)** — Entrega: Semana 15

Estructura:
1. Introducción (contexto + pregunta de investigación)
2. Antecedentes (¿qué IA se usa? ¿cómo funciona conceptualmente?)
3. Caso de estudio (ejemplo concreto y documentado)
4. Análisis crítico (limitaciones, sesgos, ética)
5. Conclusiones
6. Referencias (mínimo 8 fuentes verificadas)

**2. Presentación oral (10 min + 5 min Q&A)** — Semana 15

---

# Temas sugeridos

| N° | Tema |
|---|---|
| 1 | Cámaras trampa + clasificación automática |
| 2 | Monitoreo acústico de biodiversidad |
| 3 | Clasificación satelital para deforestación |
| 4 | Modelos de distribución + cambio climático |
| 5 | IA para predicción de caza furtiva |
| 6 | LLMs para educación ambiental |
| 7 | Predicción de dispersión de especies invasoras |
| 8 | Ética de la IA en territorios indígenas |
| 9 | IA en genómica de conservación |
| 10 | Drones + IA para conteo de fauna |

*Pueden proponer temas propios si los justifican.*

---

# Lecturas sugeridas (disponibles en Notion)

Cuatro artículos como punto de partida — cada grupo lea al menos uno:

| Artículo | Temas que cubre |
|---|---|
| **Weinstein (2018)** · "A computer vision for animal ecology" · *J. Animal Ecology* | Temas 1, 2, 10 — revisión fundacional, glosario de visión computacional |
| **Fergus et al. (2024)** · "Harnessing AI for Wildlife Conservation" · *Conservation* | Temas 1, 5, 10 — Conservation AI: 30M imágenes, condenas por caza furtiva |
| **Obisa et al. (2025)** · "A Review of AI, ML, and DL in Detecting Wildlife" · *Springer* | Temas 1, 3, 10 — arquitecturas CNN, YOLO, SSD, R-CNN explicadas |
| **Nandutu et al. (2023)** · "AI Ethics in Wildlife Conservation in South Africa" · *AI & Society* | Tema 8 — ciber-caza furtiva, marco ético, leyes sudafricanas |

> Estos artículos son también modelos de escritura académica. Weinstein es una revisión; Nandutu es un análisis crítico con propuesta.

---

# Rúbrica

| Criterio | Peso |
|---|---|
| Claridad de la pregunta de investigación | 15% |
| Comprensión técnica de la IA (usando vocabulario Sem. 1–6) | 20% |
| Calidad del caso de estudio | 20% |
| **Análisis crítico** (limitaciones, sesgos, ética) | **25%** |
| Calidad de las fuentes (mínimo 8, verificadas) | 10% |
| Presentación oral | 10% |

> El criterio más pesado es el **análisis crítico**. No busco que digan "la IA es buena" o "la IA es mala". Busco que piensen con rigor.

---

<!-- _class: lab -->

# Taller de investigación
## Formar grupos, elegir temas, definir preguntas

---

<!-- _class: lab -->

# Fase 1 · Formar grupos (10 min)

- Grupos de **3–4 personas**
- Autoelegidos, con la condición de que nadie quede sin grupo
- Registrar los integrantes con el docente

---

<!-- _class: lab -->

# Fase 2 · Definir la pregunta (25 min)

Trabajen con la **hoja de planificación**:

1. **Tema elegido**
2. **Pregunta de investigación** — específica, no genérica
   - ❌ *"¿Cómo se usa la IA en conservación?"*
   - ✅ *"¿Qué tan preciso es BirdNET para identificar aves del bosque valdiviano, y cuáles son las principales fuentes de error?"*
3. **5 fuentes preliminares** — búsquenlas ahora. Pueden usar LLMs para encontrar pistas, pero **verifiquen que las fuentes existen**
4. **Esquema** del informe (títulos de secciones)
5. **Distribución de tareas** dentro del grupo

---

<!-- _class: lab -->

# Fase 3 · Puesta en común (15 min)

Cada grupo presenta en **1 minuto**:
- Su tema
- Su pregunta de investigación
- Una fuente que ya encontraron

El curso y el docente dan retroalimentación:
💬 *¿La pregunta es suficientemente específica? ¿Es abordable en 2000 palabras?*

---

<!-- _class: lab -->

# Fase 4 · Entrega

Entregar la **hoja de planificación**:
- Pregunta de investigación
- 5 fuentes preliminares
- Esquema del informe

**Fecha de entrega del informe final:** Semana 15
**Presentaciones orales:** Semana 15

---

<!-- _class: invert -->

# Cierre de la Sección 1

---

# Lo que construimos en 7 semanas — sin tocar un computador

Semana 1: un computador **sigue instrucciones** precisas.
Semana 2: toda información se **codifica en bits**.
Semana 3: la información se puede **medir**.
Semana 4: los algoritmos tienen **costos diferentes**.
Semana 5: hay problemas que **no se pueden resolver**.
Semana 6: los LLMs son poderosos pero **no entienden**.
Semana 7: la IA ya está en la conservación — con **oportunidades y riesgos**.

---

# Próxima semana: empieza la Sección 2

## Semana 8 · Primeros pasos en Python

<div class="img-placeholder">
📎 IMAGEN: Screenshot de un Jupyter Notebook con un "Hello World" ecológico — por ejemplo: `print("Bienvenidos al bosque valdiviano")` o un cálculo de densidad poblacional. Generar uno propio y hacer screenshot.
</div>

*La semana que viene abren Python. Pero no llegan como novatos: ya saben qué es una variable, un condicional, un bucle y una función. La Sección 2 es ponerle **sintaxis** a lo que ya entienden.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 7 · IA y Conservación: síntesis e investigación grupal*
*Cierre de la Sección 1*
