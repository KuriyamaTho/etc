def print_reversed(n):
    if n > 0:
        print(n % 10, end="")
        print_reversed(n // 10)


n = int(input("Введите натуральное число: "))
print_reversed(n)
print()
