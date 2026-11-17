s = input("Введите текст: ")
total = 0
number = 0
inside = False
for ch in s:
    if "0" <= ch <= "9":
        number = number * 10 + int(ch)
        inside = True
    else:
        if inside:
            total = total + number
        number = 0
        inside = False
if inside:
    total = total + number
print("Сумма всех чисел в тексте:", total)
