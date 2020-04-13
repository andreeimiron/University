import networkx
from Chromosome import Chromosome
from GA import GA

def readNetwork(fileName):
    network = {}
    degrees = []
    file = './files/' + fileName
    data = networkx.read_gml(file, label = 'id')
    
    network['noNodes'] = data.number_of_nodes()
    network['noEdges'] = data.number_of_edges()
    network['mat'] = networkx.adjacency_matrix(data).todense()
    for node, value in data.degree():
        degrees.append(value)
    network['degrees'] = degrees
    network['graph'] = data

    return network

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    
    Q = 0.0
    for i in range(noNodes):
        for j in range(noNodes):
            if (communities[i] == communities[j]):
               Q += (mat.item(i, j) - degrees[i] * degrees[j] / M)
    
    return Q * 1 / M

def initParams(fileName):
    network = readNetwork(fileName)
    param = {
        'popSize': 500,
        'noGen': 50
    }
    problParam = {
        'function': modularity,
        'network': network
    }

    return param, problParam

def communitiesNumber(param, repres):
    communities = []

    for _ in range(param['network']['noNodes'] + 1):
        communities.append([])

    for i in range(param['network']['noNodes']):
        communities[repres[i]].append(i + 1)

    comm = 0
    for i in range(len(communities)):
        if len(communities[i]) > 0:
            comm += 1
            
    return comm

def main():
    #fileName = 'dolphins.gml'
    #fileName = 'football.gml'
    fileName = 'karate.gml'
    #fileName = 'krebs.gml'
    #fileName = 'ex1.gml'
    #fileName = 'ex2.gml'
    
    param, problParam = initParams(fileName)
    ga = GA(param, problParam)

    ga.initialisation()
    ga.evaluation()

    globalBest = Chromosome(problParam);
    generation = 0
    while not generation > param['noGen']:
        ga.oneGeneration()
        bestChromosome = ga.bestChromosome()
        if bestChromosome.fitness > globalBest.fitness:
            globalBest = bestChromosome
        print('\nGeneration: ' + str(generation))
        print(bestChromosome)
        print('Fitness: ' + str(bestChromosome.fitness))
        print('Communities: ' + str(communitiesNumber(problParam, bestChromosome.repres)))
        generation += 1
    
    print('\nGlobal Best')
    print(globalBest)
    print('Fitness: ' + str(globalBest.fitness))
    

if __name__ == '__main__':
    main()