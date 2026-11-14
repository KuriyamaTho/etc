n = int(input("Введите натуральное число: "))

# а)
a = int(input("а) Введите цифру a: "))
m = n
k = 0
while m > 0:
    if m % 10 == a:
        k = k + 1
    m = m // 10
print("а) Цифра a встречается раз:", k)

# б)
z = int(input("б) Введите z (2, 3 или 4): "))
m = n
k = 0
while m > 0:
    if m % 10 % z == 0:
        k = k + 1
    m = m // 10
print("б) Количество цифр, кратных z:", k)

# в)
a = int(input("в) Введите a (0 <= a <= 8): "))
m = n
s = 0
while m > 0:
    if m % 10 > a:
        s = s + m % 10
    m = m // 10
print("в) Сумма цифр, больших a:", s)

# г)
x = int(input("г) Введите цифру x: "))
y = int(input("г) Введите цифру y: "))
m = n
k = 0
while m > 0:
    if m % 10 == x or m % 10 == y:
        k = k + 1
    m = m // 10
print("г) Цифры x и y встречаются всего раз:", k)
