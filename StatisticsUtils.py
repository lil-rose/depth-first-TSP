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