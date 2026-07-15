

### Tarea B: Reconocer palíndromos binarios (grupos 4, 5, 6)



**Problema:** determinar si una cadena binaria es un palíndromo (se lee igual al derecho y al revés).



**Entrada:** una cadena binaria rodeada de blancos.



**Estrategia:** comparar el primer y último símbolo, marcarlos como "visitados" (X), moverse al siguiente par, y repetir. Si todos los pares coinciden → aceptar. Si alguno no → rechazar.



**Tabla de transiciones:**



| Estado | Lee | Escribe | Mueve | Nuevo estado | Comentario |
|---|---|---|---|---|---|
| q0 | 0 | X | → | q1 | Vio 0 al inicio, buscar 0 al final |
| q0 | 1 | X | → | q2 | Vio 1 al inicio, buscar 1 al final |
| q0 | X | X | → | q0 | Saltar X ya marcadas |
| q0 | □ | □ | — | qACCEPT | Todos marcados, es palíndromo |
| q1 | 0 | 0 | → | q1 | Avanzar buscando el final |
| q1 | 1 | 1 | → | q1 | |
| q1 | X | X | → | q1 | Saltar X |
| q1 | □ | □ | ← | q3 | Llegó al final, retroceder |
| q3 | X | X | ← | q3 | Saltar X al final |
| q3 | 0 | X | ← | q4 | ¡Coincide! Marcar y volver |
| q3 | 1 | 1 | — | qREJECT | No coincide: no es palíndromo |
| q2 | 0 | 0 | → | q2 | Avanzar buscando el final |
| q2 | 1 | 1 | → | q2 | |
| q2 | X | X | → | q2 | |
| q2 | □ | □ | ← | q5 | Llegó al final |
| q5 | X | X | ← | q5 | Saltar X al final |
| q5 | 1 | X | ← | q4 | ¡Coincide! |
| q5 | 0 | 0 | — | qREJECT | No coincide |
| q4 | 0 | 0 | ← | q4 | Volver al inicio |
| q4 | 1 | 1 | ← | q4 | |
| q4 | X | X | → | q0 | Volver a empezar |



**Variantes por grupo:**

- Grupo 4: entrada `1001` (palíndromo → ACCEPT)
- Grupo 5: entrada `1010` (no es palíndromo → REJECT)
- Grupo 6: entrada `10101` (palíndromo → ACCEPT)

 
