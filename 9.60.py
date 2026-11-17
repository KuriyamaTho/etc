s = input("Введите предложение: ")
k = 0
for ch in s:
    if ch == " ":
        k = k + 1
print("Число пробелов:", k)
