'''
Features:
1) d(X), number of distinct values in column X
2) |X|, number of tuples in column X
3) r(X), ratio of unique values in col X
4) max(X) and min(X)
5) T(X), data type of column
6) c(X,Y), correlation of two columns 
7) visualization type

Input into these functions:
X column data
Y column data

'''

import numpy as np
from classes.visualization import Visualization

# MATCHING FUNCTIONS
# Py(Y): calculates the probability of a elem of Y occuring in Y
# Input: column 
# Output: Dictionary of values and probabilities
def Py(Y):
    unique_vals, unique_counts = np.unique(np.array(Y), return_counts=True)
    n = len(Y)
    prob = {}

    for i in range(0, len(unique_vals)):
        proby = unique_counts[i] / n
        prob.update({unique_vals[i] : proby})

    return prob

# pieChartMatch: 

def pieChartMatch(X, Y, transY = None):
    if transY == 'avg':
        return 0
    if len(set(X)) == 1:    # Number of distinct values is 1
        return 0        
    elif (min(Y) < 0):      # The min of Y is below 0
        return 0
    elif len(set(X)) >= 2 and len(set(X)) <= 10:
        probs = Py(Y)
        sum = 0
        for val in probs.values():
            sum += -val * np.log10(val)
        return sum
    elif len(set(X)) > 10:
        probs = Py(Y)
        sum = 0
        for val in probs.values():
            sum += -val * np.log10(val)
        return sum * (10/len(set(X)))

def barChartMatch(X, Y):
    if len(set(X)) == 1:
        return 0
    elif len(set(X)) >= 2 and len(set(X)) <= 20:
        return 1
    elif len(set(X)):
        return (20/len(set(X)))
    
# Need to implement different types of correlation in the future
def scatterChartMatch(X,Y):
    return np.corrcoeff(X,Y)

def lineChartMatch(X, Y, threshold = .9):
    if Trend(X, Y, threshold):
        return 1
    else:
        return 0

def Trend(X, Y, threshold):
    #Testing linear distribution
    corr_matrix = np.corrcoef(X, Y)
    corr = corr_matrix[0,1]
    linear_R_sq = corr**2

    if linear_R_sq >= threshold:   
        #print(linear_R_sq, 'linear')   #DEBUGGING
        return True
    
    #Testing power low distribution

    #Testing log disribution
    corr_matrix = np.corrcoef(np.power(X,10), Y)
    corr = corr_matrix[0,1]
    log_R_sq = corr**2

    if log_R_sq >= threshold: 
        #print(log_R_sq, 'log') #DEBUGGING
        return True
    
    #Testing exponential distribution
    corr_matrix = np.corrcoef(np.log10(X), Y)
    corr = corr_matrix[0,1]
    exp_R_sq = corr**2

    if exp_R_sq >= threshold: 
        #print(exp_R_sq, 'exponential') #DEBUGGING
        return True
   
    # If data doesnt have a trend
    return False

# QUALITY FUNCTIONS 
def quality(X, Y):
    return 0

def getFunctionValues(viz):
    # Getting matching quality value
    if viz.visualiztion == 'bar':
        mv = barChartMatch(viz.X, viz.Y)
    elif viz.visualiztion == 'pie':
        mv = pieChartMatch(viz.X, viz.Y, viz.y_transform)
    elif viz.visalization == 'line':
        mv = lineChartMatch(viz.X, viz.Y)
    elif viz.visualization == 'scatter':
        mv = scatterChartMatch(viz.X, viz.Y)
    else:
        mv = 0

    # Geting transformation quality value

    

def calcWeight(v: Visualization, u: Visualization):
    mv, qv, wv = getFunctionValues(v)
    mu, qu, wu = getFunctionValues(u)
    