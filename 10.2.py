import math


def f(t):
    return (t + math.sin(t)) / 3


def g(a, b):
    return (a + math.sin(a)) / (b + math.sin(b))


def h(p, q, r):
    return (p + math.sin(q)) / (q + math.sin(r))


# а)
y = f(1) + f(5) + f(3)
print("а) y =", y)

# б)
y = g(2, 5) + g(6, 3) + g(1, 4)
print("б) y =", y)

# в)
y = h(1, 4, 1) + h(7, 5, 7) + h(3, 2, 3)
print("в) y =", y)

# г)
y = h(2, 3, 2) + h(1, 5, 1) + h(4, 7, 3)
print("г) y =", y)
