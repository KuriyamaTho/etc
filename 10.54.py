def to_binary(n):
    if n > 0:
        to_binary(n // 2)
        print(n % 2, end="")


n = int(input("Введите натуральное число: "))
to_binary(n)
print()
