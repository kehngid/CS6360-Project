from SearchSpace.generate import generateSearchSpace
import pandas as pd
import numpy as np

import PartialOrderFunctions.graph as graph

def runPartialOrder(filename, k = 10):
    nodes = generateSearchSpace(filename)
    graph.makeGraph(nodes)

    if isinstance(k, int):
        print("Show top ", k, " results")
        for i in range(0,k):
            print(nodes[i])
    elif k == 'all':
        print('Showing all')
        for i in nodes: 
            print(i)

runPartialOrder('./data/testing.csv')
runPartialOrder('./data/testing.csv', 'all')
