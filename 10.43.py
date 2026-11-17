def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def digit_count(n):
    if n < 10:
        return 1
    return 1 + digit_count(n // 10)


n = int(input("Введите натуральное число: "))
print("а) Сумма цифр:", digit_sum(n))
print("б) Количество цифр:", digit_count(n))
