total = 0
m1 = 0
m2 = 0
m3 = 0
for worker in range(1, 13):
    s = 0
    for month in range(1, 4):
        z = float(input(f"Работник {worker}, зарплата за месяц {month}: "))
        s = s + z
        if month == 1:
            m1 = m1 + z
        elif month == 2:
            m2 = m2 + z
        else:
            m3 = m3 + z
    print("б) Зарплата работника", worker, "за квартал:", s)
    total = total + s
print("а) Общая сумма, выплаченная за квартал всем работникам:", total)
print("в) Общая зарплата за месяц 1:", m1)
print("в) Общая зарплата за месяц 2:", m2)
print("в) Общая зарплата за месяц 3:", m3)
