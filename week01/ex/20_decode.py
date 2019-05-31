mess = str()
string = input("Enter your encrypted message:")
if string == "":
    print("Nothing to decode")
else:
    for x in string:
        x = ord(x)
        if x >= 65 and x+13 <= 103:
            x += 13
            if x > 90:
                x -= 26
        elif x >= 97 and x+13 <= 135:
            x += 13
            if x > 122:
                x -= 26
        else:
            x = x
        mess += chr(x)
    print(str(mess))
