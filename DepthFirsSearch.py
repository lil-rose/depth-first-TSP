import numpy as np
import copy
class DepthFirsSearch:
    def __init__(self, graph, n):
        """
            graph: Matriz con los valores de los nodos y los costos entre nodos
            n: cantidad de nodos del grafo.
        """
        self.solutionsArr = []
        self.costsArray = []
        self.graph = graph
        self.n = n
        self.bestSolution = -1

    def findDepthFirst(self, firstNode):
        self.depthFirst(firstNode, [0], 0)


    def depthFirst(self, currentNode, currentPath, cost):
        """
            currentNode: Nodo actual que se está evaluando.
            currentPath: Array que representa el camino recorrido hasta el momento
            cost: Costo acumulado hasta el momento por el camino recorrido
        """
        if len(currentPath) == self.n:
            solution = []
            for cp in currentPath:
                solution.append(cp)
            self.solutionsArr.append(solution)
            self.costsArray.append(cost)
            cantSolutionsFound = len(self.costsArray)
            if cantSolutionsFound == 1:
                self.bestSolution = 0
            elif self.costsArray[self.bestSolution] > self.costsArray[cantSolutionsFound - 1]:
                self.bestSolution = cantSolutionsFound - 1

        else:
            for i in range(self.n):
                if not (i in currentPath):
                    currentPath.append(i)
                    cost += self.graph[currentNode, i]

                    #depthFirst(graph, n, i, currentPath, cost)
                    self.depthFirst(i, currentPath, cost)

                    currentPath.pop()
                    cost -= self.graph[currentNode, i]

    # def depthFirst(graph, n):
    #     currentNode = 0
    #     cost = 0
    #     currentPath = 0
    #     solutionsArr = []
    #     costsArray = []
    #     condition = True

    #     while condition:



    
