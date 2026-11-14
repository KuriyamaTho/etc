n = int(input("Введите натуральное число с различными цифрами: "))
mx = -1
mn = 10
pos_mx = 0
pos_mn = 0
i = 0
while n > 0:
    d = n % 10
    i = i + 1
    if d > mx:
        mx = d
        pos_mx = i
    if d < mn:
        mn = d
        pos_mn = i
    n = n // 10
print("а) От конца числа: максимальная цифра -", pos_mx, ", минимальная цифра -", pos_mn)
print("б) От начала числа: максимальная цифра -", i - pos_mx + 1, ", минимальная цифра -", i - pos_mn + 1)
