from typing import List
from Monkeys import Monkey

class Manager:
    num_rounds = 10000
    players: List[Monkey] = []
    
    def registerMonkey(self, monk: Monkey):
        """ Play order is order monkeys are registered"""
        self.players.append(monk)

    def playGame(self):
        for roundNum in range(1, self.num_rounds+1):
            self.playRound()
            #self.printRoundStats(roundNum)
            print(f'Round #: {roundNum}')
        #self.printTotalInspected()  
    
    def playRound(self):
        for (idx, player) in enumerate(self.players):
            for (toMonkey, item) in player.throwItems():
                if item is None: #done throwing
                    break
                self.players[toMonkey].addItem(item)
    
    def printRoundStats(self, numRound):
        print(f'After round {numRound}, the monkeys are holding items with these worry levels:')
        for (idx, player) in enumerate(self.players):
            print(f'Monkey {idx}: {player.items}')
        print('')

    def printTotalInspected(self):
        for (idx, player) in enumerate(self.players):
            print(f'Monkey: {idx} inspected itmes {player.inspectedCount} times.')
    
    def getMonkeyBusinessLevel(self):
        inspectedArr = []
        for player in self.players:
            inspectedArr.append(player.inspectedCount)
        
        inspectedArr.sort()
        return inspectedArr[-2] * inspectedArr[-1]