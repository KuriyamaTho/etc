s = input("Введите текст: ")
k = 0
for i in range(len(s)):
    if s[i] in ".!?" and (i == 0 or s[i - 1] not in ".!?"):
        k = k + 1
print("Количество предложений:", k)
