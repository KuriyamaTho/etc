n = int(input("Введите натуральное число n (n > 9): "))

# а)
m = n
k = 0
while m > 0:
    k = k + 1
    m = m // 10
m = n
i = 0
while i < k - 2:
    m = m // 10
    i = i + 1
print("а) Вторая цифра:", m % 10)

# б)
m = n
while m >= 100:
    m = m // 10
print("б) Вторая цифра:", m % 10)
