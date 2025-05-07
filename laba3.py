def process_string(s):  #фун-ия обработки строки

    words = s.split()
    result = []

    for i,word in enumerate(words):
        if i % 2 != 0: #  нечетные индексов
            reversed_word = word[::-1] #реверсит слово
            result.append(reversed_word)

    return ' '. join(result)

input_string = input("Введите строку: ")

output_string = process_string(input_string)

print("Результат:", output_string)