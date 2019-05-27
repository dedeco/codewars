import numpy as np

def getPoints(stations):
    points = []
    for s in stations:
        s = str(s)
        if len(s)==1:
            s = str(0)+s
        points.append([int(s[0]),int(s[1])])
    #print(points)
    return points

def setPoints(points):
    a = np.zeros(shape=(10,10))   
    i = 1
    for x,y in points:
        a[x][y] = i
        i+=1
    return a
    
import collections

def bfs(m, start, goal, last):
    avoid = range(goal+1,4+1) 
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        #print(path)
        x, y = path[-1]
        #print('x',x,'y',y,'seen',seen)
        #print('q',queue)
        #print(m[x][y])
        if m[x][y] == goal:
            for x,y in path[:]:
                if m[x][y] ==0:
                    m[x][y] = -1
            return path
        for x2, y2 in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            print('x2y2', x2, y2, path)
            #if 0 <= x2 < m.shape[0] and 0 <= y2 < m.shape[1] and (x2, y2) not in seen:
            if 0 <= x2 < m.shape[0] and 0 <= y2 < m.shape[1] and (x2, y2) not in last and (x2, y2) not in seen and m[x2][y2] not in avoid:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def makeUnique(l):
    seen = set()
    seen_add = seen.add
    r = [x for x in l if not (x in seen or seen_add(x))]
    return r

def four_pass(stations):
    points = getPoints(stations)
    M = setPoints(points)
     
    print('matriz inicial:')
    print(M)

    # calculando o caminha a cada ponto e concatenando...
    path = []
    #print('points',points)
    for i in range(2, len(points) + 1):
        #print(i,points[i-2], 'goal', i)
        path = path + (bfs(M, (points[i-2][0], points[i-2][1]), i, path) or [])
    r = makeUnique([int(str(x)+str(y)) for x, y in path])
 

    print('matriz minha:')
    print(M)
    
    correct = [37, 27, 26, 25, 24, 23, 22, 21, 31, 41, 51, 61, 71,
               81, 91, 92, 93, 94, 95, 96, 86, 76, 66, 56, 46, 36]

    M = setPoints(points)
    for x, y in getPoints(correct):
        if M[x][y] == 0:
            M[x][y] = -1
    print('matriz correct:')
    print(M) 

    return r

if __name__ == "__main__":    
    print(four_pass([37, 61, 92, 36]))
""" 
    example_tests = [
        [1, 69, 95, 70],
        [0, 49, 40, 99],
        [37, 61, 92, 36],
        [51, 24, 75, 57],
        [92, 59, 88, 11]]
    
    example_solutions = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 29, 39, 49, 59, 69, 79,
	    78, 77, 76, 75, 85, 95, 94, 93, 92, 91, 81, 71, 70],
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 29, 39, 49, 48, 47, 46, 45, 44, 43,
	    42, 41, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 69, 79, 89, 99],
	[37, 27, 26, 25, 24, 23, 22, 21, 31, 41, 51, 61, 71,
	    81, 91, 92, 93, 94, 95, 96, 86, 76, 66, 56, 46, 36],
	[51, 41, 42, 43, 44, 34, 24, 25, 35, 45, 55, 65, 75, 76, 77, 67, 57],
	[92, 93, 94, 95, 96, 97, 98, 99, 89, 79, 69, 59, 58, 68, 78, 88, 87, 77, 67, 57, 47, 37, 27, 17, 16, 15, 14, 13, 12, 11]]

    for test_case, ref_solution in zip(example_tests, example_solutions):
        print('TEST CASE', test_case)
        print('ME:', four_pass(test_case[:]), len(four_pass(test_case[:])))
        print('CW:', ref_solution, len(ref_solution))

 """
# [0, 10, 20, 30, 40, 50, 60, 61, 62, 63, 64, 65, 75, 85, 84, 83, 93, 94, 95, 96, 86, 76, 66, 56, 46, 36]
# [0, 10, 20, 30, 40, 50, 60, 61, 62, 63, 64, 65, 75, 85, 95, 94, 93, 83, 73, 53, 43, 33, 34, 35, 36]
