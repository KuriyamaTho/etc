s = input("Введите предложение: ")
found = ""
for word in s.split():
    if found == "" and word[0] == "к":
        found = word
if found != "":
    print("Слово, начинающееся на букву к:", found)
else:
    print("Слов, начинающихся на букву к, в предложении нет")
