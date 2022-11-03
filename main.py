from random import choice, randint

#whatshappening

class Player:
    Points = 19
    Strength = 1
    Dexterity = 1
    Speed = 1
    Speech = 1
    Luck = 1
    
    RWeapon = None
    LWeapon = None

    def genAttributes():
        while Player.points > 0:
            attribute = randint(1, 5)
            if attribute == 1:
                Player.Strength += 1
            elif attribute == 2:
                Player.Dexterity += 1
            elif attribute == 3:
                Player.Speed += 1
            elif attribute == 4:
                Player.Speech += 1
            elif attribute == 5:
                Player.Luck += 1
            Player.Points -= 1

        Player.printAttributes()
    
    def printAttributes():
        print("Strength:",Player.Strength)
        print("Dexterity:",Player.Dexterity)
        print("Speed:",Player.Speed)
        print("Speech:",Player.Speech)
        print("Luck:",Player.Luck)
    
    def assignWeapon(weapon, slot):
        pass
    
class Weapon:
    scaleDict = {
        "S" : 1.8,
        "A" : 1.6,
        "B" : 1.4,
        "C" : 1.2,
        "D" : 1
    }

class KitchenKnife(Weapon):
    name = "Kitchen Knife"

    def __init__(self):
        self.StrScale = "C"
        self.DexScale = "D"
        self.Durability = randint(1, 100)
    

Player.genAttributes()

    



