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
<style scoped>{font-size: 3em;}</style>
<!-- _footer : "" -->
<!-- _class: invert -->

# 🧪 Laboratorio
## Trabajaremos en ![w:100px](./GColab_icon.png)

<div class='card'>

- **Primero:** Necesitas una cuenta en Google

- **Segundo:** abrir colab
https://colab.research.google.com/


- **Tercero:** Descargar archivo desde *SIVEDUC*
[`semana_08_primer_notebook.ipynb`](https://siveducmd.uach.cl/mod/resource/view.php?id=1098055)

- **Cuarto:**  Guardar una copia en *Google Drive*
</div>

---

<!-- _class: lab -->

# Nivel 1 · Fundamentos

**Ej. 1:** Variables, tipos, área basal y relación H/D de un árbol
**Ej. 2:** Strings + ASCII — codificar "PUDU" en binario

---

<!-- _class: lab -->

# Nivel 2 · Condicionales

**Ej. 3:** Clasificador UICN completo (if/elif/else + anidados)
**Ej. 4:** Decisión de muestreo con `and`, `or`, `not`

---

<!-- _class: lab -->

# Nivel 3 · Bucles

**Ej. 5:** Abundancias relativas de 5 especies con `for`
**Ej. 6:** Filtrar DAPs grandes con `for` + `if` + acumulación

---

<!-- _class: lab -->

# Desafío · Shannon $H'$ automático

```python
import math
abundancias = [45, 28, 67, 12, 33, 8, 52]
total = sum(abundancias)

H = 0
for n in abundancias:
    p = n / total
    H -= p * math.log(p)

print(f"H' = {H:.4f} nats")
```

*En la Sem. 3 calcularon H para 3 especies a mano. Ahora lo hacen para 7, o 700, con 5 líneas.*

---

# Lo que aprendimos hoy

| Concepto | Sección 1 | Python |
|---|---|---|
| Celda de memoria | Sem. 1: celda numerada | `variable = valor` |
| Codificación | Sem. 2: ASCII, tipos | `int`, `float`, `str`, `bool` |
| Decisión | Sem. 4: rombo del flujo | `if / elif / else` |
| Repetición | Sem. 4: pasadas del sort | `for` / `while` |
| Acumulación | Sem. 3: contar especies | `total += n` |

---

# Próxima semana

## Semana 9 · Colecciones: listas y diccionarios

*Una variable guarda un dato. ¿Y si necesitan guardar 100 especies? Van a usar una lista.* 

*¿Y asociar cada especie con su abundancia? Un diccionario — la tabla de frecuencias de la Semana 3.*

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?
