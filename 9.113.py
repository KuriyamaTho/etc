s = input("Введите предложение: ")
t = ""
k = 0
for ch in s:
    if ch == "с":
        k = k + 1
    else:
        t = t + ch
for i in range(k):
    t = t + "_"
print(t)
