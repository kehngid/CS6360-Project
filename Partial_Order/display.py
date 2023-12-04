# Display results
import matplotlib.pyplot as plt
import numpy as np

def generate_chart(visualization):
    match visualization.visualization:
        case 'bar':
            plt.bar(visualization.X.values, visualization.Y.values)
            plt.title('Bar Chart')
        case 'pie':
            counts = np.unique(visualization.X.values, return_counts=True)
            plt.pie(counts[1], labels=counts[0], autopct='%1.1f%%')
            plt.title('Pie Chart')
        case 'line':
            plt.plot(visualization.X.values, visualization.Y.values)
            plt.title('Line Chart')
        case 'scatter':
            plt.scatter(visualization.X.values, visualization.Y.values)
            plt.title('Scatter Chart')

    if visualization.visualization != 'pie':
        plt.xlabel(visualization.X.name)
        plt.ylabel(visualization.Y.name)

    plt.savefig(f'Results/Partial_Order/charts/{visualization.X.name}_{visualization.Y.name}_{visualization.x_transform}_{visualization.y_transform}_{visualization.order_by}_{visualization.visualization}.png')