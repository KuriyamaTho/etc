import math

for i in range(8):
    x = 3 + 0.2 * i
    angle = math.degrees(math.acos(x / 4.5))
    print(f"Нижний конец на расстоянии {x:.1f} м от стены: угол {angle:.2f} градусов")
