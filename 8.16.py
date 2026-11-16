mx = 0
best = 0
best_worker = 0
m1 = 0
m2 = 0
m3 = 0
for worker in range(1, 13):
    s = 0
    for month in range(1, 4):
        z = float(input(f"Работник {worker}, зарплата за месяц {month}: "))
        s = s + z
        if z > mx:
            mx = z
        if month == 1:
            m1 = m1 + z
        elif month == 2:
            m2 = m2 + z
        else:
            m3 = m3 + z
    if s > best:
        best = s
        best_worker = worker
if m1 >= m2 and m1 >= m3:
    best_month = 1
elif m2 >= m3:
    best_month = 2
else:
    best_month = 3
print("а) Максимальная зарплата в таблице:", mx)
print("б) Работник с наибольшей суммой за квартал:", best_worker)
print("в) Месяц с максимальной общей зарплатой:", best_month)
