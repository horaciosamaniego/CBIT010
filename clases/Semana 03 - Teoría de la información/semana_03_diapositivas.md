---
marp: true
theme: gaia
paginate: true
size: 16:9
math: mathjax
style: |
  section {
    font-size: 30px; line-height: 1.45; padding: 40px 50px;
    background: #FAFAFA; color: #222;
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  }
  section h1 { color: #1B4332; font-size: 1.6em; border-bottom: 3px solid #B2DFDB; padding-bottom: 6px; margin-bottom: 16px; }
  section h2 { color: #2E5E4E; font-size: 1.25em; margin-bottom: 12px; }
  section h3 { color: #40916C; font-size: 1.05em; }
  section strong { color: #1B4332; }
  section em { color: #555; }
  section li { margin-bottom: 4px; }
  section ul, section ol { margin: 6px 0 10px 20px; }
  section p { margin-bottom: 8px; }
  
  section.lead {
    background: #1B4332; color: #E8F5E9;
    text-align: center; display: flex; flex-direction: column; justify-content: center;
  }
  section.lead h1 { color: #fff; font-size: 2em; border-bottom: none; margin-bottom: 8px; }
  section.lead h2 { color: #A5D6A7; font-weight: 400; font-size: 1.3em; }
  section.lead p, section.lead em { color: #81C784; font-size: 0.85em; }
  
  section.invert {
    background: #2E5E4E; color: #E8F5E9;
    display: flex; flex-direction: column; justify-content: center; text-align: center;
  }
  section.invert h1 { color: #fff; border-bottom: 3px solid rgba(255,255,255,0.3); font-size: 1.8em; }
  section.invert h2 { color: #A5D6A7; font-size: 1.2em; }
  section.invert footer { display: none; }

  section.pregunta {
    background: #E8F5E9; color: #1B4332;
    text-align: center; display: flex; flex-direction: column; justify-content: center;
  }
  section.pregunta h1 { font-size: 1.5em; border-bottom: none; color: #1B4332; margin-bottom: 12px; }
  section.pregunta p, section.pregunta em { color: #2E5E4E; font-size: 0.95em; }
  
  section.lab {
    background: #FFF8E1; color: #333; border-top: 4px solid #F9A825;
  }
  section.lab h1 { color: #E65100; border-bottom: 3px solid #FFE0B2; font-size: 1.4em; }
  section.lab h2 { color: #BF360C; font-size: 1.15em; }
  table { font-size: 0.8em; width: 100%; border-collapse: collapse; margin: 8px 0; }
  thead th { background: #2E5E4E; color: #fff; padding: 6px 10px; text-align: left; font-weight: 600; }
  td { padding: 5px 10px; border: 1px solid #ccc; vertical-align: top; }
  tbody tr:nth-child(even) td { background: #F0F7F4; }
  section.lab thead th { background: #E65100; }
  section.lab tbody tr:nth-child(even) td { background: #FFF3E0; }
  blockquote {
    background: #E8F5E9; border-left: 4px solid #2E7D32;
    padding: 10px 16px; margin: 10px 0; font-size: 0.95em; border-radius: 3px;
  }
  blockquote p { margin: 0; }
  pre { font-size: 0.78em; background: #f5f5f5; border-left: 3px solid #40916C; padding: 10px 14px; }
  code { font-size: 0.88em; background: #E8F5E9; padding: 1px 5px; border-radius: 3px; }
  section::after { color: #999; font-size: 0.65em; }
  .formula-box {
    background: #E8F5E9; border: 2px solid #2E7D32; border-radius: 6px;
    padding: 16px 24px; text-align: center; margin: 12px 0; font-size: 1.1em;
  }

footer: "*CBIT010 · Conceptos básicos de teoría de la información*  - Horacio Samaniego *(horaciosamaniego@uach.cl)*"
---

<!-- _class: lead -->
<!-- _paginate: false -->

## Conceptos básicos e Introducción
# Teoría de la información

*CBIT010 · Introducción al Análisis de Datos y Programación*

2026

---

# De la semana pasada

- Cada carácter cuesta **8 bits** en ASCII
- Un libro de 500 páginas → millones de bits

**Pregunta de hoy:** ¿Se puede ser más eficiente? ¿Hay letras que necesiten menos bits que otras?

**Respuesta:** Sí. Y hay una teoría que nos dice exactamente cuántos bits necesita cada mensaje.

---

# Hoja de ruta

1. 🪙 **La moneda, el dado y la sorpresa**
2. 📐 **La fórmula de Shannon**
3. 🌿 **La conexión ecológica: H' de Shannon**
4. 📦 **Redundancia y compresión**
5. 📡 **Canales y ruido**
6. 🧪 **Laboratorio: 20 Preguntas con fauna chilena**

---

<!-- _class: invert -->

# La moneda, el dado y la sorpresa

---

# 🪙 Experimento 1: La moneda

Voy a lanzar esta moneda. **¿Cuánta información da el resultado?**

- 2 resultados posibles, equiprobables (50/50)
- Antes: incertidumbre total
- Después: la incertidumbre se resuelve completamente

> El resultado contiene exactamente **1 bit** de información. Una pregunta sí/no basta: "¿Es cara?"

---

# 🎲 Experimento 2: El dado

**¿Cuánta información da el resultado de un dado?**

- 6 resultados posibles, equiprobables
- Se necesitan **más preguntas** para adivinarlo
- "¿Mayor que 3?" → "¿Mayor que 5?" → ...

> Más posibilidades = más incertidumbre = **más información al resolverla**.

El dado "sorprende más" que la moneda.

---

# 🎲 Experimento 3: El dado cargado

**¿Y si sale 6 el 90% de las veces?**

- Sale 6 → poca sorpresa → **poca información**
- Sale 1 → mucha sorpresa → **mucha información**

> **Los eventos raros son más informativos que los comunes.**

💬 *"Hoy salió el sol en Atacama"* — ¿es informativo? No.
💬 *"Hoy nevó en Atacama"* — ¿es informativo? **Mucho.**

La diferencia es la **probabilidad** del evento.

---

<!-- _class: pregunta -->

# 🤔 ¿Se puede medir la sorpresa con una fórmula?

*Sí. La inventó un ingeniero llamado Claude Shannon en 1948.*

---

<!-- _class: invert -->

# La fórmula de Shannon
## Entropía de la información

---

# Claude Shannon (1916–2001)

- 1948: publica *"A Mathematical Theory of Communication"*
- Laboratorios Bell (compañía telefónica)
- Problema: ¿cuántos **bits por segundo** necesita un cable para transmitir una conversación?
- Inventó una forma de medir la **cantidad de información** de cualquier fuente
- De paso, inventó la palabra **"bit"**

---

# La fórmula

Para una fuente con *n* mensajes posibles, cada uno con probabilidad $p_i$:

<div class="formula-box">

$$H = -\sum_{i=1}^{n} p_i \cdot \log_2(p_i)$$

</div>

- **H** = entropía (en **bits**)
- $p_i$ = probabilidad del mensaje *i*
- $\log_2$ = logaritmo en base 2
- La suma recorre todos los mensajes posibles

---

# Ejemplo 1: La moneda justa

$p(\text{cara}) = 0.5$, $p(\text{sello}) = 0.5$

$H = -[0.5 \cdot \log_2(0.5) + 0.5 \cdot \log_2(0.5)]$

$H = -[0.5 \cdot (-1) + 0.5 \cdot (-1)]$

$H = -[-0.5 - 0.5] = \mathbf{1 \text{ bit}}$

> Confirma la intuición: una moneda justa da **exactamente 1 bit**.

---

# Ejemplo 2: La moneda cargada (90% cara)

$p(\text{cara}) = 0.9$, $p(\text{sello}) = 0.1$

$H = -[0.9 \cdot \log_2(0.9) + 0.1 \cdot \log_2(0.1)]$

$H = -[0.9 \cdot (-0.152) + 0.1 \cdot (-3.322)]$

$H = \mathbf{0.469 \text{ bits}}$

> Menos de 1 bit — porque el resultado es **parcialmente predecible**.

---

# Ejemplo 3: El dado justo

6 resultados equiprobables: $p_i = 1/6$

$H = -6 \cdot \left[\frac{1}{6} \cdot \log_2\left(\frac{1}{6}\right)\right] = \mathbf{2.585 \text{ bits}}$

Entre 2 bits (4 opciones) y 3 bits (8 opciones).

Tiene sentido: 6 posibilidades están entre 4 y 8.

---

# Tres propiedades de H

**1.** H es **máxima** cuando todos los resultados son equiprobables.
Para *n* resultados equiprobables: $H = \log_2(n)$

**2.** H **disminuye** cuando algunos resultados son más probables.
Si ya podemos predecir → menos sorpresa → menos información.

**3.** $H = 0$ solo cuando el resultado es **seguro** (probabilidad = 1).
No hay información si no hay sorpresa.

---

<!-- _class: invert -->

# La conexión ecológica
## H' de Shannon = Entropía de Shannon

---

# El índice de diversidad de Shannon

En ecología, la diversidad de especies se mide con:

<div class="formula-box">

$$H' = -\sum_{i=1}^{S} p_i \cdot \ln(p_i)$$

</div>

Donde $p_i$ = proporción de individuos de la especie *i*.

💬 *¿Les resulta familiar esta fórmula?*

---

# Son la misma fórmula

| | Entropía de Shannon | Diversidad ecológica H' |
|---|---|---|
| **Fórmula** | $H = -\sum p_i \log_2(p_i)$ | $H' = -\sum p_i \ln(p_i)$ |
| **Diferencia** | Logaritmo base 2 | Logaritmo natural |
| **Unidad** | Bits | Nats |
| **Mide** | Incertidumbre informacional | Incertidumbre ecológica |

La estructura lógica es **idéntica**. Solo cambia la base del logaritmo (y por tanto la unidad).

> **No es coincidencia.** Ambas miden la misma cosa: incertidumbre.

---

## En términos de teoría de informacion diremos que:

- *1 nat* $\approx$ información ganada cuando la incerteza es reducida por un factor de $e \approx 2.718$
- *1 bit* = reducción de la incerteza por un factor de 2

Esto hace que:
1 nat = $log_⁡2 (e) \approx 1.443$  bits, y
1 bit = $ln(2) \approx 0.693$ nats}$


### Clarificación importante (confusión común)
🔹 Nats **no es** una unidad ecológica
🔹 No significa *"número de especies"*
> solo cuantifica incerteza / información, no riqueza.

---

# Ejemplo ecológico

**Sitio A:** 100 individuos → 50 especies X, 50 especies Y
**Sitio B:** 100 individuos → 95 especies X, 5 especies Y

**Sitio A:** $H' = -[0.5 \cdot \ln(0.5) + 0.5 \cdot \ln(0.5)] = \mathbf{0.693}$ nats

**Sitio B:** $H' = -[0.95 \cdot \ln(0.95) + 0.05 \cdot \ln(0.05)] = \mathbf{0.199}$ nats

> Sitio A → alta diversidad → difícil predecir qué especie encuentro
> Sitio B → baja diversidad → casi seguro será especie X

**La diversidad ecológica ES la incertidumbre informacional.**

---

# Relaciones conceptuales

| Teoría de la información | Ecología |
|---|---|
| Mensaje | Individuo observado |
| Mensajes posibles | Conjunto de especies |
| Probabilidad $p_i$ | Proporción de la especie |
| Alta entropía | Alta diversidad |
| Baja entropía | Dominancia de una especie |

> Un ecosistema diverso es uno que **"sorprende más"**.

---

<!-- _class: invert -->

# Redundancia y compresión

---

# Redundancia

Si una fuente tiene baja entropía, parte de su contenido es **predecible**.

Esa parte predecible es **redundancia**.

💬 *"En español, después de la Q casi siempre viene una U. ¿La U aporta información?"*

Muy poca — porque es predecible.

> Si eliminamos la U después de Q y el receptor sabe la regla, no se pierde información. **Eso es compresión.**

---

# Compresión: la idea clave

Mensajes frecuentes → **menos bits**
Mensajes raros → **más bits**

| Especie | Frecuencia | Código fijo | Código variable |
|---|---|---|---|
| Especie A | 70% | 00 (2 bits) | 0 (1 bit) |
| Especie B | 15% | 01 (2 bits) | 10 (2 bits) |
| Especie C | 10% | 10 (2 bits) | 110 (3 bits) |
| Especie D | 5% | 11 (2 bits) | 111 (3 bits) |

**Promedio fijo:** siempre 2 bits
**Promedio variable:** 0.7×1 + 0.15×2 + 0.1×3 + 0.05×3 = **1.45 bits**

**Ahorro: 27.5%.** Shannon demostró que el **límite** de compresión es exactamente H.

---

<!-- _class: invert -->

# Canales y ruido

---

# El teorema de Shannon

*"¿Se puede transmitir información sin errores por un canal con ruido?"*

**Sí** — si la tasa de transmisión es menor que la **capacidad del canal** C.

> **Analogía ecológica:** una parcela de muestreo es un "canal". El ruido = error de observación. Si el protocolo es suficientemente redundante (réplicas, verificaciones), el error se elimina. Si se muestrea demasiado rápido → errores inevitables.

---

# Lo que aprendimos hasta aquí

1. **La información se mide en bits.** H cuantifica la incertidumbre promedio.
2. **La misma fórmula mide la diversidad ecológica.** Ambas miden incertidumbre.
3. **La redundancia permite la compresión.** Lo predecible necesita menos bits.

---

<!-- _class: lead -->

# 🧪 Laboratorio analógico
## "Adivina el Animal — 20 Preguntas"

*¿Cuántas preguntas de sí/no necesitan para identificar un animal de la fauna chilena?*

---

<!-- _class: lab -->

# Las reglas

- **16 especies** de fauna chilena (tarjetas)
- Un integrante del grupo es **"el oráculo"** — toma una tarjeta al azar
- Los demás hacen preguntas de **sí o no**
- El oráculo solo responde "sí" o "no"
- **Registrar cada pregunta** y la respuesta en la hoja

---

<!-- _class: lab -->

# Ronda 1 · Estrategia libre (15 min)

Pregunten como quieran. **Sin restricciones.**

Cuando adivinen, anotar:
- El animal
- El número total de preguntas usadas
- Las preguntas que hicieron

Repetir si sobra tiempo (cambiar oráculo).

---

<!-- _class: lab -->

# Análisis intermedio

💬 *¿Cuántas preguntas usó cada grupo?*

Hay 16 animales equiprobables.
$H = \log_2(16) = \mathbf{4 \text{ bits}}$

→ Con la **estrategia perfecta**, bastan **4 preguntas**.

Cada pregunta bien hecha elimina exactamente **la mitad** de las opciones.

Eso se llama **búsqueda binaria**.

---

<!-- _class: lab -->

# La estrategia óptima

Cada pregunta debe **dividir el conjunto en dos mitades iguales**:

1. "¿Es un mamífero?" → elimina ~mitad
2. "¿Vive en el bosque?" → elimina ~mitad de lo que queda
3. "¿Es carnívoro?" → elimina ~mitad
4. Pregunta final → identifica al animal

> **Cada pregunta bien hecha vale exactamente 1 bit.**

---

<!-- _class: lab -->

# Ronda 2 · Búsqueda binaria (15 min)

Ahora intenten **conscientemente** hacer preguntas que dividan a la mitad.

Antes de cada pregunta piensen:
*"¿Cuántos animales descarta un 'sí'? ¿Y un 'no'?"*

**La pregunta ideal descarta la mitad.**

Anotar el número de preguntas. Comparar con la Ronda 1.

---

<!-- _class: lab -->

# Ronda 3 · Distribución desigual (10 min)

Ahora el oráculo usa un **dado** para elegir:

| Dado | Animal | Probabilidad |
|---|---|---|
| 1, 2, 3 | Pudú | 50% |
| 4, 5 | Cóndor | 33% |
| 6 | Puma | 17% |

💬 *¿Cuántas preguntas necesitarán ahora?*

$H = -[0.5 \cdot \log_2(0.5) + 0.33 \cdot \log_2(0.33) + 0.17 \cdot \log_2(0.17)]$
$H \approx \mathbf{1.46 \text{ bits}}$

Menos de 2 preguntas en promedio.

---

<!-- _class: invert -->

# Discusión plenaria

---

<!-- _class: pregunta -->

# ¿Cuántas preguntas usaron en la Ronda 1 vs. la Ronda 2?

*La estrategia importa. Preguntas que eliminan la mitad son más eficientes.*

---

<!-- _class: pregunta -->

# ¿Por qué 4 preguntas es el mínimo para 16 animales?

*Porque $\log_2(16) = 4$. Cada pregunta aporta máximo 1 bit. Se necesitan 4 bits para distinguir entre 16 opciones.*

---

<!-- _class: pregunta -->

# ¿Por qué en la Ronda 3 necesitaron menos preguntas?

*Menos incertidumbre = menos entropía. La distribución desigual hace que algunos resultados sean predecibles.*

*Es el mismo motivo por el que H' baja cuando una especie domina un ecosistema.*

---

<!-- _class: pregunta -->

# ¿Qué tiene que ver con la compresión de datos?

*Si un evento es predecible (como el pudú en la Ronda 3), necesita menos bits para transmitirlo. Esa es la base de JPEG, MP3, ZIP: dedicar menos bits a lo frecuente.*

---

# Lo que aprendimos hoy

- **Información** = reducción de incertidumbre. No es lo mismo que "datos".
- La **entropía** de Shannon mide la sorpresa promedio de una fuente.
- La **diversidad ecológica H'** es la misma fórmula — mide la misma cosa.
- La **búsqueda binaria** es la estrategia óptima de preguntas (1 bit por pregunta).
- La **compresión** aprovecha la baja entropía: lo predecible necesita menos bits.

---

# Próxima semana

## Semana 4 · Pensamiento algorítmico
### Recetas para resolver problemas

*¿Qué es un algoritmo? ¿Cómo se mide la dificultad de un problema? La búsqueda binaria de hoy reaparece como un algoritmo fundamental.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 3 · Teoría de la información: midiendo la sorpresa*
