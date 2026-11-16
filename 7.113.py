s = 0
k = 0
for i in range(1, 10):
    b = float(input(f"Введите b{i}: "))
    if b > 10:
        s = s + b
        k = k + 1
if k > 0:
    print("Среднее арифметическое чисел, больших 10:", s / k)
else:
    print("Чисел, больших 10, среди заданных нет")
