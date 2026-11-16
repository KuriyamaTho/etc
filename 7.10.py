n = int(input("Введите n (цифра от 1 до 9): "))
for x in range(10, 100):
    if x % n == 0 or x // 10 == n or x % 10 == n:
        print(x)
