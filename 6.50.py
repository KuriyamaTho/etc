n = int(input("Введите натуральное число: "))
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
k = int(input("Введите k: "))

m = n
has_a = False
has_b = False
count_a = 0
while m > 0:
    d = m % 10
    if d == a:
        has_a = True
        count_a = count_a + 1
    if d == b:
        has_b = True
    m = m // 10

# а)
if has_a:
    print("а) Да, цифра a есть в числе")
else:
    print("а) Нет, цифры a в числе нет")

# б)
if not has_b:
    print("б) Да, цифры b в числе нет")
else:
    print("б) Нет, цифра b есть в числе")

# в)
if count_a > k:
    print("в) Да, цифра a встречается более k раз")
else:
    print("в) Нет, цифра a встречается не более k раз")

# г)
if has_a and has_b:
    print("г) Да, в числе есть цифры a и b")
else:
    print("г) Нет, в числе нет обеих цифр a и b")
