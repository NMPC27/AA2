from itertools import combinations
from typing import Set

from numpy import minimum
import random


num_comparisons = 0
num_divisions = 0
num_additions = 0
num_solutions = 0

# exhaustive search algorithm
def exhaustiveSearch(g):
    random.seed(98124)
    global num_comparisons
    global num_solutions
    global num_additions
    
    dominatingSet = [] 
    totalWeights = []
    num_comparisons = 0
    num_solutions = 0
    num_additions = 0

    subsets_list = []

    for i in range(1, g.num_vertices+1): # começa no 1 porque o conjunto vazio nao é um conjunto dominante

        for subset in combinations(range(g.num_vertices), i):
            subset = list(subset)
            subsets_list.append(subset)
            num_solutions += 1 # soluçoes/configuraçoes count



    #! atençao que se o valor de len(subsets_list) for muito baixo pode dar 0 e dps da asneira

    if len(subsets_list) < 10:
        num_sol_find = len(subsets_list)
    else:
        num_sol_find = int( len(subsets_list) * 0.1) # vamos explorar 40% das soluçoes

    solutions_explored=[]

    for i in range(num_sol_find):

        idx=random.randint(0, len(subsets_list)-1)

        while idx in solutions_explored:
            idx=random.randint(0, len(subsets_list)-1)

        solutions_explored.append(idx)

        if isDominatingSet(g, subsets_list[idx]):            
            dominatingSet.append(subsets_list[idx])
            num_additions+= 1 
            totalWeights.append(sum([g.vertices[v][2] for v in subsets_list[idx]])) # soma todos os pesos
    
    minimum = min(totalWeights) # encontra o set com menor peso
    idx = totalWeights.index(minimum) 
    
    return dominatingSet[idx] #minimum weight dominating set

def isDominatingSet(g, subset):
    global num_comparisons

    dominatingSet = set()
    vertices_lista=list(range(g.num_vertices))

    for v in subset:
        vertices_lista.remove(v)

    for v in subset:
        dominatingSet.add(v) #vertice atual

    for x in subset:
        for y in range(g.num_vertices): #vertices adjacentes ao vertice atual
            num_comparisons += 1
            if g.isAdjacent(x,y):              
                dominatingSet.add(y) # ficamos com todos os vertices adjacentes ao vertice atual + o atual (la em cima)
                
                if y in vertices_lista:
                    vertices_lista.remove(y)
    
    num_comparisons += 1
    if len(dominatingSet) == g.num_vertices:    #se o conjunto de vertices adjacentes ao vertice atual + o atual for igual ao numero de vertices do grafo, entao é um conjunto dominante
        return True
    
    return False
    
                

# greedy search algorithm
def greedy(g):
    global num_comparisons
    global num_divisions
    global num_solutions

    num_comparisons = 0
    num_divisions = 0
    num_solutions = 0

    ratios = []
    
    for i in range(0, g.num_vertices):
        vertex = g.vertices[i]
        edges = g.adjacencyMatrix[i].count(1)  # grau do vertice
        num_divisions += 1
        tpl = (i, vertex[2]/edges) if edges != 0 else (i, 0) # racio entre peso e grau do vertice
        ratios.append(tpl)


    adjacentes = set()
    ans = set()
    while ratios != [] and len(adjacentes)<g.num_vertices:
        num_comparisons += 1
        
        vertex = min(ratios, key=lambda x: x[1]) #escolher o vertice com menor racio (eu quero + grau por menos peso - ou seja o menor ratio)
        idx_vertex = vertex[0]

        adjacentes.add(idx_vertex) #vertice atual
        ans.add(idx_vertex) #vertice atual
        for v in range(g.num_vertices):
            num_comparisons += 1
            if g.isAdjacent(idx_vertex, v):
                adjacentes.add(v) #vertices adjacentes ao vertice atual

        ratios.remove(vertex)

    num_solutions += 1
    return ans

def printResults(iset, g):
    global num_comparisons
    global num_additions
    global num_divisions
    global num_solutions
    
    iset = [g.vertices[v] for v in iset]
    iset = sorted(iset, key=lambda x: x[2])
    iset.reverse()
    maximum = sum([v[2] for v in iset])

        
    print("Minimum weight dominating set: "+str(iset))
    print("Total weight: "+str(maximum))
    print("Number of comparisons: "+str(num_comparisons))
    print("Number of divisions: "+str(num_divisions))
    print("Number of additions: "+str(num_additions))
    print("Number of solutions: "+str(num_solutions))
    

    return (num_comparisons, num_divisions, num_additions, num_solutions,maximum)
    
    
    
    
