for x in range(1, 31):
    for y in range(x, 31):
        for k in range(1, 31):
            if x * x + y * y == k * k:
                print(x, y, k)
