s = input("Введите текст: ")
k = 0
for ch in s:
    if "0" <= ch <= "9":
        k = k + 1
print("Количество цифр:", k)
