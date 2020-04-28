from abc import ABC, abstractmethod
import Player
import Party

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

class UI(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def createPlayer(self):
        raise NotImplementedError

class Terminal(UI):
    def __init__(self):
        self.__options = {"Close Application":quit, "Create Player":self.createPlayer, "List Characters":self.listCharacters}

    def run(self):
        while True:
            self.menu()()
        
    def menu(self):
        for i, option in enumerate(self.__options):
            print(f"{i})\t{option}")
        action = list(self.__options)[int(input("Input the number of the action to do: "))]
        return self.__options[action]

    def createPlayer(self):
        PlayerName = input("Input the player's name: ")
        CharacterName = input("Input the character's name: ")

        def choseStats()->list:
            print("Please input stats:")
            stats = []
            for s in ("STR", "DEX", "CON", "INT", "WIS", "CHA"):
                stats.append(int(input(f"{s}: ")))
            return stats
        

        MaxHP = int(input("Input the HP of the character: "))
        
        Str, Dex, Con, Wis, Int, Cha = choseStats()

        Level = int(input("Input the level of the character: "))
        Party.party.addPlayer(Player.Player(PlayerName, CharacterName, Str, Dex, Con, Wis, Int, Cha, MaxHP, Level))

    def listCharacters(self):
        print(Party.party)

class GUI(UI):
    def __init__(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def createPlayer(self):
        raise NotImplementedError