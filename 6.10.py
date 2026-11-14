n = float(input("Введите число n: "))

# а)
k = 1
while k * k <= n:
    print(k)
    k = k + 1

# б)
k = 1
while k * k <= n:
    k = k + 1
print("б) Первое натуральное число, квадрат которого больше n:", k)
