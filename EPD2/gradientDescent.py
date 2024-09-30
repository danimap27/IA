import numpy as np
import matplotlib.pyplot as plt
from computeCost import computeCost 
def gradientDescent(X, y, theta, alpha, nIter):
    m = len(y)
    historico = []

    for i in range 1500



def plotIterationsVsCost(J_history):
    plt.plot(range(len(J_history)), J_history, 'b')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Coste J')
    plt.title('Convergencia del Descenso por Gradiente')
    plt.show()