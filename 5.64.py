people = 0
area = 0
for i in range(1, 13):
    p = float(input(f"Район {i}, количество жителей (тыс. чел.): "))
    s = float(input(f"Район {i}, площадь (км2): "))
    people = people + p
    area = area + s
print("Средняя плотность населения по области (тыс. чел./км2):", people / area)
