a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
answers = []
for i in range(len(a)):
    if a[i] not in a[:i]:
        if a[i] in b:
            answers.append("да")
        else:
            answers.append("нет")
print(" ".join(answers))
