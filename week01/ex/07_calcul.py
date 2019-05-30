total = 0
while 1:
    number = input("Enter a number: ")
    check = number.lstrip("-").isdigit()
    if number == "":
        total = total
        print("TOTAL: "+str(total))
    elif check is True:
        number = int(number)
        total += number
        print("TOTAL: "+str(total))
    elif check is False:
        if number == "exit" or number == "EXIT":
            exit()
        else:
            print("Invalid input")
