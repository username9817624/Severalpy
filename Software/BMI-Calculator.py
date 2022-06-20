print("== BMI-Calculator ==")
while True:
    q = int(input("[1]Metric or [2]US: "))
    if q == 1:
        w = float(input("Enter height (m): "))
        e = float(input("Enter weight (kg): "))
        print("BMI: ", e / (w * w))
    elif q == 2:
        r = float(input("Enter height (in): "))
        t = float(input("Enter weight (lbs): "))
        print("BMI: ", 703 * (t / (r * r)))
