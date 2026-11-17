a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
answers = []
for ch in a:
    if ch in b:
        answers.append("да")
    else:
        answers.append("нет")
print(" ".join(answers))
