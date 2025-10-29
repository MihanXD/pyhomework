num1 = int(input())
num2 = int(input())
numlist = [num1, num2]
if num1 == num2:
    print("tha numbers are equal")
elif num1 > num2 or num1 < num2:
    numlist.sort()
    print(numlist)

