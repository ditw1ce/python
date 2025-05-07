def f1(x):
    return x == int(x)

def f2(**x):
    return sum(value for key, value in x.items() if key.startswith('y'))

def f3(n,x,y):
    a0, a1 = x, y
    for _ in range(n):
        yield a0
        a0, a1 = a1, a1 + a0**2

def prime(n):
     if n <= 1:
        return False
     if n == 2:
        return True
     if n % 2 == 0:
        return False
     for i in range(3,int(n**0.5) + 1, 2):
         if n % i == 0:
             return False
     return True

def f4(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат функции: {result}")

        if prime(result):
            print("Результат — простое число.")
        else:
            print("Результат — не простое число.")

        return result

    return wrapper