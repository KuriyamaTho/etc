n = int(input("Введите натуральное число n: "))
p = float(input("Введите p: "))
s = 0
for i in range(1, n + 1):
    x = float(input(f"Введите x{i}: "))
    if x > 20.5:
        s = s + x
if s < p:
    print("Да, сумма чисел, больших 20,5, меньше p")
else:
    print("Нет, сумма чисел, больших 20,5, не меньше p")
