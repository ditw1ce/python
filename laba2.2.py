valuta = [500,200,100,50,20,10,5,2,1]

amount = int(input("Введите сумму для снятия в BYN: "))

def withdrawal(amount):
    result = {}
    for den in valuta:
        if amount >= den: # Перебираем номиналы от большего к меньшему
           count = amount // den # Определяем, сколько купюр/монет данного номинала можно выдать
           result[den] = count
           amount -= den * count
        else:
           result[den] = 0
    return result

withdrawal_result = withdrawal(amount)
print(f"{amount} BYN =") # f-строка подставляет переменные прямо в текст
for den, count in withdrawal_result.items(): # Проходим по элементам словаря withdrawal_result с помощью метода .items().
    print(f"{den}*{count}", end=" ")


