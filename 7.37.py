n = int(input("Введите количество чисел в последовательности: "))
k = 0
prev = int(input("Введите число 1: "))
for i in range(2, n + 1):
    x = int(input(f"Введите число {i}: "))
    if prev * x < 0:
        k = k + 1
    prev = x
print("Знак меняется раз:", k)
