s1 = 0
s2 = 0
for i in range(1, 9):
    a = float(input(f"Первый набор, стоимость предмета {i}: "))
    s1 = s1 + a
for i in range(1, 9):
    b = float(input(f"Второй набор, стоимость предмета {i}: "))
    s2 = s2 + b
if s1 < s2:
    print("Более дешевый первый набор")
elif s2 < s1:
    print("Более дешевый второй набор")
else:
    print("Наборы стоят одинаково")
