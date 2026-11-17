s = input("Введите слово: ")
m = int(input("Введите m: "))
n = int(input("Введите n: "))
t = list(s)
c = t[m - 1]
t[m - 1] = t[n - 1]
t[n - 1] = c
print("".join(t))
