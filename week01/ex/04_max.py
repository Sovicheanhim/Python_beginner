num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
operator = ">"
if num1 > num2:
    biggerNum = num1
    smallerNum = num2
elif num1 < num2:
    biggerNum = num2
    smallerNum = num1
else:
    operator = "=="
    biggerNum = num1
    smallerNum = num2
print("Result : "+str(biggerNum)+" "+operator+" "+str(smallerNum))
