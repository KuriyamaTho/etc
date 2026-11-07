# а)
d = 10
for day in range(2, 11):
    d = d * 1.1
    print("а) Пробег за", day, "день:", f"{d:.3f}", "км")

# б)
d = 10
total = 0
for day in range(1, 8):
    total = total + d
    d = d * 1.1
print("б) Суммарный путь за первые 7 дней:", f"{total:.3f}", "км")
