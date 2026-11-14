a = int(input("Введите числитель a: "))
b = int(input("Введите знаменатель b: "))
x = a
y = b
while y != 0:
    r = x % y
    x = y
    y = r
p = a // x
q = b // x
print("Сокращенная дробь:", f"{p}/{q}")
