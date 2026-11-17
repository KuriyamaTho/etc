s = input("Введите предложение: ")
for i in range(len(s)):
    if i % 4 == 0 or i % 4 == 1:
        print(s[i])
