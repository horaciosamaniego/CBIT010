---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  :root {
    --color-bg: #091926; --color-elime: #DEFF9A; --color-accent: #5DD9E8;
    --color-mid: #00B4CC; --color-dark: #495f71; --color-light: #6199ac;
    --color-muted: #7CA9BA; --color-white: #e1ebee; --color-warn: #E05B3A;
    --font-head: 'Georgia', serif; --font-body: 'Trebuchet MS', sans-serif;
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
  section.pregunta { background-color: var(--color-mid); color: var(--color-bg); text-align: center; justify-content: center; }
  section.pregunta h1 { color: var(--color-elime); border-bottom: none; font-size: 1.6em; }
  section.pregunta p { font-weight: bold; font-size: 1.2em; }
  section.lab { border-left: 15px solid var(--color-warn); }
  section.lab h1 { color: var(--color-warn); border-bottom-color: var(--color-dark); }
  section.lab h2 { color: var(--color-accent); }
  table { font-size: 0.78em; width: 100%; border-collapse: collapse; margin: 12px 0; }
  thead th { background-color: var(--color-dark); color: var(--color-elime); padding: 8px; text-align: left; }
  td { padding: 8px; border: 1px solid var(--color-dark); }
  tbody tr:nth-child(even) td { background-color: rgba(255,255,255,0.05); }
  blockquote { background-color: rgba(255,255,255,0.05); border-left: 6px solid var(--color-elime); padding: 15px 25px; font-style: italic; color: var(--color-accent);}
  blockquote p { color: var(--color-accent); margin: 0; }
  section.pregunta blockquote { background-color: rgba(0,0,0,0.15); border-left-color: var(--color-elime); color: var(--color-bg); font-size: 0.9em; }
  section.pregunta blockquote p { color: var(--color-bg); }
  pre { background-color: #000; border: 1px solid var(--color-dark); padding: 15px; border-radius: 6px; color: var(--color-accent); font-size: 0.82em; }
  code { background-color: var(--color-dark); color: var(--color-elime); padding: 2px 6px; border-radius: 4px; font-family: 'Consolas', monospace; font-size:0.85em }





  
  section::after { color: var(--color-dark); font-size: 0.65em; }

footer: "Semana 11 · Archivos y Pandas · Sección 2"
---



<!-- _class: lead -->
<!-- _paginate: false -->

# Archivos y Pandas
## Del CSV al análisis de datos

*Semana 11 · Sección 2*

*Horacio Samaniego*

*Laboratorio de  Ecoinformática*

*Instituto de Conservación, Biodiversidad y Territorio · UACh*

---

# De la lista de dicts al DataFrame

**Semana 9:**

```python
arboles = [{"especie": "N. dombeyi", "dap": 45.3, "parcela": 1}, ...]
daps = [a["dap"] for a in arboles]       # list comprehension
promedio = sum(daps) / len(daps)          # cálculo manual
```

**Semana 11:**

```python
import pandas as pd
df = pd.DataFrame(arboles)
df["dap"].mean()                          # una línea
```

> El DataFrame **es** la lista de diccionarios con superpoderes.

---

# Hoja de ruta

1. 📂 **Cargar** un CSV con Pandas
2. 🔍 **Explorar** el DataFrame (shape, dtypes, head, describe)
3. 🎯 **Filtrar** filas con condiciones
4. 📊 **Contar** y **agrupar** con `value_counts` y `groupby`
5. 🔧 **Aplicar** funciones propias (Sem. 10) sobre DataFrames
6. ➕ **Crear** nuevas columnas
7. 🧪 **Laboratorio** con datos ecológicos

---

<!-- _class: pregunta -->

# Cargar datos

---

# `pd.read_csv()` — una línea

```python
import pandas as pd
from google.colab import drive

drive.mount('/content/drive')
df = pd.read_csv("/content/drive/MyDrive/CBIT010_.../bosque_valdiviano_simple.csv")
```

Primera exploración:

```python
print(df.shape)       # (100, 4) → 100 filas, 4 columnas
print(df.columns)     # ['especie', 'dap_cm', 'altura_m', 'parcela']
print(df.dtypes)      # tipos detectados automáticamente
df.head()             # primeras 5 filas
```

> Pandas detecta automáticamente que `dap_cm` es float y `parcela` es int. Sin conversión manual.

---

# Exploración rápida

```python
df.info()             # resumen: columnas, tipos, no-nulos
df.describe()         # n, mean, std, min, Q1, median, Q3, max
df.tail(3)            # últimas 3 filas
df.head(10)           # primeras 10 filas
```

> `df.describe()` en **una línea** da las estadísticas que antes les tomaban 30 líneas con bucles.

---

<!-- _class: pregunta -->

# Seleccionar columnas

---

# Columnas = Series

```python
# Una columna → Serie (como una lista con nombre)
daps = df["dap_cm"]
print(type(daps))          # pandas.core.series.Series

# Estadísticas de una Serie
print(daps.mean())         # promedio
print(daps.median())       # mediana
print(daps.std())          # desviación estándar
print(daps.min(), daps.max())
```

```python
# Múltiples columnas → sub-DataFrame
df[["especie", "dap_cm"]]
```

---

<!-- _class: pregunta -->

# Filtrar filas

---
<style scope>{font-size:26px;}</style>


# Filtrado con condiciones booleanas

**Sem. 9:** `[a for a in arboles if a["dap"] > 30]`

**Sem. 11:**

```python
grandes = df[df["dap_cm"] > 30]
print(f"Árboles grandes: {len(grandes)} de {len(df)}")
```

Múltiples condiciones:

```python
# DAP > 30 Y parcela 1   (usar & y paréntesis)
filtro = df[(df["dap_cm"] > 30) & (df["parcela"] == 1)]

# Solo coigüe
coigues = df[df["especie"] == "Nothofagus dombeyi"]
```

⚠️ En Pandas: `&` (no `and`), `|` (no `or`). Cada condición entre `()`.

---

<!-- _class: pregunta -->

# Contar y agrupar

---

# `value_counts()` — la tabla de frecuencias en 1 línea

```python
df["especie"].value_counts()
```

> Esto es el `conteo = {}; for obs: conteo[obs] += 1` de la Sem. 9 — **en una línea**.

```python
df["parcela"].value_counts().sort_index()
```

---

# `groupby()` — dividir, aplicar, combinar

```python
# DAP promedio por especie
df.groupby("especie")["dap_cm"].mean()
```

> `groupby` divide los datos en grupos, aplica una función, y combina. Es el bucle `for parcela in parcelas` de la Sem. 9, automatizado.

---

# groupby con múltiples estadísticas

```python
# Tabla completa por especie
df.groupby("especie")["dap_cm"].agg(["count", "mean", "std", "min", "max"])
```

```python
# Estadísticas por parcela, múltiples columnas
df.groupby("parcela").agg({
    "dap_cm": ["mean", "std"],
    "altura_m": ["mean", "std"],
    "especie": "nunique"            # especies únicas
})
```

---

# Tabla cruzada
## tablulacion de frecuencias

```python
pd.crosstab(df["parcela"], df["especie"])
```

Resultado: una **matriz parcela × especie** con conteos.

> Exactamente la tabla que necesitan para calcular diversidad por parcela. Una línea.

---

<!-- _class: pregunta -->

# Aplicar funciones propias
## Sem. 10 + Sem. 11

---

# Shannon H' sobre datos reales

```python
import math

def shannon_entropy(abundancias):
    """H' en nats."""
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H

# H' del bosque completo
conteos = df["especie"].value_counts()
print(f"H' total: {shannon_entropy(conteos.values):.4f}")
```

---

# H' por parcela — 5 líneas

```python
for parcela, grupo in df.groupby("parcela"):
    conteos = grupo["especie"].value_counts()
    H = shannon_entropy(conteos.values)
    S = len(conteos)
    print(f"Parcela {parcela}: S={S}, H'={H:.4f}")
```

> Sem. 9: ~25 líneas. Sem. 10: ~10 líneas. **Sem. 11: 5 líneas.** El mismo resultado, cada vez más limpio.

---

# Crear columnas con `.apply()`

```python
# Columna calculada (vectorizada)
df["area_basal"] = math.pi * (df["dap_cm"] / 200) ** 2

# Columna con función propia
def clasificar(dap):
    if dap > 40: return "grande"
    elif dap > 20: return "mediano"
    else: return "pequeño"

df["tamano"] = df["dap_cm"].apply(clasificar)
df["tamano"].value_counts()
```

> `.apply(funcion)` ejecuta la función sobre **cada valor** de la columna. Es un `for` implícito.

---

# Exportar resultados

```python
df.to_csv("resultado_analisis.csv", index=False)
```

---

# La evolución del código

La misma tarea: **DAP promedio por especie**

| Semana | Código | Líneas |
|---|---|---|
| 9 | Bucle + dict + list comprehension | ~12 |
| 10 | Funciones propias | ~8 |
| **11** | `df.groupby("especie")["dap_cm"].mean()` | **1** |

> Las semanas anteriores no fueron inútiles — entienden qué hace esa línea **porque escribieron los bucles a mano primero**.

---

<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab

---

<!-- _class: lab -->

# Ej. 1 · Explorar el dataset forestal

Cargar `bosque_valdiviano_simple.csv`. `.shape`, `.dtypes`, `.head()`, `.describe()`. ¿Cuántas filas? ¿Cuántas especies? ¿DAP promedio?

---

<!-- _class: lab -->

# Ej. 2 · Filtrado

Árboles con DAP > 40. Solo *N. dombeyi*. Parcela 3 con altura > 15 m. ¿Cuántos en cada caso?

---

<!-- _class: lab -->

# Ej. 3 · Conteos y frecuencias

`value_counts()` por especie y parcela. `pd.crosstab()` parcela × especie. ¿Cuál parcela tiene más especies?

---

<!-- _class: lab -->

# Ej. 4 · groupby

DAP promedio por especie. Altura promedio por parcela. Tabla con count + mean + std. ¿Especie con mayor DAP?

---

<!-- _class: lab -->

# Ej. 5 · Funciones propias + Pandas

Shannon H' total y por parcela. `.apply(clasificar_tamano)`. Conteo grande/mediano/pequeño por parcela.

---

<!-- _class: lab -->

# Ej. 6 (Desafío) · Cámaras trampa

Cargar `camaras_trampa_simulado.csv`. H' por sitio. ¿Sitio más diverso? ¿Especie ausente en algún sitio?

---

# Lo que aprendimos hoy

| Operación | Sem. 9 (manual) | Sem. 11 (Pandas) |
|---|---|---|
| Cargar CSV | `csv.DictReader` + bucle | `pd.read_csv()` |
| Estadísticas | `sum()/len()` con bucle | `.describe()` |
| Filtrar | list comprehension | `df[df["x"] > 5]` |
| Tabla de frecuencias | dict + `.get()` | `.value_counts()` |
| Agrupar | bucle + filtro manual | `.groupby()` |
| Crear columna | bucle + append | `.apply()` o vectorizado |

---

# Próxima semana

## Semana 12 · Pandas avanzado y visualización

*Tienen los datos cargados, filtrados y agrupados. La próxima semana los convierten en **gráficos**: barras, dispersión, series de tiempo. Un buen gráfico comunica más que una tabla de números.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 11 · Archivos y Pandas: del CSV al análisis de datos*
