k = int(input("Введите k (1 <= k <= 180): "))
number = 9 + (k + 1) // 2
if k % 2 == 0:
    digit = number % 10
else:
    digit = number // 10
print("k-я цифра:", digit)
