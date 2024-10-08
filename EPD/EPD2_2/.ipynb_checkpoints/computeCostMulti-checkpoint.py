import numpy as np
# computeCostMulti Compute cost for linear regression with multiple variables
#   J = computeCostMulti(X, y, theta) computes the cost of using theta as the
#   parameter for linear regression to fit the data points in X and y

def computeCostMulti(X, y, theta):
    # Initialize some useful values
 # number of training examples
    # You need to return the following variables correctly
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta
    #               You should set J to the cost.
    return ((np.sum(np.power((np.dot(X,theta)-y),2), axis=0))/(2*len(y) ))
