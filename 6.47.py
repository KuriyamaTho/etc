n = int(input("Введите натуральное число: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
k0 = int(input("Введите k: "))
mm = int(input("Введите m: "))

m = n
s = 0
p = 1
k = 0
while m > 0:
    d = m % 10
    s = s + d
    p = p * d
    k = k + 1
    first = d
    m = m // 10

# а)
if s < a:
    print("а) Да, сумма цифр меньше a")
else:
    print("а) Нет, сумма цифр не меньше a")

# б)
if p > b:
    print("б) Да, произведение цифр больше b")
else:
    print("б) Нет, произведение цифр не больше b")

# в)
if k == k0:
    print("в) Да, число k-значное")
else:
    print("в) Нет, число не k-значное")

# г)
if first > mm:
    print("г) Да, первая цифра превышает m")
else:
    print("г) Нет, первая цифра не превышает m")
