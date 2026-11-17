def share(s, c):
    k = 0
    for ch in s:
        if ch == c:
            k = k + 1
    return k / len(s) * 100


s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
if share(s1, "б") > share(s2, "б"):
    print("Доля буквы б больше в первом предложении")
elif share(s2, "б") > share(s1, "б"):
    print("Доля буквы б больше во втором предложении")
else:
    print("Доли буквы б в предложениях равны")
