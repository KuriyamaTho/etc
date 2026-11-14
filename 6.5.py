first = int(input("Введите a1: "))
k = 1
i = 1
same = True
while i < 18 and same:
    x = int(input(f"Введите a{i + 1}: "))
    i = i + 1
    same = x == first
    k = k + same
print("Количество равных элементов в начале последовательности:", k)
