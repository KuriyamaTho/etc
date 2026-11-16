inf = float("inf")
t1 = -inf
t2 = -inf
t3 = -inf
for i in range(1, 21):
    p = int(input(f"Введите количество очков команды {i}: "))
    if p > t1:
        t3 = t2
        t2 = t1
        t1 = p
    elif p > t2:
        t3 = t2
        t2 = p
    elif p > t3:
        t3 = p
print("Сумма очков команд, занявших три первых места:", t1 + t2 + t3)
