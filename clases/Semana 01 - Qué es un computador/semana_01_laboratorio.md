

<style scoped>section{font-size:22px;}</style>
# LABORATORIO ANALÓGICO (60 minutos) "El Computador Humano"

### Preparación previa (docente)

#### Materiales por grupo (5 personas)

- 1 sobre con **tarjetas de instrucciones** en blanco (cartulina blanca, ~10 tarjetas tamaño media carta)
- 1 set de **tarjetas de rol** (5 tarjetas de colores diferentes, ver abajo)
- 1 **hoja de memoria** (tabla impresa con 10 celdas numeradas, simulando registros de memoria)
- 1 marcador
- 1 hoja en blanco para la salida (pantalla)
- 1 dado de 6 caras (para la ronda avanzada, opcional)

#### Tarjetas de rol

Imprimir en cartulinas de colores distintos. Cada tarjeta lleva el nombre del rol en grande y las reglas en el reverso.

---

**🟦 PROGRAMADOR/A**

> Eres quien diseña la solución. Escribes instrucciones en las tarjetas en blanco, **una instrucción por tarjeta**, y las pasas a la Unidad de Control en orden. NO puedes hablar con los demás componentes una vez que el programa comienza a ejecutarse. Si algo sale mal, solo puedes observar.

**Reglas:**
- Cada tarjeta debe contener UNA sola instrucción.
- Usa solo las operaciones permitidas (ver lista de instrucciones).
- Numera cada tarjeta en la esquina superior derecha.
- Una vez entregadas las tarjetas, no puedes modificarlas.

---

**🟩 UNIDAD DE CONTROL**

> Eres el director de orquesta. Lees las tarjetas de instrucción una por una, en orden, y le dices al componente correspondiente qué hacer. NO haces cálculos ni almacenas datos — solo coordinas.

**Reglas:**
- Lee las tarjetas en orden numérico, una a la vez.
- Indica en voz alta qué componente debe actuar y qué debe hacer.
- Si una instrucción es ambigua, di "ERROR: instrucción no clara" y detén la ejecución.
- Si una instrucción pide leer una celda de memoria vacía, di "ERROR: dato no encontrado".

---

**🟨 ALU (Unidad Aritmético-Lógica)**

> Eres la calculadora. Solo sabes hacer operaciones aritméticas (+, −, ×, ÷) y comparaciones (>, <, =). Recibes dos números, operas, y devuelves el resultado a quien te lo pida.

**Reglas:**
- Solo actúas cuando la Unidad de Control te lo indica.
- Solo puedes operar con los números que te entregan en ese momento.
- No recuerdas resultados anteriores (no tienes memoria propia).
- Di el resultado en voz alta.

---

**🟧 MEMORIA**

> Eres el almacén temporal. Tienes una hoja con 10 celdas numeradas (0–9). Guardas y entregas datos cuando la Unidad de Control te lo pide.

**Reglas:**
- Solo actúas cuando la Unidad de Control te lo indica.
- GUARDAR: escribe el valor en la celda indicada (borra lo que había antes).
- LEER: di en voz alta el valor almacenado en la celda indicada.
- Si te piden leer una celda vacía, di "celda vacía".

---

**🟥 ENTRADA/SALIDA (E/S)**

> Eres la conexión con el mundo exterior. **Entrada:** le das datos al sistema cuando te los piden (los lees de la "hoja de datos de entrada" que te entrega el docente). **Salida:** escribes el resultado final en la hoja en blanco (la "pantalla").

**Reglas:**
- Solo actúas cuando la Unidad de Control te lo indica.
- LEER ENTRADA: di en voz alta el siguiente dato de la hoja de entrada.
- ESCRIBIR SALIDA: escribe el valor indicado en la hoja de pantalla.
- No interpretas los datos, solo los transmites.

---


<style scoped>section{font-size:24px;}</style>
### Lista de instrucciones permitidas

Proyectar o imprimir para cada grupo:

| Instrucción | Significado | Ejemplo |
|---|---|---|
| `LEER_ENTRADA → celda X` | Tomar el siguiente dato de entrada y guardarlo en la celda X de memoria | `LEER_ENTRADA → celda 0` |
| `GUARDAR valor → celda X` | Guardar un valor fijo en la celda X | `GUARDAR 3 → celda 5` |
| `LEER celda X` | Leer y anunciar el contenido de la celda X | `LEER celda 0` |
| `OPERAR celda X ○ celda Y → celda Z` | Tomar los valores de las celdas X e Y, aplicar la operación ○ (+, −, ×, ÷), guardar resultado en celda Z | `OPERAR celda 0 + celda 1 → celda 2` |
| `ESCRIBIR_SALIDA celda X` | Escribir el valor de la celda X en la pantalla de salida | `ESCRIBIR_SALIDA celda 2` |
