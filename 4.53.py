a = float(input("Введите ребро кирпича a: "))
b = float(input("Введите ребро кирпича b: "))
c = float(input("Введите ребро кирпича c: "))
x = float(input("Введите сторону отверстия x: "))
y = float(input("Введите сторону отверстия y: "))
edges = sorted([a, b, c])
p = edges[0]
q = edges[1]
if (p <= x and q <= y) or (p <= y and q <= x):
    print("Да, кирпич пройдет в отверстие")
else:
    print("Нет, кирпич не пройдет в отверстие")
