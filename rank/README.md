I utilize various libraries, including Pandas, NumPy, and scikit-learn, to train a LambdaMART model for ranking instances based on specified features.
The data is split into training and testing sets. The training data is then formatted in RankLib's required structure and saved to a file. 
Subsequently, the script employs RankLib to train a LambdaMART model with specific parameters, such as the number of trees and shrinkage. Finally, the trained model is applied to rank these new instances, 
and the resulting scores are displayed. I have only completed learning to work for now, and I will proceed to implement the Partial Order-based approach and Diversified Ranking.
