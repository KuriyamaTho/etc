s = 0
for i in range(1, 21):
    a = int(input(f"Введите a{i}: "))
    if i % 2 == 0:
        s = s + a
print("Сумма a2 + a4 + a6 + ... =", s)
