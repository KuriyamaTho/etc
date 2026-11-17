def swap(x, y):
    return y, x


a = input("Введите a: ")
b = input("Введите b: ")
c = input("Введите c: ")
d = input("Введите d: ")
a, b = swap(a, b)
c, d = swap(c, d)
print("a =", a, "b =", b, "c =", c, "d =", d)
