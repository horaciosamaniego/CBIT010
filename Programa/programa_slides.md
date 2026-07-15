---
marp: true
theme: default
paginate: true
backgroundColor: #fbfbf4
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 1.6em;
  }
  section.title {
    background: linear-gradient(135deg, #1a5276 0%, #2e86c1 100%);
    color: #44624b;
    text-align: center;
  }
  section.title p, section.title strong, section.title em {
    color: #44624b;
  }
  section.title h1 {
    font-size: 1.6em;
    margin-bottom: 0.2em;
  }
  section.title h2 {
    font-size: 1.1em;
    font-weight: normal;
    opacity: 0.9;
  }
  section.section-header {
    background: linear-gradient(135deg, #1e8449 0%, #27ae60 100%);
    color:  #44624b;;
    justify-content: center;
    text-align: center;
  }
  section.section-header h1 {
    font-size: 2em;
  }
  section.section2-header {
    background: linear-gradient(135deg, #6c3483 0%, #9b59b6 100%);
    color: white;
    justify-content: center;
    text-align: center;
  }
  h1 { color: #1a5276; }
  h2 { color: #1e8449; border-bottom: 2px solid #27ae60; padding-bottom: 0.2em; }
  table { font-size: 0.85em; width: 100%; }
  th { background-color: #2e86c1; color: white; }
  tr:nth-child(even) { background-color: #eaf2ff; }
  .week-label {
    background: #2e86c1;
    color: white;
    border-radius: 4px;
    padding: 2px 8px;
    font-weight: bold;
  }
  ul li { margin-bottom: 0.3em; }
  blockquote {
    border-left: 4px solid #27ae60;
    color: #555;
    font-style: italic;
  }
---

<!-- _class: title -->

# Introducción a la Programación y Manejo de Datos
## para el Manejo y Conservación de Recursos Naturales

<br>

**Horacio Samaniego**
Universidad Austral de Chile
Facultad de Ciencias Forestales y Recursos Naturales

Semestre I · 2026

---

# Información General del Curso

|                         |                                                     |
| ----------------------- | --------------------------------------------------- |
| **Docente**             | Horacio Samaniego                                   |
| **Horario de atencion** | Jueves 8.10-9.40 (o por cita)                       |
| **Oficina**             | 3er piso, a mitad de pasillo                        |
| **Ayudante**            | por definir                                         |
| **Semestre**            | I 2026                                     |
| **Horario**             | Jueves 15:50–19:00 (Clase) + Martes 8:10–9:40 (lab) |
| **Carga**               | 3 h/semana + buena dedicación autónoma             |
| **Créditos**            | 6 cr                                                |
| **Prerrequisitos**      | Ninguno                                             |
| **Idioma**              | Español (e Inglés)                                  |

---

# Descripción del Curso

Este curso introduce a estudiantes de primer año de **Conservación de Recursos Naturales** e **Ingeniería Forestal** al pensamiento computacional y la programación.

> El énfasis no está en *escribir* código sino en **comprender la lógica** que lo sustenta — para evaluar, depurar y dirigir flujos de trabajo asistidos por IA con responsabilidad y criterio.

<!-- 
El curso se divide en **dos secciones**:

- **Sección 1** — *"Pensar como un computador"*: intuición computacional, actividades analógicas, culminando en un trabajo de investigación sobre IA y conservación.
- **Sección 2** — *"Fundamentos de programación con Python"*: tipos de datos, flujo de control, funciones, POO básico y análisis de datos ecológicos.
-->

## Resultados de Aprendizaje

**Al completar el curso, los estudiantes serán capaces de**:

1. Explicar los principios fundamentales de la computación (Máquina de Turing, teoría de la información).
2. Aplicar el **pensamiento algorítmico** para descomponer problemas ecológicos.
3. Evaluar críticamente las **capacidades y limitaciones de los LLMs** y su uso en conservación.
4. Escribir programas en **Python** usando variables, condicionales, bucles, funciones y POO básico.
5. Cargar, limpiar y analizar **conjuntos de datos ecológicos** con Pandas y producir visualizaciones.
6. Usar asistentes de IA de manera **responsable**: formular prompts, verificar salidas y documentar.
7. **Comunicar** procesos de pensamiento computacional por escrito y oralmente.

---

# Estructura General del Curso

| Sección | Enfoque                                                                       | Semanas | Modalidad                    |
| ------- | ----------------------------------------------------------------------------- | ------- | ---------------------------- |
| **1**   | Pensar como un computador: Fundamentos computacionales y alfabetización en IA | 1–7     | Analógica (sin computadores) |
| **2**   | Fundamentos de programación con Python                                        | 8–16    | Programación práctica        |


---

# Evaluación

| Componente | Ponderación | Sección | Tipo |
|---|---|---|---|
| Controles (6 a lo largo del semestre) | 20% | 1 y 2 | Individual |
| Trabajo grupal: IA y Conservación | 20% | 1 | Grupal |
| Tareas de programación (4, en laboratorio) | 25% | 2 | Individual |
| Examen práctico final | 25% | 2 | Individual |
| Participación y actividades de lab. | 10% | 1 y 2 | Individual |

---

# Política de Uso de IA

Los estudiantes **pueden** usar LLMs (Claude, ChatGPT, Gemini) como asistentes en las tareas de la Sección 2.

**Excepto** durante controles y examen final (salvo autorización explícita).

Al usar asistencia de IA, deben:

1. Incluir el **prompt completo** utilizado
2. Anotar qué partes de la salida fueron **modificadas** y por qué
3. **Demostrar comprensión** explicando el código con sus propias palabras

> El uso no atribuido de contenido generado por IA constituye una falta grave a la integridad académica.

---

<!-- _class: section-header -->

# Sección 1
## Pensar como un Computador
### Semanas 1–7 · Sin programación

---

# Semana 1 — ¿Qué es un computador?

**Del ábaco al silicio**

**Clase:** Historia de la computación: ábaco, Babbage, ENIAC, arquitecturas modernas. Capas de abstracción: hardware → SO → aplicaciones. ¿Qué significa *computar*?

**Laboratorio analógico — "Un computador humano"**
- Grupos de 5: un *programador* escribe instrucciones en tarjetas
- Los demás actúan como componentes: memoria, ALU, E/S, unidad de control
- Ejecutaremos instrucciones paso a paso para resolver un problema aritmético
- Discusión: ¿qué salió mal? ¿Por qué es esencial la precisión?

**Evaluación:** Control diagnóstico (sin calificación)

---

# Semana 2 — Comunicación con ceros y unos

**Binario, codificación y representación**

**Clase:** Sistemas numéricos (el decimal, binario, hexadecimal). Cómo los computadores representan texto (ASCII, UTF-8), imágenes (píxeles, RGB) y sonido (muestreo). El bit como unidad fundamental.

**Laboratorio analógico — "Pulseras binarias"**
- Codificaremos nuestras iniciales en binario con cuentas de dos colores
- Intercambiaremos pulseras y decodificaremos las del compañero
- Extensión: codificar un mensaje en ASCII y pasarlo a otro grupo

**Evaluación:** Control 1 — Conversiones binarias y codificación (15 min)

---

# Semana 3 — Teoría de la información

**Información y cómo medir eventos sorpresa**

**Clase:** Entropía de Shannon: ¿qué es la información? Redundancia vs. sorpresa. Compresión. Capacidad de canal y ruido. Conexión con ecología: **índice de diversidad H' de Shannon**.

**Laboratorio analógico — "Adivina el animal: 20 preguntas"**
- Juegan 20 preguntas con fauna chilena
- Registran el número de preguntas necesarias por ronda
- Discusión: estrategias óptimas como árboles de búsqueda binaria
- Calcular la entropía de sus conjuntos de preguntas

---

# Semana 4 — Pensamiento algorítmico

**Recetas para resolver problemas**

**Clase:** ¿Qué es un *algoritmo*? Sus propiedades: finitud, definición, entrada/salida, efectividad. Diagramas de flujo y pseudocódigo. Algoritmos de ordenamiento (burbuja, inserción). Complejidad computacional.

**Laboratorio analógico — "Red de ordenamiento"**
- Los estudiantes se ubican en una grilla dibujada en el suelo
- Cada uno sostiene una tarjeta numerada
- Siguen una red fija de comparación e intercambio para ordenarse
- Carreras cronometradas entre equipos

**Evaluación:** Control 2 — Pseudocódigo para una tarea ecológica real

---

# Semana 5 — La Máquina de Turing

**El computador universal más simple**

**Clase:** Alan Turing y el Entscheidungsproblem. Modelo de la MT: cinta, cabezal, estados, transiciones. Tesis de Church–Turing. Decidibilidad y el problema de la detención. **Todo computador es, en el fondo, una Máquina de Turing.**

**Laboratorio analógico — "Sé la Máquina de Turing"**
- Cinta = tira larga de papel; cabezal = un estudiante que se mueve físicamente
- Tabla de transiciones dada por grupo
- Tarea: implementar una MT que reconozca palíndromos o sume 1 a un número binario

---

# Semana 6 — Del perceptrón a ChatGPT

**¿Qué son los LLMs?** (Large Language Models)

**Clase:** Historia: perceptrón (1958) → redes neuronales → retropropagación → transformadores (2017) → LLMs. Tokens, embeddings, atención, predicción del siguiente token. **Lo que los LLMs pueden y no pueden hacer.** Alucinación, sesgo y la diferencia entre correlación y comprensión.

**Laboratorio — Demostración práctica**
- Los estudiantes interactúan con un LLM (Claude o ChatGPT)
- Hacen la misma pregunta ecológica de 5 formas distintas y comparan salidas
- Identifican una alucinación
- Discusión: ¿cuándo es confiable la salida?

**Evaluación:** Control 3 — Máquinas de Turing y fundamentos de LLMs

---

# Semana 7 — IA y Conservación

**Síntesis e investigación grupal**

**Clase:** Aplicaciones de la IA en conservación:
- Identificación de especies (iNaturalist, visión por computador)
- Monitoreo acústico y teledetección
- Modelamiento poblacional y predicción 
- Consideraciones éticas: soberanía de datos, sesgo algorítmico

**Laboratorio — Lanzamiento del trabajo grupal**
- Grupos de 3–4 eligen un tema de IA en conservación de biodiversidad
- Definen pregunta de investigación, búsqueda bibliográfica preliminar, esquema

**Evaluación:** Propuesta de investigación (1 página + 5 referencias + esquema)

---

<!-- _class: section2-header -->

# Sección 2
## Fundamentos de Programación con Python
### Semanas 8–16 · 28 abr–3 jul · Programación práctica

---

# Semana 8 (28 abr–2 may) — Primeros pasos en Python

**Entorno, variables y tipos**

**Clase:** ¿Por qué Python? Instalación y navegación (Jupyter / VS Code). Variables, asignación, convenciones de nombres. Tipos primitivos: `int`, `float`, `str`, `bool`. Conversión de tipos. `print()` y f-strings.

**Laboratorio de programación**
- Configurar el entorno, escribir el primer script
- Calcular razones ecológicas (densidad poblacional = conteo / área)
- Convertir unidades de temperatura
- Formatear reportes de observación de especies con f-strings

---

# Semana 9 (5–9 may) — Colecciones

**Listas, tuplas, diccionarios y conjuntos**

**Clase:** Colecciones ordenadas vs. no ordenadas. Listas: indexación, segmentación, mutabilidad, métodos (`append`, `sort`, `len`). Tuplas: inmutabilidad. Diccionarios: pares clave-valor. Conjuntos: unicidad y operaciones. Elegir la estructura adecuada.

**Laboratorio de programación**
- Almacenar datos de observación de especies en listas y diccionarios
- Calcular riqueza de especies a partir de una lista
- Usar conjuntos para encontrar especies compartidas entre dos sitios
- Construir un inventario simple de especies

**Evaluación:** Control 4 — Tipos de datos, variables, operaciones con listas

---

# Semana 10 (12–16 may) — Tomando decisiones

**Condicionales y lógica booleana**

**Clase:** Expresiones booleanas y operadores de comparación. `if / elif / else`. Operadores lógicos: `and`, `or`, `not`. Condicionales anidados. Truthiness en Python. Árboles de decisión como paralelo conceptual.

**Laboratorio de programación**
- Clasificador de estado de conservación (tamaño poblacional, tendencia y rango → categoría UICN)
- "Guía de campo" que identifica un árbol con preguntas sí/no sobre rasgos foliares

---

> **Semana de receso académico — 18 al 22 de mayo · No hay clases ni laboratorio**

---

# Semana 11 (26–30 may) — Repetición

**Bucles e iteración**

**Clase:** Bucles `for`: iterando sobre secuencias. `range()`. Bucles `while`: repetición basada en condición. Control de bucles: `break`, `continue`. Bucles anidados. Patrones comunes: acumulación, conteo, búsqueda.

**Laboratorio de programación**
- Procesar una lista de observaciones de especies
- Calcular estadísticas resumidas (abundancia media, máximo/mínimo)
- Simular crecimiento poblacional simple (modelo geométrico) con `while`
- Iterar sobre datos de cuadrantes

**Evaluación:** Control 5 — Condicionales y bucles

---

# Semana 12 (2–6 jun) — Funciones

**Modularidad y reutilización**

**Clase:** Definición de funciones: `def`, parámetros, `return`. Alcance: variables locales vs. globales. Argumentos por defecto y con nombre. Docstrings. Funciones *lambda*.

**Laboratorio de programación**
- Funciones para cálculos ecológicos:
  - Índice de diversidad de Shannon H'
  - Índice de Simpson
  - Acumulación de especies
- Refactorizar código de laboratorios anteriores en funciones
- Construir un pequeño módulo **"caja de herramientas ecológicas"**

---

# Semana 13 (9–13 jun) — Trabajando con datos

**Archivos y una introducción a Pandas**

**Clase:** Lectura y escritura de archivos de texto. Formato CSV. Introducción a **Pandas**: `Series`, `DataFrame`. Lectura de CSV. Operaciones básicas: `head()`, `describe()`, filtrado, selección de columnas. Gráficos con `matplotlib`.

**Laboratorio de programación**
- Cargar un dataset ecológico real (censo de aves de Chile en CSV)
- Limpiar los datos (manejar valores faltantes)
- Calcular estadísticas resumidas por especie/sitio
- Producir un gráfico de barras de abundancia de especies

**Evaluación:** Control 6 — Funciones y alcance (*scope*) de variables

---

# Semana 14 (16–20 jun) — Introducción a programación orientada a objetos (y clases)

**Modelando el mundo en código**

**Clase:** Pensamiento orientado a objetos: estado (atributos) y comportamiento (métodos). Definición de clases: `__init__`, `self`, métodos. Encapsulamiento. Herencia y polimorfismo (conceptual). ¿Cuándo usar POO vs. código procedural?

**Laboratorio de programación**
- Clase `Especie` (nombre, población, estado, tendencia) con métodos `esta_amenazada()`, `proyectar_poblacion(años)`
- Clase `Ecosistema` con lista de Especies y métricas agregadas
- Subclases `Planta` y `Animal` que sobreescriben un método compartido

---

# Semana 15 (23–27 jun) — Integración y presentaciones grupales

**Clase:** De datos crudos a conocimiento: cargar → limpiar → analizar → visualizar → interpretar. Buenas prácticas: Git (introducción), reproducibilidad, comentarios, ética del uso de IA en programación.

**Laboratorio — Presentaciones grupales**
- Presentaciones del trabajo de investigación sobre IA y Conservación
- 10 min de presentación + 5 min de preguntas
- Evaluación por pares

**Evaluación:**
- Entrega del informe grupal de investigación
- Formularios de evaluación por pares

---

# Semana 16 (30 jun–3 jul) — Evaluación final y cierre

**Clase:** Sesión de repaso: conceptos clave de ambas secciones. Preguntas y respuestas. Reflexión: ¿qué aprendimos sobre pensar computacionalmente? ¿Cómo usarán estas habilidades en conservación?

**Laboratorio — Examen práctico final**
- Individual, en laboratorio
- Conjunto de problemas en Python de múltiples partes con contexto ecológico
- Los estudiantes **pueden** usar LLMs como asistentes
- Deben documentar y justificar cada respuesta asistida por IA

**Evaluación:** Examen práctico final (25%)

---

# Trabajo Grupal — IA y Conservación

**Grupos de 3–4 estudiantes**

| Entregable | Detalles |
|---|---|
| **Informe escrito** (2000 palabras) | Introducción, Antecedentes, Caso de Estudio, Análisis Crítico, Conclusiones. Mín. 8 referencias. |
| **Presentación oral** (10 + 5 min) | Material visual claro; todos los integrantes participan. 20% de la nota de la presentación es evaluación por pares. |

**Temas sugeridos:** identificación de especies en cámaras trampa · monitoreo acústico · clasificación satelital de deforestación · priorización de conservación · predicción de especies invasoras · IA en territorios indígenas

---

# Uso Responsable de IA

Tres principios guían este curso:

1. **Comprender primero, automatizar después**
   No se puede evaluar código generado por IA si no se comprende la lógica detrás de él. La Sección 1 existe para construir esa base.

2. **Transparencia antes que prohibición**
   Cuando uses una herramienta de IA, dilo. Incluye tus prompts, anota la salida y explica qué modificaste. Esto es una **habilidad profesional**.

3. **Evaluación crítica siempre**
   Los LLMs producen texto y código que suenan plausibles pero pueden estar equivocados. En conservación, un mal análisis puede llevar a una mala política pública.

---

# Recursos Recomendados

**Sección 1 — Pensamiento Computacional e IA**
- *CS Unplugged* — Bell, Witten y Fellows (csunplugged.org)
- Turing (1936), Shannon (1948) — lecturas históricas (extractos)
- Wolfram (2023) — *What Is ChatGPT Doing… and Why Does It Work?*
- Crawford (2021) — *Atlas of AI*, Yale University Press

**Sección 2 — Programación en Python**
- Severance — *Python for Everybody* (py4e.com)
- Sweigart — *Automate the Boring Stuff with Python*
- McKinney — *Python for Data Analysis* (3ª ed.)

**Datos ecológicos para laboratorios**
- eBird Chile · GBIF · Datos CONAF · MMA datos abiertos

---

<!-- _class: title -->

# ¡Bienvenidos al curso!

**Preguntas:**
Horacio Samaniego
Universidad Austral de Chile


*"No se puede evaluar código que no se comprende."*
---