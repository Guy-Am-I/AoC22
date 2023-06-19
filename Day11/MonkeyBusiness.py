from GameManager import Manager
from Monkeys import Monkey

filename = 'input.txt'
supermodulo = 1
bossMan = Manager()
    
def buildFunc(lhs, oper, rhs):
    if oper == '*':
        if rhs == 'old':
            return lambda x: x * x
        else: return lambda x: x * int(rhs)
    else: #+
        if rhs == 'old':
            return lambda x: x + x
        else: return lambda x: x + int(rhs)


def readMonkey(file):
    global bossMan
    global supermodulo
    itemList = None
    while (line := file.readline().rstrip()):
        if 'items' in line:
            line2 = line.replace('Starting items: ', '').lstrip().replace(' ', '')
            splitted = line2.split(',')
            itemList = [int(item) for item in splitted]
        elif 'Operation' in line:
            line2 = line.replace('Operation: new =', '').lstrip()
            (lhs, symbol, rhs) = tuple(line2.split(' '))
            oper = buildFunc(lhs, symbol, rhs)
        elif 'Test' in line:
            divisNum = int(line.split(' ')[-1])
            supermodulo *= divisNum
        elif 'true' in line:
            truMky = int(line.split(' ')[-1])
        elif 'false' in line:
            falMky = int(line.split(' ')[-1])

    if not itemList is None:
        player = Monkey(itemList, oper, divisNum, truMky, falMky)
        bossMan.registerMonkey(player)
        #print(f'Monkey: {itemList}, {oper}, {divisNum}, {truMky}, {falMky})')

def readGameInput(filename):
    with open(filename) as file:
        for _ in range(10):
            readMonkey(file)
            



if __name__ == "__main__":
    readGameInput(filename)
    bossMan.playGame()
    print(f'level of monkey business after 20 rounds of stuff-slinging simian shenanigans: {bossMan.getMonkeyBusinessLevel()}')
