---
pdf-engine: xelatex
fontsize: 10pt

header-includes:
  - \pagenumbering{gobble}
  - \usepackage{fancyhdr}
  - \usepackage{graphicx}
  - \pagestyle{fancy}
  - \fancyhead[L]{CBIT010}
  - \fancyhead[C]{\bf Control 5}
  - \fancyhead[R]{2026}
  - \fancyfoot{}

---

**Nombre:** _______________________________________________ **Puntaje:** _____ / 30



> **Instrucciones:** Sin apuntes, sin celular, sin LLMs. Tiempo: 20 minutos.
> Responde en los espacios indicados. Para las preguntas de código, la sintaxis no necesita ser perfecta, pero la lógica sí debe ser correcta.
>
> **Contexto:** Todas las preguntas usan un DataFrame `df` con datos de un inventario forestal del bosque valdiviano:
>
> | Columna | Tipo | Descripción |
> |----|---|---|
> | `especie` | str | Nombre de la especie |
> | `dap_cm` | float | Diámetro a la altura del pecho (cm) |
> | `altura_m` | float | Altura del árbol (m) |
> | `parcela` | int | Número de parcela (1–5) |


## Parte A — Lectura de código (10 puntos)

**A1. (3 puntos)** ¿Qué devuelve el siguiente código? Describe el resultado en palabras (no necesitas calcular números exactos).

```python
df.groupby("parcela")["dap_cm"].mean()
```

Respuesta: ____________________________________________________________

\vspace{1cm}


**A2. (4 puntos)** Explica paso a paso qué hace este código:

```python
df[df["altura_m"] > 20].groupby("especie")["dap_cm"].agg(["count", "mean"])
```

Paso 1 (`df[df["altura_m"] > 20]`): ___________________________________

Paso 2 (`.groupby("especie")`): ______________________________________

Paso 3 (`["dap_cm"].agg(["count", "mean"])`): _________________________

\vspace{1cm}

**A3. (3 puntos)** Dado este código, ¿qué imprime?

```python
conteos = df["especie"].value_counts()
print(conteos.index[0])
```

Respuesta: _________________________________________________________

Explica qué representa ese valor: ____________________________________

\vspace{1cm}

## Parte B — Escritura de código (12 puntos)

**B1. (3 puntos)** Escribe UNA línea de Pandas para obtener la altura promedio de cada especie.

```python

```

\vspace{1cm}

**B2. (3 puntos)** Escribe el código para filtrar el DataFrame y quedarte solo con los árboles de la parcela 2 que tengan DAP mayor a 30 cm.

```python

```

\vspace{1cm}

**B3. (6 puntos)** Completa el código para crear un gráfico de barras de la abundancia por especie. Debe tener título y etiqueta del eje Y.

```python
import matplotlib.pyplot as plt

conteos = df["especie"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
conteos.plot(kind=__________, ax=__________)
ax.____________("Abundancia por especie")
ax.____________("Número de individuos")
plt.tight_layout()
plt.show()
```

\vspace{1cm}


## Parte C — Manejo de datos imperfectos (4 puntos)

**C1. (4 puntos)** La columna `altura_m` tiene algunos valores faltantes (NaN).

a) (1 pt) Escribe el código para contar cuántos NaN hay en esa columna:

```python

```

b) (3 pts) Describe DOS estrategias distintas para manejar esos NaN, e indica una ventaja o desventaja de cada una.

Estrategia 1: __________________________________________________

Ventaja/desventaja: ___________________________________________

Estrategia 2: __________________________________________________

Ventaja/desventaja: ___________________________________________

\vspace{1cm}


## Parte D — Interpretación ecológica (4 puntos)

**D1. (4 puntos)** La siguiente es una curva de rango-abundancia de dos sitios. Ambos tienen la misma riqueza (S = 7 especies) y un número similar de individuos totales (~100).

\begin{center}
\includegraphics[width=0.4\textwidth]{./figs/graphControl.png}
\end{center}

a) (2 pts) ¿Cuál sitio tiene mayor equitatividad (J)? Justifica observando la forma de la curva.

\vspace{1cm}

b) (2 pts) Si ambos sitios tienen el mismo número de especies (riqueza S), ¿cuál tendrá mayor índice de Shannon (H')? ¿Por qué?



\vspace{1cm}


## Bonus (2 puntos extra)

**E1.** Escribe el código para guardar una figura `fig` como un archivo PDF llamado `figura_bosque.pdf`, con bordes ajustados.

```python

```
