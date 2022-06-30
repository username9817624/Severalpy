print("== Multiplication-Table ==")
for n1 in range(1, 11):
    print('\n', end='')
    for n2 in range(1, 11):
        print(str(n1 * n2).rjust(3), end=' ')
input()
