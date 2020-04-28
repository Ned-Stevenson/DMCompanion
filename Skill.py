from enum import auto

if __name__ == "__main__":
    print("Please run DMCompanion instead")
    quit()

strength = auto()
dexterity = auto()
constitution = auto()
wisdom = auto()
intelligence = auto()
charisma = auto()

athletics = auto()
acrobatics = auto()
sleightOfHand = auto()
stealth = auto()
arcana = auto()
history = auto()
investigation = auto()
nature = auto()
religion = auto()
animalHandling = auto()
insight = auto()
medicine = auto()
perception = auto()
survival = auto()
deception = auto()
intimidation = auto()
performance = auto()
persuasion = auto()

Checks = {athletics:strength,
acrobatics:dexterity,
sleightOfHand:dexterity,
stealth:dexterity,
arcana:intelligence,
history:intelligence,
investigation:intelligence,
nature:intelligence,
religion:intelligence,
animalHandling:wisdom,
insight:wisdom,
medicine:wisdom,
perception:wisdom,
survival:wisdom,
deception:charisma,
intimidation:charisma,
performance:charisma,
persuasion:charisma}

class Skill():
    def __init__(self):
        raise NotImplementedError