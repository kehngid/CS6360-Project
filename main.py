from SearchSpace.generate import generateSearchSpace

nodes = generateSearchSpace('./data/testing.csv')

print(len(nodes))

viz1 = nodes[50]
viz2 = nodes[51]

print(viz1)
print("X values: ", viz1.X.values)

