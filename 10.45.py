def term(a1, d, n):
    if n == 1:
        return a1
    return term(a1, d, n - 1) + d


def progression_sum(a1, d, n):
    if n == 1:
        return a1
    return progression_sum(a1, d, n - 1) + term(a1, d, n)


a1 = float(input("Введите первый член прогрессии: "))
d = float(input("Введите разность прогрессии: "))
n = int(input("Введите n: "))
print("а) n-й член прогрессии:", term(a1, d, n))
print("б) Сумма n первых членов:", progression_sum(a1, d, n))
