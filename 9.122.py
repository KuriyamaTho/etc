s = input("Введите слово, оканчивающееся символом _: ")
c = input("Введите вставляемую букву: ")
i = -1
for j in range(len(s)):
    if s[j] == "и" and i == -1:
        i = j
if i != -1:
    s = s[:i + 1] + c + s[i + 1:-1]
print(s)
