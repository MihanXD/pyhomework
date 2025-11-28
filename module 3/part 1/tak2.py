num1 = int(input())
num2 = int(input())
for a in range(num1, num2):
    print(a)
for b in range(num2, num1, -1):
    print(b)
for c in range(num1, num2):
    if c % 7 == 0:
        print(c)
f = 0
for d in range(num1, num2):
    if d % 5 == 0:
        f = f +1
print(f)
