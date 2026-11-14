# а)
print("а) Последняя цифра числа - правая половина кости")
x = int(input("Введите число 1: "))
right = x % 10
i = 1
ok = True
while i < 20:
    x = int(input(f"Введите число {i + 1}: "))
    i = i + 1
    ok = ok and x // 10 == right
    right = x % 10
if ok:
    print("а) Да, ряд выложен по правилам игры")
else:
    print("а) Нет, ряд выложен не по правилам игры")

# б)
print("б) Любая цифра числа может быть любой половиной кости")
x = int(input("Введите число 1: "))
ends = {x // 10, x % 10}
i = 1
while i < 20:
    x = int(input(f"Введите число {i + 1}: "))
    i = i + 1
    left = x // 10
    right = x % 10
    new_ends = set()
    if left in ends:
        new_ends.add(right)
    if right in ends:
        new_ends.add(left)
    ends = new_ends
if len(ends) > 0:
    print("б) Да, ряд можно выложить по правилам игры")
else:
    print("б) Нет, ряд нельзя выложить по правилам игры")
