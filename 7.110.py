i = 0
dry = 0
while i < 31 and dry <= 10:
    x = float(input(f"Введите количество осадков за {i + 1} марта: "))
    i = i + 1
    if x == 0:
        dry = dry + 1
if dry == 10:
    print("Да, осадков не было ровно 10 дней")
else:
    print("Нет, осадков не было не 10 дней")
