# BLOQUE II: Cosas a tener en cuenta en el examen
## Clustering
### Algoritmo de K-means
- Inicialización de los centroides
    - Aleatoria
    - K-means++
- Número de clusters
    - Método del codo
    - Manual
- Asignación de puntos a clusters con distancia euclídea: $c^{(i)} = \arg\min_{k} ||x^{(i)} - \mu_k||^2$
- Actualización de los centroides con la media de los puntos asignados: $\mu_k = \frac{\sum_{i=1}^{m} 1\{c^{(i)} = k\} x^{(i)}}{\sum_{i=1}^{m} 1\{c^{(i)} = k\}}$
- Ver el coste
- Repetir hasta convergencia o máximo de iteraciones

### Tips en el código
- Primero se inicializan los centroides:
```python
# Inicialización de los centroides
def kMeansInitCentroids(X, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    idx = np.random.randint(0, m, K)
    for i in range(K):
        centroids[i] = X[idx[i]]
    return np.asarray(centroids)
```
- Luego se asignan los puntos a los clusters:
```python
# Asignar puntos a clusters
def findClosestCentroids(X, centroids):
    K = centroids.shape[0]
    cluster = []
    for i in range(len(X)):
        dist_eu = []
        for j in range(K):
            dist_eu.append(np.sqrt(np.sum(np.abs(X[i] - centroids[j])**2)))
        cluster.append(np.argmin(dist_eu))
    return np.asarray(cluster)
```	
- Después se actualizan los centroides:
```python
# Actualizar centroides
def computeCentroids(X, idx, K):
    centroids = np.zeros((K, X.shape[1]))
    for i in range(K):
        if np.sum(idx == i) == 0:
            centroids[i] = X[np.random.rand(0, X.shape[0])]
        else:
            centroids[i] = np.mean(X[idx == i], axis=0)
    return centroids
```
- Por último, se repite el proceso hasta convergencia con k-means:
```python
# K-means
def runkMeans(X, initial_centroids, max_iters):
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    for i in range(max_iters):
        idx = findClosestCentroids(X, centroids)
        centroids = computeCentroids(X, idx, K)
    return centroids, idx
```
- Método del codo:
```python
# Método del codo
def elbowMethod(X, K):
    cost = []
    for k in range(1, K+1):
        initial_centroids = kMeansInitCentroids(X, k)
        centroids, idx = runkMeans(X, initial_centroids, 10)
        cost.append(computeCost(X, centroids, idx))
    plt.plot(range(1, K+1), cost)
    plt.xlabel('Número de clusters')
    plt.ylabel('Coste')
    plt.title('Método del codo')
    plt.show()
```
- Coste:
```python
# Calcular coste
def computeCost(X, centroids, idx):
    m = X.shape[0]
    cost = 0
    for i in range(m):
        cost += np.sum(np.abs(X[i] - centroids[idx[i]])**2)
    return cost / m
```

## Sistemas de recomendación
### Basados en contenido
- Coste con regularización:
$J(\theta^{(j)}) = \frac{1}{2} \sum_{i:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{k=1}^n (\theta_k^{(j)})^2$

### Filtrado colaborativo
- Coste con regularización:
$J(x^{(i)}) = \frac{1}{2} \sum_{j:r(i, j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{\lambda}{2} \sum_{k=1}^n (x_k^{(i)})^2$

### Tips en el código
- Coste con regularización:
```python
# Coste con regularización
def cofiCostFuncReg(params, Y, R, num_features, lambda_param):
    num_movies, num_users = Y.shape
    
    # Desenrollar parámetros
    X = np.reshape(params[:num_movies*num_features], (num_movies, num_features), 'F')
    Theta = np.reshape(params[num_movies*num_features:], (num_features, num_users), 'F')
    J = 0
    
    error = np.multiply(np.dot(X, Theta) - Y, R)
    squared_error = np.power(error, 2)
    J = 1/2 * np.sum(squared_error)
    
    # Regularización
    J += lambda_param/2 * (np.sum(np.power(Theta, 2)) + (lambda_param/2)* np.sum(np.power(X, 2)))
    
    return J
```
- Desenrollar parámetros:
```python
# Desenrollar parámetros
params_sub = np.hstack((np.ravel(X, order='F'), np.ravel(Theta, order='F')))
```
- Enrollar parámetros:
```python
# Enrollar parámetros
X = np.reshape(params[:num_movies*num_features], (num_movies, num_features), 'F')
Theta = np.reshape(params[num_movies*num_features:], (num_features, num_users), 'F')
```
- Función del gradiente con regularización:
```python
# Gradiente con regularización
def cofiGradientFuncReg(params, Y, R, num_features, lambda_param):
    num_movies, num_users = Y.shape
    
    # Desenrollar parámetros
    X = np.reshape(params[:num_movies*num_features], (num_movies, num_features), 'F')
    Theta = np.reshape(params[num_movies*num_features:], (num_features, num_users), 'F')
    
    X_grad = np.zeros(X.shape)
    Theta_grad = np.zeros(Theta.shape)
    
    # Coste
    error = np.multiply(np.dot(X, Theta) - Y, R)
    X_grad = np.dot(error, Theta.T)
    Theta_grad = np.dot(X.T, error)
    X_grad += lambda_param * X
    Theta_grad += lambda_param * Theta
    
    # Desenrollar gradientes
    grad = np.hstack((np.ravel(X_grad, order="F"), np.ravel(Theta_grad,order="F")))

    return grad
```
- Función Optimizadora:
```python
fmin = opt.fmin_cg(gtol=g_tol, maxiter=300,f=cofiCostFuncReg, x0=params_rnd, fprime=cofiGradientFuncReg, args=(Ynorm, R, features, lambda_param))
```
- Normalizar datos:
```python
# Normalizar datos
def normalizeRatings(Y, R):
    m, n = Y.shape
    Ymean = np.zeros(m)
    Ynorm = np.zeros(Y.shape)
    for i in range(m):
        idx = R[i, :] == 1
        Ymean[i] = np.mean(Y[i, idx])
        Ynorm[i, idx] = Y[i, idx] - Ymean[i]
    return Ynorm, Ymean
```
- Sacar recomendaciones para un usuario:
```python
# Sacar recomendaciones para un usuario
predictions = np.dot(X_fmin, Theta_fmin)
# Solo el usuario j
j = 2
res_user = np.zeros((movies, 1))
pred_userj = predictions[:, j] # Seleccionar el usuario j
res_user = np.where(R[:, j] == 0, pred_userj, 0).reshape(-1, 1)
# Para cada película: A las que tenían valor previo le ponemos un 0 y a las que hemos predicho el valor de su predicción
idx = np.argsort(res_user, axis=0)[::-1] # Ordenar por las predicciones de menor a mayor y coger sus índice. [::-1] significa que le damos la vuelta a la salida: es decir lo colocamos de mayor a menor
print("Recomendaciones para el usuario j")
for i in range(10):
    print("Película: ", movieList[idx[i]], "Predicción: ", res_user[idx[i]])
```
- Sacar recomendaciones para una película:
```python
# Sacar recomendaciones para una película
predictions = np.dot(X_fmin, Theta_fmin)
# Solo la película i
i = 2
res_movie = np.zeros((users, 1))
pred_moviei = predictions[i, :] # Seleccionar la película i
res_movie = np.where(R[i, :] == 0, pred_moviei, 0).reshape(-1, 1)
# Para cada usuario: A los que tenían valor previo le ponemos un 0 y a los que hemos predicho el valor de su predicción
idx = np.argsort(res_movie, axis=0)[::-1] # Ordenar por las predicciones de menor
print("Recomendaciones para la película i")
for i in range(10):
    print("Usuario: ", idx[i], "Predicción: ", res_movie[idx[i]])
```