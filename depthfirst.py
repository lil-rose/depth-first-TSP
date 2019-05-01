import numpy as np

solutionsArr = []
costsArray = []

def findDepthFirst(graph, n):
    """
    graph: Matriz con los valores de los nodos y los costos entre nodos
    n: cantidad de nodos del grafo.
    """
    # global solutionsArr
    # global costsArray
    depthFirst(graph, n, 0, [0], 0)
    print('------------------------')
    print('------------------------')
    print('------------------------')
    print('FIN DE BÚSQUEDA DE SOLUCION')
    print('solutionsArr', solutionsArr)
    print('costsArray', costsArray)
    print('------------------------')
    print('------------------------')
    print('------------------------')
    return solutionsArr, costsArray

def depthFirst(graph, n, currentNode, currentPath, cost):
    global solutionsArr
    global costsArray
    """
    graph: Matriz con los valores de los nodos y los costos entre nodos
    n: cantidad de nodos del grafo.
    currentNode: Nodo actual que se está evaluando.
    currentPath: Array que representa el camino recorrido hasta el momento
    cost: Costo acumulado hasta el momento por el camino recorrido
    solutionsArr: array que contiene todos los caminos solución encontrados. 
    """
    print('currentPath', currentPath)
    if len(currentPath) == n: 
        solutionsArr.append(currentPath)
        costsArray.append(cost)
        print('Solución encontrada!')
        print('Solución: ', currentPath)
        print('------------------------')
        print('solutionsArr hasta el momento D:::::')
        print(solutionsArr)
    else:
        for i in range(n):
            if not (i in currentPath):
                currentPath.append(i)
                cost += graph[currentNode, i]

                # Llamada recursiva:
                depthFirst(graph, n, i, currentPath, cost)

                currentPath.pop()
                cost -= graph[currentNode, i]

def hola():
    print('hola from depthfirst')
    
