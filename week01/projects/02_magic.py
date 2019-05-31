import random

again = str()
count = 0

WELCOME_MESSAGE = "Hello, what is your name?"
TOO_HIGH = "Too high, try again!"
TOO_LOW = "Too low, try again!"
AGAIN_MESSAGE = "Do you want to play again? [Y/N]"
ERROR_MESSAGE = "Sorry, I did not understand. Let me repeat:"

print(WELCOME_MESSAGE)
name = str(input())

while again == 'y' or again == "Y" or count == 0:
    count = 0
    number = random.randrange(1, 101, 1)
    print("Well "+name+", try to guess the number I have in mind")
    while 1:
        guess = int(input())
        count += 1
        if guess > number:
            print(TOO_HIGH)
        elif guess < number:
            print(TOO_LOW)
        elif guess == number:
            if count == 1:
                print("You won in 1 turn only, that's amazing!")
                break
            else:
                print("It took you "+str(count)+" turns to guess my number which was "+str(number)+"!")
                break
    while 1:
        print(AGAIN_MESSAGE)
        again = input()
        if again == 'y' or again == "Y":
            break
        elif again == "n" or again == "N":
            print("Ok, bye "+name+"! See you later!")
            break
        else:
            print(ERROR_MESSAGE)
            continue
