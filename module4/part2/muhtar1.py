muhtar = input().split()
if muhtar[1] == "+":
    print(int(muhtar[0]) + int(muhtar[2]))
elif muhtar[1] == "-":
    print(int(muhtar[0]) - int(muhtar[2]))
elif muhtar[1] == "/":
    print(int(muhtar[0]) / int(muhtar[2]))
elif muhtar[1] == "*":
    print(int(muhtar[0]) * int(muhtar[2]))
elif muhtar[1] == "=":
    print("ты че, ДЯТЕЛ?")