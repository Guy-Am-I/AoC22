filename = 'input.txt'
"""
Start by figuring out the signal being sent by the CPU. 
The CPU has a single register, X, which starts with the value 1. 
It supports only two instructions:

addx V takes two cycles to complete. After two cycles, 
the X register is increased by the value V. (V can be negative.)
noop takes one cycle to complete. It has no other effect.

consider the signal strength 
(the cycle number multiplied by the value of the X register)
 during the 20th cycle and every 40 cycles after that
that is, during the 20th, 60th, 100th, 140th, 180th 220th cycles)
"""

# map cycles to values somehow
# either as member of class x or some sort of long list series
# created by either noop or addx lambda functions

cycles = [] #index cycle number, value x register
x_value = 1

def instruction(cmnd, val=0):
    global x_value
    if cmnd == 'noop':
        cycles.append(x_value)
    elif cmnd == 'addx':
        cycles.append(x_value)
        cycles.append(x_value)
        x_value += val
    else: raise Exception("Cmnd not supported")

def getSignalStrengths():
    indicies = [20, 60, 100, 140, 180, 220 ]
    return ([(cycleNum * cycles[cycleNum - 1])
            for cycleNum in range(1, len(cycles)+1)
                 if (cycleNum in indicies)])

def drawCrtScreen():
    lit = '#'
    dark = '.'
    #assume cycles list is full of x register values
    for cycleNum, regVal in enumerate(cycles):
        if (cycleNum % 40 == 0):
            print() #newline
        crtPos = cycleNum % 40
        #lit if x reg value in current position (cycleNum)
        spritePos = [regVal - 1, regVal, regVal + 1]
        if crtPos in spritePos:
            print(lit, end='')
        else: print(dark, end='')



if __name__ == "__main__":
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            cmd = line.split(' ')
            if (len(cmd) > 1):
                instruction(cmd[0], int(cmd[1]))
            else: instruction(cmd[0])
    cycles.append(x_value)
    #strengths = getSignalStrengths()
    #print(sum(strengths))
    drawCrtScreen()