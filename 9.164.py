s = input("Введите предложение из 10 слов: ")
words = []
word = ""
for ch in s:
    if ch != " ":
        word = word + ch
    else:
        words.append(word)
        word = ""
words.append(word)
print(words)
