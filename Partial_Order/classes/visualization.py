"""
Visualization class is the class produced by the search space generator,

X = the original X column
Y = the original Y column
visualization = the type of plot
x_transform = any transformations on X
y_transform = any transformation on Y
order_by = any order on X or Y (possible values include X', Y', or null)
"""
from .column import Column
from .features import Features
import pandas as pd
import numpy as np
import Partial_Order.Functions.matchingFunctions as mf

class Visualization: 
    def __init__(self, X: Column, Y: Column, x_transform = None, y_transform = None, order_by = None, visualization = None):
        self.X = X
        self.Y = Y
        self.visualization = visualization
        self.x_transform = x_transform
        self.y_transform = y_transform
        self.order_by = order_by
        if self.visualization != None:
            self.weight = self.calcWeight()
        else:
            self.weight = None

    def __str__(self):
        return f"{self.X.name}, {self.Y.name}, {self.x_transform}, {self.y_transform}, {self.order_by}, {self.visualization}, { self.weight }"

    def __eq__(self,other):
        if self.X.name != other.X.name:
            return False
        elif self.Y.name != other.Y.name:
            return False
        elif self.x_transform != other.x_transform:
            return False
        elif self.y_transform != other.y_transform:
            return False
        elif self.visualization != other.visualization:
            return False
        elif self.order_by != other.order_by:
            return False
        else:
            return True

    def transform(self):
        #dataset = pd.DataFrame({self.X.name: self.X.values, self.Y.name: self.Y.values}, columns=[self.X.name, self.Y.name])
        if self.X.type == 'Temporal':
            initX = self.X.values.sort_values(ascending=False).reset_index(drop=True)
        else:
            initX = self.X.values
        data = {'X': initX, 'Y': self.Y.values}
        df = pd.DataFrame(data)
        if  self.x_transform == 'group':
            if self.y_transform == 'avg':
                result = df.groupby('X')['Y'].mean().reset_index()
            elif self.y_transform == 'sum':
                result = df.groupby('X')['Y'].sum().reset_index()
            elif self.y_transform == 'cnt':
                result = df.groupby('X')['Y'].count().reset_index()
            else:
                result = df.groupby('X').reset_index()
        elif self.x_transform == 'bin':
            result = df
        else:
            result = df

        if self.X.type == 'Temporal':
            data = np.arange(0, len(result.loc[:,'X'].values), 1)
            X_col = Column('X', pd.DataFrame(list(data)), 'Numerical')
        else:
            X_col = Column('X', result.loc[:,'X'], self.X.type)
        
        Y_col = Column('Y', result.loc[:,'Y'], 'Numerical')
        return X_col, Y_col

    # Ideally will connect to Feature class a be able to retrive features
    def getFeatures(self):
        X, Y = self.transform()
        return Features(X, Y, self.visualization).calculate_features()
    
    def getFunctionValues(self):
        # Turning X and Y dataframes to a list bc thats the input the matching functions are looking for
        initX, initY = self.transform()
        ##print("from getFunctionValue: ", initX.type)
        ##print("from getFunctionValue: ", initY.type)
        X = initX.values.values.flatten().tolist()
        Y = initY.values.values.flatten().tolist()
        features = self.getFeatures()
        # Getting matching quality value
        if self.visualization == 'bar':
            mv = mf.barChartMatch(X, Y)
        elif self.visualization == 'pie':
            mv = mf.pieChartMatch(X, Y, self.y_transform)
        elif self.visualization == 'line':
            mv = mf.lineChartMatch(X, Y)
        elif self.visualization == 'scatter':
            mv = mf.scatterChartMatch(X, Y)
        else:
            mv = 0

        # Getting transformation quality value
        qv = mf.quality(X, features[1])

        # Getting the importance of columns
        wv = 0

        return mv, qv, wv
    
    def calcWeight(self):
        #print(self)
        mv, qv, wv = self.getFunctionValues()
        return (mv + qv + wv)
    
class IterableVisualization:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # This method should return an iterator object
        return iter(self.data)