from random import randint

def generateNewValue(min, max):
    return randint(min, max)

def initRepres(network):
    repres = []
    
    for i in range(network['noNodes']):
        value = generateNewValue(0, network['noNodes'] - 1)
        repres.append(value)
    
    for i in range(len(repres)):
        for j in range(len(repres)):
            if network['mat'].item(i, j) == 1:
                repres[j] = repres[i]

    return repres

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = initRepres(problParam['network'])
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring
    
    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        self.__repres[pos] = self.__repres[generateNewValue(0, self.__problParam['network']['noNodes'] - 1)]
        
    def __str__(self):
        return 'Chromo: ' + str(self.__repres)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness