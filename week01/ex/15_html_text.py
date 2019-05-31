string = str()
while 1:
    temp = input("Enter a string :")
    if temp == "Generate":
        string = string.strip()
        string = "</h1>%s</h1>" % string
        print(str(string))
    else:
        string = string + temp + " "
