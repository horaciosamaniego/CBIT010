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

footer: "Semana 10 · Funciones · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Funciones
## Encapsular y reutilizar

*Semana 10 · Sección 2*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

# El problema: copiar y pegar

Escribieron Shannon H' en la Sem. 8 **y** en la Sem. 9:

```python
# Semana 8                           # Semana 9
total = sum(abundancias)             total = sum(abundancias)
H = 0                                H = 0
for n in abundancias:                for n in abundancias:
    p = n / total                        p = n / total
    H -= p * math.log(p)                H -= p * math.log(p)
```

¿Y si hay un bug? Hay que corregirlo en **todos** los lugares donde lo copiaron.

---

<!-- _class: pregunta -->

# La solución: escribirlo UNA vez y reutilizarlo para siempre.

# Eso es una **función**.

---

# Callback: Sem. 5 — la tabla de transiciones

En la MT, la tabla de transiciones era el programa:
- Recibe una **entrada** (el contenido de la cinta)
- Ejecuta **instrucciones** internas (estados, transiciones)
- Produce una **salida** (el resultado en la cinta)
- El estado interno es **invisible** desde afuera

Una función en Python es exactamente eso.

---

# Hoja de ruta

1. 🔧 **Anatomía** de una función
2. ↩️ **`return`** vs `print`
3. 📋 **Funciones con listas** y diccionarios
4. 🏗️ **Shannon H'** como función
5. 🔒 **Scope** — variables locales vs globales
6. 🧩 **Composición** — funciones que llaman funciones
7. 📦 **Módulos** — importar funciones de otros
8. 🧪 **Laboratorio** + 📝 **Quiz 4**

---

<!-- _class: pregunta -->

# Anatomía de una función

---

# La primera función

```python
def saludar(nombre):
    """Saluda al usuario por su nombre."""
    print(f"¡Hola, {nombre}!")

saludar("Camila")    # ¡Hola, Camila!
saludar("Diego")     # ¡Hola, Diego!
```

| Parte | Significado |
|---|---|
| `def` | Palabra clave: "defino una función" |
| `saludar` | Nombre (snake_case, verbo descriptivo) |
| `(nombre)` | Parámetro (la entrada) |
| `"""..."""` | Docstring (documentación) |
| Bloque indentado | Cuerpo (las instrucciones) |

---

# Funciones que retornan valores

```python
def calcular_densidad(poblacion, area):
    """Calcula la densidad poblacional (ind/km²)."""
    densidad = poblacion / area
    return densidad

d1 = calcular_densidad(340, 12.5)
d2 = calcular_densidad(1500, 23.7)
print(f"Pudú: {d1:.2f} ind/km²")     # 27.20
print(f"Huemul: {d2:.2f} ind/km²")   # 63.29
```

`return` **devuelve** un valor. Se puede guardar, usar, pasar a otra función.

---

# `return` vs `print` — la diferencia que importa

```python
def con_return(a, b):
    return a + b

def con_print(a, b):
    print(a + b)

resultado = con_return(3, 5)
print(resultado * 2)        # 16 ← puedo usar el resultado

resultado = con_print(3, 5)  # imprime "8"
print(resultado)              # None ← no devolvió nada
```

> `return` = la **salida** de la función. `print` = un mensaje a la pantalla. Si otro código necesita el resultado, **usa return**.

---

# Valores por defecto

```python
def clasificar_dap(dap, umbral=30):
    """Clasifica un árbol como 'grande' o 'pequeño'."""
    if dap > umbral:
        return "grande"
    else:
        return "pequeño"

print(clasificar_dap(45))       # "grande" (umbral = 30)
print(clasificar_dap(45, 50))   # "pequeño" (umbral = 50)
print(clasificar_dap(25))       # "pequeño"
```

El parámetro `umbral=30` tiene un valor **por defecto** — se usa si no se especifica otro.

---

<!-- _class: pregunta -->

# Funciones con listas y diccionarios

---

# Procesar una lista

```python
def promedio(lista):
    """Calcula el promedio de una lista numérica."""
    return sum(lista) / len(lista)

def filtrar_mayores(lista, umbral):
    """Devuelve elementos mayores que el umbral."""
    return [x for x in lista if x > umbral]

daps = [45.3, 25.1, 18.7, 33.2, 55.0, 12.4, 38.9]

print(f"Promedio: {promedio(daps):.1f}")
print(f"DAP > 30: {filtrar_mayores(daps, 30)}")
```

---

# Devolver un diccionario

```python
def estadisticas(lista):
    """Estadísticas descriptivas de una lista."""
    return {
        "n": len(lista),
        "promedio": sum(lista) / len(lista),
        "minimo": min(lista),
        "maximo": max(lista),
        "rango": max(lista) - min(lista)
    }

stats = estadisticas(daps)
print(f"N={stats['n']}, Prom={stats['promedio']:.1f}")
print(f"Rango: {stats['minimo']:.1f} – {stats['maximo']:.1f}")
```

---

<!-- _class: pregunta -->

# Shannon H' como función
## El gran momento

---

# De 7 líneas sueltas a 1 línea de uso

```python
import math

def shannon_entropy(abundancias):
    """
    Índice de Shannon (H') en nats.
    
    Parámetros:
        abundancias: list[int] — abundancia de cada especie
    Retorna:
        float — H' (logaritmo natural)
    """
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H
```

---

# Ahora se usa en una línea

```python
parcela_1 = [45, 28, 67, 15, 33]
parcela_2 = [10, 10, 10, 10, 10]    # equitativa
parcela_3 = [90, 3, 2, 3, 2]        # dominada

print(f"Parcela 1: H' = {shannon_entropy(parcela_1):.4f}")
print(f"Parcela 2: H' = {shannon_entropy(parcela_2):.4f}")
print(f"Parcela 3: H' = {shannon_entropy(parcela_3):.4f}")
```

> Escribieron el cálculo **una vez**. Ahora lo usan para cualquier parcela, cualquier dataset, cualquier número de especies.

---

<!-- _class: pregunta -->

# Scope
## Variables locales vs globales

---

# Las variables dentro de una función son invisibles afuera

**Sem. 5:** *el estado interno de la MT (q0, q1...) era invisible desde afuera.*

```python
def calcular_algo():
    x = 42             # x es LOCAL
    print(f"Dentro: x = {x}")

calcular_algo()        # "Dentro: x = 42"
# print(x)             # NameError: x is not defined
```

---

# Local no modifica global

```python
x = 10

def cambiar():
    x = 20        # crea una x LOCAL — no toca la global
    return x

resultado = cambiar()
print(resultado)       # 20
print(x)               # 10 ← la global NO cambió
```

> **Regla de oro:** todo entra por los **parámetros**, todo sale por el **return**. Las funciones no deben depender de variables globales.

---

<!-- _class: pregunta -->

# Composición
## Funciones que llaman funciones

---

# Construir funciones complejas desde simples

```python
def equitatividad(abundancias):
    """J = H' / H'_max."""
    S = len(abundancias)
    if S <= 1:
        return 0
    H = shannon_entropy(abundancias)   # ← llama a la otra
    H_max = math.log(S)
    return H / H_max

def simpson_index(abundancias):
    """Índice de Simpson (1 - D)."""
    total = sum(abundancias)
    D = sum((n / total) ** 2 for n in abundancias)
    return 1 - D
```

---

# El reporte de diversidad — todo integrado

```python
def reporte_diversidad(nombre, abundancias):
    """Reporte completo usando las funciones anteriores."""
    S = len(abundancias)
    N = sum(abundancias)
    H = shannon_entropy(abundancias)
    J = equitatividad(abundancias)
    D = simpson_index(abundancias)
    
    print(f"{'='*40}")
    print(f" {nombre}")
    print(f"{'='*40}")
    print(f"  S={S}  N={N}")
    print(f"  H'={H:.4f}  J={J:.4f}  1-D={D:.4f}")

reporte_diversidad("Alerce Andino", [45, 28, 67, 15, 33])
reporte_diversidad("Huilo-Huilo",   [90, 3, 2, 3, 2])
```

> `reporte_diversidad` no calcula H' ni J — **llama** a funciones que saben hacerlo. Eso es composición.

---

# Módulos: funciones de otros

```python
import math            # funciones matemáticas
print(math.pi)         # 3.14159...
print(math.sqrt(144))  # 12.0

import random          # funciones aleatorias
print(random.randint(1, 100))
print(random.choice(["pudú", "puma", "güiña"]))

from math import log, pi    # importar solo lo necesario
```

> Los módulos son **colecciones de funciones** empaquetadas. En la Sem. 12 importarán `pandas` — un módulo con superpoderes para datos.

---

# Buenas prácticas

- **Nombre descriptivo:** `shannon_entropy`, no `calc` ni `f1`
- **Docstring:** qué hace, qué recibe, qué retorna
- **Una función = una tarea.** Si hace dos cosas → dos funciones
- **Siempre `return`** (no `print`) para el resultado principal
- **Variables locales**, no globales
- **Probar** con varios casos después de escribirla

---

<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab

---

<!-- _class: lab -->

# Ej. 1 · Funciones básicas

`celsius_a_fahrenheit(c)` · `area_basal(dap_cm)` · `relacion_hd(altura, dap)`

Probar cada una con varios valores. Incluir docstring.

---

<!-- _class: lab -->

# Ej. 2 · Funciones con condicionales

`clasificar_uicn(poblacion, tendencia)` — retorna categoría UICN
`es_arbol_grande(dap, umbral=30)` — retorna True/False

---

<!-- _class: lab -->

# Ej. 3 · Funciones con listas

`contar_especies(observaciones)` — retorna dict de frecuencias
`abundancia_relativa(abundancias)` — retorna lista de proporciones

---

<!-- _class: lab -->

# Ej. 4 · Funciones de diversidad

`shannon_entropy(abundancias)` → H' en nats
`equitatividad(abundancias)` → J
`simpson_index(abundancias)` → 1-D
`reporte_diversidad(nombre, abundancias)` → imprime reporte

---

<!-- _class: lab -->

# Ej. 5 (Desafío) · Diversidad por parcela — refactorizado

El Ej. 6 de la Sem. 9 tenía ~25 líneas.

Con funciones: **~10 líneas**. Mismo resultado, código más limpio.

---

# Lo que aprendimos hoy

| Concepto | Python | Sección 1 |
|---|---|---|
| Encapsular lógica | `def f(x): return y` | Tabla de transiciones (Sem. 5) |
| Parámetros | `f(entrada)` | Entrada de la MT |
| Return | `return resultado` | Salida de la MT |
| Scope | variables locales | Estado interno invisible |
| Composición | `f(g(x))` | Funciones que llaman funciones |
| Módulos | `import math` | Bibliotecas pre-empaquetadas |

---

# Próxima semana

## Semana 11 · Archivos y Pandas: del CSV al DataFrame

*Ya saben crear funciones. La próxima semana las aplican sobre datos reales — cargados desde archivos CSV con Pandas, el módulo que transforma Python en una herramienta de análisis de datos.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 📝 Quiz 4
## Funciones, return vs print, scope

*15 minutos · Individual · Sin apuntes ni celular*
