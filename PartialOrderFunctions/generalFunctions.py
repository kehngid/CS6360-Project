from itertools import combinations
from partial_order_graph.edges import Edges

def getAllPairs(nodeList):
    all_pairs = [(a, b) for a, b in combinations(nodeList, 2) if a != b]
    return all_pairs

def makeGraph(nodeList):
    allPairs = getAllPairs(nodeList)
    edges = []
    count = 0   #DEBUGGING

    print("Amount of edges before:", len(allPairs))
    for i in allPairs:
        count += 1
        edge = Edges(i[0], i[1])
        if count < 10:
            print(edge)
        
        if edge.weight != None:
            edges.append(edge)

    print("Amount of edges before:", len(allPairs))
    print("Amount of edges after:", len(edges))
    return edges