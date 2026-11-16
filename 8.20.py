s1 = 0
s2 = 0
s3 = 0
best_day = 0
best_day_sum = -1
best_shop = 0
best_shop_day = 0
best_single = -1
for day in range(1, 11):
    day_sum = 0
    for shop in range(1, 4):
        x = float(input(f"День {day}, магазин {shop}, доход: "))
        day_sum = day_sum + x
        if shop == 1:
            s1 = s1 + x
        elif shop == 2:
            s2 = s2 + x
        else:
            s3 = s3 + x
        if x > best_single:
            best_single = x
            best_shop = shop
            best_shop_day = day
    if day_sum > best_day_sum:
        best_day_sum = day_sum
        best_day = day
if s1 >= s2 and s1 >= s3:
    top_shop = 1
elif s2 >= s3:
    top_shop = 2
else:
    top_shop = 3
print("а) Максимальный общий доход за 10 дней получил магазин:", top_shop)
print("б) Максимальный общий доход фирма получила числа:", best_day)
print("в) Максимальный доход за день получил магазин", best_shop, "числа", best_shop_day)
