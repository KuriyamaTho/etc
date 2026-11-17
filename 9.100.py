s = input("Введите слово (не менее 5 букв): ")
t = list(s)
c = t[1]
t[1] = t[4]
t[4] = c
print("".join(t))
