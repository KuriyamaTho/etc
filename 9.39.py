s = input("Введите слово (не менее 6 букв): ")
n = len(s)

# 1)
print("1)", s[n - 3:] + s[3:n - 3] + s[:3])

# 2)
t = ""
for i in range(n - 3, n):
    t = t + s[i]
for i in range(3, n - 3):
    t = t + s[i]
for i in range(3):
    t = t + s[i]
print("2)", t)
