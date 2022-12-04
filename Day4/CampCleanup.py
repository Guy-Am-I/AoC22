def getAssignmentSets(inputLine: str):
    """
        get assignments as input file in instructions
            ex: 68-70,69-86
        return tuple of sets -
            (Set(68,69,70), Set(69,70,71,...,86))
    """
    rangeStrs = [dashedStr.split('-') for dashedStr in inputLine.split(',')]

    leftAssignment = range(int(rangeStrs[0][0]), int(rangeStrs[0][-1]) + 1)
    rightAssignment = range(int(rangeStrs[-1][0]), int(rangeStrs[-1][-1]) + 1)

    return (set(leftAssignment), set(rightAssignment))


def getCountOverlap(filename: str):
    totalSubsets = 0
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            (elf1, elf2) = getAssignmentSets(line)
            #part 1: subset, i.e. entire assignment in another
            #part 2: intersection, i.e assignments have at least 1 item/number in common
            #if elf1.issubset(elf2) or elf2.issubset(elf1):
            if len(elf1.intersection(elf2)) > 0:
                totalSubsets += 1
            
    return totalSubsets


if __name__ == "__main__":
    print(f'# Overlapping Assignments: {getCountOverlap("./input.txt")}')
