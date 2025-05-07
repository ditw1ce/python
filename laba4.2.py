def sum_between_pos(numbers):
    first_pos_index = -1
    second_pos_index = -1
    for i,num in enumerate(numbers):
        if num > 0:
            if first_pos_index == -1:
                first_pos_index = i
            else:
                second_pos_index = i
                break

    if first_pos_index == -1 or second_pos_index == -1:
        print("В списке меньше чем 2 положительных числа")
        return 0

    sum_between = sum(numbers[first_pos_index + 1:second_pos_index])
    return sum_between

input_data = input("Введите вещественные числа через пробел: ")
try:
    numbers = list(map(float, input_data.split()))
    result = sum_between_pos(numbers)
    print("Сумма элементов между первым и вторым положительными элементами:", result)
except ValueError:
    print("Введите корректные данные")


