# Clustering
## Conceptos
### Aprencizaje no supervisado:
- Sirve para explorar los datos y encontrar patrones. Entiende y resume la estructura de los datos.
- El dataset no tiene etiquetas.

### Clustering:
- Agrupa los datos en clusters (grupos) de acuerdo a su similitud.
- Cada cluster es un conjunto de puntos que son similares entre sí y diferentes a los puntos de otros clusters.
- Ejemplo: Agrupar clientes en función de sus compras, agrupar noticias en función de su contenido, agrupar pacientes en función de sus síntomas, etc.
- **Objetivo:** Minimizar la distancia intra-cluster y maximizar la distancia inter-cluster.

## K-Means
### Representación del modelo
- Es uno de los algoritmos de clustering más populares.
#### Notacion:
  - $m$ = número de ejemplos / instancias del conjunto de entrenamiento (training)
  - $n$ = número de atributos / variables / características
  - Training: $x^{(1)}, x^{(2)}, … , x^{(m)}$
  - $x \in \mathbb{R}^n$ → no vamos a añadir la columna $x_0$
  - $K$ = número de clusters
  - Centroides: $\mu_k$ Representan el centro del cluster
  - $c^{(i)}$: Índice (de 1 a $K$) del centroide más cercano a $x^{(i)}$
  - $\mu_{c^{(i)}}$: Centroide del cluster al que se ha asignado $x^{(i)}$
#### Algoritmo:
  1. Inicializar los centroides $\mu_1, \mu_2, …, \mu_K$ aleatoriamente.
  2. Asignar cada ejemplo $x^{(i)}$ al centroide más cercano: $c^{(i)} = \text{argmin}_k ||x^{(i)} - \mu_k||^2$
  3. Mover los centroides al centro de los puntos asignados: $\mu_k = \frac{\sum_{i=1}^{m} 1\{c^{(i)} = k\} x^{(i)}}{\sum_{i=1}^{m} 1\{c^{(i)} = k\}}$
  4. Ver el coste: $J(c, \mu) = \frac{1}{m} \sum_{i=1}^{m} ||x^{(i)} - \mu_{c^{(i)}}||^2$
  5. Repetir los pasos 2, 3 y 4 hasta convergencia o criterio de parada.

### Inicialización de los centroides
- Se pueden inicializar de varias formas:
  - Aleatoriamente: Se eligen $K$ ejemplos al azar y se toman como centroides.
  - K-Means++: Se elige un centroide aleatorio y luego se eligen los siguientes de forma que estén lo más lejos posible de los ya elegidos.
  - PCA (Principal Component Analysis): Se aplica PCA para reducir la dimensionalidad y se eligen los centroides en el espacio reducido.
  - Forzada: Se fuerza a que los centroides sean ejemplos específicos.
- Para evitar mínimos locales, se puede ejecutar el algoritmo varias veces con diferentes inicializaciones y quedarse con la mejor solución. Pseudocódigo:
```python
    for i in range(num_iteraciones):
        # Inicializar centroides aleatoriamente con k-means++ o instancias del dataset
        # Ejecutar K-Means
        # Calcular coste
     #seleccionar mejor solución con menor coste
```

### Elección de K
No hay una regla fija para elegir $K$.
- Manualmente: Se puede elegir un valor de $K$ que tenga sentido en el contexto del problema.
- Método del codo (Elbow Method): Se ejecuta K-Means con diferentes valores de $K$ y se representa el coste en función de $K$. Se elige el valor de $K$ en el punto donde la curva empieza a aplanarse.

[Volver al índice](../../README.md)

[Ir al siguiente tema: Tema 7: Sistemas de recomendación](../Tema7/Tema7.md)
