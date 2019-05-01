# from depthfirst import findDepthFirst
from DepthFirsSearch import DepthFirsSearch
import GraphUtils
import numpy as np

# n = 4
n = 16
ejemplo = GraphUtils.arrayRandoms(n)
print('Ejemplo randoms:')
print(ejemplo)

ejemploGrafo = GraphUtils.createGraph(ejemplo, n)
print('Ejemplo grafo:')
print(ejemploGrafo)


objetoEjemplo = DepthFirsSearch(ejemploGrafo, n)
objetoEjemplo.findDepthFirst(0)

"""
    self.solutionsArr = []  
    self.costsArray = []
    self.graph = graph
    self.n = n
    self.bestSolution = -1
"""

print('Soluciones encontradas: ')
print(objetoEjemplo.solutionsArr)

print('Costos soluciones: ')
print(objetoEjemplo.costsArray)

print('Mejor solución: ')
print(objetoEjemplo.bestSolution)