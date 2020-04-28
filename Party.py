from enum import Enum, auto
import World

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

class Party:
    def __init__(self):
        self.__players = []
    
    def __repr__(self):
        return self.__players
    
    def __str__(self):
        if len(self.__players) == 0:
            return "The party is empty"
        s=""
        for player in self.__players:
            s += player.__str__()+"\n\n\n"
        return s

    def addPlayer(self, player):
        self.__players.append(player)

    def killPlayer(self, player):
        self.__players.remove(player)

    def configureMoney(self, money:World.Account):
        self.__money = money

    @property
    def players(self):
        return self.__players

party = Party()