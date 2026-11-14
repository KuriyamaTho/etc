import math

a = int(input("Введите a: "))
b = int(input("Введите b (a > b): "))

# а)
i = a
while i >= b:
    print(math.sqrt(i))
    i = i - 1

# б)
i = a
while True:
    print(math.sqrt(i))
    i = i - 1
    if i < b:
        break
