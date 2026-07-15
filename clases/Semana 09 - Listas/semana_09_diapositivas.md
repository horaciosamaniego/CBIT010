---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  :root {
    --color-bg:      #091926;
    --color-elime:   #DEFF9A;
    --color-accent:  #5DD9E8;
    --color-mid:     #00B4CC;
    --color-dark:    #495f71;
    --color-light:   #6199ac;
    --color-muted:   #7CA9BA;
    --color-white:   #e1ebee;
    --color-warn:    #E05B3A;
    --font-head:     'Georgia', serif;
    --font-body:     'Trebuchet MS', sans-serif;
  }
  section { font-family: var(--font-body); font-size: 32px; line-height: 1.45; padding: 40px 60px; background-color: var(--color-bg); color: var(--color-white); }
  section h1, section h2, section h3 { font-family: var(--font-head); margin-top: 0; }
  section h1 { color: var(--color-elime); font-size: 1.7em; border-bottom: 4px solid var(--color-mid); padding-bottom: 8px; margin-bottom: 20px; }
  section h2 { color: var(--color-accent); font-size: 1.3em; margin-bottom: 12px; font-weight: 700; }
  section h3 { color: var(--color-light); font-size: 1.1em; }
  section strong { color: var(--color-elime); font-weight: 800; }
  section em { color: var(--color-muted); }
  section li { margin-bottom: 8px; }
  section ul, section ol { margin: 8px 0 12px 30px; }
  section p { margin-bottom: 12px; }
  section.lead { text-align: center; display: flex; flex-direction: column; justify-content: center; border: 12px solid var(--color-mid); }
  section.lead h1 { color: var(--color-elime); font-size: 2.4em; border-bottom: none; }
  section.lead h2 { color: var(--color-accent); font-size: 1.4em; font-style: italic; }
  section.lead p { color: var(--color-white); opacity: 0.8; }
  section.invert { background-color: var(--color-white); color: var(--color-bg); }
  section.invert h1 { color: var(--color-bg); border-bottom-color: var(--color-mid); }
  section.invert h2 { color: var(--color-dark); }
  section.invert strong { color: var(--color-warn); }
  section.pregunta { background-color: var(--color-mid); color: var(--color-bg); text-align: center; justify-content: center; }
  section.pregunta h1 { color: var(--color-elime); border-bottom: none; font-size: 1.6em; }
  section.pregunta h2 { color: var(--color-bg); border-bottom: none; font-size: 1.4em; }
  section.pregunta p { font-weight: bold; font-size: 1.2em; }
  section.lab { border-left: 15px solid var(--color-warn); }
  section.lab h1 { color: var(--color-warn); border-bottom-color: var(--color-dark); }
  section.lab h2 { color: var(--color-accent); }
  table { font-size: 0.8em; width: 100%; border-collapse: collapse; margin: 15px 0; }
  thead th { background-color: var(--color-dark); color: var(--color-elime); padding: 10px; text-align: left; }
  td { padding: 10px; border: 1px solid var(--color-dark); }
  tbody tr:nth-child(even) td { background-color: rgba(255,255,255,0.05); }
  blockquote { background-color: rgba(255,255,255,0.05); border-left: 6px solid var(--color-elime); padding: 15px 25px; font-style: italic; color: var(--color-accent); }
  blockquote p { color: var(--color-accent); margin: 0; }
  section.pregunta blockquote { background-color: rgba(0,0,0,0.15); border-left-color: var(--color-elime); color: var(--color-bg); }
  section.pregunta blockquote p { color: var(--color-bg); }
  pre { background-color: #000; border: 1px solid var(--color-dark); padding: 15px; border-radius: 6px; color: var(--color-accent); font-size: 0.68em; }
  code { background-color: var(--color-dark); color: var(--color-elime); padding: 2px 6px; border-radius: 4px; font-family: 'Consolas', monospace; }
  section::after { color: var(--color-dark); font-size: 0.65em; }

footer: "Semana 09 · Colecciones · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Colecciones
## Listas, diccionarios y la estructura de los datos

*Semana 9 · Sección 2*
*Laboratorio de Ecoinformática*
*Instituto de Conservación, Biodiversidad y Territorio · UACh*
*horaciosamaniego@uach.cl*

---
<style scoped>{font-size: 20px;}</style>
# Semana 8 · Resumen — Primeros pasos en Python

<div class="cols">
<div>

## Variables y tipos
`nombre = valor` — celda de memoria con nombre *(Sem. 1)*
- **`int`** `25` · **`float`** `15.3` · **`str`** `"Pudú"` · **`bool`** `True`
- Reasignar: `x += 3` · Swap: `a, b = b, a`
- Strings: `len()`, `[0]`, `[1:5]`, `.upper()`, `.split()`
- Conversión: `int("42")` · `str(100)` · `ord('N')` → 78

## Operaciones
- *Aritméticas:* `+  -  *  /  //  %  **`
- *Comparación:* `>  <  ==  !=  >=  <=` → devuelven `bool`
- *Lógicas:* `and  or  not`
- ⚠️ `=` asigna · `==` compara

</div>
<div>

---
# Semana 8 · Resumen — Primeros pasos en Python

## Condicionales *(Sem. 4: rombos del flujo)*
```
if condicion:
    ...
elif otra:
    ...
else:
    ...
```

## Bucles *(Sem. 4: pasadas del sort)*
```
for x in lista:       # recorrer
for i in range(n):    # contar
while condicion:      # repetir hasta
```
**Patrón clave:** acumulación → `total = 0` + `for` + `total += n`

---
# Semana 8 · Resumen — Primeros pasos en Python

## Entrada / Salida
`input("?")` → siempre `str` · `print(f"{x:.2f}")`

</div>
</div>

*Todo viene de la Sección 1: variables = celdas (Sem. 1) · tipos = codificación (Sem. 2) · if = rombo (Sem. 4) · for = pasadas (Sem. 4)*

---
#  Semana 9 · El problema

```python
# Semana 8: una variable por dato
especie_1 = "N. dombeyi"
especie_2 = "D. winteri"
especie_3 = "A. luma"
# ... ¿y si hay 200 especies?
```

No van a crear 200 variables. Necesitan una estructura que contenga **muchos datos bajo un solo nombre**.

---

# Hoja de ruta

1. 📋 **Listas** — secuencias ordenadas, mutables
2. 📖 **Diccionarios** — pares clave → valor
3. 📌 **Tuplas** — secuencias inmutables (breve)
4. 🗃️ **Listas de diccionarios** — la antesala de Pandas
5. 🧪 **Laboratorio** con datos ecológicos reales

---

<!-- _class: pregunta -->

# Listas
## La colección ordenada

---

# Crear y acceder

```python
especies = ["N. dombeyi", "D. winteri", "A. luma",
            "E. cordifolia", "L. philippiana"]
abundancias = [45, 28, 67, 15, 33]

print(len(especies))         # 5
print(especies[0])           # 'N. dombeyi'  (primero)
print(especies[-1])          # 'L. philippiana' (último)
print(especies[1:3])         # ['D. winteri', 'A. luma'] (slice)
```

> El índice empieza en **0** — como los strings (Sem. 8) y las celdas de memoria (Sem. 1).

---

# Modificar listas

Las listas son **mutables** (se pueden cambiar):

```python
# Cambiar un elemento
especies[0] = "Nothofagus dombeyi"

# Agregar
especies.append("Fitzroya cupressoides")

# Insertar en posición específica
especies.insert(0, "Araucaria araucana")

# Eliminar
especies.remove("D. winteri")     # por valor
ultimo = especies.pop()           # elimina el último

# Verificar pertenencia
print("A. luma" in especies)      # True
```

---

# Funciones útiles para listas numéricas

```python
abundancias = [45, 28, 67, 15, 33, 67, 12]

print(len(abundancias))       # 7
print(sum(abundancias))       # 267
print(min(abundancias))       # 12
print(max(abundancias))       # 67
print(sorted(abundancias))    # [12, 15, 28, 33, 45, 67, 67]
```

**Sem. 4:** *`list.sort()` usa internamente **Timsort** — O(n log n). Python eligió el algoritmo eficiente por ustedes.*

---

# Recorrer listas con `for`

```python
# Por elemento
for especie in especies:
    print(f"  - {especie}")

# Con índice usando enumerate()
for i, especie in enumerate(especies):
    print(f"  {i+1}. {especie}")

# Con range() cuando necesitas el índice
for i in range(len(abundancias)):
    print(f"  Especie {i+1}: {abundancias[i]} ind.")
```

---

# Construir listas con bucles

```python
# Patrón: lista vacía + append
total = sum(abundancias)
proporciones = []
for n in abundancias:
    proporciones.append(n / total)

# List comprehension (versión compacta)
proporciones = [n / total for n in abundancias]

# Filtrar con comprehension
grandes = [n for n in abundancias if n > 30]
print(f"Abundancias > 30: {grandes}")   # [45, 67, 33, 67]
```

> La **list comprehension** es un `for` comprimido en una línea. Dice: *"para cada n, calcula n/total, y ponlo en la nueva lista."*

---

<!-- _class: pregunta -->

# Diccionarios
## La tabla de frecuencias de la Semana 3

---

# Crear y acceder

**Sem. 3:** la tabla especie → abundancia. **Sem. 9:** un diccionario.

```python
inventario = {
    "N. dombeyi": 45,
    "D. winteri": 28,
    "A. luma": 67,
    "E. cordifolia": 15,
    "L. philippiana": 33
}

print(inventario["A. luma"])          # 67
print(inventario.get("Pudú", 0))     # 0 (valor por defecto)
print(len(inventario))                # 5
```

> En una lista → acceso por **posición**. En un diccionario → acceso por **nombre** (clave).

---

# Modificar diccionarios

```python
# Agregar
inventario["F. cupressoides"] = 3

# Modificar
inventario["N. dombeyi"] = 48

# Eliminar
del inventario["F. cupressoides"]

# Verificar existencia
print("A. luma" in inventario)       # True
print("Sequoia" in inventario)       # False
```

---

# Recorrer diccionarios

```python
# Claves y valores juntos con .items()
for especie, n in inventario.items():
    print(f"  {especie}: {n} individuos")

# Calcular total y proporciones
total = sum(inventario.values())

for especie, n in inventario.items():
    p = n / total
    print(f"  {especie}: {p:.3f} ({p*100:.1f}%)")
```

---

# Construir un diccionario de frecuencias

```python
observaciones = ["coigüe", "luma", "canelo", "luma",
                  "coigüe", "luma", "coigüe", "canelo",
                  "luma", "ulmo"]

conteo = {}
for obs in observaciones:
    conteo[obs] = conteo.get(obs, 0) + 1

print(conteo)
# {'coigüe': 3, 'luma': 4, 'canelo': 2, 'ulmo': 1}
```

> Es **exactamente** la tabla de frecuencias de la Sem. 3 — pero construida automáticamente. Ya no cuentan a mano.

---

<!-- _class: pregunta -->

# Tuplas
## La colección inmutable (breve)

---

# Tuplas: como listas, pero fijas

```python
coordenadas = (-39.81, -73.24)
print(coordenadas[0])        # -39.81

# No se pueden modificar
# coordenadas[0] = -40.0     # TypeError!

# Desempaquetar
latitud, longitud = coordenadas
```

| Estructura | Mutable | Sintaxis | Uso típico |
|---|---|---|---|
| **Lista** | Sí | `[a, b, c]` | Secuencias que cambian |
| **Diccionario** | Sí | `{k: v}` | Pares clave-valor |
| **Tupla** | No | `(a, b)` | Datos que no deben cambiar |

---

<!-- _class: pregunta -->

# Listas de diccionarios
## La antesala de Pandas

---

# Un árbol = un diccionario. Un inventario = una lista.

```python
inventario = [
    {"especie": "N. dombeyi", "dap": 45.3, "altura": 22.1, "parcela": 1},
    {"especie": "D. winteri", "dap": 25.1, "altura": 15.8, "parcela": 1},
    {"especie": "A. luma",    "dap": 18.7, "altura": 12.3, "parcela": 2},
]

for arbol in inventario:
    print(f"{arbol['especie']}: DAP={arbol['dap']}, H={arbol['altura']}")
```

---

# Filtrar y analizar

```python
# Filtrar: árboles con DAP > 20
grandes = [a for a in inventario if a["dap"] > 20]
print(f"{len(grandes)} árboles con DAP > 20 cm")

# Extraer una "columna"
daps = [a["dap"] for a in inventario]
promedio = sum(daps) / len(daps)
print(f"DAP promedio: {promedio:.1f} cm")
```

> Cada diccionario = una **fila**. Cada clave = una **columna**. En la Sem. 13, esto será un `DataFrame` de Pandas — pero la lógica es la misma.

---

# Programa integrador: diversidad con diccionario

```python
import math

inventario = {"N. dombeyi": 45, "D. winteri": 28, "A. luma": 67,
              "E. cordifolia": 15, "L. philippiana": 33}

S = len(inventario)
total = sum(inventario.values())

H = 0
for especie, n in inventario.items():
    p = n / total
    H -= p * math.log(p)

J = H / math.log(S)

print(f"S = {S} | N = {total}")
print(f"H' = {H:.4f} nats | J = {J:.4f}")
```

> Sem. 3 con calculadora: 20 min para 3 especies. Python: **10 líneas, cualquier número de especies**.

---

# Resumen: ¿cuándo usar qué?

| Necesito... | Estructura | Ejemplo |
|---|---|---|
| Una secuencia de valores | **Lista** | DAPs de 100 árboles |
| Asociar nombres con valores | **Diccionario** | especie → abundancia |
| Datos que no deben cambiar | **Tupla** | coordenadas GPS |
| Una "tabla" de registros | **Lista de dicts** | inventario forestal |

---

<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab

---

<!-- _class: lab -->

# Ejercicio 1 · Listas fundamentales

Crear listas con datos ecológicos. Indexar, slice, append, remove. Usar `len`, `sum`, `min`, `max`, `sorted`.

---

<!-- _class: lab -->

# Ejercicio 2 · Listas + for

Calcular DAP promedio con bucle. Filtrar árboles con altura > 20m. Encontrar la especie más abundante recorriendo la lista.

---

<!-- _class: lab -->

# Ejercicio 3 · Diccionarios — tabla de frecuencias

Dada una lista de observaciones con repeticiones, construir un diccionario de conteos. Calcular proporciones.

*Exactamente la Semana 3 — automatizada.*

---

<!-- _class: lab -->

# Ejercicio 4 · Diccionario ecológico

Crear inventario especie → abundancia. Recorrer con `.items()`. Encontrar la especie más y menos abundante.

---

<!-- _class: lab -->

# Ejercicio 5 · Listas de diccionarios

Trabajar con una lista de árboles (especie, DAP, altura, parcela). Filtrar por parcela. Calcular estadísticas por especie.

---

<!-- _class: lab -->

# Ejercicio 6 (Desafío) · Diversidad por parcela

Calcular Shannon H' para cada parcela por separado. ¿Cuál parcela es la más diversa?

*Combina diccionarios, bucles, condicionales y `math.log()` — todo lo de las Semanas 3, 8 y 9.*

---

# Tarea evaluada #1

**Entrega:** inicio de la Semana 10
**Formato:** Notebook Colab compartido
**LLMs:** permitidos con **prompt log** documentado

**Datos:** CSV con registros de cámaras trampa simulados.

**Tareas:**
1. Contar observaciones por especie (diccionario de frecuencias)
2. Identificar especie más y menos observada
3. Filtrar observaciones de un sitio específico
4. Calcular Shannon H' para el dataset completo
5. (Bonus) Comparar H' entre dos sitios

---

# Lo que aprendimos hoy

| Estructura | Sintaxis | Sem. 1–3 equivalente |
|---|---|---|
| Lista | `[45, 28, 67]` | Columna de datos |
| Diccionario | `{"luma": 67}` | Tabla de frecuencias (Sem. 3) |
| Tupla | `(-39.8, -73.2)` | Coordenada fija |
| Lista de dicts | `[{"sp": "luma", "n": 67}]` | Fila de inventario |

---

# Próxima semana

## Semana 10 · Funciones: encapsular y reutilizar

*Escribieron el cálculo de Shannon H' dos veces (Sem. 8 y Sem. 9). ¿No sería mejor escribirlo UNA vez y reutilizarlo? Eso es una función — la tabla de transiciones de la Máquina de Turing (Sem. 5), ahora en Python.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 9 · Colecciones: listas, diccionarios, tuplas*
