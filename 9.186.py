s = input("Введите строку текста: ")
length = int(input("Введите требуемую длину строки: "))
words = s.split()
if len(words) == 1:
    print(words[0])
else:
    total = 0
    for word in words:
        total = total + len(word)
    spaces = length - total
    gaps = len(words) - 1
    base = spaces // gaps
    extra = spaces % gaps
    result = words[0]
    for i in range(1, len(words)):
        gap = base
        if i <= extra:
            gap = gap + 1
        result = result + " " * gap + words[i]
    print(result)
