a = float(input("Введите a (рублей): "))
total = 0
best_product = 0
best_product_sum = -1
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
for product in range(1, 6):
    price = float(input(f"Вид товара {product}, стоимость одной штуки: "))
    product_sum = 0
    for day in range(1, 7):
        q = int(input(f"Вид товара {product}, день {day}, продано штук: "))
        income = price * q
        product_sum = product_sum + income
        if day == 1:
            d1 = d1 + income
        elif day == 2:
            d2 = d2 + income
        elif day == 3:
            d3 = d3 + income
        elif day == 4:
            d4 = d4 + income
        elif day == 5:
            d5 = d5 + income
        else:
            d6 = d6 + income
    print("а) Доход от продажи товара вида", product, ":", product_sum)
    total = total + product_sum
    if product_sum > best_product_sum:
        best_product_sum = product_sum
        best_product = product
print("б) Доход за день 1:", d1)
print("б) Доход за день 2:", d2)
print("б) Доход за день 3:", d3)
print("б) Доход за день 4:", d4)
print("б) Доход за день 5:", d5)
print("б) Доход за день 6:", d6)
print("в) Общий доход магазина за 6 дней:", total)
print("г) Максимальный общий доход получен по виду товара:", best_product)
best_day = 1
best_day_sum = d1
if d2 > best_day_sum:
    best_day_sum = d2
    best_day = 2
if d3 > best_day_sum:
    best_day_sum = d3
    best_day = 3
if d4 > best_day_sum:
    best_day_sum = d4
    best_day = 4
if d5 > best_day_sum:
    best_day_sum = d5
    best_day = 5
if d6 > best_day_sum:
    best_day_sum = d6
    best_day = 6
print("д) Максимальный общий доход получен в день:", best_day)
k = 0
if d1 > a:
    k = k + 1
if d2 > a:
    k = k + 1
if d3 > a:
    k = k + 1
if d4 > a:
    k = k + 1
if d5 > a:
    k = k + 1
if d6 > a:
    k = k + 1
print("е) Количество дней, в которые общий доход превысил a рублей:", k)
