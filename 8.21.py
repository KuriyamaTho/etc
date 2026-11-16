mx1 = -1
mx2 = -1
mx3 = -1
d1 = 0
d2 = 0
d3 = 0
for day in range(1, 11):
    best = -1
    best_shop = 0
    for shop in range(1, 4):
        x = float(input(f"День {day}, магазин {shop}, доход: "))
        if x > best:
            best = x
            best_shop = shop
        if shop == 1 and x > mx1:
            mx1 = x
            d1 = day
        if shop == 2 and x > mx2:
            mx2 = x
            d2 = day
        if shop == 3 and x > mx3:
            mx3 = x
            d3 = day
    print("б) В день", day, "максимальный доход получил магазин", best_shop)
print("а) Магазин 1 получил максимальный доход числа:", d1)
print("а) Магазин 2 получил максимальный доход числа:", d2)
print("а) Магазин 3 получил максимальный доход числа:", d3)
