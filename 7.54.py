n = int(input("Введите натуральное число n: "))
a = int(input("Введите a1: "))
mx = a
mn = a
pos_mx = 1
pos_mn = 1
for i in range(2, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a >= mx:
        mx = a
        pos_mx = i
    if a <= mn:
        mn = a
        pos_mn = i
print("Номер максимального числа:", pos_mx)
print("Номер минимального числа:", pos_mn)
