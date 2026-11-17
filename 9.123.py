s = input("Введите предложение, оканчивающееся символом _: ")
c = input("Введите вставляемую букву: ")
i = -1
for j in range(len(s)):
    if s[j] == "и":
        i = j
if i != -1:
    s = s[:i] + c + s[i:-1]
print(s)
