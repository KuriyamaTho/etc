a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = input("Введите третье слово: ")
result = []
for i in range(len(a)):
    if a[i] not in a[:i] and a[i] in b and a[i] in c:
        result.append(a[i])
print(" ".join(result))
