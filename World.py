from enum import Enum, auto

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

class Money:
    def __init__(self, exchange:dict):
        self.__exchange = exchange

    def __repr__(self):
        s = ""
        longestName = max([x for x in range(len(self.__exchange))])
        for coin, value in self.__exchange.items():
            l = f"{coin}:".ljust(longestName+3)+str(value)
            s += l+"\n"
        return s

    def __iter__(self):
        self.__n = 0
        return self
    
    def __next__(self):
        if self.__n > len(self.__exchange)-1:
            raise StopIteration
        o = self.order[self.__n]
        self.__n += 1
        return o, self.__exchange[o]

    @property
    def order(self)->list:
        """Returns a list of the coins in the world in declining order of value"""
        return list({k: v for k, v in sorted(self.__exchange.items(), key=lambda item: item[1])}) #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

    @property
    def exchange(self)->dict:
        return self.__exchange

class Account(Money):
    def __init__(self, initialMoney = {}):
        if not initialMoney:
            for coin in Money.exchange:
                initialMoney[coin] = 0
        self.__money = initialMoney

    def spendMoney(self, ammount:int, coin:str):
        if coin not in self.__money:
            raise ValueError(f"{coin} does not exist")
        if self.__money[coin] >= ammount:
            self.__money[coin] -= ammount
        elif self.value >= ammount*super.exchange[coin]:
            raise NotImplementedError("What to do when an account has sufficient money in the wrong coins")
        else:
            raise ValueError("You do not have enough money for that transaction")

    @property
    def value(self)->int:
        value = 0
        for coin, number in self.__money:
            value += number * super().exchange[coin]
        return value