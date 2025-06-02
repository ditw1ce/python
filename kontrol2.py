def check_age():
    age = (int(input("введите возраст: ")))
    if age < 18:
        print("доступ запрещен")
    elif 18 <= age <= 25:
        print("досту разрешен с ограничениями")
    else:
        print("доступ разрешен")

check_age()