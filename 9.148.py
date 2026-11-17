s = input("Введите текст: ")
best = 0
cur = 0
for ch in s:
    if "0" <= ch <= "9":
        cur = cur + 1
        if cur > best:
            best = cur
    else:
        cur = 0
print("Наибольшее количество идущих подряд цифр:", best)
