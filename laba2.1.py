name = input(" Введите ваше имя: ")
group = input(" Введите вашу группу: ")
number = int(input(" Введите число от 2 до 5: "))

if 2 <= number <= 5:
    razdelit = "*" * number
    print(name + razdelit + group)
else:
    print(" число должно быть в диапазоне от 2 до 5 ")

