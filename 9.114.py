s = input("Введите слово: ")
t = ""
for ch in s:
    if ch not in t:
        t = t + ch
for i in range(len(s) - len(t)):
    t = t + "_"
print(t)
