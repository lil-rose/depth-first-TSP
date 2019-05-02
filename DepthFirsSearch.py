import numpy as np
import itertools
class DepthFirstSearch:
    def __init__(self, graph, n):
        """
            graph: Matriz con los valores de los nodos y los costos entre nodos
            n: cantidad de nodos del grafo.
        """
        self.solutionsArr = []
        self.costsArray = []
        self.graph = graph
        self.n = n
        self.bestSolution = 0
        self.lowerCost = -1

    def findDepthFirst(self, firstNode):
        self.depthFirst(firstNode, [0], 0, 0)


    def depthFirst(self, currentNode, currentPath, cost, k):
        """
            currentNode: Nodo actual que se está evaluando.
            currentPath: Array que representa el camino recorrido hasta el momento
            cost: Costo acumulado hasta el momento por el camino recorrido
        """
        print('k:', k)
        k  += 1
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
                    self.depthFirst(i, currentPath, cost, k)

                    currentPath.pop()
                    cost -= self.graph[currentNode, i]

    def DepthFirsIterative(self, root):
        self.lowerCost = 100*self.n

        arrayOfNodes = []
        for i in range(self.n):
            if i != root:
                arrayOfNodes.append(i)
        permutArrays = itertools.permutations(arrayOfNodes)
        k = 0
        for permut in permutArrays:
            # print('iteracion: ', k)
            permut = list(permut)
            permut.insert(0, root)
            self.solutionsArr.append(permut)
            cost = 0
            for i in range(self.n-1):
                row = permut[i]
                col = permut[i+1]
                cost += self.graph[row, col]
            
            self.costsArray.append(cost)
            if(self.lowerCost > cost):
                self.lowerCost = cost
                self.bestSolution = k
            k += 1


        

    



    
