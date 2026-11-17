s = input("Введите арифметическое выражение: ")
depth = 0
first_extra_right = 0
for i in range(len(s)):
    if s[i] == "(":
        depth = depth + 1
    elif s[i] == ")":
        if depth > 0:
            depth = depth - 1
        elif first_extra_right == 0:
            first_extra_right = i + 1

# а)
if depth == 0 and first_extra_right == 0:
    print("а) да")
else:
    print("а) нет")

# б)
if first_extra_right > 0:
    print("б) Лишняя правая скобка, позиция первой такой скобки:", first_extra_right)
if depth > 0:
    print("б) Количество лишних левых скобок:", depth)
if depth == 0 and first_extra_right == 0:
    print("б) Скобки расставлены правильно")
