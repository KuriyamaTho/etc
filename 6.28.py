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
print("а) Максимальная цифра: номер от конца", pos_mx, ", номер от начала", i - pos_mx + 1)
print("б) Минимальная цифра: номер от конца", pos_mn, ", номер от начала", i - pos_mn + 1)
