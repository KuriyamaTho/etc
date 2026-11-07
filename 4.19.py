x1 = float(input("Первый прямоугольник, левый нижний угол, x: "))
y1 = float(input("Первый прямоугольник, левый нижний угол, y: "))
w1 = float(input("Первый прямоугольник, длина стороны по x: "))
h1 = float(input("Первый прямоугольник, длина стороны по y: "))
x2 = float(input("Второй прямоугольник, левый нижний угол, x: "))
y2 = float(input("Второй прямоугольник, левый нижний угол, y: "))
w2 = float(input("Второй прямоугольник, длина стороны по x: "))
h2 = float(input("Второй прямоугольник, длина стороны по y: "))

left = x1
if x2 < left:
    left = x2
bottom = y1
if y2 < bottom:
    bottom = y2
right = x1 + w1
if x2 + w2 > right:
    right = x2 + w2
top = y1 + h1
if y2 + h2 > top:
    top = y2 + h2
print("Левый нижний угол: (", left, ",", bottom, ")")
print("Правый верхний угол: (", right, ",", top, ")")
