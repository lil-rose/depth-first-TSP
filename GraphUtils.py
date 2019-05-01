import random
import numpy as np

def arrayRandoms(n):
    lenRandoms = ((n**2) - n) / 2
    lenRandoms = int(lenRandoms)
    arrRand = []
    for i in range(lenRandoms):
        number = random.randrange(1, 101, 1)
        arrRand.append(number)
    return arrRand

def createGraph(arrRand, n):
    k = 0
    graph = np.zeros((n,n))
    for i in range(1, n):
        for j in range(i, n):
            graph[i-1, j] = arrRand[k]
            graph[j, i-1] = arrRand[k]
            k += 1
    return graph
            
