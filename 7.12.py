s = 0
for x in range(31, 100):
    if x % 3 == 0 and (x % 10 == 2 or x % 10 == 4 or x % 10 == 8):
        s = s + x
print("Сумма =", s)
