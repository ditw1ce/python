import random
numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(1, 50))
    i += 1
sum_chet = 0
for num in numbers:
    if num % 2 == 0:
        sum_chet += num
print("последовательность: ",numbers)
print("сумма чет: ", sum_chet)
