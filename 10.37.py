w = int(input("Введите ширину прямоугольника: "))
h = int(input("Введите высоту прямоугольника: "))

# 1)
print("1)")
for i in range(h):
    for j in range(w):
        print("*", end="")
    print()


# 2)
def draw_line(n):
    for i in range(n):
        print("*", end="")
    print()


print("2)")
for i in range(h):
    draw_line(w)
