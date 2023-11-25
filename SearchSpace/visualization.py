"""
Visualization class is the class produced by the search space generator,

X = the original X column
Y = the original Y column
visualization = the type of plot
x_transform = any transformations on X
y_transform = any transformation on Y
order_by = any order on X or Y (possible values include X', Y', or null)
"""
from column import Column

class Visualization: 
    def __init__(self, X, Y, x_transform = None, y_transform = None, order_by = None, visualization = None):
        self.X = X
        self.Y = Y
        self.visualization = visualization
        self.x_transform = x_transform
        self.y_transform = y_transform
        self.order_by = order_by

    def __str__(self):
        return f"{self.X.name}, {self.Y.name}, {self.x_transform}, {self.y_transform}, {self.order_by}, {self.visualization}"

    # Ideally will connect to Feature class a be able to retrive features
    def getFeatures():
        return 0
    
    
