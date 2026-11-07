# а)
y = 20
for year in range(2, 9):
    y = y * 1.02
    print("а) Урожайность за", year, "год:", f"{y:.3f}", "ц/га")

# б)
area = 100
for year in range(2, 8):
    area = area * 1.05
    if year >= 4:
        print("б) Площадь участка в", year, "год:", f"{area:.3f}", "га")

# в)
area = 100
y = 20
total = 0
for year in range(1, 7):
    total = total + area * y
    area = area * 1.05
    y = y * 1.02
print("в) Урожай за первые шесть лет:", f"{total:.2f}", "ц")
