# Redes Neuronales

## Parte I: Fundamentos de Redes Neuronales

### 1. Motivación

- **Red Neuronal Artificial**:
  - Un modelo computacional inspirado en la estructura y funcionamiento de las neuronas en el cerebro humano.
  - La red neuronal se basa en una combinación de **neuronas artificiales** que pueden procesar datos y aprender a realizar tareas como clasificación o regresión.

- **Historia**:
  - Estas redes fueron muy populares en los años 80 debido a sus aplicaciones prometedoras.
  - Sin embargo, en los años 90, con la falta de avances tecnológicos, las redes neuronales cayeron en desuso (conocido como el "invierno de la IA").
  - En la última década, las redes neuronales han resurgido, gracias a la disponibilidad de grandes volúmenes de datos y avances en **deep learning**.

- **Objetivo**:
  - El objetivo principal de una red neuronal es encontrar **fronteras de decisión** para clasificar o hacer predicciones.
  - Estas fronteras pueden ser:
    - **Lineales**: Cuando los datos se separan de manera simple con una línea recta.
    - **No lineales**: Cuando se requiere una curva o una superficie más compleja para separar los datos.

### 2. Neurona Artificial

- **Neuronas Biológicas vs. Artificiales**:
  - Las neuronas biológicas son la unidad básica del cerebro, encargadas de procesar y transmitir información mediante impulsos eléctricos.
  - Las neuronas artificiales son una simplificación computacional que imita este comportamiento.
  - Cada neurona artificial recibe **entradas** ($\( x_1, x_2, ... x_n \$)) que se multiplican por un conjunto de **pesos** ($\( \theta_1, \theta_2, ... \theta_n \$)).
  - La neurona genera una salida a través de una función de activación.

- **Modelo de Regresión Lineal**:
  - En su forma más básica, una neurona realiza una **regresión lineal**:
    - $\( y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n \$)
  - Los **pesos** determinan la importancia de cada entrada.
  - El **sesgo (bias)**, representado como $\( \theta_0 \$), actúa como un término independiente que ayuda a ajustar la salida de la neurona.
  
- **Puertas Lógicas**:
  - Las neuronas artificiales pueden simular comportamientos como las puertas lógicas **AND**, **OR** y **XOR**:
    - Puerta **AND**: Solo produce una salida positiva si ambas entradas son positivas.
    - Puerta **XOR**: No puede resolverse con una sola neurona, ya que los datos no son linealmente separables.

### 3. Red Neuronal

- **Organización de las Redes**:
  - Las redes neuronales se organizan en **capas**:
    - **Capa de Entrada**: Recibe los datos de entrada.
    - **Capas Ocultas**: Intermediarias, donde ocurre el procesamiento principal.
    - **Capa de Salida**: Entrega la predicción final.
  - Las redes pueden modelar **relaciones complejas** al combinar múltiples neuronas.

- **Funciones de Activación**:
  - La regresión lineal por sí sola no puede resolver problemas complejos, por lo que se utilizan **funciones de activación no lineales**.
  - Estas funciones permiten **encadenar** las salidas de una neurona a la entrada de otra y hacer que el modelo sea más flexible:
    - **Función Sigmoide**: Común en clasificación, ya que su salida es una probabilidad entre 0 y 1.
    - **ReLU (Rectified Linear Unit)**: Amplia popularidad en redes profundas por su simplicidad y eficacia en evitar problemas de gradientes pequeños.

### 4. Propagación hacia Adelante (Forward Propagation)

- **Definición**:
  - La **propagación hacia adelante** es el proceso mediante el cual la información (las entradas) se mueve a través de las capas de la red neuronal para generar una predicción.
  
- **Proceso**:
  - En cada capa, las entradas se combinan con los **pesos** y se aplican las funciones de activación para producir una salida.
  - Este proceso continúa hasta llegar a la **capa de salida**, que genera la predicción final.
  
- **Matemáticas detrás de Forward Propagation**:
  - Si $\( a^{(l)} \$) es la activación en la capa $\( l \$), $\( \Theta^{(l)} \$) son los pesos asociados a esa capa, y $\( z^{(l)} \$) es la combinación lineal de las entradas, entonces:
    - $\( z^{(l+1)} = \Theta^{(l)} a^{(l)} \$)
    - $\( a^{(l+1)} = f(z^{(l+1)}) \$), donde $\( f \$) es la función de activación.
  - Este proceso se repite hasta obtener la salida.

---

## Parte II: Entrenamiento de Redes Neuronales

### 1. Función de Coste en Redes Neuronales

- **Objetivo**: 
  - Minimizar el error de la red comparando las predicciones con los resultados reales. Este error se mide mediante una **función de coste**.
  
- **Tipos de Problemas**:
  - **Clasificación Binaria**: Una salida que clasifica en dos categorías (e.g., 0 o 1).
  - **Clasificación Multiclase**: Varias salidas que asignan una instancia a una de varias clases posibles (e.g., reconocer peatones, coches, motos, camiones en imágenes).

- **Función de Coste (Error Cuadrático Medio)**:
  - Para redes neuronales, una función común es el **error cuadrático medio**:
    - $\( J(\theta) = \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2 \$)
  - Donde $\( h_\theta(x^{(i)}) \$) es la predicción de la red y $\( y^{(i)} \$) es el valor real.

### 2. Descenso del Gradiente y Backpropagation

- **Descenso del Gradiente**:
  - Algoritmo para optimizar los **pesos** de la red minimizando la función de coste.
  - En cada iteración, ajusta los pesos en la dirección opuesta al gradiente de la función de coste con respecto a esos pesos.
  - Fórmula:
    - $\( \theta := \theta - \alpha \cdot \nabla J(\theta) \$)
    - Donde $\( \alpha \$) es el **tamaño del paso** o tasa de aprendizaje, y $\( \nabla J(\theta) \$) es el gradiente de la función de coste.

- **Backpropagation**:
  - Algoritmo utilizado para calcular el **gradiente** de la función de coste con respecto a cada peso de la red.
  - Se utiliza para ajustar los pesos en función del error que contribuye cada neurona en la salida.
  
- **Intuición**:
  - El objetivo es calcular la "culpa" de cada neurona en el error final.
  - Se retropropaga el error desde la capa de salida hacia las capas intermedias, calculando cómo cada peso ha contribuido al error.

### 3. Implementación en Python

#### 1. Unroll y roll de Parámetros

En la implementación de redes neuronales, a menudo necesitamos "desenrollar" los parámetros (pesos de las conexiones entre neuronas) en un vector para luego aplicar funciones de optimización. Al final del proceso, los "enrollamos" nuevamente en matrices.

- **Desenrollar Parámetros**:
Los pesos de cada capa se almacenan inicialmente en matrices $\( \Theta_1, \Theta_2, \dots, \Theta_L \$). Para aplicar algoritmos de optimización, desenrollamos estas matrices en un único vector. Esto es útil en la optimización avanzada, ya que los algoritmos esperan los parámetros en esta forma de vector.

- **Enrollar Parámetros**:
Después de aplicar un algoritmo de optimización, el vector resultante debe "enrollarse" de nuevo en las matrices correspondientes a cada capa para ser utilizado en las predicciones. De esta manera, cada subconjunto de parámetros se transforma nuevamente en su forma matricial, lo que permite realizar cálculos en la red neuronal.

---

#### 2. Función de Coste y Gradiente

La función de coste se utiliza para medir el error de la red y ajustar los parámetros de la red para minimizar ese error. La función de coste se compone del error entre las predicciones y las etiquetas verdaderas. Para mejorar la capacidad de generalización de la red, se utiliza un término de **regularización** para penalizar los pesos elevados.

- **Función de Coste**:
El objetivo de la función de coste es minimizar la diferencia entre la salida esperada y la predicción de la red. La función incluye un término de regularización que penaliza los valores grandes en los pesos para evitar el sobreajuste de los datos.

- **Gradiente**:
El cálculo del gradiente permite ajustar los pesos de la red. El algoritmo de **backpropagation** se utiliza para calcular cómo cada parámetro de la red contribuye al error total. Esto permite actualizar los pesos en dirección opuesta al gradiente para minimizar el error. El término de regularización también se incluye en el cálculo del gradiente para evitar un crecimiento excesivo de los parámetros.

---

#### 3. Propagación hacia Adelante (Forward Propagation)

La **propagación hacia adelante** es el proceso mediante el cual las entradas de la red neuronal pasan a través de las diferentes capas, hasta llegar a la capa de salida, donde se genera la predicción. En cada capa, las entradas se combinan con los pesos y se aplican funciones de activación para producir salidas intermedias, que luego se utilizan como entradas para la siguiente capa.

La salida de la red es el resultado final de este proceso de múltiples capas, y es comparada con el valor esperado durante el entrenamiento para calcular el error.

---
  ```python
  def forward(Theta1, Theta2, X):
      # Añadir bias + neuras de la capa 1
      a1 = np.hstack((np.ones(1), X))
      z2 = Theta1 @ a1
      a2 = sigmoid(z2)
      # Añadir bias en la segunda capa
      a2 = np.hstack((np.ones(1), a2))
      z3 = Theta2 @ a2
      a3 = sigmoid(z3)
      return a3  # Predicción final
  ```
#### 4. Comprobación Numérica del Gradiente

Es crucial verificar que el gradiente calculado con **backpropagation** es correcto. Para esto, se puede realizar una **comprobación numérica del gradiente** comparando el valor del gradiente calculado mediante backpropagation con una aproximación numérica del gradiente.

La **fórmula de diferencia central** se utiliza para aproximar el gradiente. Esta comprobación asegura que los gradientes calculados no contienen errores, lo cual es crucial para la correcta actualización de los pesos.

---

#### 5. Inicialización de Parámetros

Es importante inicializar los pesos de la red neuronal con valores **aleatorios pequeños** para evitar problemas de simetría. Si todos los pesos se inician con ceros o valores iguales, las neuronas aprenderán características idénticas y el entrenamiento no será efectivo.

La inicialización aleatoria rompe la simetría y asegura que las neuronas puedan aprender diferentes características de los datos.

```python
def initializeWeights(L_in, L_out):
    epsilon = 0.12
    return np.random.rand(L_out, 1 + L_in) * 2 * epsilon - epsilon
```

---
  

[Volver al índice](../README.md)
