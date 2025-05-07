from aux6 import f1, f2, f3, f4

x = float(input("Введите вещественное число: "))
print("Число является целым" if f1(x) else "Число вещественное")

result_f2 = f2(x1 = 10, y1 = 20, x2 = 15 , y2 = 5)
print("Сумма аргументов при 'y': ",result_f2)

n = int(input("Введите кол-во элементов последовательности: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))
for val in f3(n,x,y):
    print (val)

@f4
def f5(x):
    return len(x)
s = input("Введите строку: ")
res = f5(s)
print("Длина строки:", res)