from SearchSpace.generate import generateSearchSpace
import pandas as pd
import numpy as np

import Functions.graph as graph

def runPartialOrder(filename, k = 10):
    filename = './' + filename
    nodes = generateSearchSpace(filename)
    # makeGraph result in list of nodes which contain a visualization, a score, and list of nodes 'less good'
    nodeList = graph.makeGraph(nodes)
    orderedList = graph.orderGraph(nodeList)

    if isinstance(k, int):
        print("Show top ", k, " results")
        for i in range(0,k):
            print(orderedList[i])
    elif k == 'all':
        print('Showing all')
        for i in orderedList: 
            print(i)

#runPartialOrder('./data/testing.csv')
runPartialOrder('./data/electricityConsumptionOfEasternChina.csv', 'all')
