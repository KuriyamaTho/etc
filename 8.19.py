m1 = 10 ** 9
m2 = 10 ** 9
m3 = 10 ** 9
m4 = 10 ** 9
for parallel in range(1, 12):
    mn = 10 ** 9
    for cls in range(1, 5):
        k = int(input(f"Параллель {parallel}, класс {cls}, число учеников: "))
        if k < mn:
            mn = k
        if cls == 1 and k < m1:
            m1 = k
        if cls == 2 and k < m2:
            m2 = k
        if cls == 3 and k < m3:
            m3 = k
        if cls == 4 and k < m4:
            m4 = k
    print("а) В параллели", parallel, "самый малочисленный класс:", mn)
print("б) Самый малочисленный класс А:", m1)
print("б) Самый малочисленный класс Б:", m2)
print("б) Самый малочисленный класс В:", m3)
print("б) Самый малочисленный класс Г:", m4)
