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

footer: "Semana 12 · Pandas avanzado + Visualización · Sección 2"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Pandas avanzado y visualización
## Del dato al gráfico

*Semana 12 · Sección 2*
*Facultad de Ciencias Forestales y Recursos Naturales · UACh*

---

# Hoja de ruta

1. 🧹 **Limpieza:** valores faltantes, ordenar
2. 📅 **Fechas:** extraer mes, agrupar por semana
3. 📊 **matplotlib:** barras, scatter, histograma, subplots
4. 📈 **Curva rango-abundancia** — la estructura de la comunidad
5. 💾 **Guardar** figuras para informes
6. 🧪 **Laboratorio** + 📝 **Quiz 5**

---

<!-- _class: pregunta -->

# Pandas avanzado
## Datos reales son datos sucios

---

# Valores faltantes (NaN)

```python
# Detectar
df.isnull().sum()           # conteo de NaN por columna

# Estrategia 1: eliminar
df_limpio = df.dropna()

# Estrategia 2: rellenar
df["dap_cm"].fillna(df["dap_cm"].median(), inplace=True)
df["especie"].fillna("Desconocida", inplace=True)
```

> Los datos reales **siempre** tienen valores faltantes. ¿Eliminar o rellenar? Depende del contexto ecológico.

---

# Ordenar y rankear

```python
# Los 10 árboles más grandes
df.sort_values("dap_cm", ascending=False).head(10)

# Ranking de DAP promedio por especie
df.groupby("especie")["dap_cm"].mean().sort_values(ascending=False)
```

---

# Trabajar con fechas

```python
cam = pd.read_csv("camaras_trampa_simulado.csv")
cam["fecha"] = pd.to_datetime(cam["fecha"])

# Extraer componentes
cam["mes"] = cam["fecha"].dt.month
cam["dia_semana"] = cam["fecha"].dt.day_name()

# Conteo por mes
cam["mes"].value_counts().sort_index()
```

> Las fechas son un tipo con estructura. Pandas permite agrupar por día, semana, mes — esencial para monitoreo temporal.

---

# Tablas pivote

```python
# Registros por sitio × método
pivot = cam.pivot_table(
    values="especie", index="sitio",
    columns="metodo", aggfunc="count", fill_value=0
)
print(pivot)
```

---

<!-- _class: pregunta -->

# matplotlib
## Un gráfico comunica más que una tabla

---

# La lógica: fig + ax

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))    # lienzo
ax.bar(["A", "B", "C"], [10, 25, 15])      # dibujar
ax.set_title("Mi primer gráfico")           # decorar
ax.set_xlabel("Categoría")
ax.set_ylabel("Valor")
plt.show()                                   # mostrar
```

> Crear lienzo → dibujar → decorar → mostrar.

---

# Barras: abundancia por especie

```python
conteos = df["especie"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
conteos.plot(kind="bar", ax=ax, color="#2E7D32", edgecolor="white")
ax.set_title("Abundancia por especie", fontsize=14)
ax.set_ylabel("Nº individuos")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()
```

---

# Scatter: DAP vs Altura

```python
fig, ax = plt.subplots(figsize=(8, 6))

for especie, grupo in df.groupby("especie"):
    ax.scatter(grupo["dap_cm"], grupo["altura_m"],
               label=especie, alpha=0.7, s=50)

ax.set_xlabel("DAP (cm)")
ax.set_ylabel("Altura (m)")
ax.set_title("Relación DAP-Altura por especie")
ax.legend(fontsize=9)
plt.tight_layout()
plt.show()
```

> La relación DAP-altura es fundamental en dasometría. Cada especie tiene su curva alométrica — el gráfico lo hace visible.

---

# Histograma: distribución de DAP

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["dap_cm"], bins=15, color="#00796B",
        edgecolor="white", alpha=0.8)
ax.axvline(df["dap_cm"].mean(), color="red",
           linestyle="--", label=f"Media: {df['dap_cm'].mean():.1f}")
ax.set_xlabel("DAP (cm)")
ax.set_ylabel("Frecuencia")
ax.legend()
plt.tight_layout()
plt.show()
```

---

<!-- _class: pregunta -->

# Curva rango-abundancia
## La estructura de la comunidad en un gráfico

---

# Rango-abundancia

Especies ordenadas de más a menos abundante:

```python
conteos = df["especie"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(range(len(conteos)), conteos.values,
       color="#1565C0", edgecolor="white")
ax.set_xticks(range(len(conteos)))
ax.set_xticklabels(conteos.index, rotation=45, ha="right")
ax.set_ylabel("Abundancia")
ax.set_title("Curva rango-abundancia")
plt.tight_layout()
plt.show()
```

> Curva **plana** = comunidad equitativa. Curva **empinada** = dominada por 1–2 especies. La forma dice más que cualquier índice.

---

# Subplots: múltiples paneles

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: barras
conteos.plot(kind="bar", ax=axes[0], color="#2E7D32")
axes[0].set_title("Abundancia")

# Panel 2: histograma
axes[1].hist(df["dap_cm"], bins=12, color="#1565C0")
axes[1].set_title("Distribución DAP")

# Panel 3: boxplot
df.boxplot(column="dap_cm", by="especie", ax=axes[2], rot=45)
axes[2].set_title("DAP por especie")
plt.suptitle("")
plt.tight_layout()
plt.show()
```

---

# Guardar figuras

```python
fig.savefig("mi_figura.png", dpi=150, bbox_inches="tight")
fig.savefig("mi_figura.pdf", bbox_inches="tight")
```

- **PNG** (150–300 dpi): para presentaciones e informes digitales
- **PDF** (vectorial): para publicaciones — se escala sin perder calidad

---

# El pipeline completo

```
CSV → pd.read_csv() → explorar → limpiar → filtrar
    → agrupar → graficar → interpretar → exportar
```

> Este flujo es lo que usarán en el proyecto grupal, en el examen, y en su carrera.

---

<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab

---

<!-- _class: lab -->

# Ej. 1 · Exploración visual

Barras de abundancia por especie. Histograma de DAP con media. Boxplot de DAP por especie.

---

<!-- _class: lab -->

# Ej. 2 · Relaciones DAP-Altura

Scatter coloreado por especie. Scatter coloreado por parcela. ¿Patrones alométricos?

---

<!-- _class: lab -->

# Ej. 3 · Diversidad visual

Calcular H' por parcela → graficar como barras. ¿Más individuos = más diversa?

---

<!-- _class: lab -->

# Ej. 4 · Cámaras trampa temporal

Fecha → datetime. Serie temporal (registros/semana). Barras sitio × método. Rango-abundancia × sitio (4 subplots).

---

<!-- _class: lab -->

# Ej. 5 (Desafío) · Figura de publicación

4 subplots en 1 figura: rango-abundancia + histograma DAP + scatter DAP-H + H' por parcela.

Guardar como PDF. Etiquetas completas.

---

# Lo que aprendimos hoy

| Operación | Código |
|---|---|
| Detectar NaN | `df.isnull().sum()` |
| Rellenar NaN | `df.fillna(mediana)` |
| Parsear fechas | `pd.to_datetime()` |
| Barras | `ax.bar()` o `.plot(kind="bar")` |
| Scatter | `ax.scatter(x, y)` |
| Histograma | `ax.hist(data, bins=)` |
| Subplots | `fig, axes = plt.subplots(1, 3)` |
| Guardar | `fig.savefig("fig.pdf")` |

---

# Próximas semanas

- **Sem. 13:** Integración + trabajo en proyecto grupal
- **Sem. 14:** Presentaciones grupales
- **Sem. 15:** Repaso + preparación examen
- **Sem. 16:** Examen final práctico

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 📝 Quiz 5
## Pandas + matplotlib

*15 minutos · Sin apuntes ni celular*
