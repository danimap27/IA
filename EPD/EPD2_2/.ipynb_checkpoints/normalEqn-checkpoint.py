import numpy as np
# normalEqn Computes the closed-form solution to linear regression
# normalEqn(X,y) computes the closed-form solution to linear regression using the normal equations.

def normalEqn(X, y):
    #theta = np.zeros(size(X, 2), 1)

    # ====================== YOUR CODE HERE ======================
    # Instructions: Complete the code to compute the closed form solution
    #               to linear regression and put the result in theta.
    # ---------------------- Sample Solution ---------------------    
    return np.dot(np.dot(np.linalg.pinv(np.dot(X.T, X)), X.T), y)


