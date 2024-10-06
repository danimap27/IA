import numpy as np

# computeCost computes cost for linear regression using theta as the parameter for linear regression to fit the data points in X and y
def computeCost(X, y, theta):
    # Initialize some useful values
    m = len(y) # number of training examples
    # You need to return the following variables correctly
    J = 0.0
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta. You should set J to the cost.
    ones = np.ones((m, 1))
    X = np.hstack((ones,X))
    h = np.dot(X,theta)
    J = (1/(2*m))* np.sum((h - y)**2)
    return J
