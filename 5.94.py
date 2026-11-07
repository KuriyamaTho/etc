n = int(input("Введите шестизначное число: "))
s = 0
for i in range(6):
    s = s + n % 10
    n = n // 10
print("Сумма цифр =", s)
