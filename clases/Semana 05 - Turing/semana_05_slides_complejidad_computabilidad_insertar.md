<!-- ════════════════════════════════════════════════════════════
     INSERTAR ESTOS SLIDES AL FINAL DE semana_05_diapositivas.md
     justo ANTES del slide "Lo que aprendimos hoy"
     ════════════════════════════════════════════════════════════ -->

---

<!-- _class: invert -->

# Complejidad vs. Computabilidad
## Dos preguntas distintas sobre un mismo problema

---

# La metáfora del explorador

Imaginen todos los problemas como un **territorio**. Ustedes son exploradores y hacen dos preguntas, en orden:

**Pregunta 1 — Computabilidad (Turing):**
*"¿Puedo llegar a este destino? ¿Existe un camino?"*

**Pregunta 2 — Complejidad (Big-O):**
*"Si puedo llegar, ¿cuánto cuesta el viaje?"*

> La primera pregunta es de **existencia**: ¿hay solución o no? La segunda es de **costo**: ¿me alcanza la vida para encontrarla?

Son preguntas diferentes. Y la confusión entre ambas es uno de los errores más comunes en computación.

---

# Tres zonas, no dos

| Zona | Pregunta que responde | Ejemplo | Situación |
|---|---|---|---|
| **Tratable** | Resoluble Y costeable | Ordenar una lista: O(n log n) | Lo hacemos rutinariamente |
| **Intratable** | Resoluble PERO incosteable | Red óptima de reservas para 500 sitios: O(2ⁿ) | El camino existe, pero el universo se acaba antes de recorrerlo |
| **No computable** | No existe solución | Problema de la detención | No hay camino. Punto. |

> La confusión típica: pensar que **intratable** y **no computable** son lo mismo. No lo son. Lo intratable es carísimo pero posible. Lo no computable es **imposible**, sin importar los recursos.

---

# El error que no deben cometer

**"Es demasiado difícil, entonces es imposible"** ← FALSO

- O(2ⁿ) es **absurdamente caro**. Pero un algoritmo O(2ⁿ) **dará** la respuesta si esperan suficiente tiempo.
- El Halting Problem **no tiene algoritmo**. No es cuestión de esperar. No es cuestión de computadores más rápidos. No existe procedimiento — ni ahora, ni nunca.

La diferencia es entre:
- **"No me alcanza la plata para el pasaje"** (intratable)
- **"El destino no existe en ningún mapa"** (no computable)

---

<!-- _class: pregunta -->

# Un ejemplo de su futuro profesional

---

# Diseñar una red de áreas protegidas

**Problema:** *"Seleccionar el conjunto mínimo de sitios que proteja las 500 especies de una región."*

Esto es el **problema de cobertura de conjuntos** — NP-difícil, esencialmente O(2ⁿ).

Con 500 sitios candidatos: 2⁵⁰⁰ combinaciones posibles.

Ese número tiene **150 dígitos**. Si cada átomo del universo fuera un computador evaluando una combinación por nanosegundo desde el Big Bang, **todavía no habrían terminado**.

> Pero el problema **SÍ es computable**. La solución existe. El problema es que nadie puede encontrarla por fuerza bruta.

---

# ¿Qué hacen los biólogos de conservación?

Usan **algoritmos heurísticos** — como Marxan o Zonation.

No garantizan la solución **óptima**, pero encuentran una solución **"suficientemente buena"** en tiempo razonable (O(n²) o O(n³)).

**Intercambio:** pierden optimalidad, ganan tratabilidad.

> Esto es ingeniería algorítmica aplicada a la conservación. Y es exactamente la lógica de la Semana 4: elegir el algoritmo adecuado para el problema y el presupuesto computacional disponible.

---

# Ahora comparen con el Halting Problem

*"Escriba un programa que determine si cualquier corrida de Marxan va a terminar."*

Esto **NO** es cuestión de esperar más o tener un computador más rápido.

Turing demostró que **no existe algoritmo** que resuelva esto en general.

| Diseño de red óptima | Halting Problem |
|---|---|
| O(2ⁿ) — costosísimo pero computable | No computable — no hay algoritmo |
| Heurísticas dan soluciones "buenas" | No hay atajos. No hay heurísticas |
| Problema de **presupuesto** | Problema de **existencia** |

---

# El mapa completo

```
FÁCIL ────────────────────────── DIFÍCIL ───────────── IMPOSIBLE
 │                                  │                       │
 O(1)   O(log n)  O(n)  O(n log n)  O(n²)    O(2ⁿ)    ║  No existe
 │        │        │       │         │         │        ║  algoritmo
 │        │        │       │         │         │        ║
Leer    Búsqueda  Recorrer Merge   Burbuja  Fuerza    ║  Halting
primer  binaria   lista   sort    sort     bruta     ║  Problem
elem.   (Sem. 3)                           reservas  ║
 │        │        │       │         │         │        ║
 ◄──────── COMPLEJIDAD (Sem. 4) ──────────────►║◄─ COMPUTABILIDAD (Sem. 5)─►
           "¿Cuánto cuesta?"                   ║   "¿Es posible?"
                                               ║
                                          Barrera de
                                            Turing
```

Todo a la izquierda de la línea: **computable** (unos fáciles, otros imposiblemente caros).
Todo a la derecha: **fundamentalmente fuera de alcance**.

---

# ¿Y qué tiene que ver con la IA?

Cuando usen un LLM y parezca "resolver" un problema complejo, pregunten:

**¿Dónde está este problema en el mapa?**

- **Zona tratable** → el LLM probablemente tiene buenos datos de entrenamiento. La respuesta puede ser razonable.
- **Zona intratable** → el LLM está usando aproximaciones (o alucinando una respuesta plausible que es incorrecta).
- **Cerca de la barrera** → ningún LLM, ningún computador, ninguna tecnología futura lo resolverá exactamente. Lo mejor que existe es **estimar**.

> Saber **dónde** está un problema en este mapa determina qué herramientas son apropiadas. Esa intuición les va a servir toda la carrera.

---

<!-- _class: pregunta -->

# Resumen en una frase:

# La **complejidad** pregunta cuánto cuesta llegar.
# La **computabilidad** pregunta si se puede llegar.

# La Máquina de Turing dibujó el mapa.
# Big-O mide las distancias dentro de él.
