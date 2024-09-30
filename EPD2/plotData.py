import matplotlib.pyplot as plt

def plotData(X, y):
    
    plt.figure()
    plt.scatter(X, y, color='red', marker='x')
    plt.xlabel('Población de la ciudad (en 10,000s)')
    plt.ylabel('Beneficios (en 10,000s)')
    plt.title('Beneficios vs. Población')