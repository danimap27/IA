# Tema 2: Introducción al Machine Learning

## ¿Qué es el Machine Learning?
Es un subconjunto de la inteligencia artificial que permite a las computadoras aprender sin ser explícitamente programadas.  
- **Definición de Arthur Samuel (1959):** “Field of study that gives computers the ability to learn without being explicitly programmed.”  
- **Definición de Tom Mitchell (1998):** Un programa de ordenador aprende a partir de una experiencia **E** al realizar una tarea **T** (de acuerdo con una medida de rendimiento **P**), si su rendimiento al realizar **T** mejora.

### Ejemplo de Machine Learning:
- **Tarea T:** Clasificación de correos electrónicos como spam o no spam.
- **Experiencia E:** Análisis de correos previamente clasificados para aprender patrones.

## Idea General de Programación
1. **Programación tradicional:** El programador define las reglas para automatizar una tarea.
2. **Machine Learning (Aprendizaje supervisado):** El sistema aprende las reglas automáticamente a partir de datos de entrenamiento.

### Aprendizaje Supervisado
Se usa para hacer predicciones relacionadas con un **atributo objetivo** o clase.
- **Regresión:** Predicción de valores numéricos.
- **Clasificación:** Predicción de valores categóricos.

### Aprendizaje No Supervisado
No busca predecir nuevos datos, sino entender las propiedades de los datos existentes.
- Ejemplos: Agrupación (Clustering), análisis de patrones.

---

## Diseño de Sistemas de Aprendizaje

### Metodología CRISP-DM
1. **Comprensión del negocio:** Identificación del problema y establecimiento de objetivos.
2. **Comprensión de los datos (EDA):** Exploración y análisis de los datos disponibles.
3. **Preparación de los datos:** Extracción, transformación y carga (ETL) de los datos.
4. **Modelado:** Selección, configuración y aplicación de algoritmos de Machine Learning.
5. **Evaluación de negocio:** Interpretación y análisis de los resultados.
6. **Despliegue:** Implementación del modelo en un entorno de producción.

---

## Comprensión de los Datos

La experiencia **E** en el Machine Learning se refiere a los datos con los que el sistema aprenderá.
- **Training Set (Datos de entrenamiento):** Datos utilizados durante el proceso de aprendizaje. Deben ser completos y de alta calidad.

### Posibles problemas en los datos de entrenamiento:
- **Ruido**
- **Valores ausentes**
- **Proporción inadecuada entre atributos e instancias**
- **Problemas de dimensionalidad o mala selección de atributos**

---

## Preparación de los Datos

### Proceso ETL:
1. **Extracción:** Obtener datos de diversas fuentes (bases de datos, APIs, web scraping, etc.).
2. **Transformación:** Limpieza, cambio de formato o tipo de datos, normalización, etc.
3. **Carga:** Almacenar los datos transformados.

### Preprocesamiento de datos
Objetivo: Obtener un conjunto de datos de alta calidad.  
Ejemplos:
- **Tratamiento de valores ausentes.**
- **Detección de outliers.**
- **Normalización y discretización de los datos.**
- **Selección de atributos.**

---

## Modelado

Definiremos una función desconocida **f** que queremos aprender.
- **Ejemplo 1:** Predicción de precios de casas → f: Casa → R.
- **Ejemplo 2:** Clasificación de emails como spam → f: Email → {Spam, No Spam}.

### Tipos de modelos:
1. **Black Box:** No ofrece interpretabilidad, como las redes neuronales profundas.
2. **Symbolic Modeling:** Modelos más interpretables, como árboles de decisión.

### Elegir el modelo de Machine Learning
Existen diferentes algoritmos para resolver distintos problemas:
- **Regresión.**
- **Clasificación.**
- **Clustering.**

Se pueden probar varios modelos y comparar sus errores usando pruebas estadísticas. Además, los algoritmos suelen tener parámetros que deben ser ajustados para optimizar el rendimiento.

---

## Evaluación y Métricas del Modelado

### Métricas de evaluación:

#### 1. **Regresión:**
- **MAE:** Error absoluto medio.
- **MSE:** Error cuadrático medio.
- **RMSE:** Raíz del error cuadrático medio.

#### 2. **Clasificación:**
- **Matriz de confusión:** Muestra el número de predicciones correctas e incorrectas.
- **Accuracy, Precisión, Sensibilidad (Recall), F1 Score:** Indicadores clave para medir el rendimiento del modelo.

---

## Conjuntos de Datos para Evaluación

Se usan diferentes conjuntos de datos para evaluar los modelos:
1. **Training Set:** Para entrenar los modelos.
2. **Validation Set:** Para ajustar hiperparámetros y seleccionar el mejor modelo.
3. **Test Set:** Para evaluar el rendimiento final del modelo.

---

## Técnicas de Evaluación

### Hold-out
Se separa el dataset en un porcentaje para entrenamiento y otro para evaluación. Es una técnica sencilla si se cuenta con muchos datos etiquetados.

### Validación Cruzada (k-fold cross validation)
Se divide el dataset en **k** subconjuntos y el modelo se entrena y evalúa **k** veces, usando diferentes combinaciones de subconjuntos. El error global se calcula promediando los errores de las **k** iteraciones.

### Validación Cruzada "Leave One Out" (LOOCV)
Para cada iteración, se usa una única instancia como conjunto de prueba y el resto como conjunto de entrenamiento. Es computacionalmente costoso pero evita el submuestreo aleatorio.

---


[Volver al índice](../README.md)

[Ir al siguiente tema: Tema 3: Regresión Lineal](Tema3.md)