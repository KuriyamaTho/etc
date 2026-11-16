n = int(input("Введите натуральное число n (n >= 2): "))
alt = 0
sign = 1
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    alt = alt + sign * a
    sign = -sign
    if i == 1:
        first = a
    if i == 2:
        second = a
last = a
print("а) a1 - a2 + a3 - ... =", alt)
print("б) a1 + an =", first + last)
print("в) a1 - a2 =", first - second)
