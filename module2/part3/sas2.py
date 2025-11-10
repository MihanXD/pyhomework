operators = {
    "МТС": 2.5,
    "Билайн": 2.3,
    "МегаФон": 2.4,
    "Теле2": 2.0
}

print(f"Доступные операторы: {operators}")

minutes = float(input("\nВведите продолжительность разговора в минутах: "))

print("\nВыберите оператор С КОТОРОГО звоните:")
from_op = input("Введите название оператора: ")

print("\nВыберите оператор НА КОТОРЫЙ звоните:")
to_op = input("Введите название оператора: ")

if from_op in operators and to_op in operators:
    if from_op == to_op:
        cost = minutes * operators[from_op] * 0.8
    else:
        cost = minutes * operators[from_op]

    print(f"\nСтоимость разговора: {cost:.2f} руб.")
    print(f"({from_op} -> {to_op}, {minutes} минут)")
else:
    print("Ошибка: введен неверный оператор!")