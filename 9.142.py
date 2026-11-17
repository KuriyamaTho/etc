s = input("Введите текст с начальными пробелами и цифрами: ")
i = 0
while s[i] == " ":
    i = i + 1
start = i
mx = -1
pos = 0
while i < len(s):
    if "0" <= s[i] <= "9" and int(s[i]) > mx:
        mx = int(s[i])
        pos = i - start + 1
    i = i + 1
print("Номер первой максимальной цифры:", pos)
