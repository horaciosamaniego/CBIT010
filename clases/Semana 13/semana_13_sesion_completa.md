# Semana 13: Integración y trabajo de proyecto

## Guía completa de la sesión

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (1 h integración guiada + 2 h trabajo de proyecto con apoyo) |
| **Rol en el curso** | Sesión bisagra: consolida el pipeline completo de análisis de datos (Sem. 8–12) y abre tiempo estructurado para avanzar el proyecto de investigación grupal antes de las presentaciones de la Sem. 15 |
| **Objetivo central** | Que los estudiantes ejecuten un análisis de datos completo de principio a fin (cargar → limpiar → analizar → visualizar → interpretar) y apliquen ese flujo a los datos de su propio proyecto |
| **Idea ancla** | Hasta ahora cada semana enseñó una pieza. Hoy las piezas se ensamblan en un solo flujo de trabajo — el mismo que usarán en su proyecto, en el examen, y en su carrera |
| **Prerrequisito** | Toda la Sección 2 (Sem. 8–12) |
| **Materiales** | Proyector, Colab, WiFi, dataset de integración (monitoreo_biodiversidad_2025.csv), datos de los proyectos grupales |
| **Mira hacia adelante** | Sem. 14 (visualización avanzada para el proyecto), Sem. 15 (presentaciones), Sem. 16 (examen final) |

---

## PARTE 1: INTEGRACIÓN GUIADA (60 minutos)

*El objetivo de esta parte es modelar el pipeline completo una vez, en vivo, para que los grupos tengan una plantilla mental clara antes de trabajar en sus propios datos.*

---

### Bloque A — El pipeline de análisis de datos (10 min)

**Proyectar el flujo completo** antes de tocar código:

```
1. CARGAR        →  pd.read_csv()
2. DIAGNOSTICAR  →  isna(), duplicated(), describe()
3. LIMPIAR       →  dropna, fillna, drop_duplicates
4. ANALIZAR      →  groupby, value_counts, funciones propias
5. VISUALIZAR    →  matplotlib
6. INTERPRETAR   →  ¿qué significan los resultados?
```

*"Cada semana de la Sección 2 fue un paso de este flujo. La Sem. 11 fue cargar y agrupar; la Sem. 12 fue limpiar y visualizar. Hoy ponemos todo junto en una sola sesión de trabajo — y este es exactamente el flujo que necesitan para su proyecto."*

**Conexión con el proyecto:** recordar que el proyecto grupal (definido en la Sem. 7) requiere un análisis de datos. Esta plantilla es la que aplicarán a sus propios datos en la Parte 2.

---

### Bloque B — El pipeline completo en vivo (45 min)

*"Vamos a hacer, juntos, un análisis completo de un dataset que nunca han visto — con todos los problemas que tienen los datos reales."*

#### Paso 1: Cargar y mirar (7 min)

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
print(df.isna().sum())                      # valores faltantes
print(f"Duplicados: {df.duplicated().sum()}")  # filas repetidas
print(df["abundancia"].describe())          # valores extraños
print(df["especie"].unique())               # consistencia de nombres
```

*"Encontramos cuatro problemas: valores faltantes en abundancia, una fila duplicada, un valor sospechosamente alto (999), y una especie escrita en minúscula. Datos reales, problemas reales."*

#### Paso 3: Limpieza (12 min)

```python
# 1) Eliminar duplicados
df = df.drop_duplicates()

# 2) Convertir abundancia a número (los vacíos se vuelven NaN)
df["abundancia"] = pd.to_numeric(df["abundancia"], errors="coerce")

# 3) El valor 999 es un error de tipeo → lo tratamos como faltante
df.loc[df["abundancia"] > 100, "abundancia"] = None

# 4) Rellenar NaN con la mediana
df["abundancia"] = df["abundancia"].fillna(df["abundancia"].median())

# 5) Corregir la inconsistencia de mayúsculas
df["especie"] = df["especie"].str.capitalize()

# Verificar
print(df.isna().sum())
print(df["abundancia"].describe())
```

> *"Cada decisión de limpieza es una decisión científica, no técnica. ¿Eliminamos el outlier o lo corregimos? ¿Rellenamos con la media o la mediana? No hay una respuesta única — pero sí hay que justificarla y documentarla. Esto vale también para los datos de su proyecto."*

#### Paso 4: Análisis (9 min)

```python
# Riqueza por sitio
df.groupby("sitio")["especie"].nunique()

# Abundancia total por grupo taxonómico
df.groupby("grupo")["abundancia"].sum()

# Diversidad de Shannon por sitio (reutilizando la función de la Sem. 10)
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

riqueza = df.groupby("sitio")["especie"].nunique().sort_values()
riqueza.plot(kind="barh", ax=axes[0], color="#2E7D32")
axes[0].set_title("Riqueza de especies por sitio")
axes[0].set_xlabel("Nº de especies")

df.groupby("grupo")["abundancia"].sum().plot(kind="bar", ax=axes[1], color="#1565C0")
axes[1].set_title("Abundancia por grupo taxonómico")
axes[1].set_ylabel("Individuos")
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()
```

*"Cargamos datos crudos, los limpiamos, calculamos diversidad y produjimos un gráfico. Este flujo es lo que aplicarán ahora a los datos de su proyecto."*

---

## PARTE 2: TRABAJO DE PROYECTO CON APOYO (120 minutos)

*Esta es la razón de ser de la sesión: tiempo estructurado para que los grupos avancen su proyecto de investigación con el docente disponible para resolver dudas técnicas en el momento.*

---

### Estructura del tiempo de trabajo

El proyecto de investigación grupal fue definido en la Semana 7 y se presenta en la Semana 15. Esta sesión les da un bloque grande de trabajo con apoyo técnico en vivo — el mejor momento para destrabar problemas de datos o código antes de la recta final.

**Metas concretas para el final de la sesión (cada grupo):**

1. Tener sus datos cargados en Colab (CSV propio o dataset asignado)
2. Haber completado el diagnóstico de calidad (¿qué problemas tienen sus datos?)
3. Tener al menos un análisis preliminar corriendo (conteos, agrupaciones, o un índice)
4. Tener al menos un gráfico borrador

*"No tienen que terminar el proyecto hoy. La meta es que salgan de esta sesión con los datos cargados, limpios, y un primer análisis funcionando — para que en las próximas dos semanas se concentren en interpretar y comunicar, no en pelear con el código."*

### Hoja de ruta de trabajo (proyectar como referencia)

| Fase | Qué hacer | Pista / semana de referencia |
|---|---|---|
| **1. Cargar** | Subir el CSV a Colab y leerlo con Pandas | Sem. 11 + métodos de carga de Drive |
| **2. Diagnosticar** | `isna()`, `duplicated()`, `describe()`, `unique()` | Sem. 12, Bloque A |
| **3. Limpiar** | Decidir y documentar cómo tratar problemas | Sem. 12 — justificar cada decisión |
| **4. Analizar** | `groupby`, `value_counts`, funciones de diversidad | Sem. 10–11 |
| **5. Graficar** | Al menos un gráfico con título y ejes | Sem. 12 |
| **6. Interpretar** | ¿Qué responde esto a su pregunta de investigación? | Sem. 7 (la pregunta del proyecto) |

### Rol del docente durante el trabajo

- **Circular activamente** entre los grupos. Esta es la oportunidad de oro para apoyo individualizado.
- **No escribir el código por ellos**, pero sí destrabar: señalar el error en un traceback, recordar qué función de qué semana aplica, sugerir el enfoque.
- **Detectar problemas comunes temprano:** grupos con datos mal estructurados, preguntas de investigación demasiado amplias para sus datos, o expectativas poco realistas sobre lo que pueden analizar.
- **Tomar nota** de qué grupos están atrasados, para seguimiento antes de la Sem. 15.

### Mini-consultas (opcional, si varios grupos comparten una duda)

Si el docente nota que varios grupos tienen el mismo problema (ej.: cómo cargar su CSV, cómo hacer un groupby con su estructura), pausar 3–5 minutos y resolverlo en el proyector para todos. Estas micro-clases just-in-time son muy efectivas porque responden a una necesidad inmediata y real.

### Cierre de la sesión (últimos 10 min)

- Pedir a cada grupo que reporte en una frase **dónde quedaron** y **qué les falta**.
- Recordar las fechas: Sem. 14 (visualización avanzada — traer sus gráficos para mejorarlos), Sem. 15 (presentaciones), Sem. 16 (examen).
- Recordar que el horario de consulta sigue disponible para grupos que necesiten apoyo extra.

---

## Materiales de apoyo para los grupos

### Plantilla de pipeline (compartir en Notion)

Un notebook plantilla con las seis secciones del pipeline como encabezados vacíos, que los grupos pueden copiar y rellenar con sus propios datos. Reduce la fricción de "página en blanco" y asegura que ningún grupo olvide un paso (especialmente el diagnóstico de calidad y la interpretación).

### Lista de verificación del proyecto (para los grupos)

- [ ] Datos cargados y leídos correctamente en Colab
- [ ] Diagnóstico de calidad completo (NaN, duplicados, outliers, consistencia)
- [ ] Limpieza realizada y **justificada** en celdas de texto
- [ ] Al menos un análisis que responda (parcial o totalmente) a la pregunta de investigación
- [ ] Al menos un gráfico con título y ejes etiquetados
- [ ] Interpretación preliminar escrita

---

## Notas pedagógicas

### Por qué una sesión de trabajo con apoyo, y no más contenido

A esta altura del curso, el cuello de botella de los estudiantes ya no es la falta de conceptos — es aplicarlos a datos reales y desordenados que no vienen pre-empaquetados como los ejercicios de clase. El tiempo de trabajo con el docente presente vale más que una clase magistral nueva: resuelve los problemas específicos de cada grupo en el momento en que surgen.

### El diagnóstico de calidad como hábito

El paso que los estudiantes más tienden a saltarse es el diagnóstico de calidad (Paso 2). Quieren ir directo a graficar. Insistir: **siempre** mirar los datos antes de analizarlos. Un gráfico hecho sobre datos sucios es peor que no tener gráfico, porque comunica con confianza algo que es falso.

### Heterogeneidad de los grupos

Los grupos avanzarán a ritmos muy distintos. Los más rápidos pueden empezar a pulir visualizaciones (adelantando la Sem. 14); los más lentos pueden necesitar ayuda con la carga de datos. Tener preparada una tarea de extensión para los grupos avanzados ("agreguen un segundo índice de diversidad", "comparen dos formas de manejar los NaN") evita que se aburran mientras se apoya a los demás.

### Conexión con el resto del curso

| Concepto consolidado | Dónde se usa después |
|---|---|
| Pipeline completo | Sem. 16 (examen: mismo flujo sobre dataset nuevo) |
| Limpieza de datos del proyecto | Sem. 14–15 (proyecto final) |
| Gráficos borrador | Sem. 14 (se pulen a calidad de presentación) |
| Interpretación preliminar | Sem. 15 (se desarrolla en la presentación) |
