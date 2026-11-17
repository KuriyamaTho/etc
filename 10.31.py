def last_position(s, c):
    pos = 0
    for i in range(len(s)):
        if s[i] == c:
            pos = i + 1
    return pos


s1 = input("Введите первое предложение с буквой ш: ")
s2 = input("Введите второе предложение с буквой ш: ")
p1 = last_position(s1, "ш")
p2 = last_position(s2, "ш")
if p1 > p2:
    print("Буква ш имеет больший номер в первом предложении:", p1)
elif p2 > p1:
    print("Буква ш имеет больший номер во втором предложении:", p2)
else:
    print("Номера буквы ш одинаковы:", p1)
