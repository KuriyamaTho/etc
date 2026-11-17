s = input("Введите текст: ")
plus = 0
star = 0
for ch in s:
    if ch == "+":
        plus = plus + 1
    if ch == "*":
        star = star + 1
print("Символ + встречается раз:", plus)
print("Символ * встречается раз:", star)
