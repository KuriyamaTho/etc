rate = float(input("Введите курс доллара (руб.): "))
for k in range(1, 21):
    print(k, "долл. -", f"{k * rate:.2f}", "руб.")
