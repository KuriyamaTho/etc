n = int(input("Введите натуральное число n: "))
equal = 0
zeros = 0
evens = 0
fives = 0
prev = int(input("Введите a1: "))
for i in range(2, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a == prev:
        equal = equal + 1
    if a == 0 and prev == 0:
        zeros = zeros + 1
    if a % 2 == 0 and prev % 2 == 0:
        evens = evens + 1
    if a % 10 == 5 and prev % 10 == 5:
        fives = fives + 1
    prev = a
print("а) Пар соседних равных чисел:", equal)
print("б) Пар соседних чисел, равных нулю:", zeros)
print("в) Пар соседних четных чисел:", evens)
print("г) Пар соседних чисел, оканчивающихся на цифру 5:", fives)
