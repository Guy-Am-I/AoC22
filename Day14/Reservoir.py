from enum import Enum
#get list of points from input  
# 498,4 -> 498,6 -> 496,6
filename = 'input.txt'
minX = 500
maxX, maxY = 0,0
VOID = (-1, -1)
INFY = 1000

def add_rocks(line):
    global content
    # assign values at coordinates as needed (based on your grid)
    
    for (x,y) in line: content[y][x-minX] = '+'

def print_grid():
    print(frameLine)
    for i,row in enumerate(reversed(content),1):
        values = " ".join(f"{v:{width}s}" for v in row)
        line   = contentLine.replace("values",values)
        line   = line.replace("#",f"{rows-i:{width}d}")
        print(line)
    print(frameLine)

def x_axis():
    numLine = contentLine.replace("|"," ")
    numLine = numLine.replace("#"," "*width)
    colNums = " ".join(f"{i:<{width}d}" for i in range(minX, minX+cols))
    numLine = numLine.replace("values",colNums)
    print(numLine)
    
def ppp():
    print_grid()
    x_axis()
    
def linePoints(point1, point2):
    global minX, maxX, maxY
    idx = 0
    minX = min(minX, point1[0], point2[0])
    maxX = max(maxX, point1[0], point2[0])
    maxY = max(maxY, point1[1], point2[1])
    
    if point1[0] == point2[0]: idx = 1
    
    f = min(point1[idx], point2[idx])
    t = max(point1[idx], point2[idx])
        
    l = list(range(f, t+1))
    
    return [(val,point1[1]) for val in l] if idx == 0 else [(point1[0],val) for val in l] 

#PART 2 - SAND
class res(Enum):
    SUCCESS = 0
    BLOCKED = 1
    ENDLESS_VOID = 2
    
def checkPoint(point):
    x,y = point[0], point[1]
    if y > maxY: return res.ENDLESS_VOID
    elif content[y][x-minX] == '+' or content[y][x-minX] == 'o':
        return res.BLOCKED
    else: 
        return res.SUCCESS

def moveSand(curr_pos):
    x, y = curr_pos[0], curr_pos[1]
    #try falldown
    downPoint = (x, y+1)
    move = checkPoint(downPoint)
    if move == res.SUCCESS: return downPoint
    elif move == res.BLOCKED:
        #if blocked try  down-left
        downLeftPoint = (x-1, y+1)
        move2 = checkPoint(downLeftPoint)
        if move2 == res.SUCCESS: return downLeftPoint
        elif move2 == res.BLOCKED:
            #if blocked try down-right
            downRightPoint = (x+1, y+1)
            move3 = checkPoint(downRightPoint)
            if move3 == res.SUCCESS: return downRightPoint
            elif move3 == res.BLOCKED:
                return curr_pos
            else: return VOID
        else: return VOID      
    else: return VOID
    
with open(filename) as file:
    allLines = []

    while (line := file.readline().rstrip()):
        lineEnds = line.split(' -> ')
        points = [(int(x),int(y)) for x,y in [item.split(',') for item in lineEnds]]
        prev = points[0]
        for key in range(1,len(points)):
            curr = points[key]
            pointsBetween = linePoints(prev, curr)
            allLines.append(pointsBetween)
            prev = curr
    infyLine = linePoints((minX - INFY, maxY + 2), (maxX + INFY, maxY + 2))
    cols = (maxX - minX) + 1
    rows = (maxY - 0) + 1

    content = [["."]*cols for _ in range(rows)]

    # build frame
    width       = len(str(max(rows,cols)-1))
    contentLine = "# | values |"

    dashes      = "-".join("-"*width for _ in range(cols))
    frameLine   = contentLine.replace("values",dashes)
    frameLine   = frameLine.replace("#"," "*width)
    frameLine   = frameLine.replace("| ","+-").replace(" |","-+")
        
    for linee in allLines:
        add_rocks(linee)
    add_rocks(infyLine)

totalSandUnits = 1
sandPoint = (500, 0)
while True:
    nextPoint = moveSand(sandPoint)
    if nextPoint == VOID: break
    if nextPoint == sandPoint: #blocked
        print(f'Blocked at: {sandPoint}')
        if (nextPoint == (500,0)): break
        content[sandPoint[1]][sandPoint[0]-minX] = 'o'
        sandPoint = (500, 0)
        totalSandUnits += 1
    else:
        sandPoint = nextPoint
print(f'Total: {totalSandUnits}')