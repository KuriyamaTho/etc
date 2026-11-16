n = int(input("Введите количество судей (n >= 3): "))
a = float(input("Введите оценку судьи 1: "))
s = a
mx = a
mn = a
for i in range(2, n + 1):
    a = float(input(f"Введите оценку судьи {i}: "))
    s = s + a
    if a > mx:
        mx = a
    if a < mn:
        mn = a
print("Оценка, идущая в зачет:", (s - mx - mn) / (n - 2))
