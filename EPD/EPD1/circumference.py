import math
import matplotlib.pyplot as plt
import numpy as np

def circ(r):
    # Computing the long and area of a circumference
    diametro = 2*r
    long = math.pi*diametro
    area = math.pi * r**2
    return diametro, long, area

def parabola():
    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-10, 10, 1000)

    # Compute the function: y=x^2
    y = x ** 2
    plt.plot(x,y)
    plt.show()
    return y

