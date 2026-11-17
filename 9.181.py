s1 = input("Введите первое предложение: ")
s2 = input("Введите второе предложение: ")
words1 = s1.split()
words2 = s2.split()
answers = []
for i in range(len(words1)):
    if words1[i] not in words1[:i]:
        if words1[i] in words2:
            answers.append("да")
        else:
            answers.append("нет")
print(" ".join(answers))
