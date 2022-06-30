import random
import os

while True:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    bet = int(input("== Kitsune bakuchi ==\nEnter a bet: $"))
    input("Enter anything to roll the dices: ")
    print("Dices show:", d1, d2, d3)
    if d1 == d2 == d3:
        print("Player wins. Payout: $" + str(bet * 4))
    else:
        print("Bank wins.")
    input("\nEnter anything to play again: "), os.system('cls||clear')
