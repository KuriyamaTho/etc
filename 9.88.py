s = input("Введите предложение: ")
i = 0
while i < len(s) and s[i] != ",":
    i = i + 1
i = i + 1
while i < len(s) and s[i] != ",":
    print(s[i], end="")
    i = i + 1
print()
