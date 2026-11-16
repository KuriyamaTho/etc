n = int(input("Введите натуральное число n: "))
s = int(input("Введите s1: "))
mx = s
mn = s
k_mx = 1
k_mn = 1
for i in range(2, n + 1):
    s = int(input(f"Введите s{i}: "))
    if s > mx:
        mx = s
        k_mx = 1
    elif s == mx:
        k_mx = k_mx + 1
    if s < mn:
        mn = s
        k_mn = 1
    elif s == mn:
        k_mn = k_mn + 1
print("а) Максимальное число встречается раз:", k_mx)
print("б) Минимальное число встречается раз:", k_mn)
