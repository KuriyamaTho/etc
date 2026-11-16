n = int(input("Введите натуральное число n: "))
p = float(input("Введите p: "))
s = 0
for i in range(1, n + 1):
    b = float(input(f"Введите b{i}: "))
    if b > p:
        s = s + b
print("Сумма чисел, больших p:", s)
