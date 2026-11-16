n = int(input("Введите натуральное число n: "))
m = int(input("Введите m: "))
q = int(input("Введите q: "))
s = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a <= m:
        s = s + a
if s > q:
    print("Да, сумма чисел, не больших m, превышает q")
else:
    print("Нет, сумма чисел, не больших m, не превышает q")
