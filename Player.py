from enum import auto
import Skill

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
    def __init__(self, PlayerName:str, CharacterName:str,Str:int, Dex:int, Con:int, Int:int, Wis:int, Cha:int, MaxHP:int, Level:int=1):
        self.__stats = {strength:Str, dexterity:Dex, constitution:Con, intelligence:Int, wisdom:Wis, charisma:Cha}
        self.__playerName = PlayerName
        self.__characterName = CharacterName
        self.__level = Level
        self.__maxHP = MaxHP
        self.__hp = MaxHP
        self.__skills = []
    
    def __repr__(self):
        return {"Player":self.__playerName, "Character":self.__characterName, "Level":self.__level, "Stats":self.__stats}

    def __str__(self):
        return f"""Player Name: {self.__playerName}
        Character Name: {self.__characterName}
        Character Class: Level {self.__level}
        ---Stats---
        STR:{self.__stats[strength]}({self.modStr(strength)})
        DEX:{self.__stats[dexterity]}({self.modStr(dexterity)})
        CON:{self.__stats[constitution]}({self.modStr(constitution)})
        INT:{self.__stats[intelligence]}({self.modStr(intelligence)})
        WIS:{self.__stats[wisdom]}({self.modStr(wisdom)})
        CHA:{self.__stats[charisma]}({self.modStr(charisma)})
        ------
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
        """Regains all HP"""
        self.__hp = self.__maxHP
    
    @property
    def PP(self):
        return 10 + self.mod(wisdom) + self.profBonus * (Skill.perception in self.__skills)
    
    @property
    def profBonus(self):
        return 2 + (self.__level-1)//4