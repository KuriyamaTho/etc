# а)
y = 20
year = 1
while y <= 22:
    y = y * 1.02
    year = year + 1
print("а) Урожайность превысит 22 ц/га в год номер", year)

# б)
area = 100
year = 1
while area <= 120:
    area = area * 1.05
    year = year + 1
print("б) Площадь участка станет больше 120 га в год номер", year)

# в)
area = 100
y = 20
total = area * y
year = 1
while total <= 800:
    area = area * 1.05
    y = y * 1.02
    total = total + area * y
    year = year + 1
print("в) Общий урожай превысит 800 ц в год номер", year)
