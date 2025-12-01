num1 = int(input())
num2 = int(input())
for hui in range(num1, num2 + 1):
    for pizda in range(1,11):
        print(f"{hui} * {pizda} = {hui * pizda}")