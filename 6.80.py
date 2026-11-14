n = int(input("Введите натуральное число: "))
zeros = 0
nines = 0
while n > 0:
    if n % 10 == 0:
        zeros = zeros + 1
    if n % 10 == 9:
        nines = nines + 1
    n = n // 10
if zeros > nines:
    print("Чаще встречается цифра 0")
elif nines > zeros:
    print("Чаще встречается цифра 9")
else:
    print("Цифры 0 и 9 встречаются одинаково часто")
