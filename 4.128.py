n = int(input("Введите возраст в месяцах n (1-1188): "))
y = n // 12
m = n % 12
if 11 <= y % 100 <= 14:
    year = "лет"
elif y % 10 == 1:
    year = "год"
elif 2 <= y % 10 <= 4:
    year = "года"
else:
    year = "лет"
if 11 <= m % 100 <= 14:
    month = "месяцев"
elif m % 10 == 1:
    month = "месяц"
elif 2 <= m % 10 <= 4:
    month = "месяца"
else:
    month = "месяцев"
if y == 0:
    print(m, month)
elif m == 0:
    print(y, year, "ровно")
else:
    print(y, year, m, month)
