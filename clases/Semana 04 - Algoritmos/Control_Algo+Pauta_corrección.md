---
pdf-engine: xelatex
header-includes:
  - \pagenumbering{gobble}
  -  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{CBIT010}
  - \fancyhead[C]{\bf Control 2}
  - \fancyhead[R]{2026}
  - \fancyfoot{}
---
# Algoritmos


**Nombre:** PAUTA DE CORRECCIÓN    **Fecha:** ____________  **Puntaje:** 20 / 20

*Tiempo: 15 minutos. Sin apuntes ni celular. (Use el reverso de la hoja si es necesario)*

**1. (4 puntos)** Enumere las cinco propiedades que debe cumplir un algoritmo. Para cada una, escriba una frase que la explique.


**2. (6 puntos)** Usted debe decidir qué cuadrantes muestrear en un transecto de 20 cuadrantes. La regla es: muestrear todo cuadrante cuya cobertura vegetal sea mayor al 60%. Los datos de cobertura están en una lista.

Escriba el **pseudocódigo** de un algoritmo que recorra la lista, evalúe cada cuadrante, y produzca como salida la lista de cuadrantes seleccionados.

**3. (4 puntos)** Dibuje un **diagrama de flujo** para el siguiente procedimiento: "Si la temperatura es menor a 5°C, registrar 'helada'. Si está entre 5°C y 15°C, registrar 'frío'. Si es mayor a 15°C, registrar 'templado'."


**4. (4 puntos)** Tiene una lista de 1.000 especies. ¿Cuántas comparaciones necesita *en el peor caso* cada algoritmo para ordenarla?

a) Bubble sort: _____________ (aprox.)

b) Un algoritmo O(n log n) como merge sort: _____________ (aprox.)

*Pista: log₂(1000) ≈ 10*


**5. (2 puntos)** En la Semana 3, la búsqueda binaria con 16 animales tardó 4 preguntas. ¿Cuántas preguntas necesitaría una búsqueda binaria con 1.024 animales?


Respuesta: _____________




# Pauta de corrección

| Pregunta | Respuesta esperada | Puntos |
|---|---|---|
| 1 | Finitud, Definición, Entrada, Salida, Efectividad — con explicación coherente de cada una | 4 pts (0.8 por propiedad bien explicada) |
| 2 | Pseudocódigo que incluya: LEER la lista, un bucle PARA CADA cuadrante, un condicional SI cobertura > 60%, agregar a la lista de seleccionados, ESCRIBIR resultado | 6 pts (2 por estructura de bucle correcta, 2 por condicional correcto, 2 por entrada/salida explícitas) |
| 3 | Diagrama con: inicio, lectura de temperatura, dos decisiones en rombo (< 5°C, luego ≤ 15°C), tres salidas en rectángulo, flechas correctas, fin | 4 pts (1 por símbolos correctos, 1 por flujo lógico, 1 por condiciones correctas, 1 por completitud) |
| 4a | Bubble sort: ~1.000.000 / 2 = ~500.000 comparaciones (n(n-1)/2 ≈ n²/2) | 2 pts (1 si orden de magnitud correcto) |
| 4b | Merge sort: ~1.000 × 10 = ~10.000 comparaciones | 2 pts (1 si orden de magnitud correcto) |
| 5 | log₂(1024) = 10 preguntas | 2 pts |


