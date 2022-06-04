import string
import random

var1 = string.ascii_lowercase
var2 = string.ascii_uppercase
var3 = string.digits
var4 = string.punctuation
var = var1 + var2 + var3 + var4

print("== Password generator ==")
while True:
    length = int(input("Enter the desired length for a password: "))
    u_print_a = int(input("Enter how many you would like to print: "))
    for i in range(u_print_a):
        password = random.sample(var, length)
        final = ''.join(password)
        print(final)
