s = input("Введите текст: ")
run = 1
found = False
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        run = run + 1
    else:
        run = 1
    if run >= 5:
        found = True
if found:
    print("Да, в тексте есть пять идущих подряд одинаковых символов")
else:
    print("Нет, пяти идущих подряд одинаковых символов в тексте нет")
