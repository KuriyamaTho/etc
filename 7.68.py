n = int(input("Введите количество пар n: "))
a = float(input("Введите a1: "))
b = float(input("Введите b1: "))
best_sum = a + b
best_prod = a * b
pos_a = 1
pos_g = 1
for i in range(2, n + 1):
    a = float(input(f"Введите a{i}: "))
    b = float(input(f"Введите b{i}: "))
    if a + b >= best_sum:
        best_sum = a + b
        pos_a = i
    if a * b < best_prod:
        best_prod = a * b
        pos_g = i
print("а) Максимальное среднее арифметическое в паре номер:", pos_a)
print("б) Минимальное среднее геометрическое в паре номер:", pos_g)
