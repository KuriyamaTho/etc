a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = input("Введите третье слово: ")

# 1)
result = []
for ch in a:
    if ch not in b and ch not in c:
        result.append(ch)
for ch in b:
    if ch not in a and ch not in c:
        result.append(ch)
for ch in c:
    if ch not in a and ch not in b:
        result.append(ch)
print("1)", " ".join(result))

# 2)
result = []
for i in range(len(a)):
    if a[i] not in a[:i] and a[i] not in b and a[i] not in c:
        result.append(a[i])
for i in range(len(b)):
    if b[i] not in b[:i] and b[i] not in a and b[i] not in c:
        result.append(b[i])
for i in range(len(c)):
    if c[i] not in c[:i] and c[i] not in a and c[i] not in b:
        result.append(c[i])
print("2)", " ".join(result))
