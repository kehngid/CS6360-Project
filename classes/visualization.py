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
        dataset = pd.DataFrame({self.X.name: self.X.values, self.Y.name: self.Y.values}, columns=[self.X.name, self.Y.name])
        if  self.x_transform == 'group':
            X = self.X
        elif self.x_transform == 'bin':
            X = self.X
        else:
            X = self.X

        
        Y = self.Y
        return X, Y

    # Ideally will connect to Feature class a be able to retrive features
    def getFeatures(self):
        return Features(self.X, self.Y, self.visualization).calculate_features()
    