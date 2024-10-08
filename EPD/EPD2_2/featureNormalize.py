import numpy as np
import pandas as pd

# featureNormalize normalizes the features in X
# featureNormalize(X) returns a normalized version of X where
# the mean value of each feature is 0 and the standard deviation
# is 1. This is often a good preprocessing step to do when
# working with learning algorithms.

def featureNormalize(X):
    mu = X.mean()
    sigma = X.std()
    return ((X-mu) / sigma), mu, sigma

