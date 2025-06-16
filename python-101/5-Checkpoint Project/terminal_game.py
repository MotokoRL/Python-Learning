import random
charactor = input("you are a: \n1. warrior\n2. mage\n")
HealthPoints = 100
if charactor == "1":
    weapon = input("choose your weapon: \n1. sword\n2. axe\n")
    if weapon == "1":
        print("you are a warrior")
        print("you chose a sword")
        print("you have", HealthPoints, "health points")
    elif weapon == "2":
        print("you are a warrior")
        print("you chose an axe")
        print("you have", HealthPoints, "health points")
    else:
        print("invalid choice")
elif charactor == "2":
    spell = input("choose your spell: \n1. fireball\n2. ice shard\n")
    if spell == "1":
        print("you are a mage")
        print("you chose fireball")
        print("you have", HealthPoints, "health points")
    elif spell == "2":
        print("you are a mage")
        print("you chose ice shard")
        print("you have", HealthPoints, "health points")
    else:
        print("invalid choice")
else:
    print("invalid character choice")

print("You now walking into a dark forest, suddenly a monster appears!")
action = input("What do you want to do? \n1. fight\n2. run\n")
HealthPoints_monster = 20
AttackPoints_player = random.randint(5, 30)
AttackPoints_monster = random.randint(5, 20)
if action == "1":
    print("You chose to fight the monster!")
    print("You attack the monster with", AttackPoints_player, "attack points!")
    HealthPoints_monster -= AttackPoints_player
    print("The monster has", HealthPoints_monster, "health points left.")
    if HealthPoints_monster >= 0:
        print("The monster attacks you with", AttackPoints_monster, "attack points!")
        HealthPoints -= AttackPoints_monster
        print("You have", HealthPoints, "health points left.")
        if HealthPoints <= 0:
            print("You have been defeated by the monster!")
        else:
            print("You defeated the monster!")
    else:
        print("You defeated the monster!")
else:
    print("You chose to run away from the monster!")
    if random.choice([True, False]):
        print("You successfully escaped!")
    else:
        print("You failed to escape and the monster attacks you!")
        HealthPoints -= AttackPoints_monster
        print("You have", HealthPoints, "health points left.")
        if HealthPoints <= 0:
            print("You have been defeated by the monster!")
        else:
            print("You managed to escape with", HealthPoints, "health points left.")
