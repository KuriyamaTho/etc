x1 = float(input("Первый прямоугольник, левый нижний угол, x: "))
y1 = float(input("Первый прямоугольник, левый нижний угол, y: "))
x2 = float(input("Первый прямоугольник, правый верхний угол, x: "))
y2 = float(input("Первый прямоугольник, правый верхний угол, y: "))
x3 = float(input("Второй прямоугольник, левый нижний угол, x: "))
y3 = float(input("Второй прямоугольник, левый нижний угол, y: "))
x4 = float(input("Второй прямоугольник, правый верхний угол, x: "))
y4 = float(input("Второй прямоугольник, правый верхний угол, y: "))

left = x1
if x3 < left:
    left = x3
bottom = y1
if y3 < bottom:
    bottom = y3
right = x2
if x4 > right:
    right = x4
top = y2
if y4 > top:
    top = y4
print("Левый нижний угол: (", left, ",", bottom, ")")
print("Правый верхний угол: (", right, ",", top, ")")
