x = float(input("Введите x: "))

# а)
if x <= -1:
    y = 0
elif x < 0:
    y = x + 1
else:
    y = 1
print("а) y =", y)

# б)
if x <= -1:
    y = 1
elif x < 1:
    y = -x
else:
    y = -1
print("б) y =", y)

# в)
if x <= -1 or x >= 1:
    y = 1
else:
    y = (1 + abs(x)) / 2
print("в) y =", y)
