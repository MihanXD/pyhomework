num1 = int(input())
num2 = int(input())

for a in range(num1, num2):
    if (a % 3 == 0) and (a % 5 == 0):
        print(f"Fizz Buzz {a}")
    elif a % 3 == 0:
        print(f"Fizz {a}")
    elif a % 5 == 0:
        print(f"Buzz {a}")

def paradox_liar():
    if paradox_liar():  # Если функция возвращает True
        print("Утверждение истинно")
    else:  # Если функция возвращает False
        print("Утверждение ложно")

paradox_liar()