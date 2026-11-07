import math

# а)
a = float(input("а) Введите a: "))
x = math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)
print("x =", x)

# б)
x = float(input("б) Введите x: "))
y = math.sin((3.2 + math.sqrt(1 + x)) / abs(5 * x))
print("y =", y)
