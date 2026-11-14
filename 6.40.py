n = int(input("Введите натуральное число n (n > 99): "))

# а)
m = n
k = 0
while m > 0:
    k = k + 1
    m = m // 10
m = n
i = 0
while i < k - 3:
    m = m // 10
    i = i + 1
print("а) Третья цифра:", m % 10)

# б)
m = n
while m >= 1000:
    m = m // 10
print("б) Третья цифра:", m % 10)
