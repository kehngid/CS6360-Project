import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import subprocess


data = pd.read_csv('C:/Users/ysy20/Desktop/HollywoodsMostProfitableStories.csv')

# 'Worldwide Gross' is output
# 'Audience  score %', 'Profitability', 'Rotten Tomatoes %' are feature vectors. Now I set up three features vectors
target_col = 'Worldwide Gross'
feature_col = ['Audience  score %', 'Profitability', 'Rotten Tomatoes %']

X = data[feature_col].values
Y = data[target_col].rank(ascending=False)


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

train_data = np.column_stack((y_train, np.zeros_like(y_train), X_train))
np.savetxt('train_ranklib.txt', train_data, delimiter='\t', comments='', header='label score ' + ' '.join([f'f{i}' for i in range(len(feature_col))]))

# Train LambdaMART model using RankLib
# (Replace the path)
ranklib_jar_path = 'C:/Users/ysy20/Desktop/RankLib-2.18.jar'
train_cmd = f'java -jar {ranklib_jar_path} -ranker 6 -metric2t NDCG@10 -tree 100 -leaf 10 -shrinkage 0.1 -train train_ranklib.txt -save ranking_model.txt'
subprocess.run(train_cmd, shell=True)

# Save new instances
new_instances = np.random.rand(5, len(feature_col))
new_instances_data = np.column_stack((np.zeros(5), np.zeros(5), new_instances))
np.savetxt('new_instances_ranklib.txt', new_instances_data, delimiter='\t', comments='', header='label score ' + ' '.join([f'f{i}' for i in range(len(feature_col))]))

# Use the trained model to rank the new instances
rank_cmd = f'java -jar {ranklib_jar_path} -load ranking_model.txt -rank new_instances_ranklib.txt -score new_instances_scores.txt'
subprocess.run(rank_cmd, shell=True)
new_instances_scores = np.loadtxt('new_instances_scores.txt')
sort_scores = sorted(new_instances_scores)
print("Scores for new instances:", sort_scores)
