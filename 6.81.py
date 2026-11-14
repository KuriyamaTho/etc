n = int(input("Введите натуральное число: "))
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
ka = 0
kb = 0
while n > 0:
    if n % 10 == a:
        ka = ka + 1
    if n % 10 == b:
        kb = kb + 1
    n = n // 10
if ka < kb:
    print("Да, цифра a встречается реже, чем цифра b")
else:
    print("Нет, цифра a встречается не реже, чем цифра b")
