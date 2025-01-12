# Sistemas de recomendación
## Conceptos
- Intentar predecir la preferencia de un usuario sobre un item.
- Algunas aplicaciones:
  - Recomendación de productos en tiendas online.
  - Recomendación de películas en plataformas de streaming.
  - Recomendación de amigos en redes sociales.
- Pueden ser basados en contenido o colaborativos:
  - **Filtrado colaborativo:** Se basa en la similitud entre usuarios o items.
  - **Filtrado basado en contenido:** Se basa en las características de los items.
### Notación
- $n_u$: Número de usuarios.
- $n_i$: Número de items.
- $n$: Número de características de los items.
- $r(i, j)$: Existe una valoración del usuario $j$ al item $i$.
- $y^{(i, j)}$: Valoración del usuario $j$ al item $i$.

## Basados en contenido
- Basándose en items valorados previamente por el usuario, hacen modelos de predicción por cada usuario y se recomiendan items similares.
- Tendremos un vector de características $x^{(i)} \in \mathbb{R}^n$ para cada item $i$.
- Haremos un modelo de regresión lineal para cada usuario $j$:
  - $h_\theta(x^{(i)}) = \theta^{(j)T} x^{(i)}$.
  - $\theta^{(j)} \in \mathbb{R}^n$ son los parámetros del usuario $j$.
  - $\theta^{(j)}$ se obtiene minimizando la función de coste:
    - $J(\theta^{(j)}) = \frac{1}{2} \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{k=1}^n (\theta_k^{(j)})^2$.
    - $\lambda$ es el parámetro de regularización.
- Añadiremos c0 = 1 a $x^{(i)}$. Así, $\theta^{(j)}$ será de dimensión $n+1$.

### Objetivo de optimización
#### Regresión lineal sin regularización
- Minimizar la función de coste:
  - $J(\theta^{(j)}) = \frac{1}{2} \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2$.

#### Regresión lineal con regularización
- Minimizar la función de coste:
  - $J(\theta^{(j)}) = \frac{1}{2} \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{k=1}^n (\theta_k^{(j)})^2$.
  - $\lambda$ es el parámetro de regularización.
  - $\lambda$ es un hiperparámetro que se puede ajustar con un conjunto de validación.
  - $\lambda$ no se aplica a $\theta_0$.
  - $\lambda$ muy grande: $\theta^{(j)}$ muy pequeño, se tiende a underfitting.
  - $\lambda$ muy pequeño: $\theta^{(j)}$ muy grande, se tiende a overfitting.
  - Se puede usar el método de validación cruzada para elegir $\lambda$.

### Algoritmo descenso del gradiente sin regularización
- Actualizar $\theta_k^{(j)}$:
  - $\theta_k^{(j)} := \theta_k^{(j)} - \alpha \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)}) x_k^{(i)}$.
  - $\alpha$ es el ratio de aprendizaje.
  - Se actualizan todos los $\theta_k^{(j)}$ simultáneamente.
  - Se repite hasta convergencia.

### Algoritmo descenso del gradiente con regularización
- Actualizar $\theta_k^{(j)}$:
  - $\theta_k^{(j)} := \theta_k^{(j)} - \alpha \left( \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)}) x_k^{(i)} + \lambda \theta_k^{(j)} \right)$.
  - $\alpha$ es el ratio de aprendizaje.
  - Se actualizan todos los $\theta_k^{(j)}$ simultáneamente.
  - Se repite hasta convergencia.

## Filtrado colaborativo
- Se basa en la similitud entre usuarios o items.
- Se llama colaborativo porque se basa en la colaboración de los usuarios.

### Idea previa
- Partimos de la idea que no tendremos las características de los items, como teníamos en el filtrado basado en contenido. Es común ya que conseguir estas características puede ser costoso.
- Sí tendremos los parámetros $\theta^{(j)}$ de los usuarios. Es decir, conocemos las preferencias de los usuarios.
- Objetivo: Conseguir vectores de características $x^{(i)}$ para los items.
- Regresión lineal:
  - Función de coste: $J(x^{(i)}) = \frac{1}{2} \sum_{j:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{k=1}^n (x_k^{(i)})^2$.
  - Minimizar $J(x^{(i)})$ para cada item $i$.
  - Usaremos el descenso del gradiente.

### Objetivo de optimización
- Unión de las dos opciones:
  - Dados los parámetros $\theta^{(1)}, …, \theta^{(n_u)}$, queremos aprender los vectores de características $x^{(1)}, …, x^{(n_i)}$.
  - Dados $x^{(1)}, …, x^{(n_i)}$, queremos aprender los parámetros $\theta^{(1)}, …, \theta^{(n_u)}$.
- Se buscan simultáneamente los $x^{(i)}$ y los $\theta^{(j)}$ que minimicen la función de coste.
  - Podemos hacerlo iterando:
    - Fijamos $x^{(1)}, …, x^{(n_i)}$ y minimizamos $J(\theta^{(1)}, …, \theta^{(n_u)})$.
    - Fijamos $\theta^{(1)}, …, \theta^{(n_u)}$ y minimizamos $J(x^{(1)}, …, x^{(n_i)})$.
    - Repetimos hasta convergencia.
  - Otra opción es minimizar $J(x^{(1)}, …, x^{(n_i)}, \theta^{(1)}, …, \theta^{(n_u)})$ simultáneamente.
- La función de coste al unir las dos opciones es:
  - $J(x^{(1)}, …, x^{(n_i)}, \theta^{(1)}, …, \theta^{(n_u)}) = \frac{1}{2} \sum_{(i, j):r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{i=1}^{n_i} \sum_{k=1}^n (x_k^{(i)})^2 + \frac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^n (\theta_k^{(j)})^2$. 
  - Formula sin regularización: $J(x^{(1)}, …, x^{(n_i)}, \theta^{(1)}, …, \theta^{(n_u)}) = \frac{1}{2} \sum_{(i, j):r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2$.

### Algoritmo descenso del gradiente sin regularización
- Actualizar $x_k^{(i)}$:
  - $x_k^{(i)} := x_k^{(i)} - \alpha \sum_{j:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)}) \theta_k^{(j)}$.
  - $\alpha$ es el ratio de aprendizaje.
  - Se actualizan todos los $x_k^{(i)}$ simultáneamente.
  - Se repite hasta convergencia.

### Algoritmo descenso del gradiente con regularización
- Actualizar $x_k^{(i)}$:
  - $x_k^{(i)} := x_k^{(i)} - \alpha \left( \sum_{j:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)}) \theta_k^{(j)} + \lambda x_k^{(i)} \right)$.
  - $\alpha$ es el ratio de aprendizaje.
  - Se actualizan todos los $x_k^{(i)}$ simultáneamente.
  - Se repite hasta convergencia.

### Algoritmo Completo
1. Inicializar $x^{(1)}, … , x^{(n_i)}, \theta^{(1)}, … , \theta^{(n_u)}$ a valores random pequeños.
2. Minimizar $J(x^{(1)}, … , x^{(n_i)}, \theta^{(1)}, … , \theta^{(n_u)})$ usando descenso del gradiente, algoritmos optimizadores, etc.
3. Para un usuario con parámetros $\theta^{(j)}$ y un ítem con características óptimas $x^{(i)}$, predecir la valoración personalizada mediante la hipótesis del modelo: $(\theta^{(j)})^T x^{(i)}$.
4. Recomendaciones al usuario $j$ de los ítems $i$ con las predicciones más altas obtenidas en el paso 3.

[Volver al índice](../../README.md)

[Ir al siguiente tema: Tema 8.1: Búsqueda no Informada](../Tema8/Tema8_1.md)