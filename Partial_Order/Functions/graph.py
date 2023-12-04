from Partial_Order.classes.node import Node

def makeNodeList(visualizationList):
    nodeList = []
    for i in visualizationList:
        nodeList.append(Node(i))
    return nodeList

def makeLessThanLists(nodeList):
    for i in range(0, len(nodeList)):
        current = nodeList[i]
        for j in range(i, len(nodeList)):
            other = nodeList[j]
            if current.visualization.weight > other.visualization.weight:
                current.less.append(other)
            elif current.visualization.weight < other.visualization.weight:
                other.less.append(current)  
        #print( current.visualization, " less than list: ", current.less)   

def getScore(node: Node):   
    sum = 0
    if len(node.less) == 0:
        node.score = 0
        return node.score
    elif node.score != 0:
        return node.score
    else:
        for i in node.less:
            sum += getScore(i) + ((node.visualization.weight - i.visualization.weight) / 3) 
    node.score = sum
    return node.score

def makeGraph(visualList):
    nodeList = makeNodeList(visualList)
    makeLessThanLists(nodeList)
    for i in nodeList:
        getScore(i)
    return nodeList
    
    '''
    # Debugging
    print('Number of visualizations', len(visualList))
    print('Number of nodes: ', len(nodeList))
    print("Printing nodes with scores")
    for i in nodeList:
        print(i)
    '''

def orderGraph(nodeList):
    sortedList = sorted(nodeList, key=lambda node: node.score, reverse=True)
    return sortedList
    
    

    