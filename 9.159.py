a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
both = a + b
result = []
for ch in both:
    k = 0
    for c in both:
        if c == ch:
            k = k + 1
    if k == 1:
        result.append(ch)
print(" ".join(result))
