# Semana 10: Funciones — Encapsular y reutilizar

## Guía completa de la sesión

---

## Visión general

| | |
|---|---|
| **Duración total** | 3 horas (1.5 h cátedra con live coding + 1.5 h laboratorio en Colab) |
| **Objetivo central** | Que los estudiantes diseñen, escriban y usen funciones propias para encapsular cálculos ecológicos reutilizables, y comprendan el concepto de alcance (scope) de variables |
| **Idea ancla** | Una función es una **mini-máquina de Turing** (Sem. 5): recibe entradas, ejecuta instrucciones, produce una salida, y su estado interno (variables locales) es invisible desde afuera. Cuando escriben `shannon_entropy(abundancias)`, están creando una nueva "tabla de transiciones" que cualquiera puede usar sin saber cómo funciona por dentro |
| **Prerrequisito** | Sem. 8 (variables, tipos, condicionales, bucles), Sem. 9 (listas, diccionarios) |
| **Materiales** | Proyector, Colab, WiFi, notebook starter, Dataset 1 |
| **Evaluación** | Quiz 4 al final de la sesión (15 min) |

---

## PARTE 1: CÁTEDRA CON LIVE CODING (90 minutos)

---

### Bloque A — ¿Por qué funciones? El problema de la repetición (10 min)

**Mostrar en el proyector:** el código de Shannon H' que escribieron dos veces — una en el Ejercicio 7 de la Sem. 8 y otra en el Ejercicio 6 de la Sem. 9.

```python
# Semana 8 — dentro del notebook
import math
abundancias = [45, 28, 67, 12, 33, 8, 52]
total = sum(abundancias)
H = 0
for n in abundancias:
    p = n / total
    H -= p * math.log(p)
print(f"H' = {H:.4f}")
```

```python
# Semana 9 — otra vez, dentro de otro notebook
import math
# ... mismo código copiado y pegado ...
```

**Preguntas al curso:**
- *"¿Cuántas veces van a copiar y pegar este bloque durante el semestre?"*
- *"¿Qué pasa si encuentran un bug? Hay que corregirlo en TODOS los lugares donde lo copiaron."*
- *"¿Y si un colega quiere usarlo? ¿Le mandan 7 líneas de código sueltas?"*

**La solución:** empaquetar el cálculo en una **función** — escribirlo una vez, usarlo para siempre.

**Callback Sem. 5:** *"En la Máquina de Turing, la tabla de transiciones ERA el programa. Definir una función es como escribir una tabla de transiciones reutilizable: le das una entrada, ejecuta sus pasos internos, y te devuelve un resultado. No necesitas saber cómo funciona por dentro — solo qué le das y qué te devuelve."*

---

### Bloque B — Anatomía de una función (20 min)

#### La primera función (5 min)

```python
def saludar(nombre):
    """Saluda al usuario por su nombre."""
    print(f"¡Hola, {nombre}! Bienvenido/a al bosque valdiviano.")

# Llamar a la función
saludar("Camila")
saludar("Diego")
```

**Anatomía:**
- `def` → palabra clave que define la función
- `saludar` → nombre de la función (snake_case, verbo descriptivo)
- `(nombre)` → parámetro (la entrada)
- `"""..."""` → docstring (documentación)
- Bloque indentado → el cuerpo (las instrucciones)

#### Funciones que retornan valores (8 min)

```python
def calcular_densidad(poblacion, area):
    """Calcula la densidad poblacional (individuos/km²)."""
    densidad = poblacion / area
    return densidad

# Usar la función
d1 = calcular_densidad(340, 12.5)
d2 = calcular_densidad(1500, 23.7)

print(f"Pudú: {d1:.2f} ind/km²")
print(f"Huemul: {d2:.2f} ind/km²")
```

**Diferencia clave:** `print()` muestra en pantalla. `return` **devuelve** un valor que se puede guardar en una variable, usar en un cálculo, o pasar a otra función.

```python
# return vs print — la diferencia que importa
def con_return(a, b):
    return a + b

def con_print(a, b):
    print(a + b)

resultado = con_return(3, 5)
print(resultado * 2)      # 16 — puedo usar el resultado

resultado = con_print(3, 5)  # imprime 8
print(resultado)              # None — no devolvió nada
```

> *"`return` es la SALIDA de la función. `print` es solo un mensaje a la pantalla."*

#### Múltiples parámetros y valores por defecto (7 min)

```python
# Múltiples parámetros
def area_basal(dap_cm):
    """Calcula el área basal de un árbol (m²) a partir del DAP en cm."""
    import math
    radio_m = (dap_cm / 100) / 2
    return math.pi * radio_m ** 2

print(f"Área basal: {area_basal(45.3):.4f} m²")

# Valores por defecto
def clasificar_dap(dap, umbral=30):
    """Clasifica un árbol como 'grande' o 'pequeño' según su DAP."""
    if dap > umbral:
        return "grande"
    else:
        return "pequeño"

print(clasificar_dap(45))       # "grande" (umbral default = 30)
print(clasificar_dap(45, 50))   # "pequeño" (umbral cambiado a 50)
print(clasificar_dap(25))       # "pequeño"
```

---

### Bloque C — Funciones con listas y diccionarios (20 min)

#### Funciones que procesan listas (7 min)

```python
def promedio(lista):
    """Calcula el promedio de una lista de números."""
    return sum(lista) / len(lista)

def filtrar_mayores(lista, umbral):
    """Devuelve los elementos mayores que el umbral."""
    return [x for x in lista if x > umbral]

daps = [45.3, 25.1, 18.7, 33.2, 55.0, 12.4, 38.9]

print(f"Promedio: {promedio(daps):.1f} cm")
print(f"DAP > 30: {filtrar_mayores(daps, 30)}")
print(f"DAP > 40: {filtrar_mayores(daps, 40)}")
```

#### Funciones que devuelven diccionarios (5 min)

```python
def estadisticas(lista):
    """Calcula estadísticas descriptivas de una lista numérica."""
    return {
        "n": len(lista),
        "suma": sum(lista),
        "promedio": sum(lista) / len(lista),
        "minimo": min(lista),
        "maximo": max(lista),
        "rango": max(lista) - min(lista)
    }

stats = estadisticas(daps)
print(f"N = {stats['n']}")
print(f"Promedio = {stats['promedio']:.1f}")
print(f"Rango = {stats['minimo']:.1f} – {stats['maximo']:.1f}")
```

#### La función Shannon H' — el gran momento (8 min)

```python
import math

def shannon_entropy(abundancias):
    """
    Calcula el índice de diversidad de Shannon (H').
    
    Parámetros:
        abundancias: lista de enteros — abundancia de cada especie
    
    Retorna:
        float — H' en nats (logaritmo natural)
    """
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H

# Ahora se usa en UNA línea
datos_parcela_1 = [45, 28, 67, 15, 33]
datos_parcela_2 = [10, 10, 10, 10, 10]
datos_parcela_3 = [90, 3, 2, 3, 2]

print(f"Parcela 1: H' = {shannon_entropy(datos_parcela_1):.4f}")
print(f"Parcela 2: H' = {shannon_entropy(datos_parcela_2):.4f}")  # máximo
print(f"Parcela 3: H' = {shannon_entropy(datos_parcela_3):.4f}")  # bajo (dominada)
```

*"Escribieron este cálculo una vez. Ahora lo usan para cualquier parcela, cualquier dataset, cualquier número de especies. Eso es el poder de una función."*

---

### Bloque D — Alcance (scope): variables locales vs globales (10 min)

**Callback Sem. 5:** *"En la MT, el estado interno (q0, q1...) era invisible desde afuera. Las variables dentro de una función son iguales: existen solo mientras la función se ejecuta."*

```python
def calcular_algo():
    x = 42           # x es LOCAL — solo existe dentro de esta función
    print(f"Dentro: x = {x}")

calcular_algo()
# print(x)          # NameError: x is not defined — no existe afuera
```

```python
# Variables globales vs locales
mensaje = "Hola"     # GLOBAL

def mi_funcion():
    mensaje = "Chao"  # LOCAL — crea una nueva variable, no modifica la global
    print(f"Dentro: {mensaje}")

mi_funcion()                    # "Chao"
print(f"Fuera: {mensaje}")     # "Hola" — la global no cambió
```

```python
# Los parámetros también son locales
def duplicar(n):
    n = n * 2
    return n

valor = 10
resultado = duplicar(valor)
print(f"resultado = {resultado}")   # 20
print(f"valor = {valor}")           # 10 — no cambió
```

**Regla de oro:** las funciones no deben depender de variables globales ni modificarlas. Todo lo que necesitan entra por los **parámetros** y sale por el **return**.

---

### Bloque E — Funciones que llaman a funciones (10 min)

```python
import math

def shannon_entropy(abundancias):
    """H' en nats."""
    total = sum(abundancias)
    H = 0
    for n in abundancias:
        if n > 0:
            p = n / total
            H -= p * math.log(p)
    return H

def equitatividad(abundancias):
    """J = H' / H'_max. Retorna 0 si solo hay 1 especie."""
    S = len(abundancias)
    if S <= 1:
        return 0
    H = shannon_entropy(abundancias)   # ← llama a la otra función
    H_max = math.log(S)
    return H / H_max

def simpson_index(abundancias):
    """Índice de Simpson (1 - D)."""
    total = sum(abundancias)
    D = sum((n / total) ** 2 for n in abundancias)
    return 1 - D

def reporte_diversidad(nombre_sitio, abundancias):
    """Genera un reporte completo de diversidad."""
    S = len(abundancias)
    N = sum(abundancias)
    H = shannon_entropy(abundancias)
    J = equitatividad(abundancias)
    D = simpson_index(abundancias)
    
    print(f"{'='*40}")
    print(f"Reporte de diversidad: {nombre_sitio}")
    print(f"{'='*40}")
    print(f"  Riqueza (S):      {S}")
    print(f"  Abundancia (N):   {N}")
    print(f"  Shannon (H'):     {H:.4f} nats")
    print(f"  Equitatividad (J):{J:.4f}")
    print(f"  Simpson (1-D):    {D:.4f}")
    print(f"{'='*40}\n")

# Usar
reporte_diversidad("Alerce Andino", [45, 28, 67, 15, 33])
reporte_diversidad("Huilo-Huilo", [90, 3, 2, 3, 2])
```

*"La función `reporte_diversidad` no calcula H' ni J directamente — llama a funciones que ya saben hacerlo. Esto es composición: construir funciones complejas a partir de funciones simples."*

---

### Bloque F — Docstrings y buenas prácticas (5 min)

```python
def shannon_entropy(abundancias):
    """
    Calcula el índice de diversidad de Shannon (H').
    
    Parámetros:
        abundancias: list[int] — abundancia de cada especie
    
    Retorna:
        float — H' en nats (logaritmo natural)
    
    Ejemplo:
        >>> shannon_entropy([10, 10, 10])
        1.0986
    """
    ...

# Acceder a la documentación
help(shannon_entropy)
```

**Buenas prácticas:**
- Nombre descriptivo: `shannon_entropy`, no `calc` ni `f1`
- Docstring que explica qué hace, qué recibe, qué devuelve
- Una función = una tarea. Si hace dos cosas, partirla en dos
- Siempre usar `return` (no `print`) para el resultado principal
- Variables locales, no globales

---

### Bloque G — Módulos: importar funciones de otros archivos (5 min)

```python
# Python tiene funciones organizadas en MÓDULOS
import math
print(math.pi)
print(math.log(100))
print(math.sqrt(144))

# Importar solo lo que necesitas
from math import log, pi
print(log(100))

# Módulo random — útil para simulaciones ecológicas
import random
print(random.randint(1, 100))        # entero aleatorio
print(random.choice(["pudú", "puma", "güiña"]))  # elegir al azar
print(random.uniform(10, 50))        # float aleatorio
```

*"Los módulos son colecciones de funciones que alguien más escribió. `math.log()` es una función igual que las que ustedes escriben — solo que viene pre-empaquetada."*

**Anticipación Sem. 12:** *"En la Semana 12 van a importar `pandas` — un módulo con funciones para análisis de datos. Y van a poder importar sus propias funciones de un archivo a otro."*

---

## PARTE 2: LABORATORIO EN COLAB (75 minutos)

---

### Ejercicios

#### Ejercicio 1: Funciones básicas (15 min)

Escribir funciones simples:
- `celsius_a_fahrenheit(c)` — convierte temperatura
- `area_circulo(radio)` — calcula π × r²
- `area_basal(dap_cm)` — calcula área basal en m²
- `relacion_hd(altura_m, dap_cm)` — calcula relación altura/diámetro

Probar cada una con varios valores.

#### Ejercicio 2: Funciones con condicionales (15 min)

- `clasificar_uicn(poblacion, tendencia)` — retorna la categoría UICN (el clasificador de Sem. 4/8, ahora como función)
- `es_arbol_grande(dap, umbral=30)` — retorna True/False
- `evaluar_muestreo(temp, viento, lluvia)` — retorna True/False y un mensaje

#### Ejercicio 3: Funciones con listas (15 min)

- `contar_especies(observaciones)` — recibe lista de nombres, retorna diccionario de frecuencias
- `abundancia_relativa(abundancias)` — retorna lista de proporciones
- `filtrar_por_parcela(arboles, parcela)` — recibe lista de diccionarios, retorna filtrada

#### Ejercicio 4: Funciones de diversidad (15 min)

- `shannon_entropy(abundancias)` — retorna H' en nats
- `equitatividad(abundancias)` — retorna J = H'/ln(S)
- `simpson_index(abundancias)` — retorna 1-D
- `reporte_diversidad(nombre, abundancias)` — imprime reporte completo usando las tres anteriores

#### Ejercicio 5 (desafío): Diversidad por parcela con funciones (15 min)

Refactorizar el Ejercicio 6 de la Semana 9: calcular H' por parcela, pero ahora usando las funciones del Ejercicio 4. El código debería ser mucho más limpio y corto.

---

## PARTE 3: QUIZ 4 (15 minutos)

### Quiz 4 — Semana 10
#### Introducción al Análisis de Datos y Programación

**Nombre:** ____________________________  **Fecha:** ____________  **Puntaje:** _____ / 20

*Sin apuntes ni celular. 15 minutos.*

---

**1. (4 puntos)** ¿Qué imprime el siguiente código?

```python
def misterio(a, b):
    c = a + b
    return c * 2

x = misterio(3, 4)
print(x)
```

Respuesta: _____________

---

**2. (4 puntos)** Escriba una función llamada `promedio` que reciba una lista de números y retorne su promedio. Incluya un docstring.

\[espacio\]

---

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

---

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

---

**5. (4 puntos)** Explique la diferencia entre `return` y `print()` dentro de una función. ¿Por qué es importante usar `return` en vez de `print` cuando el resultado será usado por otro código?

\[espacio\]

---

### Pauta de corrección

| Pregunta | Respuesta | Puntos |
|---|---|---|
| 1 | Imprime `14`. misterio(3,4) → c=7, return 14 | 4 (2 por c=7, 2 por resultado 14) |
| 2 | `def promedio(lista): """Calcula promedio.""" return sum(lista)/len(lista)` — docstring, parámetro, return correcto | 4 (1 docstring, 1 parámetro, 1 return, 1 corrección) |
| 3 | resultado=20, x=10. La x dentro de `cambiar()` es LOCAL — no modifica la x global | 4 (1 por cada valor correcto, 2 por explicación de scope) |
| 4 | `contador = 0` está DENTRO del for → se reinicia en cada iteración. Moverlo ANTES del for | 4 (2 identificar error, 2 corregir) |
| 5 | `return` devuelve un valor que se puede asignar a variable o usar en cálculos. `print` solo muestra texto — la función devuelve None. Si otro código necesita el resultado, print no sirve | 4 (2 por distinción, 2 por consecuencia práctica) |

---

## Notas pedagógicas

### El momento "aha" de las funciones

Para muchos estudiantes, las funciones son el primer concepto que se siente genuinamente nuevo (no un calco de la Sección 1). El callback a la MT ayuda, pero el verdadero momento de comprensión viene cuando ven que `shannon_entropy(datos_parcela_1)` reemplaza 7 líneas de código. **El poder es la reutilización**, no la abstracción.

### El error del acumulador dentro del for (Pregunta 4 del Quiz)

Este es el error más común en las primeras semanas con funciones. El 40–60% de los estudiantes lo cometen. Vale la pena mostrarlo en vivo durante la cátedra: escribir la versión con bug, ejecutarla, ver que siempre devuelve 0 o 1, y preguntar "¿por qué?".

### Scope como fuente de confusión

El scope es el concepto más difícil de esta semana. Estrategia: usar el debugger visual de Colab (o Python Tutor en la web: pythontutor.com) para mostrar cómo las variables locales nacen y mueren.

### Conexión con el resto del curso

| Concepto | Dónde se profundiza |
|---|---|
| Funciones con return | Sem. 11 (funciones como argumento, lambda) |
| Scope | Sem. 11 (funciones dentro de funciones) |
| Docstrings | Sem. 11 (módulos propios) |
| Módulos (import) | Sem. 12 (csv, pandas) |
| Funciones de diversidad | Sem. 12–13 (aplicarlas sobre DataFrames) |
