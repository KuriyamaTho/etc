s = input("Введите слово: ")
k = int(input("Введите k: "))
print(s[:k - 1] + s[-1] + s[k - 1:-1])
