def collatz(x):
    if x % 2 == 0:
        return x // 2
    elif x % 2 == 1:
        return 3 * x + 1


n = int(input("== Collatz ==\nEnter a number: "))
while n != 1:
    n = collatz(n)
    print(n)
