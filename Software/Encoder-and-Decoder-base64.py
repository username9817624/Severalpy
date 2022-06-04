import base64

while True:
    choice = int(input("Would you like to encode or decode base64?\n1 = encode, 2 = decode: "))
    while True:
        user_phrase = input("Enter a phrase: ")
        if choice == 1:
            user_p_encode = base64.b64encode(user_phrase.encode("utf-8"))
            print(user_p_encode)
        elif choice == 2:
            user_p_decode = base64.b64decode(user_phrase)
            user_p_r = str(user_p_decode, "utf-8")
            print(user_p_r)
        break
