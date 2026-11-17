s = input("Введите предложение: ")
t = ""
k = 0
for i in range(len(s)):
    if s[i] == "о" and i % 2 == 0:
        k = k + 1
    else:
        t = t + s[i]
for i in range(k):
    t = t + "_"
print(t)
