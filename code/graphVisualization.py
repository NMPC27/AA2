import networkx as nx
import matplotlib.pyplot as plt
   
class GraphVisualization:
   
    def __init__(self):
        self.visual = [] 
        self.nodes = []
        self.G = nx.Graph()
          
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def addNode(self, count, node):
        self.G.add_node(count, pos=node)
    
    def visualize(self):
        self.G.add_edges_from(self.visual)
        pos=nx.get_node_attributes(self.G,'pos')
        nx.draw(self.G, pos)
        plt.show()
        