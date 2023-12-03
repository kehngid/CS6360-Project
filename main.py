from classes.visualization import Visualization
from SearchSpace.generate import generateSearchSpace
import pandas as pd
import numpy as np
from classes.column import Column

import PartialOrderFunctions.matchingFunctions as mf
import PartialOrderFunctions.generalFunctions as gen

from partial_order_graph.edges import Edges
from PartialOrderFunctions.rangeTree import Graph

# FIRST: Generate Search Space (list of visualization nodes)
nodes = generateSearchSpace('./data/testing.csv')
#print('Node length: ',len(nodes))

# SECOND: Pick ranking method  
learning_to_rank = False
partial_order = True
hybrid = False
if learning_to_rank:
    # run learntorank
    print('Running with learn to rank')
elif partial_order:
    print('Running with partial order')
    graph = Graph(nodes)
elif hybrid:
    # run hybrid
    print('Running with hybrid')


#edge_list = gen.makeGraph(nodes)