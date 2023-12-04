from .visualization import Visualization
import Partial_Order.Functions.matchingFunctions as mf

class Node():
    def __init__(self, visualiztion: Visualization):
        self.visualization = visualiztion
        self.score = 0
        self.less = []
        
    def __str__(self):
        return f"Node: { self.visualization } Score: { self.score } Less Than: { len(self.less) }"

    def __eq__(self, other: Visualization):
        if self.visualization == other:
            return True
        else:
            return False
