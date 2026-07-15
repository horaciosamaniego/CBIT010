---
marp: true
theme: gaia
paginate: true
size: 16:9
style: |
  :root {
    /* YOUR COLOR SCHEME */
    --color-bg:      #091926;
    --color-elime:   #DEFF9A; /* Electric Lime */
    --color-dark:    #495f71;
    --color-mid:     #00B4CC;
    --color-accent:  #5DD9E8;
    --color-light:   #6199ac;
    --color-muted:   #7CA9BA;
    --color-white:   #e1ebee;
    --color-warn:    #E05B3A;
    --font-head:     'Georgia', serif;
    --font-body:     'Trebuchet MS', sans-serif;
  }

  /* --- Base Slide Styles --- */
  section {
    font-family: var(--font-body);
    font-size: 34px;
    line-height: 1.45;
    padding: 40px 50px;
    background-color: var(--color-bg);
    color: var(--color-white);
  }

  /* --- Typography --- */
  section h1, section h2, section h3 { font-family: var(--font-head); }
  
  section h1 { 
    color: var(--color-elime); 
    font-size: 1.6em; 
    border-bottom: 3px solid var(--color-mid); 
    padding-bottom: 6px; 
    margin-bottom: 16px; 
  }
  
  section h2 { color: var(--color-accent); font-size: 1.25em; margin-bottom: 12px; }
  section h3 { color: var(--color-light); font-size: 1.05em; }
  section strong { color: var(--color-elime); }
  section em { color: var(--color-muted); }

  /* --- Layout & Spacing --- */
  section li { margin-bottom: 4px; }
  section ul, section ol { margin: 6px 0 10px 20px; }
  section p { margin-bottom: 8px; }
  section img { display: block; margin: 0 auto;}

  /* --- Slide Variant: LEAD (Title Slides) --- */
  section.lead {
    background-color: var(--color-bg);
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 15px solid var(--color-mid); /* Added a frame for impact */
  }
  section.lead h1 { color: var(--color-elime); font-size: 2.2em; border-bottom: none; margin-bottom: 8px; }
  section.lead h2 { color: var(--color-white); font-weight: 400; font-size: 1.3em; }
  section.lead p, section.lead em { color: var(--color-accent); font-size: 0.85em; }

  /* --- Slide Variant: INVERT (Light Mode Toggle) --- */
  section.invert {
    background-color: var(--color-white);
    color: var(--color-bg);
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
  section.invert h1 { color: var(--color-bg); border-bottom: 3px solid var(--color-mid); font-size: 1.8em; }
  section.invert h2 { color: var(--color-dark); font-size: 1.2em; }
  section.invert h3 { color: var(--color-light); }
  section.invert strong { color: var(--color-warn); }

  /* --- Slide Variant: PREGUNTA (Questions) --- */
  section.pregunta {
    background-color: var(--color-mid);
    color: var(--color-bg);
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.pregunta h1 { font-size: 1.5em; border-bottom: none; color: var(--color-white); }
  section.pregunta p, section.pregunta em { color: var(--color-bg); font-weight: bold; }

  /* --- Slide Variant: LAB (Activity) --- */
  section.lab {
    background-color: var(--color-bg);
    border-left: 12px solid var(--color-warn);
  }
  section.lab h1 { color: var(--color-warn); border-bottom-color: var(--color-dark); }
  section.lab h2 { color: var(--color-light); }

  /* --- Tables --- */
  table { font-size: 0.78em; width: 100%; border-collapse: collapse; margin: 8px 0; }
  thead th { background-color: var(--color-dark); color: var(--color-elime); padding: 5px 8px; text-align: left; }
  td { padding: 4px 8px; border: 1px solid var(--color-dark); vertical-align: top; }
  tbody tr:nth-child(even) td { background-color: rgba(255,255,255,0.05); }
  section.lab thead th { background-color: var(--color-warn); color: var(--color-bg); }

  /* --- Blocks & Code --- */
  blockquote {
    background-color: rgba(255,255,255,0.05);
    border-left: 4px solid var(--color-elime);
    padding: 10px 16px; margin: 10px 0; font-size: 0.95em;
    color: var(--color-white);
  }
  pre { 
    font-size: 0.72em; 
    background-color: #000; 
    border: 1px solid var(--color-dark); 
    padding: 10px 14px; 
    color: var(--color-accent);
  }
  code { 
    font-size: 1.15em; 
    background-color: var(--color-dark); 
    color: var(--color-elime); 
    padding: 1px 5px; 
    border-radius: 3px; }

  /* --- UI Elements --- */
  .state-badge { background-color: var(--color-elime); color: var(--color-bg); padding: 2px 10px; border-radius: 12px; font-weight: bold; }
  .img-placeholder {
    border: 2px dashed var(--color-muted);
    padding: 14px; text-align: center; color: var(--color-accent); font-style: italic;
  }
  .cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 0.6em;
    color: var(--color-dark);
  }
  .card {
    background: var(--color-white);
    border-radius: 8px;
    padding: 16px 18px;
    border-top: 4px solid var(--color-accent);
    color: var(--color-dark);
  }
  .card h3 { color: var(--color-mid); margin-top: 0; }
  .card.warn { border-top-color: var(--color-warn); }
  .card.warn h3 { color: var(--color-warn); }
  .card p,
  .card li {
    color: var(--color-dark);
  }




footer: "Laboratorio · La Máquina de Turing · Horacio Samaniego (*horaciosamaniego@uach.cl*)"

---

<!-- _class: lead -->

# 🧪 Laboratorio analógico
## "Sé la Máquina de Turing"

*Ustedes son el cabezal. La tira de papel es la cinta. La tabla es el programa.*

---

<!-- _class: lab -->

# Los 5 roles

| Rol | Función |
|---|---|
| 🔵 **El Cabezal** | Señala la celda actual, lee el símbolo, se mueve |
| 🟢 **El Estado** | Sostiene tarjeta con el estado actual, la cambia cuando corresponde |
| 🟡 **El Escritor/a** | Escribe en la cinta (o pega post-it para "borrar") |
| 🟠 **El Buscador/a** | Busca la instrucción en la tabla y la anuncia |
| 🔴 **El Registrador/a** | Anota cada paso: N°, estado, símbolo, acción, nuevo estado |

---

<!-- _class: lab -->
<!-- _footer: "" -->

# El ciclo de ejecución

En cada paso:

1. **Cabezal** lee el símbolo y lo dice en voz alta
2. **Estado** muestra el estado actual
3. **Buscador/a** busca en la tabla: (estado, símbolo) → ...
4. **Buscador/a** anuncia: *"Escribir X, mover derecha, nuevo estado q1"*
5. **Escritor/a** escribe el nuevo símbolo
6. **Cabezal** se mueve
7. **Estado** cambia la tarjeta
8. **Registrador/a** anota todo

Repetir hasta **qHALT**.

---

<!-- _class: lab -->

# Tarea A · Sumar 1 a un número binario

**Grupos 1, 2, 3** — misma tabla que vimos en clase

| Grupo | Entrada | Resultado esperado |
|---|---|---|
| 1 | `1011` | `1100` (11 → 12) |
| 2 | `0111` | `1000` (7 → 8, carry completo) |
| 3 | `1001` | `1010` (9 → 10) |

⚠️ **Nadie anticipa.** Sigan la tabla paso a paso. Si ya saben cómo termina, no importa — la Máquina de Turing no piensa.

---

<!-- _class: lab -->

# Tarea B · Reconocer palíndromos

**Grupos 4, 5, 6** — ¿la cadena se lee igual al derecho y al revés?

| Grupo | Entrada | ¿Palíndromo? | Resultado |
|---|---|---|---|
| 4 | `1001` | Sí | → qACCEPT |
| 5 | `1010` | No | → qREJECT |
| 6 | `10101` | Sí | → qACCEPT |

**Estrategia:** comparar primer y último símbolo, marcarlos con X, repetir con el par siguiente. Si todos coinciden → ACCEPT.

*(La tabla de transiciones se entrega impresa.)*

---

<!-- _class: lab -->

# Verificación

Cuando la máquina llegue a **qHALT** (o qACCEPT / qREJECT):

1. ¿La cinta muestra el resultado correcto?
2. Si hay error → rastrear en la hoja de registro: ¿en qué paso se produjo?
3. ¿Cuántos pasos totales necesitaron?

<div class="img-placeholder">
📎 IMAGEN: Foto de estudiantes ejecutando una MT con tira de papel en el suelo — uno señala una celda, otro sostiene tarjeta de estado, otro escribe. Buscar: "Turing machine classroom activity students paper tape" o fotos de CS Unplugged Turing Machine activity.
</div>

---

<!-- _class: invert -->

# Discusión 

---

<!-- _class: pregunta -->

# ¿El Cabezal necesitó "entender" que estaba sumando (o buscando palíndromos)?

*No. Solo leía y seguía reglas. Igual que la ALU de la Semana 1. El significado está en el diseño de la tabla — no en la máquina.*

---

<!-- _class: pregunta -->

# ¿Podrían escribir una tabla de transiciones para cualquier algoritmo de la Semana 4?

*En principio, sí. Eso dice la tesis de Church-Turing. Sería tedioso — pero posible. Todo algoritmo se puede implementar como una MT.*

---

<!-- _class: pregunta -->

# Si esta máquina tan simple puede computar todo lo computable, ¿qué agrega un computador moderno?

*Velocidad y comodidad. Un computador no puede hacer nada que una MT no pueda — pero lo hace billones de veces más rápido.*

---

<!-- _class: pregunta -->

# ¿Qué tiene que ver con la inteligencia artificial?

*Un LLM es, en el fondo, un programa ejecutándose en una máquina equivalente a una MT. Cuando ChatGPT "escribe", sigue reglas (muy complejas) sobre una entrada (tu prompt).*

*La pregunta de Turing: ¿es eso "pensar"?*

*La próxima semana intentamos responder.*


---

# Lo que aprendimos hoy

- La **Máquina de Turing** tiene solo 4 partes: cinta, cabezal, estados, tabla de transiciones
- Es el **modelo mínimo** de computación — pero puede computar todo lo que cualquier computador puede
- La **tesis de Church-Turing**: todo lo computable puede ser computado por una MT
- Hay problemas **no computables** (como el problema de la detención)
- La MT no "entiende" — sigue reglas. El significado vive en el diseño del programa

---

# Próxima semana

## Semana 6 · Del perceptrón a ChatGPT
### ¿Qué son los LLMs?


<div class="cols">

<div class="card">
Si una MT no "piensa" pero puede computar todo... ¿qué está haciendo un LLM cuando responde a tu pregunta? ¿Y qué significa eso para la conservación?
</div>



![w:550px](https://rowlandpettit.com/machine-learning_files/figure-html/ai-timeline-1.png)


</div

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

*Semana 5 · La Máquina de Turing: el computador universal más simple*

