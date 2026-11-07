n = int(input("Введите натуральное число n: "))
first = n * (n - 1) + 1
s = 0
for i in range(n):
    s = s + first
    first = first + 2
print(f"{n} в третьей степени =", s)
