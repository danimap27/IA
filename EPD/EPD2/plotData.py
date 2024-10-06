import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
# plotData plots the data points x and y into a new figure
# plotData(x,y) plots the data points and gives the figure axes labels of population and profit.
from computeCost import computeCost

################################
######### EJERCICIO 01 #########
################################
def plotData(X, y):
    # ====================== YOUR CODE HERE ======================
    # Instructions: Plot the training data into a figure using the "scatter" and "show"
    #               commands of the library "matplotlib".
    #               Set the axes labels using the "xlabel" and "ylabel" commands.
    #               Assume the population and revenue data have been passed in as the X and y arguments of this function.
    # Hint: You can use the 'x' and 'red' options with plot to have the markers appear as red crosses.
    plt.scatter(X, y, color='red', marker='x')
    plt.xlabel('Población de la ciudad (en 10,000s)')
    plt.ylabel('Beneficios (en 10,000s)')
    plt.title('Beneficios vs. Población')


    
################################
################################

def plotIterationsVsCost(J_history, alpha):
    plt.plot(J_history['iteracion'], J_history['cost'])
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Plot to check if gradient descent is working correctly with alpha: '+str(alpha))
    plt.show()


def plotData_linearRegression(X, y, theta):
    plt.scatter(x=X['poblacion'], y=y, marker="x", c="red", label="Training data")
    plt.plot(X['poblacion'], np.dot(X, theta), c='blue', label="Linear regression") # h  -> mi modelo
    plt.xlabel("Population of City in 10,000")
    plt.ylabel("Profit in $10,000")
    plt.xticks(np.arange(5, 26, 5))
    plt.xlim(5, 25)
    plt.ylim(-5, 25)
    plt.legend()
    plt.show()

def plotData_cost(X, y, theta):
    # Grid over which we will calculate J
    theta0_vals = np.linspace(-10, 10, 100)
    theta1_vals = np.linspace(-1, 4, 100)

    # Initialize J_vals to a matrix of 0's
    J_vals = np.zeros((len(theta0_vals), len(theta1_vals)))

    # Fill out J_vals
    for i in range(1, len(theta0_vals)):
        for j in range(1, len(theta1_vals)):
            theta_ij = [[theta0_vals[i]], [theta1_vals[j]]]
            J_vals[i][j] = computeCost(X, y, theta_ij)

    # Because of the way meshgrids work in the surf command, we need to
    # transpose J_vals before calling surf, or else the axes will be flipped
    J_vals = J_vals.T

    # Surface plot
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    theta0_vals, theta1_vals = np.meshgrid(theta0_vals, theta1_vals)
    surf = ax.plot_surface(theta0_vals, theta1_vals, J_vals, cmap = cm.jet, rstride = 2, cstride = 2) #linewidth = 0, antialiased = False)
    #fig.colorbar(surf, shrink = 0.5, aspect = 5)
    plt.xlabel("theta_0")
    plt.ylabel("theta_1")
    plt.show()

    fig1, bx = plt.subplots(1,1)
    contour = bx.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20))
    fig1.colorbar(contour)
    plt.xlabel("theta_0")
    plt.ylabel("theta_1")
    plt.plot(theta[0], theta[1], marker = 'x', c='red')
    plt.show()

def plotData_problema3(X, y, theta):
    plt.scatter(X[['tam']], y[['precio']], marker="x", c="red", label="Training data")
    plt.plot(X[['tam']], np.dot(X[['uno','tam']], theta), c='blue', label="Linear regression")
    plt.xlabel("Population of City in 10,000")
    plt.ylabel("Profit in $10,000")
    plt.xlim(5, 25)
    plt.ylim(-5, 25)
    plt.legend()
    plt.show()
