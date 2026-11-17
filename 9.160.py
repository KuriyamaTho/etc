a = input("Введите первое слово: ")
b = input("Введите второе слово: ")

# 1)
ok = True
for ch in b:
    if ch not in a:
        ok = False
if ok:
    print("1) Да, из букв первого слова можно получить второе")
else:
    print("1) Нет, из букв первого слова нельзя получить второе")

# 2)
ok = True
for ch in b:
    k1 = 0
    for c in a:
        if c == ch:
            k1 = k1 + 1
    k2 = 0
    for c in b:
        if c == ch:
            k2 = k2 + 1
    if k1 < k2:
        ok = False
if ok:
    print("2) Да, из букв первого слова можно получить второе")
else:
    print("2) Нет, из букв первого слова нельзя получить второе")
