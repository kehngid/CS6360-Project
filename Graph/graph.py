# Use graph to order the ranked data

import numpy as np
import matplotlib.pyplot as plt

# from learning to rank
new_instances_scores = np.loadtxt('new_instances_scores.txt')
sort_scores = sorted(new_instances_scores)

x = list(range(len(sort_scores)))
plt.figure()

plt.plot(x, sort_scores, marker='o', linestyle='-')

plt.title('Sorted Scores for New Instances')
plt.xlabel('Instance Index')
plt.ylabel('Score')

plt.show()