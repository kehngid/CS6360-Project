from Partial_Order.SearchSpace.generate import generateSearchSpace
from Partial_Order.display import generate_chart
import pandas as pd
import numpy as np

import Partial_Order.Functions.graph as graph

def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            file.write('X,Y,x_transform,y_transform,orderby,visualization,node_info')
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"Elements written to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def runPartialOrder(filename, k = 10):
    #filename = './' + filename
    nodes = generateSearchSpace(filename)
    # makeGraph result in list of nodes which contain a visualization, a score, and list of nodes 'less good'
    nodeList = graph.makeGraph(nodes)
    orderedList = graph.orderGraph(nodeList)

    if isinstance(k, int):
        print("Show top ", k, " results")
        for i in range(0,k):
            print(orderedList[i])
            generate_chart(orderedList[i].visualization)
    elif k == 'all':
        print('Showing all')
        for i in orderedList:
            print(i)

    write_list_to_file('./Results/Partial_Order/output.txt', orderedList)
    


#runPartialOrder('./data/testing.csv')
#runPartialOrder('./data/titanicPassenger.csv', 'all')
