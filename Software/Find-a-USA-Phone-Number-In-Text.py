import re

while True:
    p_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    u = input("== Find a USA phone number ==\nEnter text: ")
    print("Numbers found:", p_num.findall(u), "\n")
