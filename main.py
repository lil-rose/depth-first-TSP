# from depthfirst import findDepthFirst
from DepthFirsSearch import DepthFirstSearch
import GraphUtils
import StatisticsUtils
import matplotlib.pyplot as plt
import numpy as np
import time

def showPath(depthFirstObj):
    pathStr = '[0]'
    bestSolution = depthFirstObj.solutionsArr[depthFirstObj.bestSolution]
    for i in range(0, len(bestSolution) - 1):
        row = bestSolution[i]
        col = bestSolution[i+1]
        pathStr = pathStr + ' -> ' + str(depthFirstObj.graph[row, col]) + ' -> [' + str(bestSolution[i+1]) + ']'
    return pathStr

def separation():
    print('\n-----------------------\n')

# Script begins
while n != -1:
    separation()
    print('Ingrese un valor de n (cantidad de ciudades)')
    print('Si desea salir del programa, ingrese 0')
    n = input()
    print()
    if n.isnumeric():
        n = int(n)
        if n == 0:
            print('Hasta luego :)')
            break
        elif n < 2:
            print('Debe ingresar una cantidad de ciudades mayor o igual a 2.')
        else:
            print('\nNumero de ciudades seleccionado:   ', n)
            randoms = GraphUtils.arrayRandoms(n)
            graph = GraphUtils.createGraph(randoms, n)
            print('\nGrafo generado:\n')
            print(graph)

            DF = DepthFirstSearch(graph, n)

            start = time.time()
            DF.DepthFirsIterative(0)
            end = time.time()

            print('\nTiempo de ejecución: ', end - start, 'segundos.\n')

            pathStr = showPath(DF)
            print('\nCamino solución: ', pathStr)
            print('\nCosto total: ', DF.lowerCost)
    else:
        print('Debe ingresar un valor numérico.')



    

