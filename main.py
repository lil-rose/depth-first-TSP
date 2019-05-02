# from depthfirst import findDepthFirst
from DepthFirsSearch import DepthFirstSearch
import GraphUtils
import matplotlib.pyplot as plt
import numpy as np
import time

def generateStatistics(n):
    arrayTimes = []
    for i in range(2,n+1):
        print('i:', i)
        randoms = GraphUtils.arrayRandoms(n)
        graph = GraphUtils.createGraph(randoms, i)
        DF = DepthFirstSearch(graph, i)

        start = time.time()
        DF.DepthFirsIterative(0)
        end = time.time()

        arrayTimes.append(end-start)
    return arrayTimes

def plotArrayTimes(arrayTimes, n):
    fig, ax = plt.subplots(figsize=(10,10))
    # agregando ejes a la figura:
    arrayN = np.arange(2,n+1)
    # ax = fig.add_axes([0.0, 0.0, 1.0, 1.0]) #izquierda, abajo, ancho, altura (rango de 0 a 1)
    ax.plot(arrayN, arrayTimes, 'b')
    ax.set_xlabel('n') # Notice the use of set_ to begin methods
    ax.set_ylabel('tiempo (segundos)')
    ax.set_title('Tiempo de ejecución')
    # plt.ylim(0,arrayTimes[n-3])
    plt.xlim(0,n + 1)
    nameFile = 'estadistica' + str(n) + '.jpg'
    fig.savefig(nameFile)

def testStatistics():
    n = 11
    arrayTimes = generateStatistics(n)
    plotArrayTimes(arrayTimes, n)

def showPath(depthFirstObj):
    pathStr = '[0]'
    bestSolution = depthFirstObj.solutionsArr[depthFirstObj.bestSolution]
    for i in range(0, len(bestSolution) - 1):
        row = bestSolution[i]
        col = bestSolution[i+1]
        pathStr = pathStr + ' -> ' + str(depthFirstObj.graph[row, col]) + ' -> [' + str(bestSolution[i+1]) + ']'
    return pathStr


n = 5
ejemplo = GraphUtils.arrayRandoms(n)

ejemploGrafo = GraphUtils.createGraph(ejemplo, n)

objetoEjemplo = DepthFirstSearch(ejemploGrafo, n)
objetoEjemplo.DepthFirsIterative(0)

showPath(objetoEjemplo)

# start = time.time()


# objetoEjemplo.findDepthFirst(0)

# end = time.time()

# print('TIEMPO: ', end - start)

### AQUI EMPIEZA EL SCRIPT
def separation():
    print('\n-----------------------\n')


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



    

