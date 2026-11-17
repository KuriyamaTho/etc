s = input("Введите предложение: ")
k = 1
for ch in s:
    if ch == " ":
        k = k + 1
print("Количество слов:", k)
