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

class Visualization: 
    def __init__(self, X: Column, Y: Column, x_transform = None, y_transform = None, order_by = None, visualization = None):
        self.X = X
        self.Y = Y
        self.visualization = visualization
        self.x_transform = x_transform
        self.y_transform = y_transform
        self.order_by = order_by

    def __str__(self):
        return f"{self.X.name}, {self.Y.name}, {self.x_transform}, {self.y_transform}, {self.order_by}, {self.visualization}"

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
    