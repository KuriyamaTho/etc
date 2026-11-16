m = int(input("Введите натуральное число m: "))
n = int(input("Введите n: "))
s = 0
k = 0
for i in range(1, m + 1):
    a = int(input(f"Введите a{i}: "))
    if a % n == 0:
        s = s + a
        k = k + 1
print("Среднее арифметическое чисел, кратных n:", s / k)
