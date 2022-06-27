import random


def pa():
    global secret_word
    global c_guesses
    global i_guesses
    global dashes
    global letters
    play_again = input("\nPlay again? y/n: ")
    yes = ['y', 'ye', 'yes']
    if play_again.lower() in yes:
        secret_word = random.choice(words)
        letters = [y.upper() for y in secret_word]
        dashes = ['_'] * len(secret_word)
        c_guesses = 0
        i_guesses = 0
    else:
        exit()


hangman = ['\n +---#\n     |\n     |\n     |\n    _|_', '\n +---#\n O   |\n     |\n     |\n    _|_',
           '\n +---#\n O   |\n |   |\n     |\n    _|_', '\n +---#\n O   |\n/|   |\n     |\n    _|_',
           '\n +---#\n O   |\n/|\\  |\n     |\n    _|_', '\n +---#\n O   |\n/|\\  |\n/    |\n    _|_',
           '\n +---#\n O   |\n/|\\  |\n/ \\  |\n    _|_\n']
words = ['CASTLE', 'LOWER', 'STAND', 'COMPUTER']
secret_word = random.choice(words)
letters = [y.upper() for y in secret_word]
dashes = ['_'] * len(secret_word)
c_guesses = 0
i_guesses = 0
while True:
    while i_guesses < 6 and c_guesses < len(secret_word):
        print(hangman[i_guesses])
        print('Letters:', ''.join(dashes))
        guess = input('Enter a letter: ').upper()
        try:
            i_x = letters.index(guess)
        except ValueError:
            i_guesses += 1
            continue
        c_guesses += 1
        dashes[i_x] = guess
        letters[i_x] = ''
    if i_guesses == 6:
        print(hangman[i_guesses])
        print('The word was', secret_word)
        print('Game over. You lost.')
        pa()
    else:
        print('The word was', secret_word)
        print('You won!')
        pa()
