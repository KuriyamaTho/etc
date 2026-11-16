x = int(input("Введите число 1: "))
right = x % 10
ok_a = True
ends = {x // 10, x % 10}
for i in range(2, 21):
    x = int(input(f"Введите число {i}: "))
    left = x // 10
    r = x % 10
    ok_a = ok_a and left == right
    right = r
    new_ends = set()
    if left in ends:
        new_ends.add(r)
    if r in ends:
        new_ends.add(left)
    ends = new_ends
if ok_a:
    print("а) Да, ряд выложен по правилам игры")
else:
    print("а) Нет, ряд выложен не по правилам игры")
if len(ends) > 0:
    print("б) Да, ряд можно выложить по правилам игры")
else:
    print("б) Нет, ряд нельзя выложить по правилам игры")
