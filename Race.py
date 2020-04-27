if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

class Race:
    def __init__(self, Name:str):
        self.__name = Name

    def __repr__(self):
        return self.__name


class Subrace(Race):
    def __init__(self, Name:str):
        self.__name = Name
    
    def __repr__(self):
        return f"{self.__name} {super()}"