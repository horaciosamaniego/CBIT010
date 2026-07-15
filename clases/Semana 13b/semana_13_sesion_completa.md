# Semana 13: Integración y cierre — Del lápiz al código

## Guía completa de la sesión (clase de cierre del curso)

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (1.5 h integración guiada + 1.5 h proyecto capstone) |
| **Rol en el curso** | **Clase de cierre.** Es el último encuentro del semestre. Integra toda la Sección 2 (Python) y la conecta con la Sección 1 (analógica). Cierra el arco completo del curso |
| **Objetivo central** | Que los estudiantes ejecuten, de principio a fin y de forma autónoma, un análisis de datos ecológicos reales: cargar → limpiar → analizar → visualizar → interpretar |
| **Idea ancla** | Hace 13 semanas no habían tocado código. Hoy toman un archivo de datos crudo, con errores, y producen un análisis completo de biodiversidad. El viaje del lápiz al código está completo |
| **Prerrequisito** | Toda la Sección 2 (Sem. 8–12) |
| **Materiales** | Proyector, Colab, WiFi, dataset capstone (monitoreo_biodiversidad_2025.csv) |

> **Nota sobre evaluación:** Como el curso cierra en la Semana 13, el proyecto capstone de esta sesión reemplaza al examen práctico final. Ver "Nota sobre cierre de evaluaciones" al final.

---

## PARTE 1: INTEGRACIÓN GUIADA (90 minutos)

---

### Bloque A — El arco completo: de dónde venimos (15 min)

**No abrir el computador todavía.** Esta es una mirada hacia atrás.

Proyectar la línea de tiempo del curso:

```
SECCIÓN 1 (analógica, sin computador)
 Sem 1: Computador Humano — qué es computar
 Sem 2: Binario y ASCII — cómo se codifican los datos
 Sem 3: Entropía y Shannon H' — medir información y diversidad
 Sem 4: Algoritmos y pseudocódigo — pensar en pasos
 Sem 5: Máquina de Turing — qué es (y no es) computable
 Sem 6: Límites e IA — modelos de lenguaje y sus sesgos
 Sem 7: IA en conservación — el estado del arte

SECCIÓN 2 (Python)
 Sem 8: Variables, tipos, condicionales, bucles
 Sem 9: Colecciones — listas y diccionarios
 Sem 10: Funciones — encapsular y reutilizar
 Sem 11: Pandas — del CSV al análisis
 Sem 12: Pandas avanzado + visualización
 Sem 13: HOY — integración y cierre
```

**Preguntas para el curso (discusión abierta, 5 min):**
- *"¿Recuerdan la primera clase, cuando ejecutaron un programa con lápiz y papel siendo el Computador Humano?"*
- *"Cada concepto de Python que aprendieron ya lo habían visto sin computador. ¿Pueden nombrar uno?"*

Mostrar el mapa de equivalencias una última vez:

| Concepto | Sección 1 (analógico) | Sección 2 (Python) |
|---|---|---|
| Variable | Celda de memoria (Sem. 1) | `x = 42` |
| Tipo de dato | Codificación ASCII (Sem. 2) | `int`, `float`, `str` |
| Diversidad H' | Cálculo a mano (Sem. 3) | `shannon_entropy()` |
| Decisión | Rombo del diagrama (Sem. 4) | `if / elif / else` |
| Repetición | Pasadas del algoritmo (Sem. 4) | `for`, `while` |
| Procedimiento | Tabla de transiciones MT (Sem. 5) | función `def` |

> *"Python no fue lo difícil. Lo difícil — pensar como un computador, entender qué es un dato, qué es un algoritmo — lo aprendieron sin pantalla. Python solo fue ponerle sintaxis a esas ideas."*

---

### Bloque B — El pipeline completo en vivo (45 min)

*"Vamos a hacer, juntos, un análisis completo de un dataset que nunca han visto. Es un archivo real de monitoreo de biodiversidad — con todos los problemas que tienen los datos reales."*

#### Paso 1: Cargar y mirar (8 min)

```python
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("monitoreo_biodiversidad_2025.csv")

print(df.shape)
df.head(10)
df.info()
```

*"Antes de analizar nada: ¿cuántas filas? ¿Qué columnas? ¿Qué tipos? Siempre miren los datos primero."*

#### Paso 2: Diagnóstico de calidad (10 min)

```python
# ¿Hay valores faltantes?
print(df.isna().sum())

# ¿Hay filas duplicadas?
print(f"Duplicados: {df.duplicated().sum()}")

# ¿La columna abundancia tiene valores extraños?
print(df["abundancia"].describe())

# ¿Las especies están escritas consistentemente?
print(df["especie"].unique())
```

*"Encontramos cuatro problemas: valores faltantes en abundancia, una fila duplicada, un valor sospechosamente alto (999), y una especie escrita en minúscula. Datos reales, problemas reales."*

#### Paso 3: Limpieza (12 min)

```python
# 1) Eliminar duplicados
df = df.drop_duplicates()

# 2) Convertir abundancia a número (los vacíos se vuelven NaN)
df["abundancia"] = pd.to_numeric(df["abundancia"], errors="coerce")

# 3) El valor 999 es claramente un error de tipeo (outlier)
#    Decisión: lo tratamos como dato faltante
df.loc[df["abundancia"] > 100, "abundancia"] = None

# 4) Rellenar NaN — decisión ecológica: usamos la mediana del grupo
df["abundancia"] = df["abundancia"].fillna(df["abundancia"].median())

# 5) Corregir la inconsistencia de mayúsculas
df["especie"] = df["especie"].str.capitalize()

# Verificar
print(df.isna().sum())
print(df["abundancia"].describe())
```

> *"Cada decisión de limpieza es una decisión científica, no técnica. ¿Eliminamos el outlier o lo corregimos? ¿Rellenamos con la media o la mediana? No hay una respuesta única — pero sí hay que justificarla y documentarla."*

#### Paso 4: Análisis (8 min)

```python
# Riqueza por sitio
df.groupby("sitio")["especie"].nunique()

# Abundancia total por grupo taxonómico
df.groupby("grupo")["abundancia"].sum()

# Diversidad de Shannon por sitio
def shannon_entropy(abundancias):
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H

print("\nDiversidad por sitio:")
for sitio, grupo in df.groupby("sitio"):
    abund = grupo.groupby("especie")["abundancia"].sum()
    H = shannon_entropy(abund.values)
    print(f"  {sitio}: S={len(abund)}, H'={H:.3f}")
```

#### Paso 5: Visualización (7 min)

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Riqueza por sitio
riqueza = df.groupby("sitio")["especie"].nunique().sort_values()
riqueza.plot(kind="barh", ax=axes[0], color="#2E7D32")
axes[0].set_title("Riqueza de especies por sitio")
axes[0].set_xlabel("Nº de especies")

# Abundancia por grupo
df.groupby("grupo")["abundancia"].sum().plot(kind="bar", ax=axes[1], color="#1565C0")
axes[1].set_title("Abundancia por grupo taxonómico")
axes[1].set_ylabel("Individuos")
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()
```

*"Cargamos datos crudos, los limpiamos, calculamos diversidad y produjimos un gráfico. Este es el trabajo de un analista de datos en conservación — y lo acaban de hacer."*

---

### Bloque C — Hacia dónde seguir (10 min)

*"Este curso fue una introducción. ¿Qué viene después?"*

**Herramientas para profundizar:**
- **R + tidyverse:** el otro gran lenguaje de análisis ecológico. Lo verán en cursos de estadística y ecología de comunidades. Lo que aprendieron de Pandas se traduce casi directo.
- **QGIS / Python (geopandas):** análisis espacial, mapas, datos de teledetección.
- **Estadística:** ahora pueden *implementar* lo que aprendan — regresiones, modelos, pruebas de hipótesis.
- **Bases de datos de biodiversidad:** GBIF, eBird, iNaturalist — todas con APIs que pueden consultar con Python.

**El mensaje de cierre:**
> *"No se vuelven programadores. Se vuelven científicos de recursos naturales que pueden hablar con los datos directamente, sin depender de que alguien más procese sus números. Esa autonomía es poder."*

---

## PARTE 2: PROYECTO CAPSTONE (90 minutos)

---

### El proyecto

Los estudiantes reciben el dataset `monitoreo_biodiversidad_2025.csv` (el mismo de la demostración, o una variante) y realizan un análisis completo de forma autónoma, en parejas. Es la culminación del curso.

**Entregable:** un notebook de Colab con el análisis completo, comentado, que incluya:

1. **Carga y exploración** — shape, columnas, tipos, primeras filas
2. **Diagnóstico de calidad** — identificar NaN, duplicados, valores atípicos, inconsistencias
3. **Limpieza documentada** — cada decisión justificada en una celda de texto (¿por qué eliminar vs rellenar? ¿por qué la mediana?)
4. **Análisis** — al menos: riqueza por sitio, abundancia por grupo, diversidad de Shannon por sitio
5. **Visualización** — al menos dos gráficos con título y ejes etiquetados
6. **Interpretación** — un párrafo final: ¿cuál sitio es más diverso? ¿qué grupo domina? ¿qué limitaciones tienen estos datos?

### Estructura sugerida del notebook (se entrega como esqueleto)

El notebook starter tiene las seis secciones como encabezados, con celdas de texto que piden la justificación y celdas de código con pistas mínimas. A diferencia de las semanas anteriores, hay **menos andamiaje** — es una evaluación de integración, no una guía paso a paso.

### Rol del docente durante el capstone

- Circular y resolver dudas puntuales, pero **no dar el código**.
- Si un grupo se traba, hacer preguntas socráticas: *"¿Cómo supieron en la Sem. 11 cuántas especies había? ¿Qué función usaron?"*
- Recordar que pueden usar sus notebooks anteriores como referencia (las funciones de diversidad de la Sem. 10, los ejemplos de Pandas de la Sem. 11–12).
- LLMs permitidos con prompt log, como en todas las tareas de la Sección 2.

### Cierre de la sesión (últimos 10 min)

- Pedir a 2–3 grupos que compartan su gráfico y una conclusión.
- Cierre del curso: agradecer, recordar el arco (Computador Humano → análisis de biodiversidad real), y los caminos a seguir.

---

## Nota sobre cierre de evaluaciones

El diseño original contemplaba presentaciones grupales (Sem. 15) y examen final práctico (Sem. 16). Como el curso cierra en la Semana 13, se proponen estos ajustes:

| Evaluación original | Ajuste propuesto |
|---|---|
| Examen práctico final (25%, Sem. 16) | Reemplazado por el **proyecto capstone** de esta sesión (individual o en parejas) |
| Presentaciones grupales (20%, Sem. 15) | El proyecto de investigación (Sem. 7) se entrega como **informe escrito**, sin presentación oral; o presentación breve en esta misma sesión si el tiempo lo permite |
| Tareas de programación (25%) | Sin cambios (Sem. 9, 11) |
| Quizzes (10%) | Sin cambios (Quiz 4 Sem. 10, Quiz 5 Sem. 12) |
| Participación (10%) | Sin cambios |

> Recalcular ponderaciones según lo que efectivamente se haya evaluado. Una opción simple: redistribuir el 25% del examen al capstone, y convertir el 20% de presentación oral en 20% de informe escrito.

---

## Notas pedagógicas

### El cierre emocional importa

Esta es la última clase. Más allá del contenido técnico, vale la pena dedicar tiempo al arco narrativo: estos estudiantes empezaron siendo "el Computador Humano" con lápiz y papel, y terminan analizando datos reales de biodiversidad. Nombrar ese viaje explícitamente les da una sensación de logro y cierre.

### El capstone como evaluación auténtica

A diferencia de un examen con preguntas aisladas, el capstone evalúa exactamente lo que un profesional hace: tomar datos imperfectos y producir un análisis defendible. Es más difícil de "estudiar de memoria" y más cercano a la práctica real.

### Menos andamiaje, a propósito

Las semanas anteriores tenían notebooks muy guiados (`# TU CÓDIGO AQUÍ` con pistas). El capstone reduce eso deliberadamente: es el momento de demostrar autonomía. Está bien que batallen un poco — es parte de la evaluación.

### Los datos sucios son el punto

El dataset tiene errores a propósito (NaN, duplicado, outlier, inconsistencia de mayúsculas). En un examen tradicional esto sería "injusto". En un capstone es el corazón del ejercicio: los datos reales siempre vienen sucios, y saber diagnosticarlos y limpiarlos es la habilidad más transferible del curso.
