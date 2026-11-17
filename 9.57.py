s = input("Введите предложение: ")
for i in range(1, len(s), 2):
    if s[i] == "и":
        print(s[i])
