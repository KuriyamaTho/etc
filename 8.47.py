v = int(input("Введите вес v, г: "))
count = 0
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                for i in range(2):
                                    for j in range(2):
                                        s = (100 * a + 200 * b + 300 * c + 500 * d + 1000 * e
                                             + 1200 * f + 1400 * g + 1500 * h + 2000 * i + 3000 * j)
                                        if s == v:
                                            count = count + 1
print("Количество способов:", count)
