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

footer: "Semana 13 · Integración y trabajo de proyecto · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Integración y trabajo de proyecto
## Ensamblar todas las piezas

*Semana 13 · Sección 2*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

# Hoy: las piezas se ensamblan

Cada semana de la Sección 2 enseñó **una pieza**:

- Sem. 8–10: variables, colecciones, funciones
- Sem. 11: cargar y agrupar con Pandas
- Sem. 12: limpiar y visualizar

**Hoy** las juntamos en un solo flujo de trabajo — y lo aplican a **su proyecto**.

---

# Estructura de la sesión

1. ⏱️ **Primera hora:** el pipeline completo en vivo (juntos)
2. ⏱️ **Dos horas:** trabajo de proyecto con apoyo del docente

> El objetivo de hoy: que salgan con sus datos cargados, limpios y un primer análisis funcionando.

---

<!-- _class: pregunta -->

# El pipeline de análisis de datos

---

# Los 6 pasos de todo análisis

```
1. CARGAR        →  pd.read_csv()
2. DIAGNOSTICAR  →  isna(), duplicated(), describe()
3. LIMPIAR       →  dropna, fillna, drop_duplicates
4. ANALIZAR      →  groupby, value_counts, funciones propias
5. VISUALIZAR    →  matplotlib
6. INTERPRETAR   →  ¿qué significan los resultados?
```

> Este es el flujo que necesitan para su proyecto, para el examen, y en su carrera.

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

> ¿Eliminar o rellenar? ¿Media o mediana? No hay respuesta única — pero hay que **justificarla**. Esto vale también para los datos de su proyecto.

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

> La función `shannon_entropy()` la escribieron en la Sem. 10. La reutilizan sin cambios.

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

> Datos crudos → análisis → gráfico. **Este es el flujo que aplicarán ahora a su proyecto.**

---

<!-- _class: lead -->

# 🔧 Trabajo de proyecto
## Su turno — con apoyo en vivo

---

<!-- _class: lab -->

# Metas para el final de hoy

Cada grupo debe salir con:

1. ✅ Datos **cargados** en Colab
2. ✅ **Diagnóstico** de calidad completo
3. ✅ Al menos un **análisis** preliminar corriendo
4. ✅ Al menos un **gráfico** borrador

> No tienen que terminar el proyecto hoy. La meta es destrabar el código para que las próximas semanas se concentren en interpretar y comunicar.

---

<!-- _class: lab -->

# Hoja de ruta de trabajo

| Fase | Qué hacer | Referencia |
|---|---|---|
| 1. Cargar | CSV → Colab → Pandas | Sem. 11 |
| 2. Diagnosticar | isna, duplicated, describe | Sem. 12 |
| 3. Limpiar | tratar y justificar problemas | Sem. 12 |
| 4. Analizar | groupby, diversidad | Sem. 10–11 |
| 5. Graficar | gráfico con título y ejes | Sem. 12 |
| 6. Interpretar | responder su pregunta | Sem. 7 |

---

<!-- _class: lab -->

# Mientras trabajan

- El docente **circula** y resuelve dudas en el momento
- Pueden usar **sus notebooks anteriores** como referencia
- LLMs permitidos **con prompt log**
- Si varios grupos comparten una duda → **mini-clase** de 5 min en el proyector

> Si se traban: ¿cómo contaron especies en la Sem. 11? ¿qué función de diversidad escribieron en la Sem. 10?

---

# Antes de irse

Cada grupo reporta en una frase:
- **Dónde quedaron** hoy
- **Qué les falta**

**Próxima semana (final):**
- Sem. 14: presentaciones del proyecto

---

<!-- _class: lead -->
<!-- _paginate: false -->

# A trabajar 🔧

*Semana 13 · Integración y trabajo de proyecto*
