import random

rps = ['Rock', 'Paper', 'Scissor']

print("== Rock, Paper, Scissor. ==")
while True:
    user_i = int(input("\nEnter 0 for rock, 1 for paper and 2 for scissor: "))
    user_r = rps[user_i]
    computer = rps[random.randint(0, 2)]
    for i in range(len(rps)):
        print("User:", user_r, "\nComputer:", computer)
        if user_r == computer:
            print("Result: Tied")
        elif user_r == 'Rock' and computer == 'Scissor':
            print("Result: User won")
        elif user_r == 'Paper' and computer == 'Rock':
            print("Result: User won")
        elif user_r == 'Scissor' and computer == 'Paper':
            print("Result: User won")
        else:
            print("Result: User lost")
        break
