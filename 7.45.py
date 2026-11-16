s = 0
k = 0
for i in range(1, 13):
    c = int(input(f"Введите c{i}: "))
    if c % 2 == 0:
        s = s + c
        k = k + 1
print("Среднее арифметическое четных чисел:", s / k)
