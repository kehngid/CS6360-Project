"""
This file produces the graph search space
To get list of possible graphs/visualization node use generateSearchSpace(datasetFilename) located at the very bottom
"""
import pandas as pd

from Partial_Order.classes.column import Column
from Partial_Order.classes.visualization import Visualization

# Copied from features.py, come up with better to way to identify datetime
def get_column_type(column):
        """
        Determine the data type of a column using pandas.
        """
        dtype = pd.Series(column).dtype.name
        if 'int' in dtype or 'float' in dtype:
            return 'Numerical'
        elif 'datetime' in dtype:
            return 'Temporal'
        else:
            return 'Categorical'

"""
getColumns: turns CSV data into Column objects 
input: csv filename and deliminator
output: list of file objects 
Notes: check data types of each function
"""
def getColumns(filename, deliminator = ','):
    colList = []
    df = pd.read_csv(filename, header=0, delimiter=deliminator)
    for x in df.columns.values.tolist():
        colType = get_column_type(df[x])
        colList.append(Column(x, df[x], colType))
    return colList

"""
checkColumnType: my version of correct column identification, user manual confirms column type
input: list of column objects with code-detected datatype
output: list of column objects with user-confirmed datatypes
"""
def checkColumnType(colList):
    for i in range(0, len(colList)):
        change = input("Column " + colList[i].name + " is of type " + colList[i].type + ", is this correct? (Y/N)")
        if change.lower() != 'y':
            newType = input("What is the correct type? (Numerical/Categorical/Temporal)")
            colList[i].type = newType
    return colList

"""
transformationRules: creates visualization nodes of appropriate transformed data
input: a visualization node with just X and Y assigned
output: list of new Visualization nodes with transformations assigned
"""
def transformationRules(visual):
    X = visual.X
    Y = visual.Y
    if X.type == 'Categorical':
        if Y.type == 'Numerical':
            avgVisual = Visualization(X, Y, 'group', 'avg')
            sumVisual = Visualization(X, Y, 'group', 'sum')
            cntVisual = Visualization(X, Y, 'group', 'cnt')
            return [avgVisual, sumVisual, cntVisual]
        elif Y.type != 'Numerical':
            cntVisual = Visualization(X, Y, 'group', 'cnt')
            return [cntVisual]
        ''' Move in one, should be in line with if X.type == Catagorical
        elif X.type == 'Numerical':
            if Y.type == 'Numerical':
                avgVisual = Visualization(X, Y, 'bin', 'avg')
                sumVisual = Visualization(X, Y, 'bin', 'sum')
                cntVisual = Visualization(X, Y, 'bin', 'cnt')
                return [avgVisual, sumVisual, cntVisual]
            elif Y.type != 'Numerical':
                cntVisual = Visualization(X, Y, 'bin', 'cnt')
                return [cntVisual]
        '''
    elif X.type == 'Temporal':
        if Y.type == 'Numerical':
            groupAvgVisual = Visualization(X, Y, 'group', 'avg')
            groupSumVisual = Visualization(X, Y, 'group', 'sum')
            groupCntVisual = Visualization(X, Y, 'group', 'cnt')
            #binAvgVisual = Visualization(X, Y, 'bin', 'avg')
            #binSumVisual = Visualization(X, Y, 'bin', 'sum')
            #binCntVisual = Visualization(X, Y, 'bin', 'cnt')
            return [groupAvgVisual, groupSumVisual, groupCntVisual] #, binAvgVisual, binSumVisual, binCntVisual]
        elif Y.type != 'Numerical':
            groupCntVisual = Visualization(X, Y, 'group', 'cnt')
            #binCntVisual = Visualization(X, Y, 'bin', 'cnt')
            return [groupCntVisual] #, binCntVisual]
    else:
        return []

"""
sortingRule: creates visualization nodes with appropriate order by values
input: visualization node with X,Y, x_transform, and y_transform assigned (transforms can be None)
output: list of new Visualization nodes with order_by value assigned
"""
def sortingRule(visual):
    X = visual.X
    Y = visual.Y
    sortingList =[]
    if X.type == 'Numerical' or X.type == 'Temporal':
        sortingList.append(Visualization(X, Y, visual.x_transform, visual.y_transform, 'orderX'))
    if Y.type == 'Numerical' or visual.x_transform == 'group' or visual.x_transform == 'bin':
        sortingList.append(Visualization(X, Y, visual.x_transform, visual.y_transform, 'orderY'))
    
    return sortingList

"""
visualizationRules: assigned appropriate graph type to node
input: visualization node with everything but type assigned
output: list of new Visualization nodes with type assigned
"""
def visualizationRules(visual):
    X = visual.X
    Y = visual.Y
    x_tran = visual.x_transform
    y_tran = visual.y_transform
    order_by = visual.order_by
    if X.type == 'Categorical':
        if Y.type == 'Numerical' or x_tran == 'bin' or x_tran == 'group':
            barVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'bar')
            pieVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'pie')
            return [barVisual, pieVisual]
        else:
            return []
    elif X.type == 'Numerical':
        if Y.type == 'Numerical' or x_tran == 'bin' or x_tran == 'group':
            lineVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'line')
            barVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'bar')
            scatterVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'scatter')
            return [lineVisual, barVisual, scatterVisual] # Technically only scatter if correlated
        else:
            return []
    elif X.type == 'Temporal':
        if Y.type == 'Numerical' or x_tran == 'bin' or x_tran == 'group':
            lineVisual = Visualization(X, Y, x_tran, y_tran, order_by, 'line')
            return [lineVisual]
        else:
            return []
    else:
        return []

"""
generateVisualizations: finds correct graph search space
input: list of column objects of the dataset 
output: list of all possible visualiztion nodes/possible graphs according to rules (pg108 in paper)
"""
def generateVisualizations(colList):
    nodeList = []
    # Listing all of the possible pairs
    for i in range(0,len(colList)):
        for j in range(0, len(colList)):
            if i != j:
                nodeList.append(Visualization(colList[i], colList[j]))

    # DEBUGGING (Showing all of the possible pairs)
    ##print("Inital Node List:")
    ##print("Inital Node list length: ", len(nodeList))
    '''
    for i in nodeList:
        ##print(i)
    '''

    # Using rule to prune search space
    # Generating all possible transformation combos
    transformList = []
    for node in nodeList:
        transformList.extend(transformationRules(node))
    nodeList.extend(transformList)
    #DEBUGGING
    ##print('\nTranformation list:')
    ##print('Number of new nodes: ', len(transformList))
    '''
    for i in transformList:
        ##print(i)
    '''

    # Generating all possible sorting combos
    sortList = []
    for node in nodeList:
        sortList.extend(sortingRule(node))
    nodeList.extend(sortList)
    ##print('Number of new nodes: ', len(sortList))  #DEBUGGING

    # Assigning visualization roles/graph types 
    finalNodeList = []
    for node in nodeList:
        finalNodeList.extend(visualizationRules(node))
    ###print('Number of total nodes with graphs: ', len(finalNodeList))
    
    return finalNodeList

"""
generateSearchSpace(): function that produces columns and all visualizations
input: datafile name and deliminator
output: list of all possible visualizations of the dataset
"""
def generateSearchSpace(filename, deliminator = None):
    colList = getColumns(filename)
    colList = checkColumnType(colList)
    nodes = generateVisualizations(colList)

    ##print('\nTotal visualizations length: ', len(nodes))
    return(nodes)




