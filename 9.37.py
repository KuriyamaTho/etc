s = input("Введите слово из четного числа букв: ")
n = len(s)

# 1)
print("1)", s[n // 2:] + s[:n // 2])

# 2)
t = ""
for i in range(n // 2, n):
    t = t + s[i]
for i in range(n // 2):
    t = t + s[i]
print("2)", t)
