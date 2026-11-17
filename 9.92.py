s = input("Введите предложение: ")
t = ""
for i in range(len(s)):
    if i % 2 == 1:
        t = t + "ы"
    else:
        t = t + s[i]
print(t)
