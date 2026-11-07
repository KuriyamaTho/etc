total = 0
area = 0
for i in range(1, 11):
    s = float(input(f"Район {i}, площадь посева пшеницы (га): "))
    u = float(input(f"Район {i}, средняя урожайность (ц/га): "))
    total = total + s * u
    area = area + s
print("Количество пшеницы, собранное в области (ц):", total)
print("Средняя урожайность по области (ц/га):", total / area)
