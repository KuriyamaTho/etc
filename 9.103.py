s = input("Введите слово из четного числа букв: ")
t = list(s)
for i in range(0, len(t), 2):
    c = t[i]
    t[i] = t[i + 1]
    t[i + 1] = c
print("".join(t))
