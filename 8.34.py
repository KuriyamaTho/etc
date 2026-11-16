found = False
for n in range(100, 301):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s = s + d
    if s == 50:
        print(n)
        found = True
if not found:
    print("Таких чисел нет")
