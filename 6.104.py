a = 425
b = 131
while b != 0:
    print("Квадратов со стороной", b, ":", a // b)
    r = a % b
    a = b
    b = r
