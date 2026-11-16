# а)
for i in range(1, 6):
    for j in range(i):
        print(i - 1 - j, end=" ")
    print()

# б)
for i in range(1, 6):
    print(5 + i, end=" ")
    for j in range(5 - i):
        print(6 - i - j, end=" ")
    print()

# в)
for i in range(1, 6):
    for j in range(i):
        print(31 - i + j, end=" ")
    print()

# г)
for i in range(1, 6):
    for j in range(6 - i):
        print(21 - i + j, end=" ")
    print()
