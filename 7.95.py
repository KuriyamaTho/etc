s = float(input("Введите s: "))
p = 1
for i in range(1, 7):
    d = float(input(f"Введите d{i}: "))
    p = p * d
if p > s:
    print("Да, произведение больше s")
else:
    print("Нет, произведение не больше s")
