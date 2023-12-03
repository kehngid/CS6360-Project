import PartialOrderFunctions.matchingFunctions as mf
from classes.visualization import Visualization

class Edges:
    def __init__(self, v: Visualization, u: Visualization):
        self.v = v
        self.u = u
        self.weight = self.getWeight()

    def __str__(self):
        return f"From: {self.v}, To: {self.u}, Edge weight= {self.weight}"
    
    def getWeight(self):
        vFeatures = self.v.getFeatures()
        uFeatures = self.u.getFeatures()

    


