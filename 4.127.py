n = int(input("Введите стоимость в копейках n (1-9999): "))
r = n // 100
k = n % 100
if 11 <= r % 100 <= 14:
    rub = "рублей"
elif r % 10 == 1:
    rub = "рубль"
elif 2 <= r % 10 <= 4:
    rub = "рубля"
else:
    rub = "рублей"
if 11 <= k % 100 <= 14:
    kop = "копеек"
elif k % 10 == 1:
    kop = "копейка"
elif 2 <= k % 10 <= 4:
    kop = "копейки"
else:
    kop = "копеек"
if r == 0:
    print(k, kop)
elif k == 0:
    print(r, rub, "ровно")
else:
    print(r, rub, k, kop)
