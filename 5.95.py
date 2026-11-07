number = int(input("Введите натуральное число: "))
n = int(input("Введите n (количество последних цифр): "))
s = 0
for i in range(n):
    s = s + number % 10
    number = number // 10
print("Сумма последних n цифр =", s)
