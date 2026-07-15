# Semana 12: Pandas avanzado y visualización con matplotlib

## Guía completa de la sesión

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (1.5 h cátedra + 1.5 h laboratorio) |
| **Objetivo central** | Manejar operaciones avanzadas de Pandas (limpieza, fechas, tablas pivote) y producir visualizaciones ecológicas con matplotlib |
| **Idea ancla** | Un buen gráfico comunica más que 100 números. La curva rango-abundancia muestra la estructura de una comunidad de una forma que ningún índice individual puede |
| **Prerrequisito** | Sem. 11 (Pandas básico) |
| **Evaluación** | Quiz 5 al final (15 min) |

---

## PARTE 1: CÁTEDRA CON LIVE CODING (90 min)

### Bloque A — Pandas avanzado (35 min)

#### Limpieza de datos (10 min)
- `df.isnull().sum()` — detectar NaN
- `df.dropna()` — eliminar filas con NaN
- `df.fillna(valor)` — rellenar (mediana, media, constante)
- Crear dataset sucio para practicar

#### Ordenar y ranking (5 min)
- `df.sort_values("dap_cm", ascending=False)`
- `df.groupby("especie")["dap_cm"].mean().sort_values(ascending=False)`

#### Fechas (10 min)
- `pd.to_datetime()` sobre columna fecha
- `.dt.month`, `.dt.day_name()` — extraer componentes
- `.resample("W")` — agrupar por semana
- Aplicar sobre dataset de cámaras trampa

#### Tablas pivote (10 min)
- `pd.pivot_table()` — abundancia por sitio × método
- `groupby` con múltiples columnas + `.unstack()`

### Bloque B — matplotlib (45 min)

#### Lógica: fig + ax (5 min)
- `fig, ax = plt.subplots(figsize=(10, 6))`
- Dibujar → decorar → mostrar

#### Gráfico de barras (8 min)
- Abundancia por especie con `.plot(kind="bar")`
- Colores, título, ejes, rotación de etiquetas

#### Scatter plot (8 min)
- DAP vs Altura coloreado por especie
- Leyenda, transparencia, tamaño de puntos

#### Histograma (5 min)
- Distribución de DAP con bins, línea de media

#### Curva rango-abundancia (7 min)
- Ordenar abundancias de mayor a menor
- Barras decrecientes → forma = estructura de comunidad
- Curva plana = equitativa, empinada = dominada

#### Subplots (7 min)
- `fig, axes = plt.subplots(1, 3)` — múltiples paneles
- Barras + histograma + boxplot en una figura

#### Guardar (5 min)
- `.savefig("figura.png", dpi=150)` y `.savefig("figura.pdf")`

### Bloque C — Pipeline completo (10 min)
CSV → read_csv → explorar → limpiar → filtrar → agrupar → graficar → interpretar

---

## PARTE 2: LABORATORIO (75 min)

### Ej. 1: Exploración visual del bosque (15 min)
Barras de abundancia, histograma de DAP, boxplot por especie

### Ej. 2: Relaciones DAP-Altura (15 min)
Scatter por especie, scatter por parcela

### Ej. 3: Análisis por parcela (15 min)
H' por parcela en barras, ¿más individuos = más diversa?

### Ej. 4: Cámaras trampa temporal (15 min)
Serie temporal por semana, barras por sitio y método, rango-abundancia × sitio

### Ej. 5 (desafío): Figura de publicación (15 min)
4 subplots: rango-abundancia + histograma DAP + scatter DAP-H + H' por parcela. Guardar como PDF.

---

## PARTE 3: QUIZ 5 (15 min)

1. (4 pts) Código Pandas para DAP promedio por sitio
2. (4 pts) Interpretar código con filtro + groupby + agg
3. (4 pts) Código matplotlib para barras con título y ejes
4. (4 pts) Dos estrategias para manejar NaN
5. (4 pts) Qué es una curva rango-abundancia, formas equitativa vs dominada
