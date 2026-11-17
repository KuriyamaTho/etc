a = input("Введите название первого города: ")
b = input("Введите название второго города: ")
c = input("Введите название третьего города: ")
longest = a
shortest = a
if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c
if len(b) < len(shortest):
    shortest = b
if len(c) < len(shortest):
    shortest = c
print("Самое длинное название:", longest)
print("Самое короткое название:", shortest)
