import random
import os

while True:
    print("== Coinflip ==")
    v = random.randint(0, 1)
    if v == 0:
        print("Heads.")
    elif v == 1:
        print("Tails.")
    input(">"), os.system('cls||clear')
