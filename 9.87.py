s = input("Введите последовательность слов: ")
result = ""
errors = 0
i = 0
while i < len(s):
    if i < len(s) - 1 and (s[i] == "ч" or s[i] == "щ" or s[i] == "Ч" or s[i] == "Щ") and s[i + 1] == "я":
        result = result + s[i] + "а"
        errors = errors + 1
        i = i + 2
    else:
        result = result + s[i]
        i = i + 1
if errors == 0:
    print("Буквосочетания ча и ща записаны правильно")
else:
    print("Исправлено ошибок:", errors)
    print(result)
