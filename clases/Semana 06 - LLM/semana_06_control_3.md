---
pdf-engine: xelatex
header-includes:
  - \pagenumbering{gobble}
  -  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{CBIT010}
  - \fancyhead[C]{\bf Control 3}
  - \fancyhead[R]{2026}
  - \fancyfoot{}
  
---


# LLM e Inteligencia Artificial

**Nombre:** ____________________________  **Fecha:** ____________  **Puntaje:** _____ / 24

*Tiempo: 20 minutos. Sin apuntes ni celular. Use el reverso si necesario*


**1. (4 puntos)** Nombre las cuatro partes de una Máquina de Turing y explique brevemente la función de cada una.

<!-- \vspace{3.0cm}  -->


**2. (4 puntos)** La tesis de Church-Turing dice que todo lo computable puede ser computado por una MT. ¿Qué implicación práctica tiene esto para los computadores modernos? Explique en 2–3 oraciones.

<!-- \vspace{3.5cm}  -->

**3. (4 puntos)** ¿Qué es el "problema de la detención" (Halting Problem)? ¿Por qué es importante para la informática?

<!-- \vspace{3.0cm}  -->

**4. (4 puntos)** Explique qué significa "predicción del siguiente token" en el contexto de un LLM. ¿Cómo genera texto un LLM?
<!-- \vspace{3.0cm}  -->

**5. (4 puntos)** ¿Qué es una "alucinación" en un LLM? Dé un ejemplo concreto de cómo podría ser problemático en un contexto de conservación de biodiversidad.

<!-- \vspace{3.5cm}  -->

**6. (4 puntos)** Un compañero dice: *"ChatGPT entiende lo que le digo, por eso responde bien."* ¿Está de acuerdo? Argumente su respuesta usando conceptos de las Semanas 5 y 6.




### Pauta de corrección

| Pregunta | Respuesta esperada                                                                                                                                                                                                                                                        | Puntos                                                                    |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| 1        | Cinta (almacenamiento), Cabezal (lee/escribe/mueve), Estados (memoria interna), Tabla de transiciones (programa/instrucciones) — 1 pt por cada componente bien explicado                                                                                                  | 4                                                                         |
| 2        | Los computadores modernos no pueden resolver más problemas que una MT — solo lo hacen más rápido. Si una MT no puede resolverlo, ningún computador puede.                                                                                                                 | 4 (2 por la equivalencia, 2 por la implicación)                           |
| 3        | Es la pregunta de si se puede crear un programa que determine si otro programa terminará o no. Turing demostró que es imposible → hay problemas no computables → hay límites a lo que las máquinas pueden resolver.                                                       | 4 (2 por definición, 2 por importancia)                                   |
| 4        | El LLM genera una distribución de probabilidad sobre todos los tokens posibles y elige el más probable (con algo de aleatoriedad). Luego agrega ese token a la secuencia y repite, generando texto palabra por palabra.                                                   | 4 (2 por distribución/probabilidad, 2 por el carácter secuencial)         |
| 5        | Una alucinación es cuando el LLM genera información falsa con apariencia de verdad (e.g., citar un paper inexistente). En conservación podría llevar a usar datos erróneos, aplicar métodos inadecuados, o tomar decisiones de manejo basadas en información falsa.       | 4 (2 por definición, 2 por ejemplo ecológico concreto)                    |
| 6        | No — un LLM no "entiende" en el sentido humano. Manipula patrones estadísticos (correlaciones) en texto. Produce la respuesta más probable, no la "verdadera". Es como la MT de la Semana 5: sigue reglas sin comprender su significado. Analogía de la habitación china. | 4 (2 por argumento contra la comprensión, 2 por conexión con MT/Semana 5) |
