s = input("Введите слово: ")
k = int(input("Введите k: "))
n = len(s)

# 1)
print("1)", s[k:] + s[:k])

# 2)
t = ""
for i in range(k, n):
    t = t + s[i]
for i in range(k):
    t = t + s[i]
print("2)", t)
