s = input("Введите слово: ")
n = len(s)
if n % 2 == 1:
    t = s[:n // 2] + s[n // 2 + 1:] + "_"
else:
    t = s[:n // 2 - 1] + s[n // 2 + 1:] + "__"
print(t)
