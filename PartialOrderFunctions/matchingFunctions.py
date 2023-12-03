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
    corr_matrix = np.corrcoef(X, Y)
    corr = corr_matrix[0,1]
    linear_R_sq = corr**2
    return linear_R_sq

def lineChartMatch(X, Y, threshold = .9):
    if Trend(X, Y, threshold):
        return 1
    else:
        return 0

def Trend(X, Y, threshold):
    #Testing linear distribution
    ##print('From Trend in matching Functions: ', X)
    ##print('From Trend in matching Functions: ', Y)
    corr_matrix = np.corrcoef(X, Y)
    corr = corr_matrix[0,1]
    linear_R_sq = corr**2

    if linear_R_sq >= threshold:   
        ##print(linear_R_sq, 'linear')   #DEBUGGING
        return True
    
    #Testing power low distribution

    #Testing log disribution
    corr_matrix = np.corrcoef(np.power(X,10), Y)
    corr = corr_matrix[0,1]
    log_R_sq = corr**2

    if log_R_sq >= threshold: 
        ##print(log_R_sq, 'log') #DEBUGGING
        return True
    
    #Testing exponential distribution
    try:
        with np.errstate(divide='ignore', invalid='ignore'):
            corr_matrix = np.corrcoef(np.log10(X), Y)
        corr = corr_matrix[0,1]
        exp_R_sq = corr**2

        if exp_R_sq >= threshold: 
            ##print(exp_R_sq, 'exponential') #DEBUGGING
            return True
    except Exception as e:
        #print(f'Error occurred in Trend in matchingFunctions.py: {e}')
        pass
   
    # If data doesnt have a trend
    return False
    

# QUALITY FUNCTIONS 
def quality(X, transformed_X_tuples):
    q = 1 - (transformed_X_tuples / len(X))
    return q

# COLUMN IMPORTANCE 
    # will implement at future date, requires use of Search Space metadata 

def getFunctionValues(viz):
    # Turning X and Y dataframes to a list bc thats the input the matching functions are looking for
    initX, initY = viz.transform()
    ##print("from getFunctionValue: ", initX.values.values)
    ##print("from getFunctionValue: ", initY.values.values)
    X = initX.values.values.flatten().tolist()
    Y = initY.values.values.flatten().tolist()
    features = viz.getFeatures()
    # Getting matching quality value
    if viz.visualization == 'bar':
        mv = barChartMatch(X, Y)
    elif viz.visualization == 'pie':
        mv = pieChartMatch(X, Y, viz.y_transform)
    elif viz.visualization == 'line':
        mv = lineChartMatch(X, Y)
    elif viz.visualization == 'scatter':
        mv = scatterChartMatch(X, Y)
    else:
        mv = 0

    # Getting transformation quality value
    qv = quality(X, features[1])

    # Getting the importance of columns
    wv = 0

    return mv, qv, wv
    

def calcWeight(v: Visualization, u: Visualization):
    mv, qv, wv = getFunctionValues(v)
    mu, qu, wu = getFunctionValues(u)
    
    #print("The mv, qv, and wv values of node v:", mv,qv,wv)
    #print("The mu, qu, and wu values of node u:", mu,qu,wu)

    weight = (mu - mv + qu - qv + wu - wv)/3

    return(weight)