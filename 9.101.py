s = input("Введите слово: ")
t = list(s)
c = t[2]
t[2] = t[-1]
t[-1] = c
print("".join(t))
