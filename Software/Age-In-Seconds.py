print("== Age in seconds ==")
while True:
    u = int(input("Enter an age: "))
    if u % 4 == 0:
        print(u * 366 * 24 * 60, "seconds.")
    elif u % 4 != 0:
        print(u * 365 * 24 * 60, "seconds.")
