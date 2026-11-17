s = input("Введите слово из четного числа букв: ")
t = list(s)
n = len(t)
for i in range(n // 2):
    c = t[i]
    t[i] = t[n - 1 - i]
    t[n - 1 - i] = c
print("".join(t))
