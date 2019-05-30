number = input("Enter a number :")
if number == "":
    print("Nothing to display")
else:
    number = int(number)
    while number > 0:
        print("Hello World!")
        number -= 1
