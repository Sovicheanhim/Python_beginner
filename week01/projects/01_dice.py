import random

result = random.randrange(1, 7, 2)
number = str(0)
total = 0

INTRO_MESSAGE = "Welcome to the dice game!"
RULE_MESSAGE = "USAGE: The number must be between 1 and 8"
NUMBER_REQUEST = "Enter the number of dices you want to roll: "

print(INTRO_MESSAGE)
while 1:
    number = input(NUMBER_REQUEST)
    if number == "":
        print(RULE_MESSAGE)
    else:
        number = int(number)
        if not number >= 1 and number < 8:
            print(RULE_MESSAGE)
        else:
            break
number = int(number)
if number == 1:
    result = random.randrange(1, 7, 2)
    total += result
    print("RESULT: " + str(total))
else:
    count = 1
    while number > 0:
        if number == 1:
            result = random.randrange(1, 7, 2)
            total += result
            print("Dice "+str(count)+": "+str(result))
            print("==========")
            print("RESULT: "+str(total))
            print("==========")
            break
        else:
            result = random.randrange(1, 7, 1)
            print("Dice "+str(count)+": "+str(result))
            number -= 1
            total += result
        count += 1
