import re

while True:
    https = re.compile(r'https?://(?:[a-zA-Z]|\d|[$-_@.&+]|[!*(),]|%[\da-fA-F][\da-fA-F])+')
    u = input("== Find URLs ==\nEnter text: ")
    print("URLs found:", ' '.join(https.findall(u)))
