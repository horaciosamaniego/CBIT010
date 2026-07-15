
### Tarea A: Sumar 1 a un número binario (grupos 1, 2, 3)

La misma tarea explicada en la cátedra. Los estudiantes ya vieron la ejecución paso a paso, pero ahora deben ejecutarla **ellos mismos** físicamente.

**Entrada en la cinta:** `□ □ □ 1 0 1 1 □ □ □` (centrada, con blancos a los lados)

**Tabla de transiciones:** (misma que en clase, entregar impresa)

| Estado | Lee | Escribe | Mueve | Nuevo estado |
|--------|-----|---------|-------|--------------|
| q0     | 0   | 0       | →     | q0           |
| q0     | 1   | 1       | →     | q0           |
| q0     | □   | □       | ←     | q1           |
| q1     | 0   | 1       | ←     | q2           |
| q1     | 1   | 0       | ←     | q1           |
| q1     | □   | 1       | ←     | q2           |
| q2     | 0   | 0       | ←     | q2           |
| q2     | 1   | 1       | ←     | q2           |
| q2     | □   | □       | →     | qHALT        |


**Variantes por grupo:**

- Grupo 1: entrada `1011` (→ `1100`)
- Grupo 2: entrada `0111` (→ `1000`, con carry que se propaga completamente)
- Grupo 3: entrada `1001` (→ `1010`, carry simple)
