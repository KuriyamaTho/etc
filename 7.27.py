k = 0
for i in range(1, 9):
    b = float(input(f"Введите b{i}: "))
    if b < 100:
        k = k + 1
print("Количество чисел, меньших 100:", k)
