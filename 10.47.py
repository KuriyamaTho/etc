def fibonacci(k):
    if k <= 2:
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)


k = int(input("Введите номер члена k: "))
print(f"f{k} =", fibonacci(k))
