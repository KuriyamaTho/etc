s = input("Введите предложение: ")
words = s.split()
mn = len(words[0])
for word in words:
    if len(word) < mn:
        mn = len(word)
print("Длина самого короткого слова:", mn)
