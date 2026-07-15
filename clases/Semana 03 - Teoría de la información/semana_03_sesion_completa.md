# Semana 3: Teoría de la información — Midiendo la sorpresa

## Guía completa de la sesión

---

## Visión general

|                           |                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Duración total**        | 3 horas (2 h cátedra + 1 h laboratorio analógico)                                                                                                                                                                                               |
| **Objetivo central**      | Que los estudiantes comprendan que la información se puede medir, que la sorpresa es cuantificable, y que la fórmula de Shannon es la misma que ya conocen (o conocerán) como índice de diversidad en ecología                                  |
| **Idea ancla**            | La información no es lo mismo que los datos. Información es lo que *reduce la incertidumbre*. Cuanta más sorpresa produce un mensaje, más información contiene                                                                                  |
| **Prerrequisito**         | Semana 2 (bits, binario, codificación)                                                                                                                                                                                                          |
| **Materiales**            | Proyector, pizarra, dados de 6 caras (6 dados, uno por grupo), monedas, tarjetas de fauna chilena (impresas), hojas de registro para el laboratorio, calculadoras simples (o celulares en modo calculadora)                                     |
| **Conexión con Semana 2** | La semana pasada vimos que cada carácter cuesta 8 bits. ¿Se puede ser más eficiente? ¿Hay letras que necesiten menos bits que otras? Hoy respondemos: sí, y la teoría de la información nos dice exactamente cuántos bits necesita cada mensaje |

---

## PARTE 1: CÁTEDRA (120 minutos)

---

### Bloque A — Apertura: la moneda, el dado y la sorpresa (20 min)

#### Experimento 1: La moneda (5 min)

Sacar una moneda. Preguntar al curso:

*"Voy a lanzar esta moneda. ¿Cuánta información me da el resultado?"*

- Hay 2 resultados posibles, equiprobables.
- Antes del lanzamiento: incertidumbre total (50/50).
- Después: la incertidumbre se resuelve completamente.
- **El resultado contiene exactamente 1 bit de información.**

¿Por qué 1 bit? Porque se necesita una sola pregunta de sí/no para determinarlo: "¿Es cara?"

#### Experimento 2: El dado (5 min)

Sacar un dado de 6 caras.

*"¿Cuánta información da el resultado de un dado?"*

- 6 resultados posibles, equiprobables.
- Se necesitan más preguntas para adivinarlo: "¿Es mayor que 3?" → "¿Es mayor que 5?" → "¿Es 4?" ...
- **Más posibilidades = más incertidumbre = más información al resolverla.**

Intuición: el dado "sorprende más" que la moneda, porque hay más resultados posibles.

#### Experimento 3: El dado cargado (10 min)

*"¿Y si el dado está cargado — sale 6 el 90% de las veces?"*

- Si lanzo y sale 6: poca sorpresa → poca información.
- Si lanzo y sale 1: mucha sorpresa → mucha información.
- **Los eventos raros son más informativos que los eventos comunes.**

Preguntar al curso: *"Si un colega les dice 'hoy salió el sol en Atacama', ¿es informativo?"* → No, es obvio. *"¿Y si les dice 'hoy nevó en Valdivia'?"* → Muy informativo. La diferencia es la probabilidad del evento.

**Transición:** *"¿Se puede medir esto con una fórmula? Sí. Y la inventó un ingeniero llamado Claude Shannon en 1948."*

---

### Bloque B — Shannon y la teoría de la información (30 min)

#### Claude Shannon: el contexto histórico (5 min)

- 1948: Shannon publica "A Mathematical Theory of Communication" en los laboratorios Bell.
- Problema práctico: ¿cuántos bits por segundo necesita un cable telefónico para transmitir una conversación sin perder información?
- Shannon inventó una forma de medir la **cantidad de información** de cualquier fuente.
- De paso, inventó la palabra **"bit"** como unidad de información.

#### La fórmula de Shannon (15 min)

Para una fuente con $n$ posibles mensajes, cada uno con probabilidad $p_i$:

**$$H = − \sum p_i · log_2(p_i)$$**

Donde:
- $H$ = entropía (medida en **bits**)
- $p_i$ = probabilidad del mensaje $i$
- $log_2$ = logaritmo en base 2
- La suma recorre todos los mensajes posibles

**Ejemplo 1: La moneda**

Dos resultados: $p(cara) = 1/2 = 0.5$, $p(sello) = 1/2 = 0.5$

$$H = −[0.5 · log_2(0.5) + 0.5 · log_2(0.5)]$$
$$H = −[0.5 · (−1) + 0.5 · (−1)]$$
$$H = −[−0.5 − 0.5]$$
$$H = \mathbf{1 bit}$$

Confirma la intuición de que una moneda 'justa' da exactamente 1 bit de información.

**Ejemplo 2: La moneda cargada (90% cara)**

$p(cara) = 0.9$, $p(sello) = 0.1$

$$H = −[0.9 · log₂(0.9) + 0.1 · log₂(0.1)]$$
$$H = −[0.9 · (−0.152) + 0.1 · (−3.322)]$$
$$H = −[−0.137 − 0.332]$$
$$H = \mathbf{0.469 bits}$$

Menos de 1 bit — porque el resultado es parcialmente predecible. Si ya sé que "casi siempre es cara", el resultado me sorprende menos → contiene menos información.

**Ejemplo 3: El dado 'justo'**

Hay 6 resultados igual de probables: $p_i = 1/6$ para todo $i$.

$$H = −6 · [1/6 · log₂(1/6)]$$
$$H = −6 · [1/6 · (−2.585)]$$
$$H = \mathbf{2.585 bits}$$

Más de 1 bit, pero menos de 3 (que serían 8 resultados equiprobables). Tiene sentido: 6 posibilidades están entre 4 (2 bits) y 8 (3 bits).

#### La intuición fundamental (10 min)

Tres propiedades de H:

1. **H es máxima cuando todos los resultados son equiprobables.** La máxima incertidumbre = la máxima información posible. Para n resultados equiprobables: H = log₂(n).

2. **H disminuye cuando algunos resultados son mucho más probables que otros.** Si ya podemos predecir el resultado, la fuente es menos informativa.

3. **H = 0 solo cuando el resultado es seguro** (un evento con probabilidad 1). No hay información si no hay sorpresa.

**Dibujar en la pizarra** el gráfico de H vs. p para la moneda (una parábola invertida con máximo en p = 0.5).

---

### Bloque C — La conexión ecológica: H' de Shannon (20 min)

#### El índice de diversidad de Shannon (10 min)

En ecología, la diversidad de especies se mide con:
$$H' = − \sum pᵢ · ln(p_i)$$

Donde $p_i =$ proporción de individuos de la especie $i$.

*"¿Les resulta familiar esta fórmula?"*

Es **la misma fórmula de Shannon**, con una sola diferencia: usa logaritmo natural ($ln$) en vez de $log_2$. El cambio de base solo cambia la unidad de medida (nats en vez de bits), pero la estructura lógica es idéntica.

**Esto no es coincidencia.** Shannon se inspiró en la termodinámica (donde la entropía mide desorden), y los ecólogos adoptaron su fórmula porque mide exactamente lo que necesitan: la incertidumbre sobre qué especie encontraré si tomo un individuo al azar.

#### Ejemplo ecológico concreto (10 min)

**Sitio A:** 100 individuos $\rightarrow$ 50 especie X, 50 especie Y

**Sitio B:** 100 individuos $\rightarrow$ 95 especie X, 5 especie Y

Calcular H' para cada sitio (en la pizarra, con el curso):

**Sitio A:**
$$H' = −[0.5 · ln(0.5) + 0.5 · ln(0.5)]$$
$$H' = −[0.5 · (−0.693) + 0.5 · (−0.693)]$$
$$H' = \mathbf{0.693 nats}$$

**Sitio B:**
$$H' = −[0.95 · ln(0.95) + 0.05 · ln(0.05)]$$
$$H' = −[0.95 · (−0.051) + 0.05 · (−2.996)]$$
$$H' = −[−0.049 − 0.150]$$
$$H' = \mathbf{0.199 nats}$$

**Interpretación:**
- Sitio A tiene mayor diversidad (H' más alto) $\rightarrow$ si tomo un individuo al azar, es más difícil predecir su especie.
- Sitio B tiene baja diversidad (H' bajo) $\rightarrow$ si tomo un individuo al azar,es casi seguro que será especie X.
- **La diversidad ecológica ES la incertidumbre informacional.** Un ecosistema diverso es uno que "sorprende más".

#### El puente conceptual (resumen en la pizarra)

| Teoría de la información            | Ecología                                      |
|-------------------------------------|-----------------------------------------------|
| Mensaje                             | Individuo observado                           |
| Conjunto de mensajes posibles       | Conjunto de especies                          |
| Probabilidad del mensaje pᵢ         | Proporción de la especie pᵢ                   |
| Entropía H (bits)                   | Diversidad H' (nats)                          |
| Alta entropía → mucha incertidumbre | Alta diversidad → difícil predecir la especie |
| Baja entropía → mensaje predecible  | Baja diversidad → dominancia de una especie   |

---

### Bloque D — Redundancia y compresión (20 min)

#### Redundancia (10 min)

Si una fuente tiene baja entropía, parte de su contenido es **predecible** $\rightarrow$ es redundante.a parte predecible es **redundancia**.

**Ejemplo con texto:**

*"En español, después de la letra Q casi siempre viene una U. ¿La U aporta información?"*

Muy poca — porque es predecible. Si eliminamos la U después de Q y el receptor sabe la regla, no se pierde información. Eso es compresión.

**Datos sobre la redundancia del español:**
- La letra E aparece ~13% de las veces; la W aparece ~0.01%.
- Si todas las letras fueran equiprobables (27 letras + espacio), H sería log₂(28) ≈ 4.81 bits por carácter.
- Pero la entropía real del español es ~4.0 bits por carácter (hay redundancia).
- La entropía baja aún más si consideramos pares de letras (bigramas) o palabras completas.

#### Compresión (10 min)

**Idea:** si los mensajes frecuentes se codifican con menos bits y los raros con más bits, el promedio baja.

**Ejemplo intuitivo:**

| Especie   | Frecuencia | Código fijo (2 bits) | Código variable |
|-----------|------------|----------------------|-----------------|
| Especie A | 70%        | 00                   | 0 (1 bit)       |
| Especie B | 15%        | 01                   | 10 (2 bits)     |
| Especie C | 10%        | 10                   | 110 (3 bits)    |
| Especie D | 5%         | 11                   | 111 (3 bits)    |

**Promedio con código fijo:** siempre 2 bits.
**Promedio con código variable:** 0.7×1 + 0.15×2 + 0.10×3 + 0.05×3 = 0.7 + 0.3 + 0.3 + 0.15 = **1.45 bits**.

**Ahorro: 27.5%.** Y Shannon demostró que el límite teórico de compresión es exactamente H — no se puede comprimir más que la entropía sin perder información.

**Aplicación práctica:** JPEG, MP3, ZIP usan variantes de esta idea. Y en bioinformática, las secuencias genómicas se comprimen aprovechando que ciertas combinaciones de bases son mucho más frecuentes que otras.

---

### Bloque E — Capacidad de canal y ruido (15 min)

#### La idea (10 min)

Shannon también respondió otra pregunta: *"¿Se puede transmitir información sin errores por un canal con ruido?"*

- **Canal:** cualquier medio de transmisión (cable, aire, fibra óptica).
- **Ruido:** interferencias que pueden alterar los bits.
- **Teorema de Shannon:** todo canal tiene una **capacidad máxima** (C, en bits/segundo). Si se transmite a una tasa menor que C, se pueden corregir todos los errores. Si se transmite más rápido que C, los errores son inevitables.

**Analogía ecológica:** Piensen en una parcela de muestreo como un "canal". El ruido es el error de observación (identificación errónea, individuos que se esconden, doble conteo). Shannon dice que si el protocolo de muestreo es suficientemente redundante (repeticiones, verificaciones), se puede eliminar el error. Pero si se muestrea demasiado rápido (pocas réplicas, poco tiempo), el error es inevitable.

#### Códigos correctores de errores (5 min, conceptual)

- La idea más simple: enviar cada bit 3 veces (001 → 000 000 111). Si hay un error en uno, los otros dos lo corrigen por mayoría.
- Esto es ineficiente (triplica el costo), pero la teoría de la información muestra que hay formas mucho más elegantes de hacerlo.
- Internet funciona porque tiene códigos correctores de errores en cada capa del protocolo.

---

### Bloque F — Cierre y puente al laboratorio (15 min)

#### Recapitulación (5 min)

En la pizarra, las tres ideas centrales:

1. **La información se mide en bits.** La entropía H cuantifica la incertidumbre promedio de una fuente.
2. **La misma fórmula mide la diversidad ecológica.** No es coincidencia: ambas miden incertidumbre.
3. **La redundancia permite la compresión.** Los mensajes predecibles necesitan menos bits.

#### Anticipación del laboratorio (10 min)

*"Ahora vamos a jugar a las 20 preguntas — pero con un giro. Van a intentar adivinar un animal de la fauna chilena haciendo solo preguntas de sí/no. Después de cada ronda, van a analizar cuántas preguntas necesitaron y por qué algunas estrategias son mejores que otras. Van a descubrir que la mejor estrategia de preguntas es, en el fondo, una búsqueda binaria."*

---

## PARTE 2: LABORATORIO ANALÓGICO (60 minutos)

## "Adivina el Animal — 20 Preguntas"

---

### Preparación previa (docente)

#### Tarjetas de fauna chilena

Preparar un mazo de **16 tarjetas** con especies de la fauna chilena. Se eligen 16 porque es una potencia de 2 (2⁴), lo que permite un análisis limpio de la entropía.

| N° | Especie               | Clase    | Hábitat          | Dieta               |
|----|-----------------------|----------|------------------|---------------------|
| 1  | Pudú                  | Mamífero | Bosque           | Herbívoro           |
| 2  | Huemul                | Mamífero | Bosque/Montaña   | Herbívoro           |
| 3  | Puma                  | Mamífero | Montaña/Matorral | Carnívoro           |
| 4  | Chungungo             | Mamífero | Costa            | Carnívoro           |
| 5  | Monito del monte      | Mamífero | Bosque           | Omnívoro            |
| 6  | Cóndor                | Ave      | Montaña          | Carroñero           |
| 7  | Carpintero negro      | Ave      | Bosque           | Insectívoro         |
| 8  | Martín pescador       | Ave      | Ríos/Lagos       | Carnívoro           |
| 9  | Pingüino de Humboldt  | Ave      | Costa            | Carnívoro           |
| 10 | Rana de Darwin        | Anfibio  | Bosque           | Insectívoro         |
| 11 | Lagartija de Valdivia | Reptil   | Bosque           | Insectívoro         |
| 12 | Tortuga marina        | Reptil   | Océano           | Omnívoro            |
| 13 | Salmón chinook        | Pez      | Ríos             | Carnívoro (invasor) |
| 14 | Pejerrey              | Pez      | Ríos/Lagos       | Omnívoro            |
| 15 | Araña pollito         | Arácnido | Bosque           | Carnívoro           |
| 16 | Vaquita del campo     | Insecto  | Pradera/Jardín   | Herbívoro           |

**Imprimir:** 6 sets de tarjetas (uno por grupo) + la tabla maestra para proyectar.

#### Materiales por grupo

| Material                       | Cantidad                    |
|--------------------------------|-----------------------------|
| Set de 16 tarjetas de fauna    | 1                           |
| Hoja de registro de preguntas  | 2 por grupo (una por ronda) |
| Calculadora simple (o celular) | 1                           |

---

### Desarrollo de la actividad

#### Fase 1 — Ronda libre: estrategia espontánea (15 min)

**Reglas:**
- Un integrante del grupo ("el oráculo") toma una tarjeta al azar sin mostrarla.
- Los demás hacen preguntas de **sí o no** para adivinar el animal.
- El oráculo solo responde "sí" o "no".
- **Registrar cada pregunta** en la hoja de registro (columna: pregunta textual + respuesta).
- Contar cuántas preguntas se necesitaron.

**Instrucción clave:** *"No se les dice ninguna estrategia. Pregunten como quieran."*

**Después de adivinar:** anotar el total de preguntas usadas. Repetir con otro oráculo y otra tarjeta si sobra tiempo.

**Observación esperada:** la mayoría de los grupos usará una estrategia ineficiente (preguntas del tipo "¿Es el pudú?" "¿Es el cóndor?"), lo que puede tomar 8–15 preguntas.

#### Fase 2 — Análisis intermedio (10 min)

Proyectar los resultados: *"¿Cuántas preguntas usó cada grupo?"*

Anotar en la pizarra. Luego preguntar:

*"¿Cuántas preguntas serían necesarias si usaran la mejor estrategia posible?"*

Ayudar al curso a razonar:
- Hay 16 animales, equiprobables.
- $H = log_2(16)$ = **4 bits** → 4 preguntas de sí/no deberían bastar si cada una elimina exactamente la mitad de las posibilidades.
- **La estrategia óptima es una búsqueda binaria:** cada pregunta divide el conjunto en dos mitades iguales.

Ejemplo de estrategia óptima:
1. "¿Es un mamífero?" (elimina ~mitad)
2. "¿Vive en bosque?" (elimina ~mitad del restante)
3. "¿Es carnívoro?" (elimina ~mitad)
4. "¿Tiene más de 1 kg?" (identifica al animal)

*"Cada pregunta bien hecha vale exactamente 1 bit de información."*

#### Fase 3 — Ronda estratégica: búsqueda binaria (15 min)

**Reglas:** las mismas que la Ronda 1, pero ahora los grupos deben **intentar conscientemente** usar preguntas que dividan el conjunto a la mitad.

**Instrucción:** *"Antes de hacer cada pregunta, piensen: ¿cuántos animales descartaría un 'sí'? ¿Y un 'no'? La pregunta ideal descarta la mitad."*

Repetir 2 veces (cambiar oráculo y tarjeta). Registrar el número de preguntas.

**Observación esperada:** los grupos deberían bajar a 4–6 preguntas. Probablemente no lleguen a 4 exactamente porque las categorías no se dividen en mitades perfectas (ej: hay 5 mamíferos y 4 aves, no 8 y 8). Esa imperfección es pedagógicamente valiosa.

#### Fase 4 — Ronda con distribución desigual (10 min)

**Cambio:** ahora el oráculo no toma una tarjeta al azar. En su lugar, usa un **dado** para seleccionar:

| Resultado del dado | Animal (probabilidad) |
|--------------------|-----------------------|
| 1, 2, 3 (50%)      | Pudú                  |
| 4, 5 (33%)         | Cóndor                |
| 6 (17%)            | Puma                  |

Solo 3 animales posibles, pero con probabilidades desiguales.

**Pregunta antes de jugar:** *"¿Cuántas preguntas creen que necesitarán ahora?"*

Calcular la entropía juntos:
H = −[0.5 · log₂(0.5) + 0.33 · log₂(0.33) + 0.17 · log₂(0.17)]
H = −[0.5·(−1) + 0.33·(−1.60) + 0.17·(−2.56)]
H = −[−0.5 − 0.528 − 0.435]
H ≈ **1.46 bits**

Menos de 2 preguntas en promedio — porque la distribución no es uniforme. Si preguntan primero "¿Es el pudú?", la mitad de las veces terminan con 1 sola pregunta.

**Conexión ecológica:** *"Esto es exactamente lo que mide H' de Shannon en ecología. Un ecosistema donde una especie domina (como el sitio B de la clase) tiene baja entropía — es fácil predecir qué especie vas a encontrar."*

#### Fase 5 — Discusión plenaria (10 min)

**Preguntas guía:**

1. *"¿Cuántas preguntas usaron en la Ronda 1 vs. la Ronda 2?"*
→ La estrategia importa. Preguntas que eliminan la mitad son más eficientes.

2. *"¿Por qué 4 preguntas es el mínimo teórico para 16 animales?"*
→ Porque $log_2(16) = 4$. Cada pregunta aporta máximo 1 bit. Se necesitan 4 bits para distinguir entre 16 opciones.

3. *"¿Por qué en la Ronda 3 necesitaron menos preguntas, aunque el juego era 'más fácil'?"*
→ Porque había menos incertidumbre (menos entropía). La distribución desigual hace que algunos resultados sean predecibles.

4. *"¿Qué tiene que ver esto con la conservación?"*
→ El H' de Shannon les dice cuánta "sorpresa" tiene un ecosistema. Un ecosistema saludable suele tener alta diversidad (alta entropía). La degradación ambiental a menudo reduce la diversidad (baja la entropía: unas pocas especies dominan).

5. *"¿Qué tiene que ver esto con la compresión de datos?"*
→ Si un evento es predecible (como el pudú en la Ronda 3), necesita menos bits para transmitirlo. Esa es la base de toda compresión de datos: dedicar menos bits a lo frecuente y más a lo raro.

---

## Notas pedagógicas

### El momento "eureka" esperado

El momento más potente de esta clase es cuando los estudiantes ven que la fórmula de Shannon y el índice H' de ecología son **la misma fórmula**. Para muchos será la primera vez que una herramienta matemática que conocen de biología aparece en un contexto completamente diferente (telecomunicaciones). La lección implícita: las matemáticas no son herramientas de un solo uso — las mismas estructuras aparecen en fenómenos muy distintos.

### Manejo del nivel matemático

Estos son estudiantes de primer año recién salidos del colegio. Pueden no estar cómodos con logaritmos. Estrategias:

- **No derivar la fórmula.** Presentarla como hecho y trabajar con ejemplos numéricos.
- **Usar log₂ como "número de preguntas de sí/no":** log₂(16) = 4 porque se necesitan 4 preguntas para distinguir 16 opciones. Esto da una intuición concreta antes de entrar en la fórmula general.
- **Permitir calculadoras** en el laboratorio. El cálculo manual de logaritmos no es el objetivo; la interpretación sí.
- **Si alguien pregunta "¿por qué logaritmo?":** porque la información es aditiva. Si lanzo dos dados independientes, la información total es la suma de las individuales. Solo el logaritmo convierte un producto (de probabilidades) en una suma.

### Errores conceptuales frecuentes

- **"Más datos = más información":** No necesariamente. Si los datos son redundantes (siempre lo mismo), aportan poca información nueva. Distinguir datos de información es un objetivo de esta clase.
- **"La entropía siempre debe ser alta":** Depende del contexto. En compresión, baja entropía es buena (permite comprimir más). En ecología, baja entropía suele indicar degradación. La fórmula es la misma; la interpretación depende del dominio.
- **Confundir entropía de Shannon con la entropía termodinámica:** Están relacionadas conceptualmente (ambas miden "desorden"), pero no son la misma cantidad física. Para primer año, basta con mencionar la conexión sin entrar en termodinámica.

### Conexión con el resto del curso

| Concepto de esta semana         | Dónde se profundiza                                      |
|---------------------------------|----------------------------------------------------------|
| Entropía de Shannon             | Semana 12 (función en Python para calcular H')           |
| Búsqueda binaria                | Semana 4 (algoritmos, complejidad logarítmica)           |
| Compresión                      | Semana 6 (tokenización en LLMs como forma de compresión) |
| H' como medida de diversidad    | Semana 12 (módulo "caja de herramientas ecológicas")     |
| Redundancia en lenguaje natural | Semana 6 (cómo los LLMs predicen la siguiente palabra)   |
