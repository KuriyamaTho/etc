n = int(input("Введите натуральное число: "))

# а)
m = n
mx = 0
while m > 0:
    if m % 10 > mx:
        mx = m % 10
    m = m // 10
print("а) Максимальная цифра:", mx)

# б)
m = n
mn = 9
while m > 0:
    if m % 10 < mn:
        mn = m % 10
    m = m // 10
print("б) Минимальная цифра:", mn)
