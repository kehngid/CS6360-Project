from classes.visualization import Visualization
import PartialOrderFunctions.matchingFunctions as mf

class Node():
    def __init__(self, visualiztion: Visualization, score = 0):
        self.visualization = visualiztion
        self.score = score
        self.visualWeight = self.calcWeight()
        
    
    def __str__(self):
        return f"Node: { self.visualization } Score: { self.score }"

    def __eq__(self, other: Visualization):
        if self.visualization == other:
            return True
        else:
            return False
        
    def calcWeight(self):
        mv, qv, wv = mf.getFunctionValues(self.v)
