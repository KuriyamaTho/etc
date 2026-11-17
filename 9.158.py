a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
result = []
for ch in a:
    if ch not in b:
        result.append(ch)
for ch in b:
    if ch not in a:
        result.append(ch)
print(" ".join(result))
