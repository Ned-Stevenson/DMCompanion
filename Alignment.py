from enum import auto

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

lawful = auto()
chaotic = auto()
neutral = auto()
good = auto()
evil = auto()

class Alignment:

    Names = {lawful: "Lawful", neutral: "Neutral", chaotic: "Chaotic", good: "Good", evil:"Evil"}

    def __init__(self, lawfulness, morals):
        self.__law = lawfulness
        self.__morals = morals
    
    def __repr__(self):
        if self.__law == neutral and self.__morals == neutral:
            return "True Neutral"
        return f"{Alignment.Names[self.__law]} {Alignment.Names[self.__morals]}"