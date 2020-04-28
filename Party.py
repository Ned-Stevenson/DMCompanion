from enum import Enum, auto

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

class Dice:
    def __init__(self, number:int, sides:int):
        self.__number = number
        self.__sides = sides
    
    def __str__(self):
        return f"{self.__number}d{self.__sides}"
    
    def __add__(self, other):
        if type(other) == Dice:
            if other.__sides == self.__sides:
                number = other.sides
            else:
                raise TypeError("Dice must have the same number of sides to add")
        elif type(other) == int:
            number = other
        else:
            raise TypeError(f"Unsupported type {type(other)} for addition with type Dice")
        return Dice(self.__number + number, self.__sides)
    
    def __sub__(self, other):
        try:
            if type(other) == Dice:
                assert self.__number >= other.number
                if other.__sides == self.__sides:
                    number = other.number
                else:
                    raise TypeError("Dice must have the same number of sides to subtract")
            elif type(other) == int:
                assert self.__number >= other
                number = other
            else:
                raise TypeError(f"Unsupported type {type(other)} for subtraction with type Dice")
        except AssertionError:
            raise ArithmeticError(f"Cannot subtract {number} from {self}. Cannot have negative dice")
        else:
            return Dice(self.__number - number, self.__sides)
    
    def __iadd__(self, other):
        if type(other) == Dice:
            if other.__sides == self.__sides:
                number = other.sides
            else:
                raise TypeError("Dice must have the same number of sides to add")
        elif type(other) == int:
            number = other
        else:
            raise TypeError(f"Unsupported type {type(other)} for addition with type Dice")
        self.__number += number
        return self

    def __isub__(self, other):
        try:
            if type(other) == Dice:
                assert self.__number >= other.number
                if other.__sides == self.__sides:
                    number = other.number
                else:
                    raise TypeError("Dice must have the same number of sides to subtract")
            elif type(other) == int:
                assert self.__number >= other
                number = other
            else:
                raise TypeError(f"Unsupported type {type(other)} for subtraction with type Dice")
        except AssertionError:
            raise ArithmeticError(f"Cannot subtract {number} from {self}. Cannot have negative dice")
        else:
            self.__number -= number
            return self

    @property
    def number(self):
        return self.__number
    
    @property
    def sides(self):
        return self.__sides
    
    @number.setter
    def number(self, val):
        self.__number = val

class Money:
    CP = auto()
    SP = auto()
    EP = auto()
    GP = auto()
    PP = auto()

    def __init__(self):
        self.__money = {Money.CP:0, Money.SP:0, Money.EP:0, Money.GP:0, Money.PP:0}
        self.__exchange = {Money.CP:1, Money.SP:10, Money.EP:50, Money.GP:100, Money.PP:1000}
    
    def convert(self, Coins:dict)->dict:
        #Takes in a dictionary of coins with Money autos as keys and integers to represent the number of those keys
        CP = self.value
        recieve = {Money.CP:0, Money.SP:0, Money.EP:0, Money.GP:0, Money.PP:0}
        for coin in self.order.remove(Money.CP):
            while CP>= self.__exchange[coin]:
                CP -= self.__exchange[coin]
                recieve[coin] += 1
        return recieve

    @property
    def order(self):
        return list({k: v for k, v in sorted(self.__exchange.items(), key=lambda item: item[1])}) #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

    @property
    def value(self):
        return sum([self.__exchange[x]*self.__money[x] for x in self.order]) #Calculating the value of the coins in CP


class Party:
    def __init__(self):
        self.__players = []
        self.__money = {Money.CP:0, Money.SP:0, Money.EP:0, Money.GP:0, Money.PP:0}
    
    def __repr__(self):
        return self.__players
    
    def __str__(self):
        s=""
        for player in self.__players:
            s += player.__str__()+"\n\n\n"
        return s

    def addPlayer(self, player):
        self.__players.append(player)

    def killPlayer(self, player):
        self.__players.remove(player)

    @property
    def players(self):
        return self.__players

party = Party()