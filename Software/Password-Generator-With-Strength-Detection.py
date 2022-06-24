import os
import random
import re
import string

x = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
while True:
    for i in range(1):
        password = random.sample(x, 14)
        print("== Password generator with strength detection ==\n\n[  ", ''.join(password), "  ]")
        if re.fullmatch(r'[\w!"#$%&()*+,./\\:;<=>?@^_`{|}~-]{8,}', ''.join(password)):
            print("\nStrong password."), input("\nPress enter to print another one..."), os.system('cls||clear')
        else:
            print("\nWeak password."), input("\nPress enter to print another one..."), os.system('cls||clear')
