def read_and_print():
    x = int(input("Введите число (0 - конец последовательности): "))
    if x != 0:
        read_and_print()
        print(x)


read_and_print()
