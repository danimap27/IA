import numpy as np

# computeCost computes cost for linear regression using theta as the parameter for linear regression to fit the data points in X and y
def computeCost(X, y, theta):
    # Initialize some useful values
    # You need to return the following variables correctly
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta. You should set J to the cost.
    return ((np.sum(np.power((np.dot(X,theta)-y),2), axis=0))/(2*len(y) ))
