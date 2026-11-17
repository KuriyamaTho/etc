def days_in_month(month, year):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def previous_day(g, m, n):
    if n > 1:
        return g, m, n - 1
    if m > 1:
        return g, m - 1, days_in_month(m - 1, g)
    return g - 1, 12, 31


def next_day(g, m, n):
    if n < days_in_month(m, g):
        return g, m, n + 1
    if m < 12:
        return g, m + 1, 1
    return g + 1, 1, 1


g = int(input("Введите год g: "))
m = int(input("Введите порядковый номер месяца m: "))
n = int(input("Введите число n: "))
y, mo, d = previous_day(g, m, n)
print("а) Предыдущий день:", d, mo, y)
y, mo, d = next_day(g, m, n)
print("б) Следующий день:", d, mo, y)
