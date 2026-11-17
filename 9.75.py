# 1)
s = input("1) Введите предложение, в котором есть запятые: ")
i = 0
while s[i] != ",":
    print(s[i], end="")
    i = i + 1
print()

# 2)
s = input("2) Введите предложение (запятых может не быть): ")
i = 0
while i < len(s) and s[i] != ",":
    print(s[i], end="")
    i = i + 1
print()
