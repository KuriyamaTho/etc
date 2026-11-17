def term(b1, q, n):
    if n == 1:
        return b1
    return term(b1, q, n - 1) * q


def progression_sum(b1, q, n):
    if n == 1:
        return b1
    return progression_sum(b1, q, n - 1) + term(b1, q, n)


b1 = float(input("Введите первый член прогрессии: "))
q = float(input("Введите знаменатель прогрессии: "))
n = int(input("Введите n: "))
print("а) n-й член прогрессии:", term(b1, q, n))
print("б) Сумма n первых членов:", progression_sum(b1, q, n))
