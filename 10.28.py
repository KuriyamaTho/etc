def count_n(s):
    k = 0
    for ch in s:
        if ch == "н":
            k = k + 1
    return k


s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
print("Общее количество букв н:", count_n(s1) + count_n(s2))
