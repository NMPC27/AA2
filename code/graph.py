import random
from graphVisualization import GraphVisualization

class Graph():
    
    def __init__(self, num_vertices, density):
        self.vertices = []
        self.edges = []
        self.density = density
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adjacencyMatrix = [[0]* self.num_vertices for _ in range(self.num_vertices)]

    def buildGraph(self):
        random.seed(98124)
        i = 0
        while i < self.num_vertices:
            x = random.randint(1, 9) 
            y = random.randint(1, 9)
            weight = random.randint(1, 100)
            tpl = (x, y, weight)
            
            if any(v[0] == x and v[1] == y for v in self.vertices): #avoid duplicate vertices
                continue
            self.vertices.append(tpl)
            i += 1
        
        self.num_edges = int((self.density/100) * (self.num_vertices*(self.num_vertices-1)/2)) 
        
        i = 0
        while i < self.num_edges:
            vert1 = random.randint(0, self.num_vertices-1)
            vert2 = random.randint(0, self.num_vertices-1)
            if vert1 != vert2 and (vert1, vert2) not in self.edges and (vert2, vert1) not in self.edges: # avoid loops
                self.adjacencyMatrix[vert1][vert2] = 1
                self.adjacencyMatrix[vert2][vert1] = 1
                
                edge = (vert1, vert2)
                self.edges.append(edge)
                i += 1  
        
    def isAdjacent(self, v1, v2):
        return self.adjacencyMatrix[v1][v2] == 1

    
    def showGraph(self):
        G = GraphVisualization()
        i = 0
        for vertice in self.vertices:
            G.addNode(i, (vertice[0], vertice[1]))
            i += 1
        for edge in self.edges:
            G.addEdge(edge[0], edge[1])
        G.visualize()
       