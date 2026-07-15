---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  section {
    font-size: 28px; line-height: 1.45; padding: 40px 50px;
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
  section.pregunta h1 { font-size: 1.5em; border-bottom: none; color: #1B4332; margin-bottom: 12px; }
  section.pregunta p, section.pregunta em { color: #2E5E4E; font-size: 0.95em; }
  section.lab {
    background: #FFF8E1; color: #333; border-top: 4px solid #F9A825;
  }
  section.lab h1 { color: #E65100; border-bottom: 3px solid #FFE0B2; font-size: 1.4em; }
  section.lab h2 { color: #BF360C; font-size: 1.15em; }
  table { font-size: 0.8em; width: 100%; border-collapse: collapse; margin: 8px 0; }
  thead th { background: #2E5E4E; color: #fff; padding: 6px 10px; text-align: left; font-weight: 600; }
  td { padding: 5px 10px; border: 1px solid #ccc; vertical-align: top; }
  tbody tr:nth-child(even) td { background: #F0F7F4; }
  section.lab thead th { background: #E65100; }
  section.lab tbody tr:nth-child(even) td { background: #FFF3E0; }
  blockquote {
    background: #E8F5E9; border-left: 4px solid #2E7D32;
    padding: 10px 16px; margin: 10px 0; font-size: 0.95em; border-radius: 3px;
    color: #1B4332;
  }
  blockquote p { margin: 0; color: #1B4332; }
  blockquote strong { color: #1B4332; }
  blockquote em { color: #2E5E4E; }
  section.invert blockquote { background: rgba(255,255,255,0.15); border-left-color: #A5D6A7; color: #fff; }
  section.invert blockquote p { color: #fff; }
  section.invert blockquote strong { color: #fff; }
  section.lead blockquote { background: rgba(255,255,255,0.15); border-left-color: #A5D6A7; color: #fff; }
  section.lead blockquote p { color: #fff; }
  section.lead blockquote strong { color: #fff; }
  pre { font-size: 0.75em; background: #f5f5f5; border-left: 3px solid #40916C; padding: 10px 14px; }
  code { font-size: 0.88em; background: #E8F5E9; padding: 1px 5px; border-radius: 3px; color: #607d71}
  section::after { color: #999; font-size: 0.65em; }


footer: "Semana 04 · # Pensamiento algorítmico - Horacio Samaniego *(horaciosamaniego@uach.cl)*"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Pensamiento algorítmico
## Recetas para resolver problemas

*Semana 4 · Introducción al Análisis de Datos y Programación*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

# Recuerdo de la Semana 3

- La **búsqueda binaria** en las 20 Preguntas: 4 preguntas para 16 animales
- Cada pregunta bien hecha descartaba **la mitad** de las opciones
- Hoy formalizamos eso: ¿qué hace que una estrategia sea un *algoritmo*?

---

# Hoja de ruta

1. 🥪 **La receta del sándwich** — por qué la precisión importa
2. 📋 **¿Qué es un algoritmo?** — cinco propiedades
3. 🔀 **Diagramas de flujo y pseudocódigo** — herramientas de expresión
4. 🔢 **Algoritmos de ordenamiento** — burbuja e inserción
5. 📈 **Complejidad** — ¿qué tan caro es resolver un problema?
6. 🧪 **Laboratorio** — Red de ordenamiento
7. 📝 **Control 2**

---

<!-- _class: pregunta -->

# 🥪 Actividad: explíquenme cómo hacer un sándwich

# Paso a paso. Voy a ejecutar sus instrucciones *literalmente*.

---

# ¿Qué aprendimos del sándwich?

"Pon el pan sobre la mesa" → ¿**Qué** pan? ¿**Cuál** mesa? ¿Con qué **lado** hacia arriba?

"Ponle jamón" → ¿**Cuántas** láminas? ¿**Sobre** cuál cara?

"Cierra el sándwich" → *Pone otro pan al lado* 🤷

> El lenguaje natural es **ambiguo**. Un computador (y yo haciendo de computador) ejecuta las instrucciones *al pie de la letra*. Si la instrucción es vaga, el resultado es incorrecto.

¿Cómo se escribe una receta que no admita ambigüedad? **Eso es un algoritmo.**

---

<!-- _class: invert -->

# ¿Qué es un algoritmo?

---

# Definición

Un **algoritmo** es un conjunto finito de instrucciones bien definidas que transforma una **entrada** en una **salida** deseada.

La palabra viene de **al-Juarismi** (Muhammad ibn Musa al-Khwarizmi, ~780–850), matemático persa que describió procedimientos paso a paso para resolver ecuaciones.

> No es un invento moderno. Es una idea de más de mil años.

---

# Las cinco propiedades

| Propiedad | Significado | Contraejemplo |
|---|---|---|
| **Finitud** | Termina en un número finito de pasos | "Repita hasta que sea perfecto" |
| **Definición** | Cada paso es preciso, no ambiguo | "Agregue sal al gusto" |
| **Entrada** | Recibe cero o más datos iniciales | — |
| **Salida** | Produce al menos un resultado | Un proceso que nunca entrega nada |
| **Efectividad** | Cada paso es realizable con los recursos disponibles | "Calcule todos los primos" (infinitos) |

---

<!-- _class: pregunta -->

# 🤔 *"Encontrar el mejor lugar para un área protegida"*

# ¿Es un algoritmo?

---

# No — pero *puede* convertirse en uno

**"Mejor"** no está definido. ¿Mejor para qué especie? ¿Con qué presupuesto? ¿Minimizando qué función?

Si definimos:
*"Seleccionar el conjunto de parcelas que maximice el número de especies protegidas sin exceder un presupuesto de X millones"*

...entonces **sí** se puede construir un algoritmo (es un problema de optimización bien definido).

> La diferencia entre un deseo vago y un algoritmo es la **precisión en la formulación**.

---

<!-- _class: invert -->

# Herramientas de expresión
## Diagramas de flujo y pseudocódigo

---

# Diagrama de flujo: los símbolos

| Símbolo | Forma | Significado |
|---|---|---|
| **Inicio / Fin** | Óvalo | Marca comienzo o final |
| **Proceso** | Rectángulo | Acción o cálculo |
| **Decisión** | Rombo | Pregunta sí/no (bifurcación) |
| **Entrada / Salida** | Paralelogramo | Lectura de datos o escritura |
| **Flecha** | Línea con punta | Dirección del flujo |

---

# Ejemplo: ¿está amenazada esta especie?

```
[INICIO]
   ↓
[Leer: población, tendencia]
   ↓
◇ ¿Población < 1000?
 Sí → ◇ ¿Tendencia decreciente?
        Sí → [EN PELIGRO CRÍTICO]
        No → [EN PELIGRO]
 No → ◇ ¿Población < 10000?
        Sí → [VULNERABLE]
        No → [PREOCUPACIÓN MENOR]
   ↓
[Escribir: clasificación]
   ↓
[FIN]
```

*Cada rombo = una decisión. Cada rectángulo = una acción. Las flechas = el flujo.*

---

# Pseudocódigo: el intermedio

No es un lenguaje de programación — es un **bosquejo** claro de la lógica.

**Convenciones que usaremos:**

```
LEER variable
ESCRIBIR variable
SI condición ENTONCES
    instrucciones
SINO
    instrucciones
FIN SI
PARA i DESDE a HASTA b HACER
    instrucciones
FIN PARA
MIENTRAS condición HACER
    instrucciones
FIN MIENTRAS
```

---

# El mismo ejemplo en pseudocódigo

```
LEER población, tendencia

SI población < 1000 ENTONCES
    SI tendencia = "decreciente" ENTONCES
        clasificación ← "En peligro crítico"
    SINO
        clasificación ← "En peligro"
    FIN SI
SINO SI población < 10000 ENTONCES
    clasificación ← "Vulnerable"
SINO
    clasificación ← "Preocupación menor"
FIN SI

ESCRIBIR clasificación
```

---

# ¿Cuál usar?

| | Diagrama de flujo | Pseudocódigo |
|---|---|---|
| **Formato** | Visual | Textual |
| **Bueno para** | Comunicar, vista panorámica | Detallar, más cercano al código |
| **Malo para** | Procedimientos largos (se enreda) | Personas no técnicas |
| **Se parece a** | Un mapa | Una receta |

> En la Sección 2 del curso, el pseudocódigo se transformará en **Python** casi directamente.

---

<!-- _class: invert -->

# Algoritmos de ordenamiento
## Misma tarea, diferentes estrategias

---

# ¿Por qué ordenar?

- Ordenar especies por **abundancia** → identificar dominantes
- Ordenar parcelas por **riqueza** → priorizar las más diversas
- Ordenar datos por **fecha** → analizar tendencias

> Ordenar es una de las operaciones más comunes en computación. Hay docenas de algoritmos para hacerlo. Hoy vemos los dos más simples.

---

# Bubble Sort (Burbuja)

**Idea:** recorrer la lista comparando pares adyacentes. Si están desordenados, intercambiarlos. Repetir hasta que no haya más intercambios.

**Ejemplo:** ordenar `[5, 2, 8, 1]`

```
Pasada 1: [5,2,8,1] → [2,5,8,1] → [2,5,8,1] → [2,5,1,8]  (8 "burbujeó" al final)
Pasada 2: [2,5,1,8] → [2,5,1,8] → [2,1,5,8]
Pasada 3: [2,1,5,8] → [1,2,5,8]                             ✅ Ordenado
```

> Después de cada pasada, el número más grande queda en su lugar. Como una burbuja que sube.

---

# Bubble Sort: pseudocódigo

```
PARA i DESDE 1 HASTA n-1 HACER
    PARA j DESDE 1 HASTA n-i HACER
        SI lista[j] > lista[j+1] ENTONCES
            intercambiar(lista[j], lista[j+1])
        FIN SI
    FIN PARA
FIN PARA
```

Dos bucles anidados → cada elemento se compara con (casi) todos los demás.

---

# Insertion Sort (Inserción)

**Idea:** mantener una parte "ya ordenada" e ir insertando cada nuevo elemento en su posición correcta.

**Analogía:** así ordenamos las cartas en la mano — tomamos una del mazo y la deslizamos al lugar correcto.

```
[5, | 2, 8, 1]  → insertar 2 → [2, 5, | 8, 1]
[2, 5, | 8, 1]  → insertar 8 → [2, 5, 8, | 1]
[2, 5, 8, | 1]  → insertar 1 → [1, 2, 5, 8]  ✅
```

*La línea `|` separa la parte ordenada de la desordenada.*

---

# Insertion Sort: pseudocódigo

```
PARA i DESDE 2 HASTA n HACER
    clave ← lista[i]
    j ← i - 1
    MIENTRAS j > 0 Y lista[j] > clave HACER
        lista[j+1] ← lista[j]
        j ← j - 1
    FIN MIENTRAS
    lista[j+1] ← clave
FIN PARA
```

---

# Comparación

| | Burbuja | Inserción |
|---|---|---|
| **Idea** | Comparar adyacentes, intercambiar | Insertar en posición correcta |
| **Mejor caso** | Lista ya ordenada: pocas pasadas | Lista ya ordenada: una sola pasada |
| **Peor caso** | Lista al revés: máximos intercambios | Lista al revés: máximos desplazamientos |
| **¿Eficiente?** | No para listas grandes | Algo mejor, pero tampoco escala |

💬 *"Ambos funcionan. Pero ¿qué pasa si la lista tiene un millón de elementos?"*

---

<!-- _class: invert -->

# Complejidad
## ¿Qué tan caro es resolver un problema?

---

# La pregunta

No basta con que un algoritmo **funcione**. Necesitamos saber **cuánto cuesta ejecutarlo**.

**Costo de ejecución** = cuántas operaciones necesita en función del tamaño de la entrada (**n**).

> Si duplico los datos, ¿el tiempo se duplica? ¿Se cuadruplica? ¿Se multiplica por un millón?

---

# La escala de complejidad

| Complejidad    | Nombre      | Ejemplo                             | Crece como... |
| -------------- | ----------- | ----------------------------------- | ------------- |
| **O(1)**       | Constante   | Leer el primer elemento             | Instantáneo   |
| **O(log n)**   | Logarítmica | Búsqueda binaria (Sem. 3)           | Muy lento     |
| **O(n)**       | Lineal      | Recorrer toda una lista             | Proporcional  |
| **O(n log n)** | Log-lineal  | Merge sort (ordenamiento eficiente) | Razonable     |
| **O(n²)**      | Cuadrática  | Burbuja, inserción (peor caso)      | Problemático  |
| **O(2ⁿ)**      | Exponencial | Probar todas las combinaciones      | Intratable    |

---

# La diferencia importa — mucho

Ordenar una lista de **n** especies:

| n             | Burbuja O(n²) | Merge sort O(n log n) |
| ------------- | ------------- | --------------------- |
| 10            | ~100          | ~33                   |
| 100           | ~10.000       | ~664                  |
| 1.000         | ~1.000.000    | ~9.966                |
| **1.000.000** | **~10¹²**     | **~20.000.000**       |

> Con un millón de especies: burbuja necesita un **billón** de operaciones. Merge sort necesita 20 millones. No es "un poco más rápido" — es la diferencia entre **segundos y días**.

---

# La búsqueda binaria revisitada

La Semana 3, con 16 animales:
- **Búsqueda lineal** ("¿es el pudú?", "¿es el cóndor?"): hasta **16** preguntas
- **Búsqueda binaria** (dividir a la mitad): **4** preguntas

¿Y con 1.000.000 de animales?
- Lineal: hasta **1.000.000** preguntas
- Binaria: **20** preguntas (log₂(1.000.000) ≈ 20)

> **O(n) vs. O(log n)** — la diferencia entre preguntar un millón de veces y preguntar veinte.

---

<!-- _class: pregunta -->

# 🤔 ¿Por qué no usamos siempre el algoritmo más eficiente?

*Porque los algoritmos eficientes suelen ser más difíciles de diseñar, implementar y depurar. La simplicidad tiene valor. Pero cuando los datos crecen, la eficiencia se vuelve indispensable.*

---

<!-- _class: lead -->

# 🧪 Laboratorio analógico
## "Red de Ordenamiento"

*Ustedes son los datos. Ordénense.*

---

<!-- _class: lab -->

# Preparación

- **8 voluntarios** por equipo, cada uno con una tarjeta numerada
- Posiciones marcadas en el suelo con cinta: `[1] [2] [3] [4] [5] [6] [7] [8]`
- Secuencia inicial: **7, 3, 5, 1, 8, 2, 6, 4**
- Registradores cuentan **comparaciones** e **intercambios**
- Cronómetro en marcha

---

<!-- _class: lab -->

# Ronda 1 · Bubble Sort (15 min)

**Reglas:**
1. Un "director" recorre la fila de izquierda a derecha
2. En cada par adyacente: si el izquierdo > derecho → **se cruzan**
3. Al llegar al final → volver al inicio y repetir
4. Parar cuando una pasada completa no tenga intercambios

**Registrar:** comparaciones, intercambios, tiempo total.

💬 *¿Qué pasó con el número más grande en la primera pasada?*

---

<!-- _class: lab -->

# Ronda 2 · Insertion Sort (15 min)

**Reglas:**
1. El primero se queda (la "parte ordenada" tiene 1 elemento)
2. El segundo se compara → se inserta antes o después
3. El tercero busca su posición entre los dos ya ordenados → se inserta
4. Continuar hasta que todos estén ordenados

**Registrar:** comparaciones, desplazamientos, tiempo total.

💬 *¿Fue más rápido o más lento que burbuja? ¿Por qué?*

---

<!-- _class: lab -->

# Ronda 3 · Competencia (20 min)

Tres equipos. Misma secuencia: **7, 3, 5, 1, 8, 2, 6, 4**

| Equipo | Algoritmo |
|---|---|
| A | Bubble Sort |
| B | Insertion Sort |
| C | **Estrategia libre** (inventen la suya) |

**Restricción:** solo pueden comparar con el **vecino inmediato** (no vale mirar toda la fila).

¿Quién termina primero? ¿Con menos intercambios? ¿Con menos comparaciones?

---

<!-- _class: lab -->

# Registro de resultados

| Equipo | Algoritmo | Comparaciones | Intercambios | Tiempo |
|---|---|---|---|---|
| A | Burbuja | | | |
| B | Inserción | | | |
| C | Libre | | | |

💬 *¿Qué hizo el equipo C? ¿Se parece a algún algoritmo conocido?*

---

<!-- _class: invert -->

# Discusión plenaria

---

<!-- _class: pregunta -->

# ¿Qué pasaría si fueran 80 personas en vez de 8?

*Burbuja: 80² = 6.400 comparaciones. Con 800: 640.000. Crece cuadráticamente. En algún momento se vuelve impráctico.*

---

<!-- _class: pregunta -->

# ¿La estrategia libre fue más rápida? ¿Qué hicieron?

*Muchos equipos intuitivamente inventan algo parecido a "buscar el mínimo y ponerlo al inicio" (selection sort) o "dividir en mitades" (merge sort). La intuición humana a veces redescubre algoritmos clásicos.*

---

<!-- _class: pregunta -->

# ¿Qué paralelo ven con la conservación?

*Priorizar parcelas, seleccionar sitios de monitoreo, rankear amenazas — todo requiere ordenamiento. Y cuando los datos son grandes, el algoritmo importa tanto como los datos mismos.*

---

# Lo que aprendimos hoy

- Un **algoritmo** es un procedimiento finito, definido, efectivo, con entrada y salida
- Se expresa como **diagrama de flujo** (visual) o **pseudocódigo** (textual)
- Los **algoritmos de ordenamiento** muestran que la misma tarea se puede resolver con costos muy distintos
- La **complejidad** (Big-O) mide cómo crece el costo cuando crecen los datos
- La diferencia entre O(n²) y O(n log n) es la diferencia entre lo **posible** y lo **imposible**

---

# Próxima semana

## Semana 5 · La Máquina de Turing
### El computador universal más simple

*Si un algoritmo es una receta, ¿existe una "cocina universal" que pueda ejecutar cualquier receta? Turing demostró que sí — y es más simple de lo que imaginan.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 4 · Pensamiento algorítmico: recetas para resolver problemas*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 📝 Control 2
## Pseudocódigo para una tarea ecológica

*15 minutos · Individual · Sin apuntes ni celular*
