# """
# 1. Generate stacks from input
#     - read file line by line 
#     - for each line split into elements arr
#             (In manager class)
#     - first time generate (stack/queue) based on len
#     - otherwise insert item (proper stack) to container (if empty do nothing)
#     - if last line (elements would be numbers without brackets)
#         - map contianers: key is number value is stack/queue
#     - Lastly: if stack chosen "flip/reverse" if queue create stack with Front @ Top


# 2. Generate Move cmnd based on text
#     - read file (from prev point) line by line
#     - for each line:    
#         - parse text into (count, from, to) Cmnd Tuple
#         - send cmnd to "manager/game" class holding containers

# 3. Get Result
#     - function in manager class to 'pop' all internal containers
# """
SPACE_BETWEEN_VALS = '    '

class CrateManager:

    cratesMap = {} #Key: int, Val: List[str]

    def createEmptyCrates(self, amount: int):
        """
            will create [amount] empty crates
            each crate will get index from 1 -> amount
        """
        for i in range(1, amount + 1):
            self.cratesMap[i] = []

    def pushToBottom(self, crateIdx: int, crateVal: str):
        """
            Index starts at 1
        """
        if crateIdx in self.cratesMap:
            self.cratesMap[crateIdx].append(crateVal)

    def pushToTop(self, crateIdx: int, crateVal: str):
        """
            Index starts at 1
        """
        if crateIdx in self.cratesMap:
            self.cratesMap[crateIdx].insert(0, crateVal)

    def popFromTop(self, crateIdx):
        """
            removes the item from top of crate and returns it
        """
        if crateIdx in self.cratesMap:
            return self.cratesMap[crateIdx].pop(0)

    def moveCrates(self, fromIdx: int, toIdx: int, count: int):
        if count == 1:
            popped = self.popFromTop(fromIdx)
            self.pushToTop(toIdx, popped)
        else:
            # print(f"before: [{count}]")
            # print(f'F: {self.cratesMap[fromIdx]}')
            # print(f'T: { self.cratesMap[toIdx]}')
            #pop chunk from idx
            chunk = self.cratesMap[fromIdx][0:count]
            self.cratesMap[fromIdx] = self.cratesMap[fromIdx][count:]
            self.cratesMap[toIdx][0:0] = chunk
            # print("after: ")
            # print(f'F: {self.cratesMap[fromIdx]}')
            # print(f'T: { self.cratesMap[toIdx]}')

    
def parseInputLine(line: str, crate_manager):
    stacksValues = []

    splitted = line.split(SPACE_BETWEEN_VALS)
            
    better = [item.translate(str.maketrans('','', '[]')) for item in splitted]
  
    for combined in better:
        stacksValues += combined.split(' ')

    idx = 1
    for val in stacksValues:
        if val != '':
            crate_manager.pushToBottom(idx, val)
        idx += 1

def parseMoveCmnd(cmndStr: str):
    
    remWords = [value if value.isdigit() else '' for value in cmndStr.split(' ')]
    cmndVals = list(filter(lambda val: val != '', remWords))
    num = int(cmndVals[0])
    f = int(cmndVals[1])
    t = int(cmndVals[2])
    return (num, f, t)

def readInput(filename: str):
    """
        file in format from advent of code 2022 day 5
    """
    crate_manager = CrateManager()
    crate_manager.createEmptyCrates(9)

    with open(filename, 'r') as file:
        #section 1
        while(line := file.readline().rstrip()):
            if (line[1].isdigit()):
                continue
            parseInputLine(line, crate_manager)
        
        while(line := file.readline().rstrip()):
            (count, fromCrate, toCrate) = parseMoveCmnd(line)
            #print(f'Count: {count}, from: {fromCrate}, to: {toCrate}')
            crate_manager.moveCrates(fromCrate, toCrate, count)
        
    #print(crate_manager.cratesMap)
    for crate in crate_manager.cratesMap.values():
        print(crate)
      



if __name__ == "__main__":
    """
        AoC Day5: Supply Stacks
    """
    readInput('input.txt')