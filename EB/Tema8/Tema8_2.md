# Búsqueda Informada
## Introducción
- ¿Qué es la búsqueda?
  - Es un problema de optimización.
  - Dado un problema, se busca una solución.
  - Se busca una secuencia de acciones que lleven a un estado objetivo.
- Si se tiene alguna información extra sobre el problema, se llama búsqueda informada.
- "heurística" viene de "descubrir" en griego.
- RAE: "En algunas ciencias, manera de buscar la solución de un problema mediante métodos no rigurosos, como la intuición, la experiencia, etc."
- Método heurístico es un método de resolución de un problema basado en conocimiento específico de dicho problema.
- Usaremos heurísticos para decidir qué nodos expandir en la búsqueda.

## Conceptos básicos
Un árbol (tree) es una estructura no lineal en la que los elementos están organizados jerárquicamente. Un árbol se compone de nodos (nodes) y aristas (edges). Un nodo puede tener cero o más nodos hijos. Un nodo sin hijos se llama nodo hoja (leaf node). Un nodo con hijos se llama nodo interno (internal node).	
- Factor de ramificación (branching factor): Número medio de hijos por nodo.
- Nivel de un nodo (depth): Número de aristas en el camino desde el nodo raíz hasta el nodo.
- Profundidad de un árbol (depth): Número máximo de aristas en cualquier camino desde el nodo raíz hasta un nodo hoja.
- Profundidad: Nodo objetivo más superficial.

- Completa: Encuentra la solución si existe.
- Óptima: Encuentra la solución de menor coste.
- Tiempo: Tiempo que tarda en encontrar la solución (número de nodos generados).
- Espacio: Memoria que necesita para encontrar la solución (número de nodos almacenados).

## Búsqueda voraz
- Se expande el nodo más prometedor.
- Se implementa con una cola de prioridad.
- Se expande el nodo con menor valor de la función heurística.
- No tiene memoria.
- No es óptima.
- Complejidad en tiempo: $O(b^m)$.
- Complejidad en espacio: $O(b^m)$.
- No se garantiza encontrar la solución (no es completa).

## Algoritmo A*
- Se expande el nodo con menor valor de $f(n) = g(n) + h(n)$.
- $g(n)$: Coste del camino desde el nodo inicial hasta el nodo $n$.
- $h(n)$: Estimación del coste del camino más barato desde el nodo $n$ hasta el nodo objetivo.
- Si h es admisible, A* es óptima.
- Si h es consistente, A* es óptima.
- Para que h sea consistente, tiene que cumplir la desigualdad triangular: $h(n) \leq c(n, n') + h(n')$.
- Secuencia de nodos expandidos por A* es en orden no decreciente de $f(n)$.
A* expande todos los nodos con $f(n) \leq C^*$, donde $C^*$ es el coste de la solución óptima.

## Diseño de heurísticos
- Un heurístico es admisible si nunca sobreestima el coste de llegar al objetivo.
- Un heurístico es consistente si para cada nodo $n$ y cada sucesor $n'$ de $n$ generado por cualquier acción $a$, el coste estimado de llegar al objetivo desde $n$ es no mayor que el coste de llegar a $n'$ más el coste estimado de llegar al objetivo desde $n'$.
- Un heurístico es óptimo si es consistente y admisible.
- Ejemplo de heurístico admisible: distancia en línea recta, distancia de Manhattan, etc.
- Heurísticas con las propiedades:
  - Consistencia: $h(n) \leq c(n, n') + h(n')$.
  - Lo más cercano al objetivo: $h(n) = 0$ si $n$ es el objetivo.
  - Fácil de computar.
- Ejemplo 8-puzzle:
  - $h_1(n)$: Número de fichas mal colocadas.
  - $h_2(n)$: Suma de las distancias de Manhattan de cada ficha a su posición correcta.
  - $h_2(n) \geq h_1(n)$. $h_2(n)$ es mejor que $h_1(n)$.
- h2 es siempre mejor que h1 porque para cualquier nodo n, h2(n) es mayor o igual que h1(n). Por tanto, h2 es más informativa que h1.
- Un método para diseñar heurísticos es relajar las restricciones del problema original.

[Volver al índice](../../README.md)

# FIN