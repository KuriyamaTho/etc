n = int(input("Введите натуральное число: "))

# а)
m = n
has3 = False
while m > 0 and not has3:
    has3 = m % 10 == 3
    m = m // 10
if has3:
    print("а) Да, цифра 3 есть в числе")
else:
    print("а) Нет, цифры 3 в числе нет")

# б)
m = n
has2 = False
has5 = False
while m > 0:
    if m % 10 == 2:
        has2 = True
    if m % 10 == 5:
        has5 = True
    m = m // 10
if has2 and has5:
    print("б) Да, в числе есть цифры 2 и 5")
else:
    print("б) Нет, в числе нет цифр 2 и 5 одновременно")
