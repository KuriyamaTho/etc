h = int(input("Введите h (0 < h <= 23): "))
m = int(input("Введите m (0 <= m <= 59): "))
s = int(input("Введите s (0 <= s <= 59): "))
angle = (h * 3600 + m * 60 + s) / 120
print("Угол (в градусах):", angle)
