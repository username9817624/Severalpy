import random
import string

print("== Switching Numbers ==")
while True:
    print(''.join(random.choice(string.digits) for i in range(24)), end='\r')
