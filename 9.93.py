s = input("Введите предложение: ")
t = ""
for i in range(len(s)):
    if i % 3 == 2:
        t = t + "а"
    else:
        t = t + s[i]
print(t)
