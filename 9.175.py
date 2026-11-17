s = input("Введите предложение: ")
words = s.split()
for word in words:
    k = 0
    for w in words:
        if w == word:
            k = k + 1
    if k == 1:
        print(word, end=" ")
print()
