---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  :root {
    --color-bg:      #091926;
    --color-elime:   #DEFF9A;
    --color-accent:  #5DD9E8;
    --color-mid:     #00B4CC;
    --color-dark:    #495f71;
    --color-light:   #6199ac;
    --color-muted:   #7CA9BA;
    --color-white:   #e1ebee;
    --color-warn:    #E05B3A;
    --font-head:     'Georgia', serif;
    --font-body:     'Trebuchet MS', sans-serif;
  }

  section {
    font-family: var(--font-body);
    font-size: 32px;
    line-height: 1.45;
    padding: 40px 60px;
    background-color: var(--color-bg);
    color: var(--color-white);
  }

  section a { color: var(--color-accent); text-decoration: underline; text-underline-offset: 6px; text-decoration-thickness: 3px; font-weight: bold; }
  section h1, section h2, section h3 { font-family: var(--font-head); margin-top: 0; }
  section h1 { color: var(--color-elime); font-size: 1.7em; border-bottom: 4px solid var(--color-mid); padding-bottom: 8px; margin-bottom: 20px; }
  section h2 { color: var(--color-accent); font-size: 1.3em; margin-bottom: 12px; font-weight: 700; }
  section h3 { color: var(--color-light); font-size: 1.1em; }
  section strong { color: var(--color-elime); font-weight: 800; }
  section em { color: var(--color-muted); }
  section li { margin-bottom: 8px; }
  section ul, section ol { margin: 8px 0 12px 30px; }
  section p { margin-bottom: 12px; }

  section.lead {
    text-align: center; display: flex; flex-direction: column; justify-content: center;
    border: 12px solid var(--color-mid);
  }
  section.lead h1 { color: var(--color-elime); font-size: 2.4em; border-bottom: none; }
  section.lead h2 { color: var(--color-accent); font-size: 1.4em; font-style: italic; }
  section.lead p { color: var(--color-white); opacity: 0.8; }

  section.invert {
    background-color: var(--color-white); color: var(--color-bg);
  }
  section.invert h1 { color: var(--color-bg); border-bottom-color: var(--color-mid); }
  section.invert h2 { color: var(--color-dark); }
  section.invert strong { color: var(--color-warn); }

  section.pregunta {
    background-color: var(--color-mid); color: var(--color-bg);
    text-align: center; justify-content: center;
  }
  section.pregunta h1 { color: var(--color-elime); border-bottom: none; font-size: 1.6em; }
  section.pregunta h2 { color: var(--color-bg); border-bottom: none; font-size: 1.4em; }
  section.pregunta p { font-weight: bold; font-size: 1.2em; }
  section.pregunta pre,
  section.pregunta code { text-align: left; }
  section.lab {
    border-left: 15px solid var(--color-warn);
  }
  section.lab h1 { color: var(--color-warn); border-bottom-color: var(--color-dark); }
  section.lab h2 { color: var(--color-accent); }

  table { font-size: 0.8em; width: 100%; border-collapse: collapse; margin: 15px 0; }
  thead th { background-color: var(--color-dark); color: var(--color-elime); padding: 10px; text-align: left; }
  td { padding: 10px; border: 1px solid var(--color-dark); }
  tbody tr:nth-child(even) td { background-color: rgba(255,255,255,0.05); }

  blockquote {
    background-color: rgba(255,255,255,0.05);
    border-left: 6px solid var(--color-elime);
    padding: 15px 25px;
    font-style: italic;
    color: var(--color-accent);
  }
  blockquote p { color: var(--color-accent); margin: 0; }
  section.pregunta blockquote { background-color: rgba(0,0,0,0.15); border-left-color: var(--color-elime); color: var(--color-bg); }
  section.pregunta blockquote p { color: var(--color-bg); }

  pre { background-color: #000; border: 1px solid var(--color-dark); padding: 15px; border-radius: 6px; color: var(--color-accent); font-size: 0.72em; }
  code { background-color: var(--color-dark); color: var(--color-elime); padding: 2px 6px; border-radius: 4px; font-family: 'Consolas', monospace; }

  .img-placeholder {
    background-color: rgba(255,255,255,0.05); border: 2px dashed var(--color-dark); border-radius: 8px;
    padding: 14px; text-align: center; color: var(--color-muted); font-style: italic; font-size: 0.7em; margin: 8px 0;
  }
  section::after { color: var(--color-dark); font-size: 0.65em; }

footer: "Semana 08 · Laboratorio: Primeros pasos en Python · Sección 2"



---
<style scoped>{font-size: 2.6em;}</style>
<!-- _footer : "" -->
<!-- _class: lead -->

# 🧪 Laboratorio
## Notebook en Google Colab


---
<style scoped>{font-size: 2.6em;}</style>
<!-- _footer : "" -->
<!-- _class: invert -->

# 🧪 Laboratorio
## Trabajaremos en ![w:100px](./GColab_icon.png)

<div class='card'>

**Primero:** Necesitas una cuenta en Google

**Segundo:** abrir colab
https://colab.research.google.com/


**Tercero:** Descargar archivo desde *SIVEDUC*
[`semana_08_primer_notebook.ipynb`](https://siveducmd.uach.cl/mod/resource/view.php?id=1098055)

**Cuarto:**  Guardar una copia en *Google Drive*
</div>

---

<!-- _class: lab -->

# Ejercicio 1 · Inventario forestal

Creen variables para un árbol del bosque valdiviano:

- Especie: `"Eucryphia cordifolia"`
- DAP: `45.3` cm
- Altura: `22.1` m
- ¿Nativa?: `True`
- Parcela: `3`

Muestren el **tipo** de cada variable con `type()`.

---

<!-- _class: lab -->

# Ejercicio 2 · Cálculos forestales

Con los datos del Ejercicio 1, calculen:

**Área basal** del árbol:
`π × (DAP/2)² / 10000` (DAP en cm → resultado en m²)

```python
import math
area_basal = math.pi * (dap_cm / 2) ** 2 / 10000
```

**Relación altura/diámetro:**
`altura_m / (dap_cm / 100)`

Muestren con f-strings y 2 decimales.

---

<!-- _class: lab -->

# Ejercicio 3 · Entrada interactiva

Pidan al usuario:
- Nombre del sitio
- Número de individuos
- Número de especies

Calculen la **razón individuos/especie** y muestren un reporte con f-strings.

---

<!-- _class: lab -->

# Ejercicio 4 · Conexión con la Semana 2

```python
palabra = "PUDU"

for letra in palabra:
    codigo = ord(letra)
    binario = bin(codigo)
    print(f"{letra} → ASCII {codigo} → {binario}")
```

¿Cuántos **bits** necesita `"PUDU"` en ASCII?

*(4 caracteres × 8 bits = 32 bits)*

---
<style scoped>{font-size: 2.1em;}</style>

<!-- _class: lab -->

# Ejercicio 5 (Desafío) · Computador Humano: Ronda 2

Reproduzcan la Ronda 2 de la Semana 1:

| Especie | Individuos |
|---|---|
| *N. dombeyi* | 45 |
| *D. winteri* | 28 |
| *A. luma* | 67 |

Calculen: total, abundancia relativa de cada especie, y (**bonus**) el índice de Shannon H'.

```python
import math
# H' = -Σ(pi × ln(pi))
```

---

# Errores: son normales

Los errores más comunes hoy:

| Error | Causa | Solución |
|---|---|---|
| `NameError` | Variable no definida | ¿Ejecutaron la celda anterior? |
| `TypeError` | Operar `str` con `int` | Usar f-string o `int()` / `str()` |
| `IndentationError` | Sangría incorrecta | Verificar espacios después de `:` |
| `SyntaxError` | Falta `:`, paréntesis sin cerrar | Leer el mensaje — Python señala la línea |

> Los programadores profesionales pasan **la mitad del tiempo** leyendo errores. Si les aparece uno, están programando.

---

# Lo que aprendimos hoy

- **Variables** = celdas de memoria con nombre (Sem. 1 → `x = 42`)
- **Tipos** = cómo Python interpreta los bits (Sem. 2 → `int`, `float`, `str`, `bool`)
- **Operaciones** = la ALU (Sem. 1 → `+`, `-`, `*`, `/`, `**`)
- **Entrada/salida** = `input()` y `print()` con f-strings
- **Todo lo nuevo es cosmético** — la lógica ya la conocían

---

# Próxima semana

## Semana 9 · Colecciones: listas y diccionarios

*Una variable guarda un dato. ¿Y si necesitan guardar los datos de 100 especies? No van a crear 100 variables — van a crear una lista.*

*Y si necesitan asociar cada especie con su abundancia, van a usar un diccionario — que es exactamente la tabla de frecuencias de la Semana 3.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 8 · Primeros pasos en Python*
*Sección 2 · De la instrucción al código*
