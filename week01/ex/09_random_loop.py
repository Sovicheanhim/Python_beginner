import random

number = input("Enter a number: ")
number = int(number)
while number > 0:
    print(random.randrange(0, 101, 1))
    number -= 1
