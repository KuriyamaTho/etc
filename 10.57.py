def is_symmetric(s, i, j):
    if i >= j:
        return True
    if s[i - 1] != s[j - 1]:
        return False
    return is_symmetric(s, i + 1, j - 1)


s = input("Введите строку s: ")
i = int(input("Введите i: "))
j = int(input("Введите j: "))
if is_symmetric(s, i, j):
    print("Да, часть строки симметрична")
else:
    print("Нет, часть строки не симметрична")
