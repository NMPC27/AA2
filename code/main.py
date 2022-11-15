import time
from graph import Graph
from search import exhaustiveSearch
from search import greedy
from search import printResults
import csv


def writeCSV(dens):

    with open('exhaustiveSearch'+str(dens)+'.csv', 'w', newline='') as file:
    #with open('greedy'+str(dens)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['vertices', 'edges', 'Density','Comparisons', 'Divisions', 'Additions' , 'Solutions', 'Time', 'resposta', 'peso'])

        for i in range(1, 22):
            print(i)
            g = Graph(i, dens)
            g.buildGraph()
            #g.showGraph()

            start = time.time()
            iset = exhaustiveSearch(g)
            #iset = greedy(g)
            end = time.time()

            counts=printResults(iset, g)

            writer.writerow([g.num_vertices, g.num_edges, g.density,counts[0], counts[1], counts[2], counts[3], end - start, iset, counts[4]])

writeCSV(50)