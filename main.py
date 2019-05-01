# from depthfirst import findDepthFirst
from DepthFirsSearch import DepthFirsSearch
import GraphUtils
import numpy as np
import time

DepthFirsSearch

    # i.push(0)
    # print(i)

# n = 4
n = 10
ejemplo = GraphUtils.arrayRandoms(n)
# print('Ejemplo randoms:')
# print(ejemplo)

ejemploGrafo = GraphUtils.createGraph(ejemplo, n)
# print('Ejemplo grafo:')
# print(ejemploGrafo)


objetoEjemplo = DepthFirsSearch(ejemploGrafo, n)


start = time.time()

objetoEjemplo.DepthFirsIterative(0)

end = time.time()


print('TIEMPO: ', end - start)
# print('graph: ')
# print(objetoEjemplo.graph)
# print('- - - - - - - - - - - - - - - - ')

# print('solutionsArr:')
# for s in objetoEjemplo.solutionsArr:
#     print(s)
# print('- - - - - - - - - - - - - - - - ')
# print('costsArray', objetoEjemplo.costsArray)
# print('bestSolution', objetoEjemplo.bestSolution)
# print('lowerCost', objetoEjemplo.lowerCost)

# objetoEjemplo.findDepthFirst(0)

# """
#     self.solutionsArr = []  
#     self.costsArray = []
#     self.graph = graph
#     self.n = n
#     self.bestSolution = -1
# """

# print('Soluciones encontradas: ')
# print(objetoEjemplo.solutionsArr)

# print('Costos soluciones: ')
# print(objetoEjemplo.costsArray)

# print('Mejor solución: ')
# print(objetoEjemplo.bestSolution)

