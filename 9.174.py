s = input("Введите предложение: ")
words = s.split()
n = len(words)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(words[j]) > len(words[j + 1]):
            t = words[j]
            words[j] = words[j + 1]
            words[j + 1] = t
print(" ".join(words))
