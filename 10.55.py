def to_base(n, base):
    if n > 0:
        to_base(n // base, base)
        print("0123456789ABCDEF"[n % base], end="")


n = int(input("Введите натуральное число: "))
base = int(input("Введите N (2 <= N <= 16): "))
to_base(n, base)
print()
