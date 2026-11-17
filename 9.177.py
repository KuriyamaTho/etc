s = input("Введите предложение, в котором только два одинаковых слова: ")
words = s.split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            print("Одинаковые слова:", words[i])
