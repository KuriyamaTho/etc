n = int(input("Введите количество квартир: "))
k = int(input("Введите число жильцов квартиры 1: "))
mx = k
count = 1
for i in range(2, n + 1):
    k = int(input(f"Введите число жильцов квартиры {i}: "))
    if k > mx:
        mx = k
        count = 1
    elif k == mx:
        count = count + 1
print("Больше всего жильцов проживает в таком числе квартир:", count)
