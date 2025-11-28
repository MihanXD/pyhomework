while True:
    num1 = int(input())
    num2 = int(input())
    if num1 and num2 == 7:
        print("goodbye!")
        break

    numlist = [num1,num2]
    summ = (num1 + num2)

    print(summ, max(numlist), min(numlist))
