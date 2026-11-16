n = int(input("Введите натуральное число n: "))
p = int(input("Введите p: "))
k = int(input("Введите k: "))
more = 0
five = 0
mult = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a > p:
        more = more + 1
    if a % 10 == 5:
        five = five + 1
    if a % k == 0:
        mult = mult + 1
print("а) Количество чисел, больших p:", more)
print("б) Количество чисел, оканчивающихся цифрой 5:", five)
print("в) Количество чисел, кратных k:", mult)
