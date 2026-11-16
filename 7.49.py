n = int(input("Введите натуральное число n: "))
first = 0
last = 0
for i in range(1, n + 1):
    a = int(input(f"Введите a{i}: "))
    if a == 10:
        if first == 0:
            first = i
        last = i
print("а) Номер последнего числа, равного 10:", last)
print("б) Номер первого числа, равного 10:", first)
