n = int(input("Введите натуральное число: "))
pos = 0
i = 0
while n > 0:
    i = i + 1
    if n % 10 == 8:
        pos = i
    n = n // 10
print("Номер цифры 8 (от конца числа):", pos)
