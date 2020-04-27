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
    def __init__(self, lawfulness, morals):
        self.__law = lawfulness
        self.__morals = morals
    
    def __repr__(self):
        d = {lawful: "Lawful", neutral: "Neutral", chaotic: "Chaotic", good: "Good", evil:"Evil"}
        return f"{d[self.__law]} {d[self.__morals]}"