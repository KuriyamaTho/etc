monitor = float(input("Стоимость монитора: "))
block = float(input("Стоимость системного блока: "))
keyboard = float(input("Стоимость клавиатуры: "))
mouse = float(input("Стоимость мыши: "))
n = int(input("Введите N (количество компьютеров): "))

one = monitor + block + keyboard + mouse
print("3 компьютера будут стоить", 3 * one)
print(n, "компьютеров будут стоить", n * one)
