string = input("Enter a string:")
newString = str()
if string == "":
    print("Empty")
else:
    for x in string:
        check = x.istitle()
        if check is True:
            x = x.lower()
        else:
            x = x.upper()
        newString += x
    print(newString)
