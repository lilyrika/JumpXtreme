from random import choice, randint
from math import ceil

#whatshappening

class Player:
    Level = 1
    Quid = 0

    Strength = 1
    Dexterity = 1
    Endurance = 1
    Agility = 1
    Charisma = 1
    Luck = 1
    
    RWeapon = None
    LWeapon = None

    Stamina = 92

    def genAttributes():
        AllocatedPoints = 24
        while AllocatedPoints > 0:
            attribute = randint(1, 6)
            if attribute == 1:
                Player.Strength += 1
            elif attribute == 2:
                Player.Dexterity += 1
            elif attribute == 3:
                Player.Endurance += 1
            elif attribute == 4:
                Player.Agility += 1
            elif attribute == 5:
                Player.Charisma += 1
            elif attribute == 6:
                Player.Luck += 1
            AllocatedPoints -= 1

        Player.printAttributes()
    
    def printAttributes():
        print("Strength:",Player.Strength)
        print("Dexterity:",Player.Dexterity)
        print("Endurance:",Player.Endurance)
        print("Agility:",Player.Agility)
        print("Charisma:",Player.Charisma)
        print("Luck:",Player.Luck)

    def LevelUp():
        attribute = str(input("Which attribute would you like to level?\n1. Strength\n2. Dexterity"))
        if attribute == "Strength":
            Player.Strength += 1
        elif attribute == "Dexterity":
            Player.Dexterity += 1
        elif attribute == "Endurance":
            Player.Endurance += 1
        elif attribute == "Agility":
            Player.Agility += 1
        elif attribute == "Charisma":
            Player.Charisma += 1
        elif attribute == "Luck":
            Player.Luck += 1
    
class Weapon:
    scaleDict = {
        "S" : 2,
        "A" : 1.8,
        "B" : 1.6,
        "C" : 1.4,
        "D" : 1.2,
        "E" : 1
    }

    def scaleDamage(self, Attribute):
        if Attribute != "-":
            bonusDamage = ceil(self.Damage / 59.4 * 0.146 * Attribute ** 2 * Weapon.scaleDict.get(Attribute) ** 2)
        else:
            bonusDamage = 0
        print(bonusDamage)
        return bonusDamage
    def scaleDex():
        Player.RWeapon.scaleDamage(Player.Dexterity)
    def scaleStr():
        Player.RWeapon.scaleDamage(Player.Strength)
    def calcDamage(Weapon):
        damage = 0
        bonusDamage = Weapon.scaleDex()
        damage += bonusDamage
        bonusDamage = Weapon.scaleStr()
        damage += bonusDamage
        
        damage = damage * (1 - Enemy.Defence/100)
        return damage

    def RAttack():
        damage = Player.calcDamage(Player.RWeapon)
        Enemy.HP -= damage
        print("You dealt",damage,"damage with your",Player.RWeapon.name)
    def LAttack():
        damage = Player.calcDamage(Player.LWeapon)
        Enemy.HP -= damage
        print("You dealt",damage,"damage with your",Player.LWeapon.name)


#region Weapons

class KitchenKnife(Weapon):
    Name = "Kitchen Knife"
    StrScale = "E"
    DexScale = "C"

    def __init__(self):
        self.Level = 1
        self.Damage = 65

class MetalBar(Weapon):
    Name = "Metal Bar"
    StrScale = "D"
    DexScale = "D"

    def __init__(self):
        self.Level = 1
        self.Damage = 140

class Person:
    names = [
        "James",
        "Jimmy"
        "Robert",
        "Rob",
        "Bob"
        "John",
        "Michael",
        "Mike",
        "David",
        "Dave",
        "William",
        "Liam",
        "Richard",
        "Joseph",
        "Joe",

        "Olivia",
        "Emma",
        "Charlotte",
        "Amelia",
        "Emily",
        "Sophia",
        "Isabella",
        "Mia",
        "Ella",
        "Abigail",
        "Sofia",
        "Scarlett",
        "Lily",
        "Grace",
        "Violet",
    ]
    weapons = [
        KitchenKnife(),
        MetalBar(),
    ]

    def __init__(self):
        self.Name = choice(Person.names)
        self.HP = randint()
        self.Weapon = choice(Person.weapons)
        self.Defence = randint(100, 250) / 10
    
    def printInfo(self):
        print()
        print("Name:",self.Name)
        print("Weapon:",self.Weapon.Name)
        print("Defence:",str(self.Defence)+"%")

class Enemy:
    pass

#endregion

def Start():
    Player.genAttributes()
    Player.RWeapon = KitchenKnife()
    SillyGuy = Person() 
    SillyGuy.printInfo()

Start()


