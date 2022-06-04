import random

wordlist = ["the", "computer", "drill", "several", "python"]
word = random.choice(wordlist)

while True:
    user_g = input("\nGuess a letter or guess the word (all lowercase): ")
    if user_g == word:
        print("You guessed the word.")
        break
    elif user_g in word:
        print(user_g, "is in the word.")
    elif user_g not in word:
        print(user_g, "is not in the word.")
