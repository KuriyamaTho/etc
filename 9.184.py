s = input("Введите текст: ")
opened = False
extra_left = 0
first_extra_right = 0
for i in range(len(s)):
    if s[i] == "(":
        if opened:
            extra_left = extra_left + 1
        opened = True
    elif s[i] == ")":
        if opened:
            opened = False
        elif first_extra_right == 0:
            first_extra_right = i + 1
if opened:
    extra_left = extra_left + 1

# а)
if extra_left == 0 and first_extra_right == 0:
    print("а) да")
else:
    print("а) нет")

# б)
if first_extra_right > 0:
    print("б) Лишняя правая скобка, позиция первой такой скобки:", first_extra_right)
if extra_left > 0:
    print("б) Количество лишних левых скобок:", extra_left)
if extra_left == 0 and first_extra_right == 0:
    print("б) Скобки расставлены правильно")
