n = int(input("Введите натуральное число с различными цифрами (не менее двух цифр): "))
mx1 = -1
mx2 = -1
mn1 = 10
mn2 = 10
p_mx1 = 0
p_mx2 = 0
p_mn1 = 0
p_mn2 = 0
i = 0
while n > 0:
    d = n % 10
    i = i + 1
    if d > mx1:
        mx2 = mx1
        p_mx2 = p_mx1
        mx1 = d
        p_mx1 = i
    elif d > mx2:
        mx2 = d
        p_mx2 = i
    if d < mn1:
        mn2 = mn1
        p_mn2 = p_mn1
        mn1 = d
        p_mn1 = i
    elif d < mn2:
        mn2 = d
        p_mn2 = i
    n = n // 10
print("а) Номера двух максимальных цифр от конца:", p_mx1, p_mx2)
print("а) Номера двух максимальных цифр от начала:", i - p_mx1 + 1, i - p_mx2 + 1)
print("б) Номера двух минимальных цифр от конца:", p_mn1, p_mn2)
print("б) Номера двух минимальных цифр от начала:", i - p_mn1 + 1, i - p_mn2 + 1)
