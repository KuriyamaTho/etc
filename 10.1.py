import math


def f(t):
    return (math.sqrt(t) + t) / 2


def g(a, b):
    return (a + math.sqrt(a)) / (b + math.sqrt(b))


def h(a, b):
    return (a + math.sqrt(b)) / (b + math.sqrt(a))


# а)
x = f(6) + f(13) + f(21)
print("а) x =", x)

# б)
x = g(5, 7) + g(12, 8) + g(31, 2)
print("б) x =", x)

# в)
x = h(15, 8) + h(6, 12) + h(7, 21)
print("в) x =", x)

# г)
x = h(13, 7) + h(15, 12) + h(32, 21)
print("г) x =", x)
