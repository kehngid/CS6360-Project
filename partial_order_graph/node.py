from classes.visualization import Visualization

class Node():
    def __init__(self, visualiztion: Visualization, score = 0):
        self.visualization = visualiztion
        self.score = score
    
    def __str__(self):
        return f"Node: { self.visualization } Score: { self.score }"

