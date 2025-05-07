import aux5
stroka = input("введите строку ")
words = stroka.split()
d = {words[i]: words[i + 1] for i in range(0, len(words), 2)}
result = aux5.f2(d)
output = [v for k, v in result.items() if k.isdigit()]
print("результат",output)
