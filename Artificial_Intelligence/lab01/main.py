import math

def prob2(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def testProb2():
    assert prob2(5, 2, 7, 2) == 2
    assert prob2(1, 5, 4, 1) == 5

def prob4(list):
    elems = list.split(" ")
    l = []
    l2 = []
    
    for e in elems:
        if e in l:
            l2.append(e)
            l.remove(e)
        elif e not in l2:
            l.append(e)
            
    return l


def testProb4():
    elems = prob4("ana are ana are mere rosii ana")
    
    assert(len(elems) == 2)
    assert(elems[0] == "mere")
    assert(elems[1] == "rosii")

def convert(n):
    aux = ""
    
    while (n > 0):
        if (n % 2):
            aux += "1"
        else:
            aux += "0"
        n //= 2 
    
    return aux[::-1]

def prob8(n):
    list = []
    
    for i in range(1, n + 1):
        list.append(convert(i))
        
    return list

def testProb8():
    list = prob8(3)
    
    assert(len(list) == 3)
    assert(list[0] == "1")
    assert(list[1] == "10")
    assert(list[2] == "11")
    
def prob9(mat, x1, y1, x2, y2):
    sum = 0
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += mat[i][j]
            
    return sum


def testProb9():
    mat = [[0, 2, 5, 4, 1],
           [4, 8, 2, 3, 7],
           [6, 3, 4, 6, 2],
           [7, 3, 1, 8, 3],
           [1, 5, 7, 9, 4]]
    
    assert prob9(mat, 0, 0, 1, 1) == 14
    assert prob9(mat, 1, 1, 3, 3) == 38
    
def nrUnu(list):
    st = 0
    n = dr = len(list)
    
    while (st <= dr):
        m = (st + dr) // 2
        if (list[m] == 1 and (m == 0 or list[m - 1] == 0)):
            return n - m
        elif (list[m] == 1):
            dr = m - 1
        else:
            st = m + 1


def prob10(mat):
    indexLinie = -1
    max = -1

    for index, linie in enumerate(mat):
        sum = nrUnu(linie)
        if sum > max:
            max = sum
            indexLinie = index
            
    return indexLinie

def runPb10():
    matrix = [[0, 0, 0, 1, 1],
              [0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1]]
    
    lineIndex = getMaxLineIndex(matrix)

    print(matrix[lineIndex])

def testProb10():
    mat = [[0, 0, 1, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1],
           [1, 1, 1, 1, 1]]
    
    assert prob10(mat) == 3

def main():
    testProb2()
    print("Prob 2 OK!")
    testProb4()
    print("Prob 4 OK!")
    testProb8()
    print("Prob 8 OK!")
    testProb9()
    print("Prob 9 OK!")
    testProb10()
    print("Prob 10 OK!")
    
main()
    