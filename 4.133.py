def days_in_month(month):
    if month == 2:
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


m = int(input("Введите порядковый номер месяца m: "))
n = int(input("Введите число n: "))

# а)
if n > 1:
    pn = n - 1
    pm = m
else:
    pm = m - 1
    pn = days_in_month(pm)
print("а) Предыдущий день:", pn, "число,", pm, "месяц")

# б)
if n < days_in_month(m):
    nn = n + 1
    nm = m
else:
    nn = 1
    nm = m + 1
print("б) Следующий день:", nn, "число,", nm, "месяц")
