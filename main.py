import pandas as pd
import numpy as np

from Partial_Order.partialOrder import runPartialOrder
#Pick ranking method  
learning_to_rank = False
partial_order = True
hybrid = False
if learning_to_rank:
    # run learntorank
    print('Running with learn to rank')
elif partial_order:
    print('Running with partial order')
    filename = './data/testing.csv'
    runPartialOrder(filename)
# NOT IMPLEMENTED
elif hybrid:
    # run hybrid
    print('Running with hybrid')