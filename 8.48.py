n = int(input("Введите n (n < 100): "))

# а)
count = 0
for tens in range(n // 10 + 1):
    for fives in range(n // 5 + 1):
        for twos in range(n // 2 + 1):
            if 10 * tens + 5 * fives + 2 * twos <= n:
                count = count + 1
print("а) Число способов выплаты:", count)

# б)
print("б) Все способы выплаты:")
for tens in range(n // 10 + 1):
    for fives in range(n // 5 + 1):
        for twos in range(n // 2 + 1):
            rest = n - 10 * tens - 5 * fives - 2 * twos
            if rest >= 0:
                print("10 руб.:", tens, ", 5 руб.:", fives, ", 2 руб.:", twos, ", 1 руб.:", rest)
