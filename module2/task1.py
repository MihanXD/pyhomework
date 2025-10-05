num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))
summ = (num1 + num2 + num3)
multiply = (num1*num2*num3)
userchoice = int(input("what do you want to do(1 or 2): \n 1-summ \n 2-multiply \n answer: "))
if userchoice == 1:
    print(summ)
elif userchoice == 2:
    print(multiply)
else:
    print("Error!")
