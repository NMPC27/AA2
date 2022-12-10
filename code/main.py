import time
from graph import Graph
from search import RandomSearch
from search import printResults
import csv


def writeCSV(dens):

    with open('RandomSearch'+str(dens)+'.csv', 'w', newline='') as file:
    #with open('greedy'+str(dens)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['vertices', 'edges', 'Density','Comparisons', 'Divisions', 'Additions' , 'Solutions', 'Time', 'resposta', 'peso'])

        for i in range(1, 101):
            print("vertices", i)
            g = Graph(i, dens)
            g.buildGraph()
            #g.showGraph()

            start = time.time()
            iset = RandomSearch(g)
            end = time.time()

            counts=printResults(iset, g)

            writer.writerow([g.num_vertices, g.num_edges, g.density,counts[0], counts[1], counts[2], counts[3], end - start, iset, counts[4]])

writeCSV(100)

# g = Graph(100, 0)
# g.buildGraph()
# #g.showGraph()
# start = time.time()
# iset = RandomSearch(g)
# end = time.time()

# counts=printResults(iset, g)