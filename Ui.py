from abc import ABC, abstractmethod
import Player
import Party
import World

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

class UI(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def menu(self):
        raise NotImplementedError

class Terminal(UI):
    def __init__(self):
        self.__options = {"Close Application":quit, "Create Player":self.createPlayer, "List Characters":self.listCharacters, "View Player":self.viewPlayer, "Configure Party Money":self.configurePartyMoney, "Configure World":self.configureWorld}

    def run(self):
        while True:
            self.menu()()
        
    def menu(self):
        """List the avaliable functions to run, taken from self.__options, and run the asociated function"""
        print("\n------------------------------------------\n")
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
                try:
                    stats.append(int(input(f"{s}: ")))
                except ValueError:
                    print("That is not a valid input")
                    continue
            return stats

        MaxHP = int(input("Input the HP of the character: "))
        
        Str, Dex, Con, Wis, Int, Cha = choseStats()

        Level = int(input("Input the level of the character: "))
        Party.party.addPlayer(Player.Player(PlayerName, CharacterName, Str, Dex, Con, Wis, Int, Cha, MaxHP, Level))

    def listCharacters(self):
        print(Party.party)
    
    def viewPlayer(self):
        if len(Party.party.players) == 0:
            print("There are no players in the party. Please create a player to use this feature")
            return
        for i, player in enumerate(Party.party.players):
            print(f"{i+1})\t{player.playerName}/{player.characterName}")
        p = int(input("Input the number of the player to view: "))
        print(Party.party.players[p-1])
    
    def configurePartyMoney(self):
        if not World.economy:
            print("First, configure the value and names of coins used")
            return
        print(World.economy)
        d = {}
        for coin, value in World.economy:
            d[coin] = int(input(f"Input the number of {coin} to give the party. They have value {value}: "))
        Party.party.configureMoney(World.Account(d))
    
    def configureWorld(self):
        settings = Settings()
        settings.menu()

class GUI(UI):
    def __init__(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def menu(self):
        raise NotImplementedError

    def createPlayer(self):
        raise NotImplementedError

class Settings:
    def __init__(self):
        self.__options = {"Configure Money":self.configureMoney, "Create Location":self.createLocation, "View Location":self.printLocation}
    
    def menu(self):
        while True:
            print("\n------------------------------------------\n")
            print("0)\tReturn to top menu")
            for i, option in enumerate(self.__options):
                print(f"{i+1})\t{option}")
            num = int(input("Input the number of the action to do: "))
            if num == 0:
                break
            action = list(self.__options)[num-1]
            self.__options[action]()

    def configureMoney(self):
        coins = {}
        print("""Input the different coins used along with their values in the form Name:Value eg. Gold Pieces:100
Enter an empty line to finish""")
        while line:=input():
            try:
                name, value = line.split(":")
                if name in coins:
                    if input(f"Are you sure you want to overwrite the value of {name} from {coins[name]} to {value}? y/n ").lower()[0] != "y":
                        print("Overwrite aborted")
                        continue
                value = int(value)
            except ValueError:
                print("Invalid input. Ensure that it follows Name:Value format eg. Gold Pieces:100")
            else:
                coins[name] = value
        World.economy = World.Money(coins)
        print(World.economy)
    
    def createLocation(self):
        """Creates a location in the World.locations list"""
        name = input("Input the name of the location: ")
        Type = input("Input the type of location it is eg. city, farmhouse, cave: ")
        notes = ""
        print(f"Input notes about {name}. Enter an empty line to enter")
        while line:=input():
            notes += line+"\n"
        World.locations.append(World.Location(name, Type, notes))
    
    def printLocation(self):
        """Lists out the locations in the World.locations list
        Let's the user view one of the locations"""
        if not World.locations:
            print("There are no locations. Please Create one before viewing locations")
            return
        for i, location in enumerate(World.locations):
            print(f"{i+1})\t{location.name}")
        x=int(input("Input a number to view a location: "))-1
        print(World.locations[x])