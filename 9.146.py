s = input("Введите текст вида d1-d2+d3-...: ")
total = 0
sign = 1
for ch in s:
    if "0" <= ch <= "9":
        total = total + sign * int(ch)
        sign = -sign
print("Алгебраическая сумма:", total)
