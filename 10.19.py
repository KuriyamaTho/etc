def digit_count(n):
    k = 0
    while n > 0:
        k = k + 1
        n = n // 10
    return k


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
if digit_count(a) > digit_count(b):
    print("Цифр больше в первом числе")
elif digit_count(b) > digit_count(a):
    print("Цифр больше во втором числе")
else:
    print("Количество цифр одинаково")
