n = int(input("Введите натуральное число: "))
m = n
mn = 9
while m > 0:
    if m % 10 < mn:
        mn = m % 10
    m = m // 10
k = 0
m = n
while m > 0:
    if m % 10 == mn:
        k = k + 1
    m = m // 10
print("Минимальная цифра встречается раз:", k)
