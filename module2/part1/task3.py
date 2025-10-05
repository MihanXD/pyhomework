meters = int(input("enter meters: "))
userchoice = int(input("what do you want to do(1 - 3): \n 1-milimeters \n 2-inches \n 3-yards \n answer: "))
milimeters = (meters*1000)
inches = (meters*39.3701)
yards = (meters*1.09361)
if userchoice == 1:
    print(milimeters)
elif userchoice == 2:
    print(inches)
elif userchoice == 3:
    print(yards)
else:
    print("Error!")
