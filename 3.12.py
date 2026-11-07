x = 1
y = -1
print("а)", x ** 2 - y ** 2 <= 0)

x = 2
y = -2
print("б)", (x >= 2) or (y ** 2 != 4))

x = 2
y = 2
print("в)", (x >= 0) and (y ** 2 > 4))

x = 1
y = 2
print("г)", (x * y != 4) and (y > x))

x = 2
y = 1
print("д)", (x * y != 0) or (y < x))

x = 1
y = 2
print("е)", (not (x * y < 1)) and (y > x))

x = 2
y = 1
print("ж)", (not (x * y < 0)) or (y > x))
