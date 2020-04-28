from enum import auto, Enum
import Ui

if input("Do you want to use the GUI? y/n ").lower()[0] == "y":
    UI = Ui.GUI()
else:
    UI = Ui.Terminal()

class Dice:
    def __init__(self, number:int, sides:int):
        self.__number = number
        self.__sides = sides
    
    def __str__(self):
        return f"{self.__number}d{self.__sides}"
    
    @property
    def number(self):
        return self.__number
    
    @property
    def sides(self):
        return self.__sides
    
    @number.setter
    def number(self, val):
        self.__number = val

class Money(Enum):
    CP = auto()
    SP = auto()
    EP = auto()
    GP = auto()
    PP = auto()

    @classmethod
    def convert(self, Coins:dict)->dict:
        #Takes in a dictionary of coins with Money autos as keys and integers to represent the number of those keys
        rates = {Money.CP:1, Money.SP:10, Money.EP:50, Money.GP:100, Money.PP:1000}
        order = list({k: v for k, v in sorted(rates.items(), key=lambda item: item[1])}) #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        CP = sum([rates[x]*Coins[x] for x in order]) #Calculating the value of the coins in CP
        recieve = {Money.CP:0, Money.SP:0, Money.EP:0, Money.GP:0, Money.PP:0}
        for coin in order.remove(Money.CP):
            while CP>=rates[coin]:
                CP -= rates[coin]
                recieve[coin] += 1
        return recieve

class Party:
    def __init__(self):
        self.__players = []
        self.__money = {Money.CP:0, Money.SP:0, Money.EP:0, Money.GP:0, Money.PP:0}

    def addPlayer(self):
        self.__players.append(UI.createPlayer())

    def killPlayer(self, player):
        self.__players.remove(player)