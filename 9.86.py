s = input("Введите последовательность слов: ")
errors = []
for word in s.split():
    for i in range(len(word) - 1):
        if (word[i] == "ж" or word[i] == "ш" or word[i] == "Ж" or word[i] == "Ш") and word[i + 1] == "ы":
            errors.append(word)
if len(errors) == 0:
    print("Да, буквосочетания жи и ши записаны правильно")
else:
    print("Нет, ошибки в словах:", " ".join(errors))
