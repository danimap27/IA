import numpy as np

def computeCost(X,y,theta):
    # Vectorizando
    m = len(y)
    h = np.dot(X,theta)
    J = (1/(2*m))*np.sum((h - y)**2)
    return J