import statistics
num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))
numlist = [num1, num2, num3]
userchoice = int(input("what do you want to do(1 - 3): \n 1-min \n 2-max \n 3-mean \n answer: "))
if userchoice == 1:
    print(min(numlist))
elif userchoice == 2:
    print(max(numlist))
elif userchoice == 3:
    print(statistics.mean(numlist))





