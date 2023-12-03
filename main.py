from SearchSpace.generate import generateSearchSpace
import pandas as pd

# FIRST: Generate Search Space (list of visualization nodes)
nodes = generateSearchSpace('./data/testing.csv')

# SECOND: Pick ranking method  



print(len(nodes))

viz1 = nodes[25]
viz2 = nodes[26]

print(viz1)
print(viz2)

# Assuming X and Y are your arrays
data = {'X': viz1.X.values, 'Y': viz1.Y.values}

print(data)
# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'X' and apply the sum aggregation function on 'Y'
result = df.groupby('X')['Y'].count().reset_index()

# 'result' now contains the grouped data with the sum of 'Y' for each group in 'X'
print(result)

# Assuming X and Y are your arrays
data = {'X': viz2.X.values, 'Y': viz2.Y.values}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'X' and apply the sum aggregation function on 'Y'
result = df.groupby('X')['Y'].count().reset_index()

# 'result' now contains the grouped data with the sum of 'Y' for each group in 'X'
print(result)