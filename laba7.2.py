with open('data.txt',  'r+') as file:
    for n in range(1, 10001):
        octal = oct(n)[2:]
        count = sum(1 for d in octal if int(d) % 2 == 1)
        file.write(f"{n}:{count}\n")