s = input("Введите предложение: ")
k = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i].isalpha():
        k = k + 1
print("Количество одинаковых соседних букв:", k)
