from enum import auto

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

class Armour:

    light = auto()
    medium = auto()
    heavy = auto()

    def __init__(self, AC:int, Name:str, StealthDis:bool, Weight:auto):
        self.__ac = AC
        self.__name = Name
        self.__stealthDis = StealthDis
        self.__weight = Weight

    def ac(self, dex):
        if self.__weight == Armour.light:
            return self.__ac+dex
        elif self.__weight == Armour.medium:
            return self.__ac+(2 if dex >= 2 else dex)
        elif self.__weight == Armour.heavy:
            return self.__ac
        else:
            raise ValueError(f"Armour weight was not a valid weight ID for instance of {self.__name}")
    
    @property
    def stealthDis(self):
        return self.__stealthDis