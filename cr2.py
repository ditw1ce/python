A = int(input("введите A "))
B = int(input("введите B "))
if A == B:
    C = "Конечно"
elif A % B == 0:
    C = "DA"
else:
    C = "NO"
print(C)