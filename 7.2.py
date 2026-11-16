a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
for i in range(a, b + 1):
    if i % c == 0:
        print(i)
