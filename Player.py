from enum import auto
import Alignment
import Race
import Class
import Armour
import Skill
import random

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

strength = Skill.strength
dexterity = Skill.dexterity
constitution = Skill.constitution
intelligence = Skill.intelligence
wisdom = Skill.wisdom
charisma = Skill.charisma

class Player:
    def __init__(self, PlayerName:str, CharacterName:str, Race:Race.Subrace, Class:Class.Class, Str:int, Dex:int, Con:int, Int:int, Wis:int, Cha:int, MaxHP:int, Alignment:Alignment.Alignment,Level:int=1):
        self.__stats = {strength:Str, dexterity:Dex, constitution:Con, intelligence:Int, wisdom:Wis, charisma:Cha}
        self.__playerName = PlayerName
        self.__characterName = CharacterName
        self.__race = Race
        self.__class = Class
        self.__level = Level
        self.__armour = None
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
        """Returns the modifier of a player's requested stat
        Arguments: The auto ID of the stat"""
        return (self.__stats[stat]-10)//2
    
    def modStr(self, stat:auto):
        """Returns a string representation of a stat modifier
        Arguments: The auto ID of the stat"""
        m = self.mod(stat)
        return f"+{m}" if m >= 0 else str(m)
    
    def longRest(self):
        """Regains HP and hit dice. Spells pending"""
        self.__hp = self.__maxHP
        hitDiceGain = 1 if self.__maxHitDice.number == 1 else self.__maxHitDice.number//2 
        if self.__maxHitDice.number - self.__hitDice.number <= hitDiceGain:
            self.__hitDice = self.__maxHitDice
        else:
            self.__hitDice += hitDiceGain

    def spendHitDice(self, heal:int=0)->int:
        """Spends a hit dice on a player and heals HP
        Input the number of HP to heal in \"heal\" argument to heal set number of HP or 0 for randint
        Returns the number of HP healed"""
        assert heal > 0
        if self.__hitDice.number > 0:
            if heal == 0:
                self.__hitDice -= 1
                heal = random.randint(1, self.__hitDice.sides)+self.mod(self.__stats[constitution])
            if self.__hp >= self.__maxHP - heal:
                self.__hp = self.__maxHP
            else:
                self.__hp += heal
        return heal


    @property
    def AC(self):
        if self.__armour == None:
            return 10 + self.mod(dexterity)
        return self.__armour.ac(self.mod(dexterity))
    
    @property
    def PP(self):
        return 10 + self.mod(wisdom) + self.profBonus * (Skill.perception in self.__skills)
    
    @property
    def profBonus(self):
        return 2 + (self.__level-1)//4