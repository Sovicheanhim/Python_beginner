while 1:
    number = input("Enter a number:")
    check = number.isdigit()
    if check is True:
        number = int(number)
        if number % 2 == 0:
            print(str(number)+" is EVEN")
        else:
            print(str(number)+" is ODD")
    else:
        if number == "exit" or number == "EXIT":
            exit()
        else:
            print(number+" is not a valid number.")
    continue
