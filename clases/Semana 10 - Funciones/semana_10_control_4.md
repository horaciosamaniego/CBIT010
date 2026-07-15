---
pdf-engine: xelatex
fontsize: 12pt

header-includes:
  - \pagenumbering{gobble}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{CBIT010}
  - \fancyhead[C]{\bf Control 4}
  - \fancyhead[R]{2026}
  - \fancyfoot{}
  
---



**Nombre:** ______________________  **Fecha:** ______  **Puntaje:** _____ / 20

*Sin apuntes ni celular. 15 minutos.*


**1. (4 puntos)** ¿Qué imprime el siguiente código?

```python
def misterio(a, b):
    c = a + b
    return c * 2

x = misterio(3, 4)
print(x)
```

Respuesta: _____________


**2. (4 puntos)** Escriba una función llamada `promedio` que reciba una lista de números y retorne su promedio. Incluya un docstring.

\vspace{2.5cm}



**3. (4 puntos)** ¿Qué imprime este código? Explique por qué.

```python
x = 10

def cambiar():
    x = 20
    return x

resultado = cambiar()
print(resultado)
print(x)
```

Respuesta: resultado = _______ , x = _______

Explicación: _______________________________________________


**4. (4 puntos)** Identifique el error en esta función y corríjalo:

```python
def contar_grandes(lista, umbral):
    for n in lista:
        contador = 0
        if n > umbral:
            contador += 1
    return contador
```

Error: _______________________________________________
Corrección: _______________________________________________


**5. (4 puntos)** Explique la diferencia entre `return` y `print()` dentro de una función. ¿Por qué es importante usar `return` en vez de `print` cuando el resultado será usado por otro código?

\vspace{2.5cm}


### Pauta de corrección

| Pregunta | Respuesta | Puntos |
|---|---|---|
| 1 | Imprime `14`. misterio(3,4) → c=7, return 14 | 4 (2 por c=7, 2 por resultado 14) |
| 2 | `def promedio(lista): """Calcula promedio.""" return sum(lista)/len(lista)` — docstring, parámetro, return correcto | 4 (1 docstring, 1 parámetro, 1 return, 1 corrección) |
| 3 | resultado=20, x=10. La x dentro de `cambiar()` es LOCAL — no modifica la x global | 4 (1 por cada valor correcto, 2 por explicación de scope) |
| 4 | `contador = 0` está DENTRO del for → se reinicia en cada iteración. Moverlo ANTES del for | 4 (2 identificar error, 2 corregir) |
| 5 | `return` devuelve un valor que se puede asignar a variable o usar en cálculos. `print` solo muestra texto — la función devuelve None. Si otro código necesita el resultado, print no sirve | 4 (2 por distinción, 2 por consecuencia práctica) | 
