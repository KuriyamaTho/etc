s = input("Введите последовательность слов: ")
words = s.split()

# а)
print("а) Слова, отличные от первого, без повторяющихся букв:")
for i in range(1, len(words)):
    word = words[i]
    if word != words[0]:
        ok = True
        for j in range(len(word)):
            if word[j] in word[:j]:
                ok = False
        if ok:
            print(word)

# б)
print("б) Слова, отличные от первого и симметричные:")
for i in range(1, len(words)):
    word = words[i]
    if word != words[0]:
        ok = True
        for j in range(len(word) // 2):
            if word[j] != word[len(word) - 1 - j]:
                ok = False
        if ok:
            print(word)
