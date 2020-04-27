import Alignment
import Location

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

class NPC:
    def __init__(self, Name:str, Alignment:Alignment.Alignment, Location:Location.Location):
        self.__name = Name
        self.__alignment = Alignment
        self.__location = Location
        print(f"Input the notes you want to leave on {self.__name}. You may leave multiple lines of notes. Enter an empty line to enter")
        lines = []
        while line:=input():
            lines.append(line)
        self.__notes = lines
    
    def __repr__(self):
        notes = "\n".join(self.__notes)
        return f"""Name: {self.__name}
        Alignment: {self.__alignment}
        Location: {self.__location}
        Notes: {notes if self.__notes else None}"""