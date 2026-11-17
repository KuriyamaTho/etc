s = input("Введите предложение: ")
i = 0
while i < len(s) and s[i] == " ":
    i = i + 1
k = 0
while i < len(s) and s[i] != " ":
    if s[i] == "о":
        k = k + 1
    i = i + 1
print("Количество букв о в первом слове:", k)
