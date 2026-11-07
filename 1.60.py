# а)
a = float(input("а) Введите a: "))
b = float(input("а) Введите b: "))
c = float(input("а) Введите c: "))
t = a
a = b
b = c
c = t
print("а) a =", a, "b =", b, "c =", c)

# б)
a = float(input("б) Введите a: "))
b = float(input("б) Введите b: "))
c = float(input("б) Введите c: "))
t = c
c = b
b = a
a = t
print("б) a =", a, "b =", b, "c =", c)
