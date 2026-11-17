s = input("Введите предложение: ")
t = ""
for ch in s:
    if ch == " ":
        t = t + "_"
    else:
        t = t + ch
print(t)
