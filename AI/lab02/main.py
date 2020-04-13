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
    src = int(file.readline())
    dest = int(file.readline())
    
    return n, src, dest

# determ varful cu valoarea distantei minime, din cele nevizitate
def minDistance(n, dist, visited):
    min = 99999
    vertex = -1

    for index in range(n):
        if dist[index] < min and dist[index] != 0 and index + 1 not in visited:
            min = dist[index]
            vertex = index + 1

    return min, vertex


def solve(mat, n, src = None, dest = None):
    visited = [src] if src else [1]
    sum = 0

    for i in range(n - 1):
        if len(visited) != n:
            min, vertex = minDistance(n, mat[visited[-1] - 1], visited)
            sum += min
            visited.append(vertex)
            if (dest and vertex == dest):
                break
    
    if src is None:
        sum += mat[visited[-1] - 1][visited[0] - 1]

    print(len(visited))
    print(visited)
    print(sum)


def main():
    #file = 'easy_01_tsp.txt'
    #file = 'easy_03_tsp.txt'
    #file = 'medium_01_tsp.txt'
    file = 'hard_01_tsp.txt'
    
    mat = []
    n, src, dest = readFile(mat, file)
    
    solve(mat, n)
    solve(mat, n, src, dest)

if __name__ == '__main__':
    main()
