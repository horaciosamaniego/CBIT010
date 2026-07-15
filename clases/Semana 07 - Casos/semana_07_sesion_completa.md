# Semana 7: IA y Conservación — Síntesis e investigación grupal

## Guía completa de la sesión

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (2 h cátedra + 1 h taller de investigación) |
| **Objetivo central** | Que los estudiantes conozcan aplicaciones concretas de IA en conservación de biodiversidad, desarrollen criterio para evaluarlas críticamente, y lancen su trabajo de investigación grupal |
| **Idea ancla** | La IA no es magia ni es infalible. Es una herramienta con fortalezas y limitaciones concretas. Evaluar una aplicación de IA en conservación requiere las mismas habilidades que evaluar cualquier método científico: ¿qué datos usa? ¿Qué supuestos hace? ¿Qué errores puede cometer? ¿Quién se beneficia y quién podría perjudicarse? |
| **Prerrequisito** | Semanas 1–6 completas (todo el marco conceptual de la Sección 1) |
| **Materiales** | Proyector, acceso a internet, computador del docente para demos, copias de la rúbrica del trabajo grupal, copias de la hoja de planificación de investigación |
| **Conexión con semanas previas** | Esta clase sintetiza TODO lo anterior. Cada aplicación de IA que se presente puede analizarse con las herramientas de Semanas 1–6 |

---

## PARTE 1: CÁTEDRA (120 minutos)

---

### Bloque A — Apertura: ¿Dónde ya están usando IA en conservación? (15 min)

**Pregunta al curso:**

*"¿Han usado alguna app que use inteligencia artificial para identificar especies?"*

Probablemente varios hayan usado:
- **iNaturalist** (identificación de especies por foto)
- **Merlin** (identificación de aves por canto)
- **PlantNet** (identificación de plantas)
- **Shazam** (no es ecología, pero el principio es el mismo)

*"Cada vez que iNaturalist les dice 'esto parece un Dromiciops gliroides', hay una red neuronal convolucional detrás que analiza los píxeles de la foto y los compara con millones de imágenes etiquetadas. ¿Recuerdan la Semana 2? Los píxeles son números RGB. La red opera sobre esos números — no 've' al monito del monte."*

**Ejercicio rápido (5 min):** Pedir a los estudiantes que abran iNaturalist (o Merlin, o PlantNet) en sus celulares y le muestren una foto de un animal o planta de la sala (un poster, una imagen en pantalla, incluso una foto de otra foto). ¿Lo identifica correctamente? ¿Con qué confianza?

---

### Bloque B — Seis aplicaciones de IA en conservación (50 min)

Presentar seis casos de uso concretos, ~8 minutos cada uno. Para cada caso: qué hace, cómo funciona (conceptualmente), un ejemplo real, y una limitación o riesgo.

#### Caso 1: Identificación automática de especies — Cámaras trampa (8 min)

**Qué hace:** Clasificar automáticamente las fotos de cámaras trampa (¿qué especie aparece?).

**Cómo funciona:** Una red neuronal convolucional (CNN) entrenada con miles de fotos etiquetadas de cada especie. La red aprende patrones de píxeles asociados a cada animal.

**Ejemplo real:** El proyecto **Wildlife Insights** (Google + organizaciones de conservación) ha procesado millones de fotos de cámaras trampa con modelos de clasificación automática.

**Conexión con el curso:**
- Semana 2: las fotos son matrices de píxeles RGB.
- Semana 4: la clasificación es un algoritmo que recibe una entrada (imagen) y produce una salida (especie).
- Semana 6: el modelo "no ve" al animal — opera sobre patrones numéricos.

**Limitación:** Las CNN entrenadas en un ecosistema (e.g., sabana africana) funcionan mal en otro (e.g., bosque valdiviano). Los datos de entrenamiento importan. Si no hay fotos etiquetadas de pudú en el dataset, el modelo no lo reconocerá.

#### Caso 2: Monitoreo acústico — Identificación de cantos (8 min)

**Qué hace:** Grabar sonido ambiental 24/7 y detectar automáticamente qué especies están vocalizando.

**Cómo funciona:** Se convierte el sonido en un **espectrograma** (una imagen donde el eje X es tiempo, el eje Y es frecuencia, y el color es intensidad). Luego se aplica una CNN sobre el espectrograma — el problema de audio se convierte en un problema de imagen.

**Ejemplo real:** **BirdNET** (Cornell Lab of Ornithology) identifica más de 6.000 especies de aves por su canto. En Chile: proyectos de monitoreo acústico en parques nacionales usando AudioMoth + BirdNET.

**Conexión con el curso:**
- Semana 2: el sonido es muestreo + cuantización → secuencias de números.
- Semana 3: la entropía del paisaje sonoro se puede medir — ecosistemas más diversos tienen paisajes sonoros de mayor entropía.
- Semana 6: BirdNET es un modelo de deep learning que clasifica espectrogramas.

**Limitación:** Funciona mal con especies de bajo volumen, en ambientes muy ruidosos (viento, lluvia, ríos), o con especies cuyo canto no está bien representado en el dataset de entrenamiento.

#### Caso 3: Teledetección y clasificación de uso de suelo (8 min)

**Qué hace:** Clasificar imágenes satelitales en categorías de uso de suelo: bosque nativo, plantación, pradera, urbano, agua, etc.

**Cómo funciona:** Cada píxel de la imagen satelital tiene valores en múltiples bandas espectrales (visible, infrarrojo cercano, infrarrojo de onda corta). Un algoritmo de clasificación (puede ser una CNN, un Random Forest, o un SVM) asigna cada píxel a una categoría basándose en su "firma espectral".

**Ejemplo real:** El mapa de cambio de uso de suelo de Chile (CONAF / Universidad Austral) usa imágenes Landsat y clasificación supervisada para monitorear la deforestación y la expansión de plantaciones forestales.

**Conexión con el curso:**
- Semana 2: los píxeles satelitales son como RGB pero con más canales.
- Semana 3: la calidad de la clasificación depende de la relación señal/ruido (nubes = ruido en el canal atmosférico).
- Semana 4: el clasificador es un algoritmo con entrada (píxeles), procedimiento (reglas de decisión), y salida (categoría).

**Limitación:** La clasificación es tan buena como los datos de entrenamiento (puntos de control en terreno). Si los puntos de entrenamiento tienen errores, el mapa completo hereda esos errores. La resolución del satélite también limita: Landsat (30m) no distingue árboles individuales.

#### Caso 4: Modelamiento predictivo — Distribución de especies (8 min)

**Qué hace:** Predecir dónde es probable encontrar una especie, basándose en variables ambientales (clima, topografía, vegetación).

**Cómo funciona:** Modelos como MaxEnt o Random Forest reciben registros de presencia de la especie + capas ambientales, y aprenden la relación entre la distribución y las condiciones. Luego proyectan a áreas no muestreadas o a escenarios futuros (cambio climático).

**Ejemplo real:** Modelos de distribución del huemul bajo escenarios de cambio climático en la Patagonia.

**Conexión con el curso:**
- Semana 3: el modelo aprende patrones de los datos — como un LLM aprende patrones del texto.
- Semana 5: el modelo es computable (es un algoritmo) pero su predicción no es "verdad" — es una estimación basada en supuestos.
- Semana 6: ¿el modelo "entiende" la ecología del huemul? No — encuentra correlaciones estadísticas.

**Limitación:** "Correlation is not causation." El modelo puede predecir que el huemul estará en un lugar porque la temperatura es adecuada, pero no considera que ese lugar esté lleno de ganado o no tenga conectividad.

#### Caso 5: IA para anti-caza furtiva y predicción de amenazas (8 min)

**Qué hace:** Predecir dónde y cuándo es más probable que ocurra caza furtiva, para asignar patrullajes de forma eficiente.

**Cómo funciona:** Modelos de machine learning entrenados con datos históricos de incidentes de caza furtiva, patrullajes, condiciones climáticas, cercanía a caminos, ciclos lunares, etc.

**Ejemplo real:** **PAWS** (Protection Assistant for Wildlife Security), desarrollado por la Universidad de Harvard y desplegado en áreas protegidas de Cambodia, Uganda y Malasia.

**Conexión con el curso:**
- Semana 4: es un problema de optimización — ¿cómo distribuir recursos limitados (patrulleros) para maximizar la cobertura?
- Semana 5: el problema general de "predecir el comportamiento humano" no es computable — pero estimaciones útiles sí son posibles.

**Limitación:** Sesgo de los datos: se registran más incidentes donde hay más patrullajes. El modelo puede aprender que "las zonas más patrulladas son las más peligrosas" — cuando en realidad son las más vigiladas. Es un sesgo de observación idéntico al de la detección imperfecta en ecología (Semana 3).

#### Caso 6: Dimensiones éticas — IA, datos y territorios indígenas (10 min)

**Qué hace:** Plantear las preguntas éticas que las aplicaciones anteriores a menudo ignoran.

**Temas:**
- **Soberanía de datos:** ¿Quién es dueño de los datos de biodiversidad recopilados en territorio indígena? ¿Quién decide cómo se usan?
- **Conocimiento tradicional:** Los modelos de IA se entrenan con datos científicos occidentales. El conocimiento ecológico tradicional rara vez se incorpora — y cuando se incorpora, ¿con consentimiento informado?
- **Sesgo algorítmico en priorización:** Si los algoritmos de priorización de conservación (Marxan, Zonation) optimizan biodiversidad sin considerar los derechos territoriales de comunidades locales, ¿están haciendo conservación o colonialismo verde?
- **Vigilancia:** Los sistemas de monitoreo con cámaras y sensores acústicos diseñados para detectar fauna también pueden monitorear a las personas. ¿Quién controla esos datos?

**Conexión con el curso:**
- Semana 6: los LLMs tienen sesgos porque sus datos de entrenamiento los tienen.
- Semana 3: el "ruido" en los datos ecológicos tiene dimensiones sociales, no solo técnicas.

> *"La IA no es neutra. Toda herramienta incorpora los valores de quien la diseña y los sesgos de los datos que la alimentan. Evaluar críticamente esos sesgos es tan importante como evaluar la precisión técnica."*

---

### Bloque C — El mapa conceptual: lo que aprendieron en la Sección 1 (15 min)

Proyectar un mapa que conecte TODOS los conceptos de las Semanas 1–6 con las aplicaciones presentadas:

```
Sem 1: Instrucciones precisas ─── → Algoritmos de clasificación
Sem 2: Binario, codificación ──── → Píxeles, espectrogramas, tokens
Sem 3: Entropía, redundancia ──── → Diversidad, compresión, detección
Sem 4: Algoritmos, complejidad ── → Optimización de reservas, Marxan
Sem 5: Máquina de Turing ──────── → Límites de la predicción
Sem 6: LLMs, alucinación ──────── → Sesgos, verificación, confianza

                    ↓ TODO CONVERGE EN ↓

      Evaluación crítica de IA en conservación
```

*"No les pedimos que aprendieran estas cosas por separado. Les pedimos que construyeran un marco de pensamiento. Ahora lo van a aplicar."*

---

### Bloque D — El trabajo de investigación grupal (25 min)

#### Presentación del trabajo (10 min)

**Dos entregables:**
1. **Informe escrito** (2000 palabras) — Entrega: Semana 15.
2. **Presentación oral** (10 min + 5 min Q&A) — Semana 15.

**Estructura del informe:**
1. Introducción (contexto + pregunta de investigación)
2. Antecedentes (¿qué tecnología de IA se usa? ¿cómo funciona conceptualmente?)
3. Caso de estudio / Aplicación (un ejemplo concreto y documentado)
4. Análisis crítico (limitaciones, sesgos, cuestiones éticas)
5. Conclusiones
6. Referencias (mínimo 8 fuentes académicas o técnicas)

**Grupos:** 3–4 personas. Se forman hoy.

#### Temas sugeridos (5 min)

| N° | Tema | Palabras clave |
|---|---|---|
| 1 | Identificación automática con cámaras trampa | CNN, Wildlife Insights, cámaras trampa |
| 2 | Monitoreo acústico de biodiversidad | BirdNET, AudioMoth, espectrogramas |
| 3 | Clasificación de imágenes satelitales para deforestación | Landsat, Sentinel, Random Forest, LULCC |
| 4 | Modelos de distribución de especies y cambio climático | MaxEnt, SDM, nicho ecológico |
| 5 | IA para predicción y prevención de caza furtiva | PAWS, machine learning, patrullaje |
| 6 | LLMs para educación ambiental y comunicación científica | ChatGPT, Claude, divulgación |
| 7 | Predicción de dispersión de especies invasoras | Modelos predictivos, invasiones biológicas |
| 8 | Ética de la IA en gestión de territorios indígenas | Soberanía de datos, consentimiento, sesgo |
| 9 | IA en genómica de la conservación | Secuenciación, bioinformática, diversidad genética |
| 10 | Uso de drones + IA para conteo de fauna | Fotogrametría, detección automática, censos |

Los grupos pueden proponer temas propios si los justifican.

#### Rúbrica (10 min)

Proyectar y explicar:

| Criterio | Ponderación | Descripción |
|---|---|---|
| **Claridad de la pregunta de investigación** | 15% | ¿La pregunta es específica, abordable y relevante? |
| **Comprensión técnica de la IA** | 20% | ¿Explican conceptualmente cómo funciona la tecnología? (No se espera nivel técnico profundo, pero sí comprensión de los principios — usando el vocabulario de las Semanas 1–6) |
| **Calidad del caso de estudio** | 20% | ¿El ejemplo es concreto, documentado y bien descrito? |
| **Análisis crítico** | 25% | ¿Identifican limitaciones, sesgos, riesgos éticos? ¿Van más allá de "la IA es buena/mala"? |
| **Calidad de las fuentes** | 10% | ¿Mínimo 8 fuentes? ¿Son académicas o técnicas de calidad? ¿Se verificaron? |
| **Presentación oral** | 10% | Claridad, distribución del tiempo, participación de todos, respuesta a preguntas |

**Evaluación por pares:** cada grupo evalúa a otros dos grupos en la presentación oral (formulario simple: 1–5 en claridad, contenido, y respuesta a preguntas). La evaluación por pares contribuye un 20% de la nota de la presentación.

---

### Bloque E — Cierre de la Sección 1 (15 min)

*"Hoy termina la primera mitad del curso. Partimos hace 7 semanas sin tocar un computador. Lo que construimos fue un marco de pensamiento:*

*— Semana 1: un computador sigue instrucciones precisas.*
*— Semana 2: toda información se codifica en bits.*
*— Semana 3: la información se puede medir, y la sorpresa tiene un precio.*
*— Semana 4: los algoritmos tienen costos diferentes.*
*— Semana 5: hay problemas que no se pueden resolver.*
*— Semana 6: los LLMs son poderosos pero no entienden.*
*— Semana 7: la IA ya está en la conservación — con oportunidades y riesgos.*

*La próxima semana abren Python por primera vez. Pero no van a llegar como novatos: ya saben qué es una variable (celda de memoria), qué es un condicional (rombo en el diagrama de flujo), qué es un bucle (pasadas del bubble sort), y qué es una función (una tabla de transiciones de la MT). La Sección 2 es ponerle sintaxis a lo que ya entienden."*

---

## PARTE 2: TALLER DE INVESTIGACIÓN (60 minutos)

---

### Desarrollo

#### Fase 1 — Formación de grupos (10 min)

- Formar grupos de 3–4 personas (se permiten grupos autoelegidos, con la condición de que no quede nadie sin grupo).
- Si hay 30 alumnos: 8 grupos de 3–4 personas.
- Cada grupo elige un tema (o propone uno propio) y lo registra con el docente.

#### Fase 2 — Trabajo en grupo: definir la pregunta (25 min)

Cada grupo trabaja con la **hoja de planificación** (impresa):

1. **Tema elegido:** _______________
2. **Pregunta de investigación** (específica, no genérica): _______________
   - Malo: "¿Cómo se usa la IA en conservación?"
   - Bueno: "¿Qué tan preciso es BirdNET para identificar aves del bosque valdiviano, y cuáles son las principales fuentes de error?"
3. **Fuentes preliminares** (buscar al menos 5 ahora — pueden usar LLMs para encontrar pistas, pero deben verificar que las fuentes existen):
   - Fuente 1: _______________
   - Fuente 2: _______________
   - Fuente 3: _______________
   - Fuente 4: _______________
   - Fuente 5: _______________
4. **Esquema preliminar** del informe (títulos de secciones)
5. **Distribución de tareas** dentro del grupo

El docente circula entre grupos, orientando las preguntas de investigación (demasiado amplias → acotar; demasiado específicas → ampliar ligeramente).

#### Fase 3 — Puesta en común rápida (15 min)

Cada grupo presenta en **1 minuto**:
- Su tema
- Su pregunta de investigación
- Una fuente que ya encontraron

El docente y el curso dan retroalimentación breve: ¿la pregunta es lo suficientemente específica? ¿El tema es abordable?

#### Fase 4 — Entrega (10 min)

Cada grupo entrega la **hoja de planificación** (propuesta de investigación: 1 página con pregunta, 5 fuentes preliminares, y esquema).

Esto se evalúa como parte de la Semana 7 (ver programa del curso).

---

## Notas pedagógicas

### El tono de esta clase

Esta es la clase de **síntesis**: todo lo que se vio en 6 semanas debe converger. El riesgo es que se sienta como un "resumen" pasivo. Para evitarlo:

- Los 6 casos de uso deben presentarse como **historias**, no como fichas técnicas.
- Cada caso debe incluir al menos una **pregunta al curso** que conecte con semanas anteriores.
- Los videos y demos (iNaturalist, BirdNET, imágenes satelitales) son esenciales para mantener la atención.

### La investigación grupal como evaluación formativa

La investigación no solo evalúa conocimiento — evalúa la capacidad de **buscar, verificar y sintetizar** información sobre IA. Las habilidades que practican aquí (verificar si una fuente existe, distinguir hype de evidencia, identificar sesgos) son las mismas que necesitan para usar LLMs responsablemente en la Sección 2.

### Manejo de grupos

Con 30 alumnos y ~8 grupos, la Fase 2 requiere que el docente circule eficientemente. Estrategia: dedicar ~3 minutos a cada grupo en un primer round (orientar la pregunta), y luego un segundo round de ~2 minutos (verificar fuentes).

Si hay ayudante de cátedra: dividir los grupos entre los dos.

### Conexión con el resto del curso

| Concepto de esta semana | Dónde se profundiza |
|---|---|
| Casos de IA en conservación | Semanas 8–14 (ejemplos de programación usan datos ecológicos reales) |
| Evaluación crítica de fuentes | Semana 15 (presentación oral: Q&A del curso) |
| Trabajo en equipo | Semana 15 (evaluación por pares) |
| Búsqueda bibliográfica con LLMs | Sección 2 (política de IA: documentar prompts, verificar) |
| Ética de la IA | Semana 16 (reflexión final del curso) |
