s = input("Введите текст с несколькими идущими подряд цифрами: ")
i = 0
while not ("0" <= s[i] <= "9"):
    i = i + 1
number = 0
while i < len(s) and "0" <= s[i] <= "9":
    number = number * 10 + int(s[i])
    i = i + 1
print("Число, образованное цифрами:", number)
