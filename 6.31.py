n = int(input("Введите натуральное число: "))
m = n
mx = 0
while m > 0:
    if m % 10 > mx:
        mx = m % 10
    m = m // 10
k = 0
m = n
while m > 0:
    if m % 10 == mx:
        k = k + 1
    m = m // 10
print("Максимальная цифра встречается раз:", k)
