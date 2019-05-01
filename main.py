# from depthfirst import findDepthFirst
from DepthFirsSearch import DepthFirsSearch
import numpy as np

n = 4

ejemploGrafo = np.zeros((n,n))

ejemploGrafo[0,1] = 10
ejemploGrafo[0,2] = 15
ejemploGrafo[0,3] = 12

ejemploGrafo[1,0] = 10
ejemploGrafo[1,2] = 8
ejemploGrafo[1,3] = 13

ejemploGrafo[2,0] = 15
ejemploGrafo[2,1] = 8
ejemploGrafo[2,3] = 6

ejemploGrafo[3,0] = 12
ejemploGrafo[3,1] = 13
ejemploGrafo[3,2] = 6

# print('ejemploGrafo')
# print(ejemploGrafo)

objetoEjemplo = DepthFirsSearch(ejemploGrafo, n)
print('totalPaths', objetoEjemplo.totalPaths)
# print('objetoEjemplo:')
# print(objetoEjemplo.graph)
# print(objetoEjemplo.n)
# print(objetoEjemplo.solutionsArr)
# print(objetoEjemplo.costsArray)

# solutionsArr, costsArray = objetoEjemplo.findDepthFirst()

objetoEjemplo.findDepthFirst()
# solutionsArr, costsArray = depthfirst.findDepthFirst(ejemploGrafo, n)

# print('solutionsArr: ')
# print(objetoEjemplo.solutionsArr)
# print('----------------------------------')
# print('costsArray: ')
# print(costsArray)