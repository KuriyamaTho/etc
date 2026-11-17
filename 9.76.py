s = input("Введите предложение с несколькими буквами е: ")
first = 0
last = 0
for i in range(len(s)):
    if s[i] == "е":
        if first == 0:
            first = i + 1
        last = i + 1
print("а) Номер первой буквы е:", first)
print("б) Номер последней буквы е:", last)
