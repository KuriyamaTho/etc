a = float(input("Введите вещественное число a: "))
print("Последовательность бесконечна, рассматриваются ее первые 1000 членов.")
k = 1
while k <= 1000:
    if k == 1:
        term = 1
    else:
        term = 1 + 1 / k
    if term < a:
        print(term)
    k = k + 1
