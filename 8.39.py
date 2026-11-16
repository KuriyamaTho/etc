s = int(input("Введите натуральное число s: "))

# а)
print("а) Перестановки сторон считаются разными:")
for a in range(1, s + 1):
    if s % a == 0:
        print(a, "x", s // a)

# б)
print("б) Перестановки сторон считаются совпадающими:")
for a in range(1, s + 1):
    if s % a == 0 and a <= s // a:
        print(a, "x", s // a)
