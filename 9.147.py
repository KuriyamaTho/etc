s = input("Введите текст вида d1±d2±...±dn (знаки + или -): ")
total = 0
sign = 1
for ch in s:
    if ch == "+":
        sign = 1
    elif ch == "-" or ch == "–" or ch == "−":
        sign = -1
    elif "0" <= ch <= "9":
        total = total + sign * int(ch)
print("Алгебраическая сумма:", total)
