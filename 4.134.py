def days_in_month(month, feb):
    if month == 2:
        return feb
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

def previous_day(g, m, n, feb):
    if n > 1:
        return g, m, n - 1
    if m > 1:
        return g, m - 1, days_in_month(m - 1, feb)
    return g - 1, 12, 31


def next_day(g, m, n, feb):
    if n < days_in_month(m, feb):
        return g, m, n + 1
    if m < 12:
        return g, m + 1, 1
    return g + 1, 1, 1


g = int(input("Введите год g: "))
m = int(input("Введите порядковый номер месяца m: "))
n = int(input("Введите число n: "))

if g % 4 == 0 and (g % 100 != 0 or g % 400 == 0):
    feb2 = 29
else:
    feb2 = 28

# 1) год не является високосным
y, mo, d = previous_day(g, m, n, 28)
print("1) а) Предыдущий день:", d, mo, y)
y, mo, d = next_day(g, m, n, 28)
print("1) б) Следующий день:", d, mo, y)

# 2) год может быть високосным
y, mo, d = previous_day(g, m, n, feb2)
print("2) а) Предыдущий день:", d, mo, y)
y, mo, d = next_day(g, m, n, feb2)
print("2) б) Следующий день:", d, mo, y)
