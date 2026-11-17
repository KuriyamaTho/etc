s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
words = s1.split() + s2.split()
result = []
for word in words:
    k = 0
    for w in words:
        if w == word:
            k = k + 1
    if k == 1:
        result.append(word)
print(" ".join(result))
