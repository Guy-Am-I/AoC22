import itertools, ast
from enum import Enum
from functools import cmp_to_key
#parse input in pairs
filename = 'input.txt'

class CMD(Enum):
    WRONG_ORDER = -1
    RIGHT_ORDER = 1
    KEEP_CHECKING = 0

def compare_pairs(leftPair, rightPair):
    isLeftInteger = type(leftPair) is int
    isRightInteger = type(rightPair) is int
    #print(f'Compare {leftPair} vs {rightPair}')

    if isLeftInteger and isRightInteger:
        if leftPair == rightPair: return CMD.KEEP_CHECKING
        elif leftPair < rightPair: return CMD.RIGHT_ORDER
        else: return CMD.WRONG_ORDER
    elif isLeftInteger:
        asList = [leftPair]
        return compare_pairs(asList, rightPair)
    elif isRightInteger:
        asList = [rightPair]
        return compare_pairs(leftPair, asList)
    else:
        leftEmpty = len(leftPair) == 0
        rightEmpty = len(rightPair) == 0
        if leftEmpty and not rightEmpty: 
            return CMD.RIGHT_ORDER
        elif rightEmpty and not leftEmpty:
            return CMD.WRONG_ORDER
        elif leftEmpty and rightEmpty: #should reach here   
            return CMD.KEEP_CHECKING

        res = compare_pairs(leftPair[0], rightPair[0])
        if res == CMD.KEEP_CHECKING:
            return compare_pairs(leftPair[1:], rightPair[1:])
        else: return res

def compare(item1, item2):
    return compare_pairs(item1, item2).value

# with open(filename) as file:
#     pairIdx = 1
#     goodPairs = []
#     for line1, line2 in itertools.zip_longest(*([file]*2)):
#         pair1 = ast.literal_eval(line1)
#         pair2 = ast.literal_eval(line2)
#         #print(f'Pair-{pairIdx} -> {compare_pairs(pair1, pair2).value}')
#         if compare_pairs(pair1, pair2) == CMD.RIGHT_ORDER:
#             goodPairs.append(pairIdx)
#         file.readline()
#         pairIdx += 1

#     print(sum(goodPairs))
allPackets = []
with open(filename) as file:
    for line in file:
        line = line.rstrip()
        if line == '':
            continue
        allPackets.append(ast.literal_eval(line))

dividerPacket1 = [[2]]
dividerPacket2 = [[6]]
allPackets.append(dividerPacket1)
allPackets.append(dividerPacket2)

allPackets.sort(key=cmp_to_key(compare))
for idx, item in enumerate(reversed(allPackets)):
    if item == dividerPacket1:
        idx1 = idx
    if item == dividerPacket2:
        idx2 = idx

print(f'DECODER KEY: {(idx1+1) * (idx2+1)}')
# for item in reversed(allPackets):
#     print(item)
