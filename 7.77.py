count = 4
for a in (0, 8):
    if a > 8:
        result = 1
    elif a == 8:
        result = count + 1
    else:
        result = count
    print("При A =", a, "максимальных элементов стало:", result)
