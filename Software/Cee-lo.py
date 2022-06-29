import random
import os


def game(x, y):
    while True:
        os.system('cls||clear')
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        win_p = [d1 == d2 != d3]  # True or False
        print(x, "TURN")
        print("Dice rolls:", d1, d2, d3)
        if d1 == d2 == d3 or d1 == 4 and d2 == 5 and d3 == 6 or win_p[0] is True and (d3 == 6):  # Automatic Win
            return print(x, "wins!")
        elif d1 == 1 and d2 == 2 and d3 == 3 or win_p[0] is True and (d3 == 1):  # Automatic Loss
            return print(y, "wins!")
        elif win_p[0] is True and (int(d3) in range(2, 5)):  # Set Bank Point / Switch. w. Player
            set_point = 0
            set_point_p = 0
            set_point += d3
            set_point_p += d3
            if set_point == d3 and x == "Bank":  # Checks if  set_point has a value and that x = Bank
                set_point_p -= d3
                print("SET POINT =", set_point, "\nAction -> SWITCH\n")
                return input("Press anything to continue: "), game("Player", "Bank")
            elif set_point_p > set_point and x == "Player":  # Checks if Player has a higher number than Bank
                return print(x, "wins!")
            elif set_point_p == set_point and x == "Player":  # Checks if Player ties with Bank
                return print("Push! No winner.")
            elif set_point_p < set_point and x == "Bank":  # Checks if Player has a lower number than Bank
                return print(x, "wins!")
        else:
            print("Action -> RE-ROLL"), input("Press anything to roll: ")  # Re-roll if no win/lose condition is met


def res():  # Restart function
    restart = input("\nRESTART? (y/n): ")
    if restart == ('y' or 'Y'):
        return os.system('cls||clear')  # Returns to loop
    else:
        exit()


print("== Cee-lo ==\nYou will be playing against the bank."), input("Press anything to begin...")
while True:
    game("Bank", "Player")
    res()
