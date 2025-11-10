num = int(input())
if (num > 100) or (num < 1):
    print("sas")
else:
    for a in range(1, num):
        if (a % 3 == 0) and (a % 5 == 0):
            print(f"Fizz Buzz {a}")
        elif a % 3 == 0:
            print(f"Fizz {a}")
        elif a % 5 == 0:
            print(f"Buzz {a}")


