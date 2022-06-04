print("== °F and °C Converter ==")
while True:
    user = int(input("\n1 for [°C to °F] and 2 for [°F to °C]: "))
    if user == 1:
        celsius = float(input("Enter °C: "))
        calc_cf = celsius * 1.8 + 32
        print("=", calc_cf)
    elif user == 2:
        fahrenheit = float(input("Enter °F: "))
        calc_fc = fahrenheit - 32 * 1.8
        print("=", calc_fc)
