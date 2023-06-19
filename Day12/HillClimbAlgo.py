import numpy as np
import collections

filename = 'input.txt'

array2D = []

# with open(filename, 'r') as f:
#     while (line := f.readline().rstrip()):
#         array2D.append(list(line))

with open(filename) as file:
    for line in file.readlines():
        array2D.append(line.rstrip())

width = len(array2D[0])
height = len(array2D)

numpyArr = np.array(array2D)
start = np.argwhere(numpyArr == 'S') #20 0
end = np.argwhere(numpyArr == 'E')# 20 148
# print(array2D)
#print(f'Start: {start}, End: {end}')

def validStep(fromVal, toVal):
    if fromVal == 'S':
        convFrom = 'a'
    elif fromVal == 'E':
        convFrom = 'z'
    else:
        convFrom = fromVal
    
    if toVal == 'S':
        convTo = 'a'
    elif toVal == 'E':
        convTo = 'z'
    else:
        convTo = toVal

    res = 0 <= ord(convTo) - ord(convFrom) <= 1
    # if (convFrom == 'o' or convTo == 'o'): #and (convFrom == 'o' or convTo == 'o'):
    #     print(f'valid step? from: {fromVal}  to: {toVal} res: {res}')
    
    return res

def bfs(grid, start):
    global width, height
    print(f'width: {width}, height: {height}')
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == 'E':
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if (0 <= x2 < width and 0 <= y2 < height):
                    if grid[y][x] == 'n':
                        print(f'y,x: {(y, x)}, y2,x2: {(y2,x2)}, val: {grid[y2][x2]}')
                    if(validStep(grid[y][x], grid[y2][x2]) and (x2, y2) not in seen):
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))

path = bfs(array2D, (0,20))
print(path)
#print(len(path) - 1)