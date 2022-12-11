
import random


num_comparisons = 0
num_divisions = 0
num_additions = 0
num_solutions = 0

# random search algorithm
def RandomSearch(g):#! diminuir o numero de vertices se encontrar uma solucao o prof diz que era melhor
    random.seed(98124)
    global num_comparisons
    global num_solutions
    global num_additions
    
    dominatingSet = [] 
    totalWeights = []
    num_comparisons = 0
    num_solutions = 0
    num_additions = 0

    per_subsets = 0.10
    
    num_ver = g.num_vertices
    if g.num_vertices > 15:
        num_ver = int(g.num_vertices/2)
        
    firstTime = True
    while num_ver>0:

        
        
        nSubsets=int( (pow(2, g.num_vertices) -1) * per_subsets ) 
        num_comparisons += 1
        if nSubsets<75:
            nSubsets=75 

        num_comparisons += 1
        if nSubsets>10000:
            nSubsets=10000

        # start= time.time()

        vistos = set()

        foundDominatingSet=False
        for set2 in range(nSubsets):#fazer nSubsets subsets de num_ver vertices

            sset = random.sample(range(g.num_vertices), num_ver)

            num_comparisons += 1
            if str(sset) in vistos:
                continue

            vistos.add(str(sset))

            num_comparisons += 1
            if isDominatingSet(g, sset):   
                # print("num_ver=", num_ver)
                # print(set,"/",nSubsets)
                # input()
                foundDominatingSet=True
                dominatingSet.append(sset)
                num_additions+= 1 
                totalWeights.append(sum([g.vertices[v][2] for v in sset])) 
                break

        num_comparisons += 1
        if not foundDominatingSet and firstTime:
            num_ver=g.num_vertices # se nao encontrar um conjunto dominante com metade dos vertices, entao tenta com todos os vertices
            continue
        
        num_comparisons += 1
        if not foundDominatingSet or num_ver==0:

            # end= time.time()
            # print('time1:', end-start)
            # start= time.time()

            vistos2 = set()

            nSubsets=10000*num_ver
            for set3 in range(nSubsets):#fazer nSubsets subsets de num_ver vertices

                num_comparisons += 1
                if num_ver==g.num_vertices:
                    subset = random.sample(range(g.num_vertices), num_ver)
                else:
                    subset = random.sample(range(g.num_vertices), (num_ver+1))

                num_comparisons += 1
                if str(subset) in vistos2:
                    continue

                vistos2.add(str(subset))

                num_comparisons += 1
                if isDominatingSet(g, subset): 
                    dominatingSet.append(subset)
                    num_additions+= 1 
                    totalWeights.append(sum([g.vertices[v][2] for v in subset])) 
            
            break

        num_ver-=1
        firstTime=False

    # end= time.time()
    # print('time2:', end-start)

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
    
    
    
    
