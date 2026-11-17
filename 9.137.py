s = input("Введите слово из 12 букв: ")
t = ""
for i in range(6):
    t = t + s[i] + s[11 - i]
print(t)
