from typing import List

supermodulo = 1

class Monkey:
    #items: List[int]

    #operation = None # function (item) -> item
    inspectedCount = 0

    def __init__(self, itemList, operation, testNum, trueIdx, falseIdx):
        global supermodulo
        self.items = itemList
        self.operation = operation
        self.trueMonkey = trueIdx
        self.falseMonkey = falseIdx
        self.testDivisible = testNum
        supermodulo *= testNum
    
    def addItem(self, item):
        self.items.append(item)
    
    def throwItems(self):
        toThrow = []
        for item in self.items:
            self.inspectedCount += 1
            #print(f'Monkey inspects an item with a worry level of {item}.')
            worrryLevel = int(self.operation(item))
            worrryLevel = worrryLevel % supermodulo 
            #print(f'Monkey plays with item: wry lvl now: {worrryLevel}.')
            if worrryLevel % self.testDivisible == 0:
                #print(f'Current worry level is divisible by {self.testDivisible}.')
                toMky = self.trueMonkey
            else:
                #print(f'Current worry level is not divisible by {self.testDivisible}.')
                toMky = self.falseMonkey

            #print(f'Item with worry level {worrryLevel} is thrown to monkey {toMky}.')

            toThrow.append((toMky, worrryLevel))
        self.items = []
        return toThrow
    