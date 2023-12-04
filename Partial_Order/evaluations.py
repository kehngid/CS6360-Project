from sklearn.metrics import ndcg_score
import pandas as pd
import re

class VisualLite():
    def __init__(self, X, Y, x_transform, y_transform, visualization = None):
        self.X = X
        self.Y = Y
        self.x_transform = self.setXTransform(x_transform)
        self.y_transform = self.setYTransform(y_transform)
        self.visualization = visualization
    
    def __str__(self):
        return f"{self.X}, {self.Y}, {self.x_transform}, {self.y_transform}, {self.visualization}"

    
    def setXTransform(self, x_transform):
        if issubclass(type(x_transform), str) == False:
            return None
        if re.search("^group", x_transform) != None:
            return 'group'
        else:
            return None

    def setYTransform(self, y_transform):
        if issubclass(type(y_transform), str) == False:
            return None
        if re.search("^sum", y_transform) != None:
            return 'sum'
        elif re.search("^cnt", y_transform) != None:
            return 'cnt'
        elif re.search("^avg", y_transform) != None:
            return 'avg'
        else:
            return None
        
    def diffScore(self, other):
        score = 0
        if self.X != other.X:
            score += 1
        if self.Y != other.Y:
            score += 1
        if self.x_transform != other.x_transform:
            score += 1
        if self.y_transform != other.y_transform:
            score += 1
        if self.visualization != other.visualization:
            score += 1
        return score

def nodeifyDeepEyeResults(trueFilename, targetFilename):
    trueDf = pd.read_csv(trueFilename)
    targetDf = pd.read_csv(targetFilename)

    # Converting deepeye results into visualizations
    trueVisList = []

    for i in trueDf.index:
        trueVisList.append(VisualLite(trueDf['X'][i], trueDf['Y'][i], trueDf['GROUP_BY'][i], trueDf['AGG'][i], trueDf['VISUALIZATION'][i]))
    
    targetVisList = []
    for i in targetDf.index:
        targetVisList.append(VisualLite(targetDf['X'][i], targetDf['Y'][i], targetDf['x_transform'][i], targetDf['y_transform'][i], targetDf['visualization'][i]))

    print('The difference in the first 10 reccommended graphs:')
    print('The higher the score the more different they are')
    for i in range(0, 10):
        print(trueVisList[i].diffScore(targetVisList[i]))

    #print(trueDf.to_string()) 
    #print(targetDf.to_string())

deepeyeResults = './data/DeepEyeResults/electricity.txt'
results = './Results/Partial_Order/electricityConsumptionResults.txt'

nodeifyDeepEyeResults(deepeyeResults, results)