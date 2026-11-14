n = int(input("Введите n: "))
k = 0
i = 0
negative = True
while i < n and negative:
    x = float(input(f"Введите a{i + 1}: "))
    i = i + 1
    negative = x < 0
    k = k + negative
print("Количество отрицательных чисел в начале последовательности:", k)
