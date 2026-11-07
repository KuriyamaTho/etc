x = float(input("Введите x: "))
if x <= 0:
    f = 0
elif x <= 1:
    f = x
else:
    f = x ** 2
print("f(x) =", f)
