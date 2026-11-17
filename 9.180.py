s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
words2 = s2.split()
answers = []
for word in s1.split():
    if word in words2:
        answers.append("да")
    else:
        answers.append("нет")
print(" ".join(answers))
