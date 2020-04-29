# Player Character Sheets
-	Inventory
-	Stats
-	AC/HP/PP
    -	HP max and current
-	Hit dice
-	Attack rolls
-	Damage Rolls
-	Saves
-	Move speed
-	Languages
-	Proficiencies
    -	Tool and skill
-	Character Name
-	Player name
-	Class
-	Race
-	Level
-	XP
# Party Tracking
-	Party Gold
-	Location
-	Players
# NPCs
-	Name
-	Alignment
-	Notes
-	Location
# World
-	Locations


# Menus
1.	Exit
2.  Party Settings
    1.	Create Player
    2.	List Players
    3.	Look up player
    4.  Manage Player
        1.  Manage inventory
        2.  Assign XP
    5.  Party Inventory
    6.  Party Actions
        1.  Long Rest
        2.  Short Rest
        3.  Assign XP
        4.  Level Up (Milestone)
3.  World Settings
    1.  Configure Money
    2.  Create Location
    3.  View Location
        1.  Add note
4.  NPC tracking
    1.  Create NPC
    2.  Look up NPC
    3.  Add Notes
5.  Track Encounter
    1.  Input initiative
        -   Step through encounter displaying current turn and character details
    2.  NPC and PC hp tracking
    3.  NPC attacks on player AC
    4.  Encounter Map?
        1.  Create new
        2.  Load from template
        3.  Move Character
            -   Standard move
            -   Jump
        4.  Move NPC
    5.  Ammo Tracking

# Stages and Roadmap
### MVP:
-	Terminal interface with storage of basic character sheets
    -	Sheets do not persist after program is ended
-	Values such as AC and PP are calculated automatically
-   Basic settings of the world eg. locations, currency etc

### Stage 2
-   Storage of character sheets in `.csv` files
-   Character Sheets able to have armour, class, race, subrace, proficiencies & alignment
-   Different armour, classes etc. stored in `.csv` files and objects built from them
