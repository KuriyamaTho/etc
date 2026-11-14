# а)
s = 1000
month = 1
inc = s * 0.02
while inc <= 30:
    s = s + inc
    month = month + 1
    inc = s * 0.02
print("а) Ежемесячное увеличение вклада превысит 30 руб. за месяц номер", month)

# б)
s = 1000
months = 0
while s <= 1200:
    s = s * 1.02
    months = months + 1
print("б) Вклад превысит 1200 руб. через месяцев:", months)
