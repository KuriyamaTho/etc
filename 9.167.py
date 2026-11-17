s = input("Введите предложение: ")
for word in s.split():
    if word != "привет":
        print(word, end=" ")
print()
