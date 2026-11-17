s = input("Введите текст с цифрами: ")
total = 0
mx = -1
for ch in s:
    if "0" <= ch <= "9":
        d = int(ch)
        total = total + d
        if d > mx:
            mx = d
print("а) Сумма цифр:", total)
print("б) Максимальная цифра:", mx)
