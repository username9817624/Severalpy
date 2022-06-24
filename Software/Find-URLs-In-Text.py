import re

while True:
    http_s = re.compile(r'https?://(?:[a-zA-Z]|\d|[$-_@.&+]|[!*(),]|%[\da-fA-F][\da-fA-F])+')
    u = input("== Find URLs ==\nEnter text: ")
    print("URLs found:", ' '.join(http_s.findall(u)))
