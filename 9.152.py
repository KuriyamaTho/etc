s = input("Введите предложение: ")
best = 0
cur = 0
for ch in s:
    if ch == " ":
        cur = cur + 1
        if cur > best:
            best = cur
    else:
        cur = 0
print("Наибольшее количество идущих подряд пробелов:", best)
