def is_palindrome(n):
    m = n
    r = 0
    while m > 0:
        r = r * 10 + m % 10
        m = m // 10
    return r == n


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
if is_palindrome(a) or is_palindrome(b):
    print("Да, хотя бы одно из чисел является палиндромом")
else:
    print("Нет, ни одно из чисел не является палиндромом")
