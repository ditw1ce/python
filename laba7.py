import math

def f(x):
    try:
        return 1 / math.log(x)**2 - 1
    except ValueError as e:
        raise ValueError("Функция не определена для данного x") from e

def calculate():
    for i in range(5):
        try:
            try:
                x = float(input("Введите x-> "))
                result = f(x)
                print(result)
            except ValueError as e:
                if "Функция не определена для данного x" in str(e):
                    print("Ошибка в функции: " + str(e))
                else:
                    print("Ошибка введенного значения")
        except OverflowError:
            print("Ошибка переполнения")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
        except KeyboardInterrupt:
            print("Кол-во оставшихся итераций: " + str(4 - i))
            continue

calculate()