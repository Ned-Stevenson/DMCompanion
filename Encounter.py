import Player

class Grid:
    def __init__(self, width:int, height:int):
        self.__grid = [[None for _ in range(height)] for _ in range(width)]
    
    def __repr__(self):
        h = "-"*(2*self.width+1)
        s = ""
        for row in range(self.height):
            s += h+"\n"
            s += "|"+"|".join([self.__grid[row][col] for col in range(self.width)])+"|\n"
        s += h
        return s

    def __len__(self):
        return self.height*self.width

    def __getitem__(self, row):
        return self.__grid[row]

    def expand(self, extraColumns:int=1):
        for _ in range(extraColumns):
            self.__grid.append([None for _ in range(self.height)])
    
    def extend(self, extraRows:int=1):
        for _ in range(extraRows):
            for column in self.__grid:
                column.append(None)

    @property
    def height(self):
        return len(self.__grid[0])
    
    @property
    def width(self):
        return len(self.__grid)

class Encounter:
    def __init__(self, width:int=20, height:int=20, *characters):
        self.__board = Grid(width, height)
        self.__players = self.__monsters = []
        for c in characters:
            if type(c) == Player.Player:
                self.__players.append(c)
            else:
                self.__monsters.append(c)
    
    def __repr__(self):
        return self.__board
    
    def run(self, **initiative):
        for char, init in initiative.items():
            if char not in self.__players + self.__monsters:
                del initiative[char]