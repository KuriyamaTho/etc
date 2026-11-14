found = False
i = 0
while i < 30 and not found:
    power = float(input(f"Введите мощность двигателя модели {i + 1} (л. с.): "))
    i = i + 1
    found = power > 200
if found:
    print("Да, есть модель с мощностью двигателя более 200 л. с.")
else:
    print("Нет, такой модели нет")
