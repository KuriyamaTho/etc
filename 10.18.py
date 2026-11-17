def digit_sum(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
if digit_sum(a) > digit_sum(b):
    print("Сумма цифр больше в первом числе")
elif digit_sum(b) > digit_sum(a):
    print("Сумма цифр больше во втором числе")
else:
    print("Суммы цифр равны")
