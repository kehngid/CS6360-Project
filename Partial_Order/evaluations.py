from sklearn.metrics import ndcg_score
import pandas as pd

#from Partial_Order.classes.node import Node

def nodeifyDeepEyeResults(filename):
    df = pd.read_csv(filename)

    print(df.to_string()) 

filename = './data/DeepEyeResults/electricity.txt'

nodeifyDeepEyeResults(filename)