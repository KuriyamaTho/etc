n = int(input("Введите n: "))
s = 0
i = 0
odd = True
while i < n and odd:
    x = float(input(f"Введите a{i + 1}: "))
    i = i + 1
    odd = x % 2 == 1
    s = s + x * odd
print("Сумма идущих подряд в начале нечетных чисел:", s)
