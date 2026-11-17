s = input("Введите предложение: ")
words = s.split()
best = words[0]
for word in words:
    if len(word) > len(best):
        best = word
print("Самое длинное слово:", best)
