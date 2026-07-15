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
  blockquote { background-color: rgba(255,255,255,0.05); border-left: 6px solid var(--color-elime); padding: 15px 25px; font-style: italic; color: var(--color-accent); font-size: 0.9em; }
  blockquote p { color: var(--color-accent); margin: 0; }
  pre { background-color: #000; border: 1px solid var(--color-dark); padding: 15px; border-radius: 6px; color: var(--color-accent); font-size: 0.78em; }
  code { background-color: var(--color-dark); color: var(--color-elime); padding: 2px 6px; border-radius: 4px; font-family: 'Consolas', monospace; font-size: 0.85em; }
  section::after { color: var(--color-dark); font-size: 0.65em; }

footer: "Semana 13 · Integración y cierre · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Integración y cierre
## Del lápiz al código

*Semana 13 · Última clase del curso*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

<!-- _class: pregunta -->

# Hace 13 semanas no habían escrito una línea de código.

# Hoy van a analizar datos reales de biodiversidad.

---

# El arco completo del curso

**Sección 1 — sin computador**
- Sem 1–2: qué es computar, cómo se codifican los datos
- Sem 3: entropía y diversidad de Shannon
- Sem 4–5: algoritmos, pseudocódigo, Máquina de Turing
- Sem 6–7: límites, IA y conservación

**Sección 2 — Python**
- Sem 8–10: variables, colecciones, funciones
- Sem 11–12: Pandas y visualización
- **Sem 13: hoy — integrar todo**

---

# Todo lo de Python ya lo sabían

| Concepto | Sección 1 | Python |
|---|---|---|
| Variable | Celda de memoria (S1) | `x = 42` |
| Tipo de dato | ASCII (S2) | `int`, `float`, `str` |
| Diversidad H' | Cálculo a mano (S3) | `shannon_entropy()` |
| Decisión | Rombo del flujo (S4) | `if / elif / else` |
| Repetición | Pasadas del algoritmo (S4) | `for`, `while` |
| Procedimiento | Tabla de la MT (S5) | función `def` |

> Python no fue lo difícil. Lo difícil — pensar como un computador — lo aprendieron **sin pantalla**.

---

<!-- _class: pregunta -->

# El recorrido completo
## Un análisis de principio a fin

---

# Los 5 pasos de todo análisis

```
1. CARGAR     →  pd.read_csv()
2. DIAGNOSTICAR → isna(), duplicated(), describe()
3. LIMPIAR    →  dropna, fillna, drop_duplicates
4. ANALIZAR   →  groupby, value_counts, shannon_entropy()
5. VISUALIZAR →  matplotlib
   + INTERPRETAR
```

> Hoy lo hacemos sobre un dataset que **nunca han visto** — con errores reales.

---

# Paso 1 · Cargar y mirar

```python
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("monitoreo_biodiversidad_2025.csv")

print(df.shape)
df.head(10)
df.info()
```

> Antes de analizar nada: ¿cuántas filas? ¿qué columnas? ¿qué tipos? **Siempre miren los datos primero.**

---

# Paso 2 · Diagnóstico de calidad

```python
df.isna().sum()              # ¿valores faltantes?
df.duplicated().sum()        # ¿filas duplicadas?
df["abundancia"].describe()  # ¿valores extraños?
df["especie"].unique()       # ¿nombres consistentes?
```

Encontramos: **NaN** en abundancia, una fila **duplicada**, un valor de **999** (outlier), y una especie en minúscula.

> Datos reales, problemas reales.

---

# Paso 3 · Limpieza (cada decisión es científica)

```python
df = df.drop_duplicates()
df["abundancia"] = pd.to_numeric(df["abundancia"], errors="coerce")

# 999 es un error de tipeo → lo tratamos como faltante
df.loc[df["abundancia"] > 100, "abundancia"] = None

# Rellenar con la mediana
df["abundancia"] = df["abundancia"].fillna(df["abundancia"].median())

# Corregir mayúsculas
df["especie"] = df["especie"].str.capitalize()
```

> ¿Eliminar o rellenar? ¿Media o mediana? No hay respuesta única — pero hay que **justificarla**.

---

# Paso 4 · Análisis

```python
# Riqueza por sitio
df.groupby("sitio")["especie"].nunique()

# Abundancia por grupo
df.groupby("grupo")["abundancia"].sum()

# Diversidad de Shannon por sitio
for sitio, grupo in df.groupby("sitio"):
    abund = grupo.groupby("especie")["abundancia"].sum()
    H = shannon_entropy(abund.values)
    print(f"{sitio}: S={len(abund)}, H'={H:.3f}")
```

> La función `shannon_entropy()` la escribieron en la Sem. 10. La reutilizan aquí sin cambios.

---

# Paso 5 · Visualización

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

riqueza = df.groupby("sitio")["especie"].nunique().sort_values()
riqueza.plot(kind="barh", ax=axes[0], color="#2E7D32")
axes[0].set_title("Riqueza por sitio")

df.groupby("grupo")["abundancia"].sum().plot(
    kind="bar", ax=axes[1], color="#1565C0")
axes[1].set_title("Abundancia por grupo")

plt.tight_layout()
plt.show()
```

> Datos crudos → análisis → gráfico. **Esto es el trabajo de un analista en conservación.**

---

<!-- _class: pregunta -->

# ¿Hacia dónde seguir?

---

# El camino continúa

- **R + tidyverse** — el otro gran lenguaje ecológico. Pandas se traduce casi directo.
- **QGIS / geopandas** — análisis espacial, mapas, teledetección.
- **Estadística** — ahora pueden *implementar* lo que aprendan.
- **GBIF, eBird, iNaturalist** — bases de biodiversidad con APIs consultables desde Python.

> No se vuelven programadores. Se vuelven **científicos de recursos naturales que hablan con los datos directamente.**

---

<!-- _class: lead -->

# 🧪 Proyecto de cierre
## Su turno — análisis completo, en parejas

---

<!-- _class: lab -->

# El proyecto de cierre

Toman `monitoreo_biodiversidad_2025.csv` y producen un análisis completo:

1. **Cargar** y explorar
2. **Diagnosticar** calidad (NaN, duplicados, outliers)
3. **Limpiar** — justificando cada decisión
4. **Analizar** — riqueza, abundancia, Shannon H' por sitio
5. **Visualizar** — 2 gráficos etiquetados
6. **Interpretar** — ¿qué sitio es más diverso? ¿qué limitaciones?

> Menos pistas que las semanas anteriores. Es el momento de demostrar autonomía.

---

<!-- _class: lab -->

# Reglas del capstone

- En **parejas**
- Pueden usar **sus notebooks anteriores** como referencia
- LLMs permitidos **con prompt log**
- Cada decisión de limpieza va **justificada** en una celda de texto
- Entrega: notebook de Colab comentado

> Si se traban: ¿cómo contaron especies en la Sem. 11? ¿qué función de diversidad escribieron en la Sem. 10?

---

# Lo que lograron este semestre

- Entienden **qué es computar** (no solo cómo escribir código)
- Saben **codificar y medir información** (binario, entropía, diversidad)
- Piensan en **algoritmos** y reconocen lo computable de lo que no
- Programan en **Python**: datos, decisiones, repetición, funciones
- Analizan datos reales con **Pandas** y los **visualizan**
- Usan **IA de forma crítica**, verificando en vez de confiar ciegamente

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Empezaron siendo el Computador Humano.
# Terminan analizando biodiversidad real.

## Gracias.

*Introducción al Análisis de Datos y Programación · UACh 2026*
