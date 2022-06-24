import string
import random
import os

var = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
while True:
    for i in range(1):
        print("== Password generator ==\n\n[  ", ''.join(random.sample(var, 14)), "  ]")
        input("\nPress enter to print another one..."), os.system('cls||clear')
