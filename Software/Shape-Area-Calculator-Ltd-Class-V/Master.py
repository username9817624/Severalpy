from vtriangle import class1
from vcircle import class2
from vsquare import class3

print("== Shape Area Calculator ==")
while True:
    print("\nWould you like to calculate the area of a [1]triangle, [2]circle or [3]square?")
    var1 = int(input("Enter 1, 2 or 3: "))
    if var1 == 1:
        print("\n== Area calculation for a triangle ==")
        var2 = int(input("Enter the base: "))
        var3 = int(input("Enter the height: "))
        var4 = class1.triangle(var2, var3)
        print("The area is", var4)
    elif var1 == 2:
        print("\n== Area calculation for a circle ==")
        var5 = int(input("Enter the radius: "))
        var6 = class2.circle(var5)
        print("The area is", var6)
    elif var1 == 3:
        print("\n== Area calculation for a square ==")
        var7 = int(input("Enter the base: "))
        var8 = int(input("Enter the height: "))
        var9 = class3.square(var7, var8)
        print("The area is", var9)
