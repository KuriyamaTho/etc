# а)
s = 1000
for month in range(1, 11):
    inc = s * 0.02
    s = s + inc
    print("а) Прирост за", month, "месяц:", f"{inc:.2f}", "руб.")

# б)
s = 1000
for month in range(1, 13):
    s = s * 1.02
    if month >= 3:
        print("б) Сумма вклада через", month, "месяцев:", f"{s:.2f}", "руб.")
