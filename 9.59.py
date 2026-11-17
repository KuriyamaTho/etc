s = input("Введите предложение: ")
k = 0
for ch in s:
    if ch == "о":
        k = k + 1
print("Число букв о:", k)
