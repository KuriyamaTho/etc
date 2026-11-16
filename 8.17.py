mx1 = -1
mx2 = -1
mx3 = -1
w1 = 0
w2 = 0
w3 = 0
for worker in range(1, 13):
    best = -1
    best_month = 0
    for month in range(1, 4):
        z = float(input(f"Работник {worker}, зарплата за месяц {month}: "))
        if z > best:
            best = z
            best_month = month
        if month == 1 and z > mx1:
            mx1 = z
            w1 = worker
        if month == 2 and z > mx2:
            mx2 = z
            w2 = worker
        if month == 3 and z > mx3:
            mx3 = z
            w3 = worker
    print("а) Работник", worker, "получил наибольшую зарплату в месяце", best_month)
print("б) В месяце 1 наибольшую зарплату получил работник", w1)
print("б) В месяце 2 наибольшую зарплату получил работник", w2)
print("б) В месяце 3 наибольшую зарплату получил работник", w3)
