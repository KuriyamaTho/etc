s = input("Введите текст вида d1+d2+...+dn: ")
total = 0
for ch in s:
    if "0" <= ch <= "9":
        total = total + int(ch)
print("Сумма:", total)
