n = int(input("Введите количество покупателей n: "))
total = 0
min_t = 0
pos = 0
for i in range(1, n + 1):
    t = float(input(f"Введите время обслуживания покупателя {i}: "))
    total = total + t
    print(f"c{i} =", total)
    if i == 1 or t < min_t:
        min_t = t
        pos = i
print("Самое малое время обслуживания потребовалось покупателю номер:", pos)
