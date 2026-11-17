s = input("Введите текст: ")
k = 0
for ch in s:
    if ch == "+" or ch == "–" or ch == "-":
        k = k + 1
print("Общее число вхождений символов + и -:", k)
