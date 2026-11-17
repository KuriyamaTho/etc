s = input("Введите предложение: ")
k = 0
for ch in s:
    if ch == "а":
        k = k + 1
print("Доля букв а (в %):", k / len(s) * 100)
