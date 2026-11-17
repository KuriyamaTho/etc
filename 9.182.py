s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
words1 = s1.split()
words2 = s2.split()
result = []
for word in words1:
    if word not in words2:
        result.append(word)
for word in words2:
    if word not in words1:
        result.append(word)
print(" ".join(result))
