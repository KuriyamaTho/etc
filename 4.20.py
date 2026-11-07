m = int(input("Введите m: "))
n = int(input("Введите n: "))
if m % n == 0:
    print(m // n)
else:
    print(m, "на", n, "нацело не делится")
