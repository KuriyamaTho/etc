s = input("Введите слово: ")
i = 0
j = len(s) - 1
while i < j and s[i] == s[j]:
    i = i + 1
    j = j - 1
if i >= j:
    print("Да, слово является перевертышем")
else:
    print("Нет, слово не является перевертышем")
