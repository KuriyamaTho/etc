s = input("Введите предложение: ")
k = 0
for ch in s:
    if ch.lower() in "аеёиоуыэюя":
        k = k + 1
print("Количество гласных букв:", k)
