from enum import auto
import Alignment
import Race
import Class
import Armour

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

strength = auto()
dexterity = auto()
constitution = auto()
wisdom = auto()
intelligence = auto()
charisma = auto()

class Skill:
    def __init__(self):
        raise NotImplementedError


class Player:
    def __init__(self, PlayerName:str, CharacterName:str, Race:Race.Subrace, Class:Class.Class, Str:int, Dex:int, Con:int, Int:int, Wis:int, Cha:int, Armour:Armour.Armour, MaxHP:int, Alignment:Alignment.Alignment,Level:int=1):
        self.__stats = {strength:Str, dexterity:Dex, constitution:Con, intelligence:Int, wisdom:Wis, charisma:Cha}
        self.__playerName = PlayerName
        self.__characterName = CharacterName
        self.__race = Race
        self.__class = Class
        self.__level = Level
        self.__armour = Armour
        self.__maxHP = MaxHP
        self.__hp = MaxHP
        self.__skills = []
        self.__maxHitDice = self.__class.hitDice(self.__level)
        self.__hitDice = self.__maxHitDice
        self.__alignment = Alignment
    
    def __repr__(self):
        return {"Player":self.__playerName, "Character":self.__characterName, "Class":self.__class.__repr__, "Level":self.__level, "Race":self.__race.__repr__, "Stats":self.__stats}

    def __str__(self):
        return f"""Player Name: {self.__playerName}
        Character Name: {self.__characterName}
        Character Class: Level {self.__level} {self.__race} {self.__class}
        Alignment: {self.__alignment}
        ---Stats---
        STR:{self.__stats[strength]}({self.modStr(strength)})
        DEX:{self.__stats[dexterity]}({self.modStr(dexterity)})
        CON:{self.__stats[constitution]}({self.modStr(constitution)})
        INT:{self.__stats[intelligence]}({self.modStr(intelligence)})
        WIS:{self.__stats[wisdom]}({self.modStr(wisdom)})
        CHA:{self.__stats[charisma]}({self.modStr(charisma)})
        ------
        AC:{self.AC}
        Passive Perception:{self.PP}
        HP:{self.__hp}/{self.__maxHP}"""
    
    def mod(self, stat:auto):
        return (self.__stats[stat]-10)//2
    
    def modStr(self, stat:auto):
        m = self.mod(stat)
        return f"+{m}" if m >= 0 else str(m)
    
    def longRest(self):
        self.__hp = self.__maxHP
        hitDiceGain = 1 if self.__maxHitDice.number == 1 else self.__maxHitDice.number//2 
        if self.__maxHitDice.number - self.__hitDice.number <= hitDiceGain:
            self.__hitDice.number = self.__maxHitDice.number
        else:
            self.__hitDice.number += hitDiceGain

    @property
    def AC(self):
        return self.__armour.ac(self.__stats[dexterity])
    
    @property
    def PP(self):
        return 10 + self.__stats[wisdom] + self.profBonus * (Skill.Perception in self.__skills)
    
    @property
    def profBonus(self):
        return 2 + (self.__level-1)//4