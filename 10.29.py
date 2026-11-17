def count_letter(s, c):
    k = 0
    for ch in s:
        if ch == c:
            k = k + 1
    return k


c = input("Введите букву: ")
s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
s3 = input("Введите третье предложение: ")
print("Общее количество заданной буквы:", count_letter(s1, c) + count_letter(s2, c) + count_letter(s3, c))
