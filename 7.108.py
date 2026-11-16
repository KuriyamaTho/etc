m = int(input("Введите натуральное число m: "))
p = int(input("Введите p: "))
k = 0
for i in range(1, m + 1):
    a = int(input(f"Введите a{i}: "))
    if a > m:
        k = k + 1
if k % p == 0:
    print("Да, количество чисел, больших m, кратно p")
else:
    print("Нет, количество чисел, больших m, не кратно p")
