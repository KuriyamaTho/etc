n = int(input("Введите натуральное число: "))
k0 = float(input("Введите k: "))
b = float(input("Введите b: "))
x = int(input("Введите цифру x: "))
y = int(input("Введите цифру y: "))
a = float(input("Введите a: "))
m0 = float(input("Введите m: "))
n0 = int(input("Введите n (делитель): "))
b0 = int(input("Введите b (делитель) для пункта г): "))

m = n
s = 0
p = 1
k = 0
last = n % 10
while m > 0:
    d = m % 10
    s = s + d
    p = p * d
    k = k + 1
    first = d
    m = m // 10

# а)
if s > k0 and n % 2 == 0:
    print("а) Да")
else:
    print("а) Нет")

# б)
if k % 2 == 0 and n <= b:
    print("б) Да")
else:
    print("б) Нет")

# в)
if first == x and last == y:
    print("в) Да")
else:
    print("в) Нет")

# г)
if p < a and n % b0 == 0:
    print("г) Да")
else:
    print("г) Нет")

# д)
if s > m0 and n % n0 == 0:
    print("д) Да")
else:
    print("д) Нет")
