import Player
import NPC
from enum import auto, Enum

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
    GP = auto()
    PP = auto()

    def convert(self, From, To, Ammount):
        raise NotImplementedError

class Party:
    def __init__(self):
        self.__players = []
        self.__money = {Money.CP:0, Money.SP:0, Money.GP:0, Money.PP:0}

    def addPlayer(self):
        self.__players.append(Player.createPlayer())

    def killPlayer(self, player:Player.Player):
        self.__players.remove(player)