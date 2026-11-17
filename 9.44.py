s = input("Введите слово s: ")
t = ""
for i in range(len(s) - 1, -1, -1):
    t = t + s[i]
print("t =", t)
