from abc import ABC, abstractmethod
import Player
import Race
import Class
import Alignment

class UI(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def createPlayer(self):
        raise NotImplementedError

class Terminal(UI):
    def __init__(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def createPlayer(self):
        PlayerName = input("Input the player's name: ")
        CharacterName = input("Input the character's name: ")

        def choseRace()->Race.Subrace:
            print("Races:")
            r = "\n".join([x+1+")\t"+Race for x, Race in enumerate(Race.Races)]) #A numbered list of races available
            print(r)
            while True:
                try:
                    superRace = Race.Races[int(input("Input the number of the race to use: "))-1]
                    count = 1
                    subRaces = []
                    for subRace in Race.subRaces:
                        if subRace.superRace == superRace:
                            subRaces.append(subRace)
                            print(f"{count})\t{subRace}")
                            count += 1
                    return subRaces[int(input("Input the number of the sub-race to use: "))-1]
                except (ValueError, IndexError) as e:
                    if e==ValueError:
                        print("Please input a valid number!")
                    else:
                        print("Please input a number in the range!")
                else:
                    break
        
        def choseClass()->Class.Class:
            c = "\n".join([x+1+")\t"+Class for x, Class in enumerate(Class.Clases)]) #A numbered list of classes available
            print(c)
            while True:
                try:
                    return Class.Classes[int(input("Input the number of the class to use: "))-1]
                except (ValueError, IndexError) as e:
                    if e==ValueError:
                        print("Please input a valid number!")
                    else:
                        print("Please input a number in the range!")
                else:
                    break
        
        def choseStats()->list:
            print("Please input stats:")
            stats = []
            for s in ("STR", "DEX", "CON", "INT", "WIS", "CHA"):
                stats.append(int(input(f"{s}: ")))
            return stats
        
        c = choseClass()
        stats = choseStats()
        MaxHP = c.HP(stats[2])#Stats[2] is the constitution score of the character

        def choseAlignment()->Alignment.Alignment:
            while True:
                try:
                    l = input("Lawful/Neutral/Chaotic: ").lower()[0]
                    m = input("Good/Neutral/Evil: ").lower()[0]
                    lDict = {"l":Alignment.lawful, "n":Alignment.neutral, "c":Alignment.chaotic}
                    mDict = {"g":Alignment.good, "n":Alignment.neutral, "e":Alignment.evil}
                    return Alignment.Alignment(lDict[l], mDict[m])
                except KeyError:
                    print("Please input a valid alignment!")
                else:
                    break
        
        Str, Dex, Con, Wis, Int, Cha = stats
        Level = int(input("Input the level of the character: "))
        Player.Player(PlayerName, CharacterName, choseRace(), c, Str, Dex, Con, Wis, Int, Cha, MaxHP, choseAlignment(), Level)

class GUI(UI):
    def __init__(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def createPlayer(self):
        raise NotImplementedError