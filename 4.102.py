x = float(input("Введите x (x не равно 0): "))
y = float(input("Введите y (y не равно 0): "))
if x > 0 and y > 0:
    print("Точка принадлежит I четверти")
elif x < 0 and y > 0:
    print("Точка принадлежит II четверти")
elif x < 0 and y < 0:
    print("Точка принадлежит III четверти")
else:
    print("Точка принадлежит IV четверти")
