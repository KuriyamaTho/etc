mn = 10 ** 9
mn_row = 10 ** 9
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for parallel in range(1, 12):
    s = 0
    for cls in range(1, 5):
        k = int(input(f"Параллель {parallel}, класс {cls}, число учеников: "))
        s = s + k
        if k < mn:
            mn = k
        if cls == 1:
            c1 = c1 + k
        elif cls == 2:
            c2 = c2 + k
        elif cls == 3:
            c3 = c3 + k
        else:
            c4 = c4 + k
    if s < mn_row:
        mn_row = s
mn_col = c1
if c2 < mn_col:
    mn_col = c2
if c3 < mn_col:
    mn_col = c3
if c4 < mn_col:
    mn_col = c4
print("а) Учеников в самом малочисленном классе школы:", mn)
print("б) Минимальное общее количество учеников в параллели:", mn_row)
print("в) Минимальное общее количество учеников в классах с одной буквой:", mn_col)
