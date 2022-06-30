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
            return print(x, "wins!"), payout(d1, d2, d3, x)
        elif d1 == 1 and d2 == 2 and d3 == 3 or win_p[0] is True and (d3 == 1):  # Automatic Loss
            return print(y, "wins!"), payout(d1, d2, d3, y)
        elif win_p[0] is True and d3 in (2, 3, 4, 5):  # Set Bank Point / Switch. w. Player
            global set_point
            if x == "Bank":
                set_point = d3
                set_point_p = 0
            else:
                set_point_p = d3
            if set_point in (2, 3, 4, 5) and x == "Bank":
                print("SET POINT =", set_point, "\nAction -> SWITCH")
                return input("Press anything to continue: "), game("Player", "Bank")
            elif set_point_p > set_point and x == "Player":  # Checks if Player has a higher number than Bank
                return print(x, "wins!"), payout(d1, d2, d3, x)
            elif set_point_p == set_point and x == "Player":  # Checks if Player ties with Bank
                return print("Push! No winner. Bets returned to", x, "and", y + ".")
            elif set_point_p < set_point and x == "Bank":  # Checks if Player has a lower number than Bank
                return print(x, "wins!"), payout(d1, d2, d3, x)
        else:
            print("Action -> RE-ROLL"), input("Press anything to roll: ")  # Re-roll if no win/lose condition is met


def payout(a, b, c, o):
    if a == 1 and b == 1 and c == 1:
        return print("Payout for", o + ": $" + str(int(user_bet * 5)))
    elif a == b == c:
        return print("Payout for", o + ": $" + str(int(user_bet * 3)))
    else:
        return print("Payout for", o + ": $" + str(int(user_bet * 2)))


print("== Cee-lo ==\nYou will be playing against the bank."), input("Press anything to begin: ")
set_point = 0
while True:
    center_bet = random.randint(100, 1000)
    while True:  # Loop until Player enters equal/below the center bet and greater than 0
        os.system('cls||clear')
        print("Center bet: $" + str(center_bet))
        user_bet = int(input("Fade your bet: $"))
        if center_bet >= user_bet > 0:
            print("Final Center bet is: $" + str(user_bet)), input("Press anything to continue: ")
            break
        else:
            print("Bet has to be >0, equal or below $" + str(center_bet) + "."), input("Press anything to continue: ")
    game("Bank", "Player")
    restart = input("\nRESTART? (y/n): ")
    if restart == ('y' or 'Y'):
        continue
    else:
        exit()
