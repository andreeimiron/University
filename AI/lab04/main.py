from GA import GA

def readNetwork(fileName):
    network = {}
    mat = []
    file = open('./files/' + fileName, 'r')
    n = int(file.readline())
    network['noNodes'] = n
    
    for _ in range(n):
        data = file.readline()
        values = data.split(',')
        line = []
        for v in values:
            line.append(int(v))
        mat.append(line)
    network['mat'] = mat

    return network

def solve(repres, network):
    mat = network['mat']
    n = network['noNodes']
    sum = 0

    for i in range(n - 1):
        currentNode = repres[i]
        nextNode = repres[i + 1]
        sum += mat[currentNode - 1][nextNode - 1]
    sum += mat[repres[-1] - 1][repres[0] - 1]

    return sum

def initParams(fileName):
    network = readNetwork(fileName)
    param = {
        'popSize': 20,
        'noGen': 500,
        'network': network
    }
    problParam = {
        'function': solve,
        'noNodes': network['noNodes']
    }
    
    return param, problParam

def main():
    #fileName = 'easy1.txt'
    #fileName = 'medium.txt'
    fileName = 'hard_02.txt'
    
    param, problParam = initParams(fileName)
    ga = GA(param, problParam)
    ga.initialisation()
    ga.evaluation()

    for i in range(param['noGen'] - 1):
        ga.oneGenerationElitism()
        print(ga.bestChromosome())

if __name__ == '__main__':
    main()