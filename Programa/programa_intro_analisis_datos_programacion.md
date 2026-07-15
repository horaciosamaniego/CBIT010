# INTRODUCCIÓN A LA PROGRAMACIÓN Y MANEJO DE DATOS
## para el Manejo y Conservación de Recursos Naturales


|                    |                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------ |
| **Docente**        | Horacio Samaniego                                                                    |
| **Institución**    | Universidad Austral de Chile — Facultad de Ciencias Forestales y Recursos Naturales  |
| **Semestre**       | Semestre I 2026]                                                                     |
| **Horario**        | [ Jueves 3.50-19.00 — 2 h Clase ] + [Martes 8.10-9.40 — 1 h laboratorio ] (3 h/semana) |
| **Créditos**       | 6cr                                                                                  |
| **Prerrequisitos** | Ninguno                                                                              |
| **Idioma**         | Español (e Inglés)                                                                    |

---

## 1. Descripción del Curso

Este curso introduce a los estudiantes de primer año de Conservación de Recursos Naturales e Ing. Forestal al pensamiento computacional, los fundamentos del análisis de datos y la programación. En una era en que las herramientas de IA pueden generar código, el énfasis no está centrado en la escritura de código sino en comprender la lógica subyacente que lo sustenta — se espera que los estudiantes puedan evaluar, depurar y dirigir flujos de trabajo asistidos por IA con responsabilidad y criterio.

El curso se divide en dos secciones. La **Sección 1** ("Pensar como un computador") construye la intuición computacional a través de actividades analógicas, juegos y clases conceptuales, culminando en un trabajo grupal de investigación sobre aplicaciones de la IA para la conservación de la biodiversidad. La **Sección 2** ("Fundamentos de programación con Python") transita hacia la programación práctica, cubriendo tipos de datos, flujo de control, funciones, nociones básicas orientadas a objetos y manipulación de datos con sets de datos ecológicos reales.

## 2. Resultados de Aprendizaje

Al completar exitosamente este curso, los estudiantes serán capaces de:

- Explicar los principios fundamentales de la computación, incluyendo el modelo de la Máquina de Turing y los fundamentos de la teoría de la información.
- Aplicar el pensamiento algorítmico para descomponer problemas ecológicos y de conservación en procedimientos precisos y paso a paso.
- Evaluar críticamente las capacidades y limitaciones de los Modelos de Lenguaje de Gran Escala (LLMs) y articular cómo se está aplicando la IA en la conservación de la biodiversidad.
- Escribir programas en Python bien estructurados usando variables, condicionales, bucles, funciones y construcciones básicas de orientación a objetos.
- Cargar, limpiar y analizar conjuntos de datos ecológicos usando Python (Pandas), y producir visualizaciones simples.
- Usar asistentes de programación con IA de manera responsable: formular prompts efectivos, verificar las salidas y documentar el trabajo asistido por IA.
- Comunicar claramente los procesos de pensamiento computacional y las decisiones de programación tanto por escrito como oralmente.

## 3. Estructura General del Curso

| **Sección** | **Enfoque**                                                                   | **Semanas** | **Modalidad**                |
| ----------- | ----------------------------------------------------------------------------- | ----------- | ---------------------------- |
| **1**       | Pensar como un computador: Fundamentos computacionales y alfabetización en IA | 1–7         | Analógica (sin programación) |
| **2**       | Fundamentos de programación con Python                                        | 8–16        | Programación práctica        |

## 4. Evaluación

| **Componente**                                                              | **Ponderación** | **Sección** | **Tipo**   |
| --------------------------------------------------------------------------- | --------------- | ----------- | ---------- |
| Controles (6 a lo largo del semestre)                                       | 20%             | 1 y 2       | Individual |
| Trabajo grupal de investigación: IA y Conservación (informe + presentación) | 20%             | 1           | Grupal     |
| Tareas de programación (4, basadas en laboratorio)                          | 25%             | 2           | Individual |
| Examen práctico final                                                       | 25%             | 2           | Individual |
| Participación y actividades de laboratorio analógico                        | 10%             | 1 y 2       | Individual |

**Política de uso de IA:** Los estudiantes pueden usar LLMs (e.g., Claude, ChatGPT, Gemini) como asistentes de programación durante las tareas de la Sección 2, *excepto durante los controles y el examen final, salvo que se autorice explícitamente*. Cuando se utilice asistencia de IA, los estudiantes deben: (1) incluir el prompt completo utilizado, (2) anotar qué partes de la salida fueron modificadas y por qué, y (3) demostrar comprensión explicando el código en sus propias palabras. El uso no atribuido de contenido generado por IA constituye una falta grave a la integridad académica.

---

## 5. Calendario Semanal

### Sección 1: Pensar como un Computador

*Las semanas 1 a 7 se desarrollan enteramente sin computadores. Los estudiantes desarrollan pensamiento computacional mediante juegos físicos, discusiones grupales y ejercicios con papel y lápiz.*

### Semana 1 — Martes 17 mar / Jueves 19 mar: ¿Qué es un computador? Del ábaco al silicio

**Clase:** Historia de la computación: ábaco, máquinas de Babbage, ENIAC, arquitecturas modernas. Capas de abstracción: hardware → sistema operativo → aplicaciones. ¿Qué significa "computar"?

**Laboratorio analógico:** *"Computador humano."* Los estudiantes forman grupos de 5. Uno es el "programador" que escribe instrucciones en tarjetas; los demás son "componentes" (memoria, ALU, E/S, unidad de control) que deben ejecutarlas paso a paso para resolver un problema aritmético simple. Discusión final: ¿qué salió mal? ¿Por qué es esencial la precisión en las instrucciones?

**Evaluación:** Control diagnóstico (sin calificación): conocimientos previos sobre conceptos de computación.


### Semana 2 — Martes 24 mar / Jueves 26 mar: Hablando en ceros y unos: binario, codificación y representación

**Clase:** Sistemas numéricos (decimal, binario, hexadecimal). Cómo los computadores representan texto (ASCII, UTF-8), imágenes (píxeles, RGB) y sonido (muestreo). El bit como unidad fundamental.

**Laboratorio analógico:** *"Pulseras binarias."* Los estudiantes codifican sus iniciales en binario usando cuentas de dos colores, luego intercambian pulseras y decodifican las del compañero. Extensión: codificar un mensaje corto usando ASCII y pasarlo a otro grupo para decodificación.

**Evaluación:** Control 1: Conversiones binarias y codificación (15 min, individual).


### Semana 3 — Martes 31 mar / Jueves 2 abr ⚠️ Semana Santa: Teoría de la información: midiendo la sorpresa

**Clase:** Entropía de Shannon: ¿qué es la información? Redundancia vs. sorpresa. Compresión como eliminación de redundancia. Capacidad de canal y ruido. Conexión con la ecología: índices de diversidad (H' de Shannon) como medidas de información.

**Laboratorio analógico:** *"Adivina el animal — 20 preguntas."* Los estudiantes juegan 20 preguntas con fauna chilena. Después de cada ronda, registran el número de preguntas necesarias. Discusión: estrategias óptimas de preguntas como árboles de búsqueda binaria. Calcular la entropía de sus conjuntos de preguntas.


### Semana 4 — Martes 7 abr / Jueves 9 abr: Pensamiento algorítmico: recetas para resolver problemas

**Clase:** ¿Qué es un algoritmo? Propiedades: finitud, definición, entrada/salida, efectividad. Diagramas de flujo y pseudocódigo. Algoritmos de ordenamiento como casos de estudio (burbuja, inserción). Complejidad: la idea de "¿qué tan difícil es este problema?"

**Laboratorio analógico:** *"Red de ordenamiento."* Los estudiantes se colocan sobre una grilla dibujada con tiza en el suelo, cada uno sosteniendo una tarjeta numerada. Siguen una red fija de posiciones de comparación e intercambio para ordenarse. Carreras cronometradas entre equipos usando diferentes estrategias de ordenamiento.

**Evaluación:** Control 2: Escribir pseudocódigo para una tarea ecológica real (por ejemplo, "decidir qué cuadrantes muestrear en un transecto").


### Semana 5 — Martes 14 abr / Jueves 16 abr: La Máquina de Turing: el computador universal más simple

**Clase:** Alan Turing y el Entscheidungsproblem. El modelo de la Máquina de Turing: cinta, cabezal, estados, transiciones. Tesis de Church–Turing. Decidibilidad y el problema de la detención (conceptual). Por qué esto importa: todo computador es, en el fondo, una Máquina de Turing.

**Laboratorio analógico:** *"Sé la Máquina de Turing."* Cada grupo recibe una tira larga de papel (la cinta), un marcador y una tabla de transiciones. Un estudiante actúa como el cabezal, moviéndose físicamente a lo largo de la tira, leyendo/escribiendo símbolos y cambiando de estado. Tarea: implementar una MT simple que reconozca palíndromos o sume 1 a un número binario.


### Semana 6 — Martes 21 abr / Jueves 23 abr: Del perceptrón a ChatGPT: ¿Qué son los LLMs?

**Clase:** Breve historia: perceptrón (1958) → redes neuronales → retropropagación → aprendizaje profundo → transformadores (2017) → LLMs. ¿Cómo "funciona" un modelo de lenguaje? Tokens, embeddings, atención, predicción del siguiente token. Lo que los LLMs pueden y no pueden hacer. Alucinación, sesgo y la diferencia entre correlación y comprensión.

**Laboratorio analógico:** Demostración práctica: los estudiantes interactúan con un LLM gratuito (por ejemplo, Claude o ChatGPT). Ejercicio estructurado: hacer la misma pregunta ecológica de 5 formas diferentes y comparar las salidas. Identificar una alucinación. Discusión: ¿cuándo es confiable la salida?

**Evaluación:** Control 3: Preguntas conceptuales sobre Máquinas de Turing y fundamentos de LLMs.


### Semana 7 — Martes 28 abr / Jueves 30 abr: IA y conservación: síntesis e investigación grupal

**Clase:** Aplicaciones de la IA en conservación: identificación de especies (iNaturalist/visión por computador), monitoreo acústico, teledetección y clasificación de uso de suelo, modelamiento poblacional, predicción anti-caza furtiva. Consideraciones éticas: soberanía de datos, conocimiento indígena, sesgo algorítmico en la priorización de conservación.

**Laboratorio:** Lanzamiento del trabajo de investigación grupal (grupos de 3–4). Cada grupo selecciona un tema sobre el uso de IA/LLMs en conservación de biodiversidad. En clase: definir pregunta de investigación, búsqueda bibliográfica preliminar, esquema. Entregable: informe escrito de 2000 palabras + presentación oral de 10 min (entrega en Semana 14).

**Evaluación:** Entregar: propuesta de investigación de 1 página con pregunta, 5 referencias preliminares y esquema.


---

### Sección 2: Fundamentos de Programación con Python

*Desde la Semana 8 en adelante, cada sesión incluye programación práctica. Los estudiantes trabajan en Jupyter Notebooks (o VS Code) con conjuntos de datos ecológicos y problemas contextualizados en conservación.*


### Semana 8 — Martes 5 may / Jueves 7 may: Primeros pasos en Python: entorno, variables y tipos

**Clase:** ¿Por qué Python? Instalación y navegación del entorno (Jupyter Notebooks o VS Code). Variables, asignación, convenciones de nombres. Tipos de datos primitivos: int, float, str, bool. Conversión de tipos. La función print() y f-strings. Comentarios y legibilidad.

**Laboratorio de programación:** Programación guiada: configurar el entorno, escribir el primer script. Ejercicios: calcular razones ecológicas (por ejemplo, densidad poblacional = conteo / área), convertir unidades de temperatura, formatear reportes de observación de especies usando f-strings.


### Semana 9 — Martes 12 may / Jueves 14 may: Colecciones: listas, tuplas, diccionarios y conjuntos

**Clase:** Colecciones ordenadas vs. no ordenadas. Listas: indexación, segmentación, mutabilidad, métodos comunes (append, sort, len). Tuplas: inmutabilidad y empaquetado/desempaquetado. Diccionarios: pares clave-valor, eficiencia de búsqueda. Conjuntos: unicidad y operaciones de conjuntos. Elegir la estructura adecuada.

**Laboratorio de programación:** Ejercicios: almacenar datos de observación de especies en listas y diccionarios. Calcular riqueza de especies a partir de una lista. Usar conjuntos para encontrar especies compartidas entre dos sitios de muestreo. Contexto ecológico: construir un inventario simple de especies.

**Evaluación:** Control 4: Tipos de datos, asignación de variables, operaciones con listas.


> **Semana 18–22 may — Sin clases (feriado)**

### Semana 10 — Martes 26 may / Jueves 28 may: Tomando decisiones: condicionales y lógica booleana

**Clase:** Expresiones booleanas y operadores de comparación. if / elif / else. Operadores lógicos: and, or, not. Condicionales anidados. Truthiness en Python. Árboles de decisión como paralelo conceptual.

**Laboratorio de programación:** Ejercicios: escribir un clasificador de estado de conservación (dados el tamaño poblacional, tendencia y rango, asignar categoría UICN). Construir una simple "guía de campo" que identifique un árbol basándose en preguntas sí/no sobre rasgos foliares.


### Semana 11 — Martes 2 jun / Jueves 4 jun: Repetición: bucles e iteración

**Clase:** Bucles for: iterando sobre secuencias. range(). Bucles while: repetición basada en condición. Control de bucles: break, continue. Bucles anidados. Patrones comunes: acumulación, conteo, búsqueda. La conexión con la complejidad algorítmica (revisitada).

**Laboratorio de programación:** Ejercicios: procesar una lista de observaciones de especies, calcular estadísticas resumidas (abundancia media, máximo/mínimo). Simular crecimiento poblacional simple (modelo geométrico) usando un bucle while. Contexto ecológico: iterar sobre datos de cuadrantes.

**Evaluación:** Control 5: Condicionales y bucles (trazar la salida de código, escribir funciones cortas).


### Semana 12 — Martes 9 jun / Jueves 11 jun: Funciones: modularidad y reutilización

**Clase:** Definición de funciones: def, parámetros, return. Alcance: variables locales vs. globales. Argumentos por defecto y argumentos con nombre. Docstrings. Por qué importan las funciones: principio DRY, testing, legibilidad. Funciones lambda (breve).

**Laboratorio de programación:** Ejercicios: escribir funciones para cálculos ecológicos: índice de diversidad de Shannon H', índice de Simpson, acumulación de especies. Refactorizar código de laboratorios anteriores en funciones. Construir un pequeño módulo "caja de herramientas ecológicas".


### Semana 13 — Martes 16 jun / Jueves 18 jun: Trabajando con datos: archivos y una introducción a Pandas

**Clase:** Lectura y escritura de archivos de texto. Formato CSV. Introducción a Pandas: Series, DataFrame. Lectura de CSV en DataFrames. Operaciones básicas: head(), describe(), filtrado de filas, selección de columnas. Gráficos simples con matplotlib.

**Laboratorio de programación:** Ejercicios: cargar un conjunto de datos ecológicos real (por ejemplo, datos de censo de aves de Chile en CSV). Limpiar los datos (manejar valores faltantes). Calcular estadísticas resumidas por especie/sitio. Producir un gráfico de barras de abundancia de especies.

**Evaluación:** Control 6: Funciones (escribir una función dada una especificación, trazar el alcance de variables).


### Semana 14 — Martes 23 jun / Jueves 25 jun: Objetos y clases: modelando el mundo en código

**Clase:** Pensamiento orientado a objetos: los objetos tienen estado (atributos) y comportamiento (métodos). Definición de clases: \_\_init\_\_, self, métodos. Encapsulamiento. Herencia y polimorfismo: una introducción conceptual. Cuándo usar POO vs. código procedural.

**Laboratorio:** Presentaciones grupales del trabajo de investigación sobre IA y Conservación (10 min cada una + 5 min de preguntas). Evaluación por pares.

**Evaluación:** Entrega del informe grupal de investigación. Formularios de evaluación por pares.


### Semana 15 — Martes 30 jun / Jueves 2 jul: Evaluación final y cierre del curso

**Clase:** Sesión de repaso: conceptos clave de ambas secciones. Preguntas y respuestas. Reflexión: ¿qué aprendimos sobre pensar computacionalmente? ¿Cómo usarán estas habilidades en sus carreras en conservación?

**Laboratorio:** Examen práctico final (en laboratorio, individual): un conjunto de problemas en Python de múltiples partes con contexto ecológico. Los estudiantes pueden usar LLMs como asistentes, pero deben documentar y justificar cada respuesta asistida por IA.

**Evaluación:** Examen práctico final.


---

## 6. Recursos Recomendados

### Sección 1 — Pensamiento Computacional e IA

- Bell, T., Witten, I. y Fellows, M. — *CS Unplugged* (csunplugged.org): actividades de código abierto para enseñar conceptos de ciencias de la computación sin computadores.
- Turing, A. M. (1936). On Computable Numbers, with an Application to the Entscheidungsproblem. [Lectura histórica, extractos.]
- Shannon, C. E. (1948). A Mathematical Theory of Communication. [Extractos y lectura guiada.]
- Wolfram, S. (2023). *What Is ChatGPT Doing… and Why Does It Work?* [Gratuito en línea, explicación accesible de los LLMs.]
- Crawford, K. (2021). *Atlas of AI.* Yale University Press. [Perspectivas críticas sobre la IA.]

### Sección 2 — Programación en Python

- Severance, C. — *Python for Everybody* (py4e.com): libro de texto y curso gratuito, excelente para principiantes.
- Sweigart, A. — *Automate the Boring Stuff with Python* (automatetheboringstuff.com): gratuito en línea, enfoque práctico.
- McKinney, W. — *Python for Data Analysis* (3ª ed.): referencia para Pandas y flujos de trabajo con datos.
- VanderPlas, J. — *Python Data Science Handbook* (jakevdp.github.io/PythonDataScienceHandbook/): gratuito en línea, bueno para visualización de datos.

### Fuentes de Datos Ecológicos para Laboratorios

- eBird Chile (ebird.org/region/CL): datos de observación de aves.
- GBIF (gbif.org): Infraestructura Global de Información sobre Biodiversidad — registros de ocurrencia de especies.
- Datos geoespaciales de CONAF: áreas protegidas de Chile e inventario forestal.
- Datos abiertos del MMA (datos.mma.gob.cl): conjuntos de datos ambientales del Ministerio del Medio Ambiente de Chile.

---

## 7. Uso Responsable de IA en Este Curso

Las herramientas de IA están transformando la forma en que escribimos código y analizamos datos. Este curso abraza esa realidad en lugar de ignorarla. Nuestro enfoque se guía por tres principios:

- **Comprender primero, automatizar después.** No se puede evaluar código generado por IA si no se comprende la lógica detrás de él. La Sección 1 existe precisamente para construir esa base.
- **Transparencia antes que prohibición.** Cuando uses una herramienta de IA, dilo. Incluye tus prompts, anota la salida y explica qué modificaste. Esta es una habilidad profesional, no una confesión.
- **Evaluación crítica siempre.** Los LLMs producen texto y código que suenan plausibles pero pueden estar equivocados. Tu trabajo es verificar la corrección, no confiar ciegamente. En conservación, un mal análisis puede llevar a una mala política pública.

Las reglas específicas para cada componente de evaluación se detallan en las instrucciones de cada tarea. En caso de duda, consulta al docente.

---

## 8. Trabajo Grupal de Investigación: IA y Conservación

En grupos de 3–4, los estudiantes investigarán una aplicación específica de IA o LLMs en la conservación de la biodiversidad. El proyecto tiene dos entregables:

- **Informe escrito (2000 palabras):** estructurado como Introducción, Antecedentes, Caso de Estudio/Aplicación, Análisis Crítico (limitaciones, sesgos, cuestiones éticas) y Conclusiones. Mínimo 8 referencias académicas o técnicas.
- **Presentación oral (10 min + 5 min de preguntas):** material visual claro, todos los integrantes del grupo participan. La evaluación por pares contribuye un 20% de la nota de la presentación.

Los temas sugeridos incluyen (pero no se limitan a): identificación automatizada de especies a partir de cámaras trampa, monitoreo acústico de comunidades de aves o cetáceos, clasificación de imágenes satelitales para detección de deforestación, priorización de conservación asistida por IA, uso de LLMs para educación ambiental, modelamiento predictivo de la dispersión de especies invasoras, y dimensiones éticas de la IA en la gestión de territorios indígenas.

---

## 9. Integridad Académica

Todo trabajo entregado debe ser propio (o del grupo, para las tareas grupales). El plagio, la colaboración no autorizada y el uso no atribuido de contenido generado por IA constituyen faltas a la integridad académica y serán tratadas conforme a la normativa universitaria. En caso de duda sobre qué constituye colaboración aceptable o uso de IA, consulta al docente antes de entregar.
