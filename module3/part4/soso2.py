print("Таблица умножения (1-10):")
print("-" * 50)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()

print("-" * 50)