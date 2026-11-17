s = input("Введите текст с числами: ")
mx = -1
number = 0
inside = False
for ch in s:
    if "0" <= ch <= "9":
        number = number * 10 + int(ch)
        inside = True
    else:
        if inside and number > mx:
            mx = number
        number = 0
        inside = False
if inside and number > mx:
    mx = number
print("Максимальное число в тексте:", mx)
