s = input("Введите предложение: ")
n1 = int(input("Введите n1: "))
n2 = int(input("Введите n2 (n1 <= n2): "))
t = s[:n1 - 1] + s[n2:]
for i in range(n2 - n1 + 1):
    t = t + "_"
print(t)
