n = int(input("Введите натуральное число: "))
first = n
while first >= 10:
    first = first // 10
k = 0
m = n
while m > 0:
    if m % 10 == first:
        k = k + 1
    m = m // 10
print("Первая цифра встречается раз:", k)
