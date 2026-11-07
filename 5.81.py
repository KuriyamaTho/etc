x = int(input("Введите натуральное число x: "))
y = int(input("Введите натуральное число y: "))

# 1-й способ
p = 0
for i in range(x):
    p = p + y
print("1-й способ:", p)

# 2-й способ
p = 0
for i in range(y):
    p = p + x
print("2-й способ:", p)
