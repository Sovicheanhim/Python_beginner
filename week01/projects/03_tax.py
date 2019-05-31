WELCOME_MESSAGE = "Please enter your amount:"
TAX_INCORRECT = "Number is incorrect, try again."
TAX_RATE = "Please enter your tax rate:"
RATE_INCORRECT = "Rate is incorrect, try again."
EQUAL_SIGN = "===== ===== ===== ===== ====="

while 1:
    print(WELCOME_MESSAGE)
    amount = input()
    check = amount.isdigit()
    if check is False:
        print(TAX_INCORRECT)
        continue
    else:
        amount = int(amount)
        while 1:
            print(TAX_RATE)
            taxRate = input()
            check = taxRate.isdigit()
            taxRate = int(taxRate)
            if check is False:
                print(TAX_INCORRECT)
                continue
            elif taxRate >= 1 and taxRate <= 99:
                tax = amount * taxRate / 100
                net = amount - tax
                print(EQUAL_SIGN)
                print("AMOUNT: "+str(amount)+"$")
                print("RATE: "+str(taxRate)+"%")
                print(EQUAL_SIGN)
                print("TAX: "+str('{:.2f}'.format(tax))+"$")
                print("NET: "+str('{:.2f}'.format(net))+"$")
                print(EQUAL_SIGN)
                break
            else:
                print(TAX_INCORRECT)
                continue
        break
