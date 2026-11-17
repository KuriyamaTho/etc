s = input("Введите предложение: ")
t = ""
for ch in s:
    if ch == "е":
        t = t + "и"
    else:
        t = t + ch
print(t)
