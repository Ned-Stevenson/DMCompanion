import Player
import Race
import Class
import Armour
import NPC

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