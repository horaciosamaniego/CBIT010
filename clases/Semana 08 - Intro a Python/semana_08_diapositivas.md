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
  section { font-family: var(--font-body); font-size: 34px; line-height: 1.45; padding: 40px 60px; background-color: var(--color-bg); color: var(--color-white); }
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

  section.pregunta pre,
  section.pregunta code { text-align: left; }

footer: "Semana 08 · Primeros pasos en Python · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Primeros pasos en Python
## De la instrucción al código

*Semana 8 · Inicio de la Sección 2*

*Horacio Samaniego*
horaciosamaniego@uach.cl

*Laboratorio de Ecoinformática*
*Instituto de Conservación, Biodiversidad y Territorio · UACh*

---

# Lo que ya saben (Sección 1)

- **Variables** → celdas de memoria con contenido (Sem. 1)
- **Tipos** → el mismo byte significa cosas distintas (Sem. 2)
- **Condicionales** → rombos en el diagrama de flujo (Sem. 4)
- **Bucles** → las pasadas del bubble sort (Sem. 4)
- **Funciones** → tablas de transiciones de la MT (Sem. 5)

**Hoy:** le ponemos **sintaxis** a todo eso. Nada de lo que verán es conceptualmente nuevo.

---

<!-- _class: invert -->

# Pseudocódigo (Sem. 4) → Python (Sem. 8)

```
PSEUDOCÓDIGO                         PYTHON
───────────────────                  ──────────────────
LEER población                       poblacion = int(input())
SI población < 1000 ENTONCES         if poblacion < 1000:
    clasif ← "En peligro"               clasif = "En peligro"
SINO SI población < 10000 ENTONCES   elif poblacion < 10000:
    clasif ← "Vulnerable"               clasif = "Vulnerable"
SINO                                 else:
    clasif ← "Preocupación menor"        clasif = "Preocupación menor"
FIN SI                               # (indentación cierra el bloque)
ESCRIBIR clasificación               print(clasif)
```

---

<!-- _class: pregunta -->

# ¿Cuántas cosas nuevas hay?

<div class='card'>

```
PSEUDOCÓDIGO                         PYTHON
───────────────────                  ──────────────────
LEER población                       poblacion = int(input())
SI población < 1000 ENTONCES         if poblacion < 1000:
    clasif ← "En peligro"               clasif = "En peligro"
SINO SI población < 10000 ENTONCES   elif poblacion < 10000:
    clasif ← "Vulnerable"               clasif = "Vulnerable"
SINO                                 else:
    clasif ← "Preocupación menor"        clasif = "Preocupación menor"
FIN SI                               # (indentación cierra el bloque)
ESCRIBIR clasificación               print(clasif)
```

</div>

---

# Casi ninguna

| Pseudocódigo | Python | Cambio |
|---|---|---|
| `←` | `=` | Asignación |
| `ENTONCES` | `:` | Inicio del bloque |
| `FIN SI` / `FIN PARA` | *(indentación)* | La sangría ES la estructura |
| `SINO SI` | `elif` | Rama alternativa |
| `ESCRIBIR` | `print()` | Salida |
| `LEER` | `input()` | Entrada |

> La lógica es **idéntica**. Hoy solo aprendemos las reglas de escritura.

---

# Hoja de ruta

1. 🖥️ **Colab** — el entorno
2. 📦 **Variables** — celdas con nombre, reasignación, swap
3. 🏷️ **Tipos** — int, float, str (en profundidad), bool
4. ➗ **Operaciones** — aritméticas, comparación, lógicas
5. 🔀 **Condicionales** — if / elif / else
6. 🔁 **Bucles** — for, range, acumulación, while
7. 🧪 **Laboratorio**

---

# Google Colab

- Navegador + cuenta Google = todo lo que necesitan
- Celda de **código** → Shift+Enter → resultado abajo
- Celda de **texto** → Markdown (instrucciones)
- **Comentarios:** `# esto Python lo ignora`

```python
print("Bienvenidos al bosque valdiviano")
```

*Ejecútenlo. Si aparece el texto, están programando.*

---

<!-- _class: pregunta -->

# Variables
## Las celdas de memoria con nombre

---

# Crear variables

**Sem. 1:** la Memoria tenía celdas numeradas. **Sem. 8:** tienen nombre.

```python
poblacion = 1500                     # int
area_km2 = 23.7                      # float
especie = "Nothofagus dombeyi"       # str
amenazada = True                     # bool
```

**Reglas:** `snake_case`, no empezar con número, case-sensitive, **nombres descriptivos**.

> `d` ❌ → `densidad_por_hectarea` ✅

---

# Reasignar y acumular

```python
conteo = 10
conteo = conteo + 5      # reasignación explícita
print(conteo)             # 15

# Atajos (operadores de asignación aumentada)
conteo += 3               # conteo = conteo + 3 → 18
conteo -= 2               # 16
conteo *= 2               # 32
```

> `conteo += 3` le dice a la ALU: lee la celda, súmale 3, guarda en la misma celda.

---

# Asignación múltiple y swap

```python
# Dos variables en una línea
latitud, longitud = -39.81, -73.24
print(f"Valdivia: {latitud}, {longitud}")

# Intercambiar (sin variable temporal)
a, b = 10, 20
a, b = b, a
print(f"a={a}, b={b}")    # a=20, b=10

# None — existe pero sin valor (aún)
resultado = None
print(type(resultado))    # NoneType
```

---

<!-- _class: pregunta -->

# Tipos de datos
## ¿Cómo interpreta Python los bits?

---

# Los cuatro tipos básicos

```python
edad = 25                    # int    (entero)
temperatura = 15.3           # float  (decimal)
nombre = "Drimys winteri"    # str    (texto)
es_nativa = True             # bool   (True / False)

print(type(edad))         # <class 'int'>
print(type(temperatura))  # <class 'float'>
```

**Sem. 2:** *"El mismo byte puede ser un número o una letra. El TIPO es la codificación."*

---

# Strings: secuencias de caracteres

```python
especie = "Nothofagus dombeyi"

len(especie)           # 19 caracteres
especie[0]             # 'N' (primer carácter, índice 0)
especie[-1]            # 'i' (último)
especie[0:10]          # 'Nothofagus' (slice)
especie[11:]           # 'dombeyi'
```

> Cada carácter tiene un **índice** empezando en 0 — como las celdas de memoria de la Sem. 1.

---

# Métodos de strings

```python
especie = "Nothofagus dombeyi"

especie.upper()        # 'NOTHOFAGUS DOMBEYI'
especie.lower()        # 'nothofagus dombeyi'
especie.split()        # ['Nothofagus', 'dombeyi'] ← ¡lista!
especie.replace("dombeyi", "pumilio")
especie.startswith("Notho")  # True
especie.count("o")     # 2
```

Los strings son **inmutables**: `especie[0] = "n"` → ERROR.

---

# Conversiones y ASCII

```python
texto = "42"
numero = int(texto)
print(numero + 8)          # 50
print("42" + "8")          # "428" ← concatenación, no suma
```

**Sem. 2:**

```python
print(ord('N'))     # 78
print(chr(78))      # 'N'
print(bin(78))      # '0b1001110'
```

> El **tipo** determina qué hace `+`: con `int` suma, con `str` concatena.

---

# Booleanos: el resultado de comparar

```python
print(10 > 5)       # True
print(10 == 5)      # False   ← doble igual para COMPARAR
print(10 != 5)      # True    ← distinto
print(10 >= 10)     # True

# Guardar en variable
es_grande = poblacion > 1000
print(es_grande)    # True
```

⚠️ **El error clásico:** `=` (asignar) vs `==` (comparar)

---

<!-- _class: pregunta -->

# Operaciones
## La ALU de Python

---

# Aritméticas

```python
print(10 + 3)     # 13   suma
print(10 - 3)     # 7    resta
print(10 * 3)     # 30   multiplicación
print(10 / 3)     # 3.33 división (siempre float)
print(10 // 3)    # 3    división entera
print(10 % 3)     # 1    módulo (resto)
print(10 ** 3)    # 1000 potencia
```

**Ejemplo:**

```python
densidad = 1500 / 23.7
print(f"Densidad: {densidad:.2f} ind/km²")
```

---

# Lógicas: and, or, not

```python
temperatura = 12
lluvia = True
viento_bajo = True

# and: AMBAS deben ser True
print(temperatura < 15 and lluvia)    # True

# or: AL MENOS UNA True
print(temperatura > 20 or lluvia)     # True

# not: invierte
puede_muestrear = not lluvia and viento_bajo
print(f"¿Muestrear? {puede_muestrear}")  # False (llueve)
```

---

<!-- _class: pregunta -->

# Entrada y salida

---

# `input()` y f-strings

```python
nombre = input("¿Especie? ")         # siempre devuelve str
n = int(input("¿Población? "))       # convertir a int
area = float(input("¿Área km²? "))   # convertir a float

densidad = n / area
print(f"Densidad de {nombre}: {densidad:.1f} ind/km²")
```

| Formato | Resultado | Significado |
|---|---|---|
| `{x}` | tal cual | Sin formato |
| `{x:.1f}` | 27.2 | 1 decimal |
| `{x:.2f}` | 27.20 | 2 decimales |
| `{x:.0f}` | 27 | Sin decimales |

---

<!-- _class: pregunta -->

# Condicionales
## Los rombos del diagrama de flujo

---

# if / else

**Sem. 4:** un rombo = una decisión sí/no. **Sem. 8:** un `if`.

```python
densidad = 27.2

if densidad < 10:
    print("⚠️ Densidad baja — posible riesgo")
else:
    print("✅ Densidad dentro de rango normal")
```

**Anatomía:** `if` + condición + `:` → bloque indentado. `else:` → bloque alternativo.

---

# if / elif / else

```python
poblacion = int(input("Población: "))

if poblacion < 250:
    categoria = "En Peligro Crítico"
elif poblacion < 2500:
    categoria = "En Peligro"
elif poblacion < 10000:
    categoria = "Vulnerable"
else:
    categoria = "Preocupación Menor"

print(f"Categoría UICN: {categoria}")
```

> Es el pseudocódigo de la Sem. 4, con `elif` en vez de `SINO SI` y sin `FIN SI`.

---

# Condicionales anidados

```python
poblacion = 800
tendencia = "decreciente"

if poblacion < 1000:
    if tendencia == "decreciente":
        categoria = "En Peligro Crítico"
    else:
        categoria = "En Peligro"
else:
    categoria = "Vulnerable"

print(f"Categoría: {categoria}")
```

> La **indentación** muestra la estructura. Dos niveles de sangría = un `if` dentro de otro.

---

<!-- _class: pregunta -->

# Bucles
## Las pasadas del Bubble Sort

---

# El bucle `for`: recorrer una secuencia

```python
especies = ["coigüe", "canelo", "luma", "ulmo", "lenga"]

for especie in especies:
    print(f"Especie: {especie}")
```

En cada vuelta, `especie` toma el **siguiente valor** de la lista.

```
Especie: coigüe
Especie: canelo
Especie: luma
Especie: ulmo
Especie: lenga
```

---

# `for` con `range()`

```python
# range(n) → 0, 1, 2, ..., n-1
for i in range(5):
    print(f"Parcela {i+1}")

# range(inicio, fin)
for i in range(1, 6):
    print(f"Cuadrante {i}")      # 1, 2, 3, 4, 5

# range(inicio, fin, paso)
for i in range(0, 100, 10):
    print(f"Transecto a {i} m")  # 0, 10, 20, ..., 90
```

---

# Acumulación: el patrón más importante

```python
abundancias = [45, 28, 67, 12, 33]

total = 0                    # acumulador empieza en 0
for n in abundancias:
    total += n               # sumar cada valor

print(f"Total: {total}")    # 185
```

> **Acumular dentro de un bucle** es el patrón más usado en análisis de datos. Lo verán una y otra vez.

---

# `for` + `if`: filtrar y contar

```python
abundancias = [45, 28, 67, 12, 33]

grandes = 0
suma_grandes = 0

for n in abundancias:
    if n > 30:
        grandes += 1
        suma_grandes += n

print(f"Especies con >30 ind: {grandes}")
print(f"Suma de abundantes: {suma_grandes}")
```

> Combinan un bucle (recorrer) con un condicional (filtrar). Esto es la base de todo análisis de datos.

---

# El bucle `while`

```python
intentos = 0
password = ""

while password != "valdiviano":
    password = input("Contraseña: ")
    intentos += 1

print(f"Acceso concedido en {intentos} intentos")
```

`while` repite **mientras** la condición sea True.

⚠️ *Un `while True:` sin salida = el Halting Problem de la Sem. 5.*

---

<!-- _class: pregunta -->

# Programa integrador
## Todo junto en 20 líneas

---
<!-- _footer: "" -->
# Reporte ecológico completo

```python
print("=== Reporte Ecológico ===\n")
sitio = input("Sitio: ")
n_parcelas = int(input("Nº parcelas: "))

abundancias = []
for i in range(n_parcelas):
    n = int(input(f"  Individuos parcela {i+1}: "))
    abundancias.append(n)

total = sum(abundancias)
promedio = total / n_parcelas

print(f"\nSitio: {sitio}")
print(f"Total: {total}  |  Promedio: {promedio:.1f}")
print(f"Rango: {min(abundancias)} – {max(abundancias)}")

if promedio < 10:
    print("⚠️ Abundancia baja")
elif promedio < 50:
    print("🟡 Abundancia moderada")
else:
    print("✅ Abundancia alta")
```

---

<!-- _class: pregunta -->

# En la Sem. 1, este programa necesitaba 5 personas.

# Ahora Python hace todo.

# Pero la lógica es **exactamente la misma**.

---

# Errores: son normales y esperables

| Error | Causa | Solución |
|---|---|---|
| `NameError` | Variable no definida | ¿Ejecutaron la celda anterior? |
| `TypeError` | Operar str con int | Convertir o usar f-string |
| `IndentationError` | Sangría incorrecta | 4 espacios después de `:` |
| `SyntaxError` | Falta `:` o `=` vs `==` | Leer el mensaje |
| Bucle infinito | `while` sin salida | Interrumpir ejecución |

> Los programadores pasan **la mitad del tiempo** leyendo errores. Si les aparece uno, están programando.

---
<style scoped>{font-size: 2.6em;}</style>
<!-- _footer : "" -->
<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab

<div class='card'>

**Primero:** Necesitas una cuenta en Google

**Segundo:** abrir colab
https://colab.research.google.com/


**Tercero:** Descargar archivo desde *SIVEDUC*
[`semana_08_primer_notebook.ipynb`](https://siveducmd.uach.cl/mod/resource/view.php?id=1098055)

**Cuarto:**  Guardar una copia en *Google Drive*
</div>

---

<!-- _class: lab -->

# Nivel 1 · Fundamentos

**Ej. 1:** Variables, tipos, área basal y relación H/D de un árbol
**Ej. 2:** Strings + ASCII — codificar "PUDU" en binario

---

<!-- _class: lab -->

# Nivel 2 · Condicionales

**Ej. 3:** Clasificador UICN completo (if/elif/else + anidados)
**Ej. 4:** Decisión de muestreo con `and`, `or`, `not`

---

<!-- _class: lab -->

# Nivel 3 · Bucles

**Ej. 5:** Abundancias relativas de 5 especies con `for`
**Ej. 6:** Filtrar DAPs grandes con `for` + `if` + acumulación

---

<!-- _class: lab -->

# Desafío · Shannon H' automático

```python
import math
abundancias = [45, 28, 67, 12, 33, 8, 52]
total = sum(abundancias)

H = 0
for n in abundancias:
    p = n / total
    H -= p * math.log(p)

print(f"H' = {H:.4f} nats")
```

*En la Sem. 3 calcularon H para 3 especies a mano. Ahora lo hacen para 7, o 700, con 5 líneas.*

---

# Lo que aprendimos hoy

| Concepto | Sección 1 | Python |
|---|---|---|
| Celda de memoria | Sem. 1: celda numerada | `variable = valor` |
| Codificación | Sem. 2: ASCII, tipos | `int`, `float`, `str`, `bool` |
| Decisión | Sem. 4: rombo del flujo | `if / elif / else` |
| Repetición | Sem. 4: pasadas del sort | `for` / `while` |
| Acumulación | Sem. 3: contar especies | `total += n` |

---

# Próxima semana

## Semana 9 · Colecciones: listas y diccionarios

*Una variable guarda un dato. ¿Y si necesitan guardar 100 especies? Van a usar una lista. ¿Y asociar cada especie con su abundancia? Un diccionario — la tabla de frecuencias de la Semana 3.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 8 · Primeros pasos en Python*
