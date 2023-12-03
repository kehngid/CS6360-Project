from classes.visualization import Visualization

class Node:
    def __init__(self, visualization: Visualization, equals=None):
        self.visualization = visualization
        self.score = 0

        self.equals = [] if equals is None else equals
        self.left = None
        self.middle = None
        self.right = None

class Graph:
    def __init__(self, nodes, key=lambda visualization: visualization.weight):
        print("Initalizing a graph")
        self.root = self.build_tree(nodes, key)

    def build_tree(self, nodes, key):
        print("Running build tree function")
        if not nodes:
            return None

        for i in nodes:
            print(i)

        nodelist = sorted(nodes, key=key)

        # Find the median node
        mid = len(nodelist) // 2
        median_node = nodelist[mid]

        # Create a node for the median point and gather nodes with equal values
        equals = [p for p in nodelist if p.weight == median_node.weight]
        root = Node(median_node, equals)

        # Recursively build left, middle, and right subtrees
        root.left = self.build_tree([p for p in nodelist if p.weight < median_node.weight], key)
        root.middle = self.build_tree([p for p in nodelist if p.weight == median_node.weight], key)
        root.right = self.build_tree([p for p in nodelist if p.weight > median_node.weight], key)

        return root

    def query_range(self, x1, x2, key=lambda point: point.x, node=None):
        if node is None:
            node = self.root

        result = []

        # Check if the current node's visualization is in the range
        if x1 <= key(node.visualization) <= x2:
            result.extend(node.equals)

        # If the query range intersects with the left subtree, recursively search it
        if node.left and x1 < key(node.visualization):
            result.extend(self.query_range(x1, x2, key, node.left))

        # If the query range intersects with the middle subtree, recursively search it
        if x1 <= key(node.visualization) <= x2:
            result.extend(self.query_range(x1, x2, key, node.middle))

        # If the query range intersects with the right subtree, recursively search it
        if node.right and x2 > key(node.visualization):
            result.extend(self.query_range(x1, x2, key, node.right))

        return result
