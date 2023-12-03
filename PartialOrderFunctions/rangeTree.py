from classes.visualization import Visualization, IterableVisualization
import PartialOrderFunctions.matchingFunctions as mf

class Node:
    def __init__(self, visualization: Visualization, equals=None):
        self.visualization = visualization
        self.score = 0

        self.equals = [] if equals is None else equals  # List to store points with equal values
        self.left = None
        self.middle = None
        self.right = None

class Graph:
    def __init__(self, nodes, key=lambda visual: visual.weight):
        self.root = self.build_tree(nodes, key)

    def build_tree(self, nodes, key):
        if not nodes:
            return None

        # Sort points based on the specified key function
        #nodes = IterableVisualization(nodes)
        nodelist = sorted(nodes, key=key)

        print("Printing sorted node list based on weight: ", nodelist)

        # Find the median point
        mid = len(nodelist) // 2
        median_point = nodelist[mid]

        # Create a node for the median point and gather points with equal values
        equals = [p for p in nodelist if key(p) == key(median_point)]
        root = Node(median_point, equals)

        # Recursively build left, middle, and right subtrees
        root.left = self.build_tree([p for p in nodelist if key(p) < key(median_point)], key)
        root.middle = self.build_tree([p for p in nodelist if key(p) == key(median_point)], key)
        root.right = self.build_tree([p for p in nodelist if key(p) > key(median_point)], key)

        return root

    def query_range(self, x1, x2, key=lambda point: point.x, node=None):
        if node is None:
            node = self.root

        result = []

        # Check if the current node's point is in the range
        if x1 <= key(node.point) <= x2:
            result.extend(node.equals)

        # If the query range intersects with the left subtree, recursively search it
        if node.left and x1 < key(node.point):
            result.extend(self.query_range(x1, x2, key, node.left))

        # If the query range intersects with the middle subtree, recursively search it
        if x1 <= key(node.point) <= x2:
            result.extend(self.query_range(x1, x2, key, node.middle))

        # If the query range intersects with the right subtree, recursively search it
        if node.right and x2 > key(node.point):
            result.extend(self.query_range(x1, x2, key, node.right))

        return result