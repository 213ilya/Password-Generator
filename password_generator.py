import secrets

symbols = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!?@_+<>«»%#=÷"

while True:
    try:
        length = int(input("Длина пароля: "))
        if length < 1:
            print("Длина должна быть больше 0!")
            continue
    except ValueError:
        print("Введите целое число!")
        continue

    password = ""
    for _ in range(length):
        password += secrets.choice(symbols)

    print("Пароль:", password)

    if input("Продолжить? (да/нет): ").lower().strip() == "нет":
        break