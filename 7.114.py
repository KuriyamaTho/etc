x = int(input("Введите натуральное число x: "))
n = int(input("Введите n: "))
s = 0
k = 0
for i in range(1, x + 1):
    a = int(input(f"Введите a{i}: "))
    if a > n:
        s = s + a
        k = k + 1
if k > 0:
    print("Среднее арифметическое чисел, больших n:", s / k)
else:
    print("Чисел, больших n, среди заданных нет")
