n = int(input("Введите натуральное число: "))
m = int(input("Введите m: "))
s = 0
i = 0
while i < m and n > 0:
    s = s + n % 10
    n = n // 10
    i = i + 1
print("Сумма m последних цифр:", s)
