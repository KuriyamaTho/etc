s = input("Введите предложение: ")
words = s.split()
for i in range(len(words)):
    if words[i] not in words[:i]:
        print(words[i], end=" ")
print()
