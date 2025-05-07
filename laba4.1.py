input_data = input("Введите числа списка: ")

numbers = [float(x) if "." in x else int(x) for x in input_data.split()]

integer = [x for x in numbers if  isinstance(x, int) or (isinstance(x, float) and x.is_integer())]

print("Исходный список: ", numbers)
print("Отсортированный список: ", integer)