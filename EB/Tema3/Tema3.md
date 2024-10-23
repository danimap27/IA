# Tema 3: Regresión Lineal

## Regresión Lineal Univariable
- **Aprendizaje supervisado:** Se predice una salida que es un valor real (problema de regresión).
- **Modelo:** Se utiliza una sola variable para predecir el valor de salida.

### Representación del Modelo
La hipótesis del modelo es:
    $\ h_\theta(x) = \theta_0 + \theta_1 x \$  
Donde:
- 𝑥 es la variable de entrada.
-  $\ h_\theta(x)$ es la predicción de la variable de salida.

### Función Coste
Para evaluar la precisión del modelo, se utiliza la **función coste**, que mide el error entre los valores predichos y los valores reales.
La función coste se expresa como $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x_i) - y_i)^2$.


### Descenso del Gradiente
El algoritmo de **descenso del gradiente** se utiliza para minimizar la función coste ajustando los valores de $\(\theta_0\) y \(\theta_1\).
\[
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)
\]$
Donde $\(\alpha\)$ es la tasa de aprendizaje.

---

## Regresión Lineal Multivariable
En este caso, se utilizan múltiples variables de entrada para predecir el valor de salida.

### Representación del Modelo
La hipótesis del modelo es:
$\[
h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + \dots + \theta_nx_n
\]$

### Feature Scaling / Escalado de Variables
Es importante que todas las variables de entrada tengan una escala similar para que el descenso del gradiente converja rápidamente.

### Ecuación Normal
La **ecuación normal** ofrece una solución analítica a la regresión lineal sin necesidad de usar el descenso del gradiente:
$\[
\theta = (X^TX)^{-1}X^Ty
\]$

---

[Volver al índice](../README.md)

[Ir al siguiente tema: Tema 4: Regresión Logística](Tema4.md)