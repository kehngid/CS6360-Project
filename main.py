from classes.visualization import Visualization
from SearchSpace.generate import generateSearchSpace
import pandas as pd
import numpy as np

import PartialOrderFunctions.matchingFunctions as mf

# FIRST: Generate Search Space (list of visualization nodes)
nodes = generateSearchSpace('./data/testing.csv')

# SECOND: Pick ranking method  
learning_to_rank = False
partial_order = True
hybrid = False
if learning_to_rank:
    # run learntorank
    print('Running with learn to rank')
elif partial_order:
    print('Running with partial order')
elif hybrid:
    # run hybrid
    print('Running with hybrid')

print(len(nodes))

viz1 = nodes[25]
viz2 = nodes[26]

print(viz1)
print(viz2)

"""
# Assuming X and Y are your arrays
data = {'X': viz2.X.values, 'Y': viz2.Y.values}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'X' and apply the sum aggregation function on 'Y'
result = df.groupby('X')['Y'].count().reset_index()

# 'result' now contains the grouped data with the sum of 'Y' for each group in 'X'
"""

#print(viz2.X.values)
print(viz2.X.values.sort_values(ascending=False).reset_index(drop=True).index)

print(mf.calcWeight(viz1, viz2))
