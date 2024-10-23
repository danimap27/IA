# Tema 4: Regresión Logística

## 1. Regresión Logística Binaria
- **Aprendizaje supervisado:** Se trata de un problema de clasificación.
- **Salida:** Valores discretos.
- **Ejemplos:**
  - Predecir si lloverá o no.
  - Clasificar si un tumor es benigno o maligno (0: negativo, 1: positivo).

### Diferencias con la Regresión Lineal
- En la regresión logística, la hipótesis está entre 0 y 1: $0 \leq h_\theta(x) \leq 1$.
- La regresión lineal puede predecir valores mayores de 1 o menores de 0, lo cual no es adecuado para problemas de clasificación.

---

## 2. Hipótesis
- Se utiliza la **función sigmoide** o logística:
  $\[
  g(z) = \frac{1}{1 + e^{-z}}
  \]$
- Hipótesis del modelo de regresión logística:
  $\[
  h_\theta(x) = g(\theta^T x)
  \]$
  - $h_\theta(x)$ es la probabilidad estimada de que $y = 1$.
  
### Ejemplo:
- Si $h_\theta(x) = 0.7$, hay un 70% de probabilidad de que $y = 1$.

---

## 3. Función Coste
- La función coste utilizada en regresión logística es:
  $\[
  J(\theta) = - \frac{1}{m} \sum_{i=1}^{m} \left[ y_i \log(h_\theta(x_i)) + (1 - y_i) \log(1 - h_\theta(x_i)) \right]
  \]$
- Esta función es convexa, lo que garantiza que tiene un mínimo global.

### Interpretación:
- Si $y = 1$: $\text{Coste} = - \log(h_\theta(x))$.
- Si $y = 0$: $\text{Coste} = - \log(1 - h_\theta(x))$.

---

## 4. Descenso del Gradiente
- Igual que en la regresión lineal, se utiliza el descenso del gradiente para minimizar la función coste:
  $\[
  \theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x_i) - y_i \right) x_j
  \]$
  Donde $\alpha$ es la tasa de aprendizaje.
  
### Vectorización en Python:
```python
def gradientFunction(theta, X, y):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    return (1/m) * (np.dot(X.T, (h - y)))
```
---

## 5. Optimización Avanzada
- Otros algoritmos de optimización (además del descenso del gradiente) incluyen:
  - **Conjugate Gradient (CG)**
  - **BFGS**
  - **L-BFGS**
- Estos algoritmos no requieren seleccionar la tasa de aprendizaje y suelen converger más rápido.

---

## 6. Clasificación Multiclase
- Ejemplo: **Iris dataset**, donde se clasifican flores en 3 tipos:
  $\[
  y \in \{0, 1, 2\} \quad (0: iris-setosa, 1: iris-versicolor, 2: iris-virginica)
  \]$

---

## 7. OneVsAll
- Para problemas multiclase, se entrena un clasificador de regresión logística binaria para cada clase $i$.
- La predicción se hace seleccionando la clase que maximiza $h_\theta^{(i)}(x)$.

---

## 8. Sobreajuste
- **Overfitting (Sobreajuste):** Ocurre cuando el modelo se ajusta demasiado bien a los datos de entrenamiento, pero no generaliza bien con nuevos datos.
- **Underfitting (Subajuste):** Ocurre cuando el modelo no se ajusta bien ni siquiera a los datos de entrenamiento.

### Ejemplo:
- Regresión logística con una frontera de decisión muy compleja puede sobreajustar los datos.

---

## 9. Regularización
- **Objetivo:** Reducir el sobreajuste manteniendo todas las variables del modelo, pero penalizando grandes valores de los parámetros $\theta$.
- **Función coste regularizada:**
  $\[
  J(\theta) = - \frac{1}{m} \sum_{i=1}^{m} \left[ y_i \log(h_\theta(x_i)) + (1 - y_i) \log(1 - h_\theta(x_i)) \right] + \frac{\lambda}{2m} \sum_{j=1}^{n} \theta_j^2
  \]$
  Donde $\lambda$ es el parámetro de regularización que controla la cantidad de penalización.

---

## Regularización en la Regresión Logística
- El descenso del gradiente para la regresión logística con regularización incluye el término de regularización:
  $\[
  \theta_j := \theta_j - \alpha \left[ \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x_i) - y_i \right) x_j + \frac{\lambda}{m} \theta_j \right]
  \]$

---

[Volver al índice](../README.md)

[Ir al siguiente tema: Tema 5: Redes Neuronales](Tema5.md)