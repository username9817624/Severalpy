import random

number = random.randint(1, 10)

while True:
    user_g = int(input("\n== Guess the number (1-10) ==\nEnter a number: "))
    if user_g == number:
        print("You won!")
        break
    else:
        print("You lost. Try again...")
