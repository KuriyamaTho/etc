p = 1
for i in range(1, 9):
    a = float(input(f"Введите a{i}: "))
    p = p * a
if p < 10000:
    print("Да, произведение меньше 10 000")
else:
    print("Нет, произведение не меньше 10 000")
