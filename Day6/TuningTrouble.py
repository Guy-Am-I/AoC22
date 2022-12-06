"""
    Tuning Trouble Day 6

- input is a long buffer stream
- challange 1 - get number of charactrs until end of first start-of-packet marker
    a start-of-packet market is 4 unqiue characters in a row
    meaning find the `index` of said quadruplet

"""
SIZE_OF_PACKET_MARKER = 14

def numCharsUntilStartOfPacket(datastream: str):
    # iterate over datastream by chunks of sizeof(packet) [4]
    listWithoutLast4 = datastream[:len(datastream) - SIZE_OF_PACKET_MARKER]

    for index in range(0, len(listWithoutLast4)):
        potentialMarker = datastream[index:index + SIZE_OF_PACKET_MARKER]

        if len(potentialMarker) == len(set(potentialMarker)):
            #set has only unique elements so this way we can check if all 4 elems are unique
            return index + SIZE_OF_PACKET_MARKER
    
    return -1


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as file:
        countChars =  numCharsUntilStartOfPacket(file.read().rstrip())
        print(f"countChars: {countChars}")
    

