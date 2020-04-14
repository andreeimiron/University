import random
from Ant import Ant

def readFile(mat, fileName):
    file = open('./files/' + fileName, 'r')
    n = int(file.readline())
    
    for _ in range(n):
        data = file.readline()
        values = data.split(',')
        line = []
        for v in values:
            line.append(int(v))
        mat.append(line)
    
    return n

def initRoutes(routes, n):
    for _ in range(n):
        line = []
        for _ in range(n):
            line.append(0)
        routes.append(line)

def initialisation(ants, n):
    cities = []
    
    for i in range(1, n + 1):
        cities.append(i)
    random.shuffle(cities)
    del ants[:]
    for c in cities:
        ants.append(Ant(c))

def calculatePheromone(city, ant, routes, mat, n):
    pheromone = 0
    
    for i in range(n):
        if not ant.isVisited(i + 1):
            pheromone += routes[city - 1][i] + 1.0 / mat[city - 1][i]
    
    return pheromone

def calculateProbabilities(ant, routes, mat, n):
    probabilities = []
    city = ant.getCities()[-1]
    pheromone = calculatePheromone(city, ant, routes, mat, n)
        
    for i in range(n):
        if not ant.isVisited(i + 1):
            value = routes[city - 1][i] + 1.0 / mat[city - 1][i]
            probabilities.append(value / pheromone)
        else:
            probabilities.append(0)
            
    return probabilities

def nextCity(ant, routes, mat, n):
    value = random.uniform(0, 1)
    probabilities = calculateProbabilities(ant, routes, mat, n)
    sum = 0
    
    for i in range(n):
        sum += probabilities[i]
        if sum >= value:
            return i + 1

def move(ants, routes, mat):
    for ant in ants:
        city = nextCity(ant, routes, mat, len(ants))
        ant.addCity(city)

def update(ants, routes):
    for i in range(len(ants)):
        for j in range(len(ants)):
            routes[i][j] *= 0.5 # evaporation
    for ant in ants:
        visited = ant.getCities()
        routes[visited[-2] - 1][visited[-1] - 1] += 0.25 # pheromone

def updateRoute(ants, mat, route, cost):
    for ant in ants:
        if cost > ant.getCost(mat):
            route = ant.getCities()
            cost = ant.getCost(mat)
            
    return route, cost
        
def solve(mat, n):
    ants = []
    routes = []
    bestRoute = []
    bestCost = 99999
    
    initRoutes(routes, n)
    
    for _ in range(50):
        initialisation(ants, n)
        while ants[0].numberOfCities() < n:
            move(ants, routes, mat)
            update(ants, routes)
        bestRoute, bestCost = updateRoute(ants, mat, bestRoute, bestCost)
    
    return bestRoute, bestCost

def main():
    file = 'easy_01_tsp.txt'
    #file = 'easy_03_tsp.txt'
    #file = 'medium_01_tsp.txt'
    #file = 'hard_01_tsp.txt'
    
    mat = []
    n = readFile(mat, file)
    route, cost = solve(mat, n)
    
    print(route)
    print(cost)
    
if __name__ == '__main__':
    main()