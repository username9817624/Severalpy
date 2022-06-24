import re

while True:
    em = re.compile(r'''([\w._%+!#$&'*/=?^`{|}~-]+@[\w.-]+\.[a-zA-Z]{2,4})''', re.VERBOSE)
    u = input("== Find emails ==\nEnter text: ")
    print("Emails found:", ' '.join(em.findall(u)))
