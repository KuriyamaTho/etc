def is_even(n):
    return n % 2 == 0


k_even = 0
for i in range(1, 9):
    a = int(input(f"Введите a{i}: "))
    if is_even(a):
        k_even = k_even + 1
k_odd = 0
for i in range(1, 9):
    b = int(input(f"Введите b{i}: "))
    if not is_even(b):
        k_odd = k_odd + 1
print("Количество четных чисел в первой последовательности:", k_even)
print("Количество нечетных чисел во второй последовательности:", k_odd)
