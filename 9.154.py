s = input("Введите слово: ")
t = ""
for ch in s:
    if ch not in t:
        t = t + ch
print("Количество различных букв:", len(t))
