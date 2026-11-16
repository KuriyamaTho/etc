n = int(input("Введите n (n <= 27): "))
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a + b + c == n:
                print(a * 100 + b * 10 + c)
