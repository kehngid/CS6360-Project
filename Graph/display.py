# Display results

import numpy as np
import matplotlib.pyplot as plt


def generate_chart(a):
    x = np.arange(1, 11)
    y = np.random.randint(1, 20, size=10)

    if a == 0:
        # Bar chart
        plt.bar(x, y)
        plt.title('Bar Chart')
    elif a == 1:
        # Pie chart
        plt.pie(y, labels=x)
        plt.title('Pie Chart')
    elif a == 2:
        # Line chart
        plt.plot(x, y)
        plt.title('Line Chart')
    elif a == 3:
        # Scatter chart
        plt.scatter(x, y)
        plt.title('Scatter Chart')

    plt.show()