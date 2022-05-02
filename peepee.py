choice = 0
fightE1 = 1
fightE2 = 2
fightE3 = 3
drinkPot = 4
save = 5
saveQuit = 6
error = 7


def main():

    
    class Character:
        def __init__(self, php, patk):
            self.name = input("What is your character's name? ")
            self.role = input("What is " + self.name + "'s class? ")
            self.age = input("What is " + self.name + "'s age? ")
            self.php = php
            self.patk = patk

        def characterDisplay(self):
            print(self.name, self.role, self.age)

    class Enemy:
        def __init__(self, enemy_type, ehp, eatk):
            self.enemy_type = enemy_type          
            self.ehp = ehp
            self.eatk = eatk

    pc = Character(10, 2)
    enemy1 = Enemy("Chicken", 2, 1)
    enemy2 = Enemy("Goblin", 4, 2)
    enemy3 = Enemy("Troll", 6, 3)


    def mainMenu():
        print()
        print()
        print("Welcome to Peatopia " + pc.name + " the " + pc.role + "! What would you like to do?")
        print("-----------------------------------------------")
        print("1. Fight weak enemy!")
        print("2. Fight tougher enemy!")
        print("3. Fight toughest enemy!")
        print("4. Drink a potion!")
        print("5. Save your adventure!")
        print("6. Save and quit")
        print()
        #Input for menu
        choice = int(input('Enter your choice: '))
        while choice < fightE1 or choice >= error:
            choice = int(input('Enter a valid action: '))
        return choice

    def fightChick():
        encounter = 0
        attack = 1
        run = 2
        nah = 3
        timesRan = 0
        first = 1
        second = 2
        if timesRan == first:
            print("A menacing " + enemy1.enemy_type + "has challenged you!")
        elif timesRan == second:
            print("The " + enemy1.enemy_type + "has been injured!")
            print()
        print()
        print("1. Attack the " + enemy1.enemy_type)
        print("2. Run away from the " + enemy1.enemy_type)
        print()
        encounter = int(input("What would you like to do? "))
        while encounter < attack or encounter >= nah:
                choice = int(input('Enter a valid action: '))
        print()
        print("-------------------------------------------------")

        if encounter == 1:
            enemy1.ehp = enemy1.ehp - pc.patk
            pc.php = pc.php - enemy1.eatk 
            print()
            if enemy1.ehp > 0:
                print("Enemy " + enemy1.enemy_type + "'s HP has fallen to " + str(enemy1.ehp))
                print("Your HP is " + str(pc.php))
                print()
                if enemy1.ehp > 0:
                    fightChick()
                elif enem1.ehp <= 0:
                    mainMenu()
            elif enemy1.ehp <= 0:
                print("Enemy " + enemy1.enemy_type + "'s HP has fallen to " + str(enemy1.ehp))
                print(enemy1.enemy_type + " has died!")
                print("Your HP is " + str(pc.php))
                print()
                enemy1.ehp = 2
            if pc.php <= 0:
                print("YOU DIED")
                print()
                main()
            return pc.php
        elif encounter == 2:
            print("You ran away!")
            print()


    def fightGob():
        encounter = 0
        attack = 1
        run = 2
        nah = 3
        timesRan = 0
        first = 1
        second = 2
        if timesRan == first:
            print("A menacing " + enemy2.enemy_type + "has challenged you!")
        elif timesRan == second:
            print("The " + enemy2.enemy_type + "has been injured!")
            print()
        print()
        print("1. Attack the " + enemy2.enemy_type)
        print("2. Run away from the " + enemy2.enemy_type)
        print()
        encounter = int(input("What would you like to do? "))
        while encounter < attack or encounter >= nah:
                choice = int(input('Enter a valid action: '))
        print()
        print("-------------------------------------------------")

        if encounter == 1:
            enemy2.ehp = enemy2.ehp - pc.patk
            pc.php = pc.php - enemy2.eatk 
            print()
            if enemy2.ehp > 0:
                print("Enemy " + enemy2.enemy_type + "'s HP has fallen to " + str(enemy2.ehp))
                print("Your HP is " + str(pc.php))
                print()
                fightGob()
            elif enemy2.ehp <= 0:
                print("Enemy " + enemy2.enemy_type + "'s HP has fallen to " + str(enemy2.ehp))
                print(enemy2.enemy_type + " has died!")
                print("Your HP is " + str(pc.php))
                print()
                enemy2.ehp = 4
            if pc.php <= 0:
                print("YOU DIED")
                print()
                main()
            return pc.php
        elif encounter == 2:
            print("You ran away!")
            print()

    def fightTroll():
        encounter = 0
        attack = 1
        run = 2
        nah = 3
        timesRan = 0
        first = 1
        second = 2
        if timesRan == first:
            print("A menacing " + enemy3.enemy_type + "has challenged you!")
        elif timesRan == second:
            print("The " + enemy3.enemy_type + "has been injured!")
            print()
        print()
        print("1. Attack the " + enemy3.enemy_type)
        print("2. Run away from the " + enemy3.enemy_type)
        print()
        encounter = int(input("What would you like to do? "))
        while encounter < attack or encounter >= nah:
                choice = int(input('Enter a valid action: '))
        print()
        print("-------------------------------------------------")

        if encounter == 1:
            enemy3.ehp = enemy3.ehp - pc.patk
            pc.php = pc.php - enemy3.eatk 
            print()
            if enemy3.ehp > 0:
                print("Enemy " + enemy3.enemy_type + "'s HP has fallen to " + str(enemy3.ehp))
                print("Your HP is " + str(pc.php))
                print()
                fightTroll()
            elif enemy3.ehp <= 0:
                print("Enemy " + enemy3.enemy_type + "'s HP has fallen to " + str(enemy3.ehp))
                print(enemy3.enemy_type + " has died!")
                print("Your HP is " + str(pc.php))
                print()
                enemy3.ehp = 6
            if pc.php <= 0:
                print("YOU DIED")
                print()
                main()
            return pc.php
        elif encounter == 2:
            print("You ran away!")
            print()

    def drinkPotion():
        if pc.php < 10:
            pc.php = 10
            print("You feel fully restored!")
            print()
        else:
            print("This potion had no effect")
            print()

    def saveCharacter():
        print("hi")

    def saveQuit():
        print("hi")

    choice = 0
    while choice != saveQuit:
        choice = mainMenu()
        if choice == fightE1:
            fightChick()
        elif choice == fightE2:
            fightGob()
        elif choice == fightE3:
            fightTroll()
        elif choice == drinkPot:
            drinkPotion()
        elif choice == save:
            saveCharacter()
        elif choice == saveQuit:
            saveQuit()




main()
