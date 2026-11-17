s = input("Введите слово: ")
p = int(input("Введите s: "))
k = int(input("Введите k (s > k): "))
print(s[:k - 1] + s[p - 1] + s[k - 1:p - 1] + s[p:])
