s = input("Введите текст: ")
best = 0
cur = 0
for i in range(len(s)):
    if i > 0 and s[i] == s[i - 1]:
        cur = cur + 1
    else:
        cur = 1
    if cur > best:
        best = cur
print("Наибольшее количество идущих подряд одинаковых символов:", best)
