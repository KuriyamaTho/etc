s = input("Введите предложение: ")
c1 = input("Введите первый символ: ")
c2 = input("Введите второй символ: ")
for ch in s:
    if ch == c1 or ch == c2:
        print(ch, end=" ")
print()
