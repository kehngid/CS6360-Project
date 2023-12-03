import PartialOrderFunctions.matchingFunctions as mf
from classes.visualization import Visualization

class Edges:
    # node v points to node u 
    def __init__(self, v: Visualization, u: Visualization):
        self.v = v
        self.u = u
        self.weight = self.calcWeight()

    def __str__(self):
        return f"From: {self.v}, To: {self.u}, Edge weight= {self.weight}"
    
    def calcWeight(self):
        mv, qv, wv = mf.getFunctionValues(self.v)
        mu, qu, wu = mf.getFunctionValues(self.u)
        
        
        #print("The mv, qv, and wv values of node v:", mv,qv,wv)
        #print("The mu, qu, and wu values of node u:", mu,qu,wu)

        weight = (mu - mv + qu - qv + wu - wv)/3
        #print("Weight calculated in edges: ", weight)

        # Returns weight of edge and direction of edge
        if weight < 0:
            return abs(weight)
        else:
            return None

    


