s = input("Введите десятичную запись целого числа: ")
total = 0
for ch in s:
    if "0" <= ch <= "9":
        total = total + int(ch)
print("Сумма цифр:", total)
