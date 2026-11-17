s = input("Введите слово: ")
p = int(input("Введите s: "))
k = int(input("Введите k (s < k): "))
print(s[:p - 1] + s[p:k] + s[p - 1] + s[k:])
