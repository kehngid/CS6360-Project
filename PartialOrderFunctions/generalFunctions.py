from itertools import combinations

def getAllPairs(nodeList):
    all_pairs = [(a, b) for a, b in combinations(nodeList, 2) if (a.X.name != b.X.name and a.Y.name != b.Y.name)]
    return all_pairs
