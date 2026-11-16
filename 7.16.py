s = 0
for i in range(1, 11):
    d = int(input(f"Введите d{i}: "))
    if d % 2 == 0:
        s = s + d
print("Сумма четных чисел:", s)
