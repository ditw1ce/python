a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

print(" x | y")
print("---+---")
for x in range(-5, 6):
    y = a * x**2 + b * x + c
    print(f"{x:2} | {y:.2f}")