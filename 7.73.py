n = int(input("Введите n (n >= 3): "))
inf = float("inf")
mx1 = -inf
mx2 = -inf
mn1 = inf
mn2 = inf
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a > mx1:
        mx2 = mx1
        mx1 = a
    elif a > mx2:
        mx2 = a
    if a < mn1:
        mn2 = mn1
        mn1 = a
    elif a < mn2:
        mn2 = a
print("а) Два максимальных элемента:", mx1, mx2)
print("б) Два минимальных элемента:", mn1, mn2)
