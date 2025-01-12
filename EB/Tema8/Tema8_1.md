# Búsqueda no Informada
## Introducción
- ¿Qué es la búsqueda?
  - Es un problema de optimización.
  - Dado un problema, se busca una solución.
  - Se busca una secuencia de acciones que lleven a un estado objetivo.
- Si no se tiene alguna información extra sobre el problema, se llama búsqueda no informada.

## Aplicaciones reales de las búsquedas
- Planificación de rutas.
- Resolución de puzzles.
- Resolución de problemas de optimización.

## Formulación del problema de búsqueda
- Estados: Conjunto de estados posibles.
- Estado inicial: Estado en el que se comienza.
- Operadores: Acciones que se pueden realizar.
- Estado objetivo: Estado al que se quiere llegar.
- Coste de ruta: Coste de llegar a un estado desde el estado inicial.
- Solución: Secuencia de acciones que llevan al estado objetivo.

## Estrategias de búsqueda
### Búsqueda en anchura
- Se expanden todos los nodos de un nivel antes de pasar al siguiente.
- Se implementa con una cola.
```python
def busqueda_anchura(problema):
    cola = [problema.estado_inicial]
    while cola:
        estado = cola.pop(0)
        if problema.es_objetivo(estado):
            return estado
        for hijo in problema.hijos(estado):
            cola.append(hijo)
```

### Búsqueda de coste uniforme
- Se expanden los nodos con menor coste.
- Se implementa con una cola de prioridad.
  
```python
def busqueda_coste_uniforme(problema):
    cola = [(0, problema.estado_inicial)]
    while cola:
        coste, estado = cola.pop(0)
        if problema.es_objetivo(estado):
            return estado
        for hijo in problema.hijos(estado):
            cola.append((coste + problema.coste(estado, hijo), hijo))
        cola.sort()
```

### Búsqueda en profundidad
- Se expanden los nodos más profundos.
- Se implementa con una pila.
  
```python
def busqueda_profundidad(problema):
    pila = [problema.estado_inicial]
    while pila:
        estado = pila.pop()
        if problema.es_objetivo(estado):
            return estado
        for hijo in problema.hijos(estado):
            pila.append(hijo)
```

### Búsqueda en grafos
Hay problemas en los que las acciones son reversibles (por ejemplo, un puzzle). En estos casos, se pueden repetir estados. Para evitarlo, se puede llevar un registro de los estados visitados.

```python
def busqueda_grafo(problema):
    listaFrontera = [problema.estado_inicial]
    listaVisitados = []
    while listaFrontera:
        estado = listaFrontera.pop(0)
        if problema.es_objetivo(estado):
            return estado
        listaVisitados.append(estado)
        for hijo in problema.hijos(estado):
            if hijo not in listaVisitados and hijo not in listaFrontera:
                listaFrontera.append(hijo)
```

[Volver al índice](../../README.md)

[Ir al siguiente tema: Tema 8.2: Búsqueda Informada](../Tema8/Tema8_2.md)