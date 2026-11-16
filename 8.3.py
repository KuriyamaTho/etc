# а)
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

# б)
for i in range(5):
    for j in range(5 - i):
        print(5 + i, end=" ")
    print()

# в)
for i in range(1, 6):
    for j in range(i):
        print(10 * i, end=" ")
    print()

# г)
for i in range(1, 6):
    for j in range(6 - i):
        print(5 * i, end=" ")
    print()
