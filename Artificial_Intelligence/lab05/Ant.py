class Ant:
    def __init__(self, city):
        self.__cities = [city]
    
    def addCity(self, city):
        self.__cities.append(city)
    
    def isVisited(self, city):
        return city in self.__cities
    
    def getCities(self):
        return self.__cities
    
    def numberOfCities(self):
        return len(self.__cities)
    
    def getCost(self, mat):
        cost = 0
        
        for i in range (len(self.__cities) - 1):
            cost += mat[self.__cities[i] - 1][self.__cities[i + 1] - 1]
        cost += mat[self.__cities[-1] - 1][self.__cities[0] - 1]
        
        return cost