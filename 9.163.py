a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = input("Введите третье слово: ")
all_letters = a + b + c
result = []
for ch in all_letters:
    k = 0
    for x in all_letters:
        if x == ch:
            k = k + 1
    if k == 1:
        result.append(ch)
print(" ".join(result))
