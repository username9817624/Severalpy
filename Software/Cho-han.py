import random


def c_o_h(x):
    if cho_or_han == x:
        player_payout = bet_amount + bet_amount
        print("You win. Payout: $" + str(player_payout))
    else:
        print("You lose. Amount lost: $" + str(bet_amount))


print("== Chō-Han ==\nYou will be playing against the house.")
while True:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("\nThe dices have been shaken and rolled.")
    bet_amount = float(input("Place your bet: $"))
    print("The house places an equal bet amount: $" + str(bet_amount)),
    cho_or_han = int(input("(1)Chō or (2)Han?: "))
    if ((dice_1 + dice_2) % 2) == 0:
        print("The dices show EVEN. (" + str(dice_1), "and", str(dice_2) + ")")
        c_o_h(1)
    else:
        print("The dices show ODD. (" + str(dice_1), "and", str(dice_2) + ")")
        c_o_h(2)
