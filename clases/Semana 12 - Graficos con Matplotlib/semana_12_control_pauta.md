---
pdf-engine: xelatex
fontsize: 12pt

header-includes:
  - \pagenumbering{gobble}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{CBIT010}
  - \fancyhead[C]{\bf Control 5}
  - \fancyhead[R]{2026}
  - \fancyfoot{}
  
---

**Nombre:** _____________________  **Fecha:** ____________

**Puntaje:** _____ / 30

---

> **Instrucciones:** Sin apuntes, sin celular, sin LLMs. Tiempo: 20 minutos.
> Responde en los espacios indicados. Para las preguntas de código, la sintaxis no necesita ser perfecta, pero la lógica sí debe ser correcta.
>
> **Contexto:** Todas las preguntas usan un DataFrame `df` con datos de un inventario forestal del bosque valdiviano:
>
> | Columna | Tipo | Descripción |
> |---|---|---|
> | `especie` | str | Nombre de la especie |
> | `dap_cm` | float | Diámetro a la altura del pecho (cm) |
> | `altura_m` | float | Altura del árbol (m) |
> | `parcela` | int | Número de parcela (1–5) |



## Parte A — Lectura de código (10 puntos)

**A1. (3 puntos)** ¿Qué devuelve el siguiente código? Describe el resultado en palabras (no necesitas calcular números exactos).

```python
df.groupby("parcela")["dap_cm"].mean()
```

Respuesta:
_______________________________________________________________

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

---

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

---

## Parte D — Interpretación ecológica (4 puntos)

**D1. (4 puntos)** La siguiente es una curva de rango-abundancia de dos sitios:

```
Sitio A:  ████████ ██████ █████ ████ ███ ██ █     (cae gradualmente)
Sitio B:  ████████████████ █ █ █ █                 (una especie domina)
```

a) (2 pts) ¿Cuál sitio tiene mayor equitatividad (J)? Justifica.

_______________________________________________________________

b) (2 pts) Si ambos sitios tienen el mismo número de especies (riqueza S), ¿cuál tendrá mayor índice de Shannon (H')? ¿Por qué?

_______________________________________________________________
_______________________________________________________________

---

## Bonus (2 puntos extra)

**E1.** Escribe el código para guardar una figura `fig` como un archivo PDF llamado `figura_bosque.pdf`, con bordes ajustados.

```python

```

---

*Fin del Quiz 5*

---
---

# PAUTA DE CORRECCIÓN — Quiz 5

*(Documento del docente — no distribuir a estudiantes)*

---

## Parte A — Lectura de código (10 puntos)

**A1. (3 puntos)**
Devuelve el **DAP promedio de cada parcela**: una Serie de Pandas donde el índice son los números de parcela (1–5) y los valores son el promedio de `dap_cm` de los árboles de cada parcela.

- 3 pts: identifica que agrupa por parcela Y calcula el promedio de DAP
- 2 pts: menciona promedio pero no por grupo, o viceversa
- 1 pt: respuesta vaga ("calcula algo del DAP")

---

**A2. (4 puntos)**
- **Paso 1:** Filtra el DataFrame, quedándose solo con los árboles de altura mayor a 20 m (1 pt)
- **Paso 2:** Agrupa esos árboles filtrados por especie (1 pt)
- **Paso 3:** Para cada especie, calcula el conteo (count) y el promedio (mean) de su DAP (2 pts)

Respuesta completa: "Entre los árboles de más de 20 m de altura, muestra cuántos hay de cada especie y su DAP promedio."

---

**A3. (3 puntos)**
- Imprime el **nombre de la especie más abundante** (2 pts)
- `value_counts()` ordena de mayor a menor frecuencia, así que `.index[0]` es la especie con más individuos (1 pt por la explicación)

Errores comunes: decir que imprime el conteo (no, imprime el nombre porque accede a `.index`, no a `.values`).

---

## Parte B — Escritura de código (12 puntos)

**B1. (3 puntos)**
```python
df.groupby("especie")["altura_m"].mean()
```
- 3 pts: correcto y completo
- 2 pts: lógica correcta, error menor de sintaxis (ej. comillas, corchetes)
- 1 pt: usa groupby pero columna o función incorrecta

---

**B2. (3 puntos)**
```python
df[(df["parcela"] == 2) & (df["dap_cm"] > 30)]
```
- 3 pts: ambas condiciones, uso correcto de `&` y paréntesis
- 2 pts: lógica correcta pero usa `and` en vez de `&`, o falta algún paréntesis
- 1 pt: solo una condición correcta

Error común: usar `and` en lugar de `&` (en Pandas se usa `&`).

---

**B3. (6 puntos)** — 1.5 pts por cada blank:
```python
conteos.plot(kind="bar", ax=ax)
ax.set_title("Abundancia por especie")
ax.set_ylabel("Número de individuos")
```
- `kind="bar"` (1.5 pts)
- `ax=ax` (1.5 pts)
- `set_title` (1.5 pts)
- `set_ylabel` (1.5 pts)

Aceptar `kind="barh"` para barras horizontales.

---

## Parte C — Datos imperfectos (4 puntos)

**C1a. (1 pt)**
```python
df["altura_m"].isna().sum()
```
Aceptar `.isnull().sum()` (son equivalentes).

**C1b. (3 puntos)** — Dos estrategias válidas con ventaja/desventaja:

| Estrategia | Código | Ventaja | Desventaja |
|---|---|---|---|
| Eliminar filas | `df.dropna(subset=["altura_m"])` | No inventa datos | Pierde información, reduce muestra |
| Rellenar con media/mediana | `df["altura_m"].fillna(df["altura_m"].median())` | Conserva todas las filas | Inventa valores que pueden sesgar |
| Rellenar con 0 | `df["altura_m"].fillna(0)` | Simple | Distorsiona estadísticas gravemente |

- 1.5 pts por cada estrategia bien descrita con su ventaja/desventaja
- Aceptar interpolación u otras estrategias razonables

---

## Parte D — Interpretación ecológica (4 puntos)

**D1a. (2 puntos)**
**Sitio A** tiene mayor equitatividad. Su curva cae gradualmente, lo que indica que las abundancias están más repartidas entre las especies. El Sitio B está dominado por una sola especie (curva muy empinada), lo que significa baja equitatividad.

- 2 pts: identifica Sitio A con justificación de la forma de la curva
- 1 pt: identifica Sitio A sin justificación clara

**D1b. (2 puntos)**
**Sitio A** tendrá mayor H'. Con la misma riqueza, el índice de Shannon es máximo cuando las abundancias son equitativas. Como el Sitio B está dominado por una especie, su H' es menor a pesar de tener la misma riqueza.

- 2 pts: identifica Sitio A y conecta equitatividad con H'
- 1 pt: identifica Sitio A sin explicar el rol de la equitatividad

Conexión con Sem. 3 y Sem. 10: H' depende tanto de la riqueza (S) como de la equitatividad (J). H' = J × ln(S).

---

## Bonus (2 puntos)

**E1.**
```python
fig.savefig("figura_bosque.pdf", bbox_inches="tight")
```
- 2 pts: correcto con `bbox_inches="tight"`
- 1 pt: `savefig` correcto sin el parámetro de bordes

---

## Resumen de puntajes

| Parte | Puntos | Tema |
|---|---|---|
| A — Lectura de código | 10 | groupby, filtrado, value_counts |
| B — Escritura de código | 12 | groupby, filtrado múltiple, matplotlib |
| C — Datos imperfectos | 4 | NaN: detección y estrategias |
| D — Interpretación ecológica | 4 | Curva rango-abundancia, equitatividad, H' |
| Bonus | +2 | savefig |
| **Total** | **30 (+2)** | |

**Distribución cognitiva:** ~33% lectura/comprensión, ~40% producción de código, ~27% interpretación conceptual. El quiz equilibra la habilidad técnica (escribir Pandas/matplotlib) con la comprensión ecológica (¿qué significan los resultados?), reforzando que programar es un medio, no un fin.