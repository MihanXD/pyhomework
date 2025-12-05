try:
    with open("altushka.txt", "r") as f:
        text = f.read()
        count = 0
        for i in text.splitlines():
            if i == "":
                count += 1

        print(f"строк: {len(text.splitlines())} , слов: {len(text.split())}, символов: {len(text)}, пустых строк: {count}")
except FileNotFoundError:
     print("Скуф не нашел альтушку")