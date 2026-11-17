s = input("Введите предложение: ")
m = 0
n = 0
for ch in s:
    if ch == "м":
        m = m + 1
    if ch == "н":
        n = n + 1
if m > n:
    print("Букв м больше")
elif n > m:
    print("Букв н больше")
else:
    print("Букв м и н поровну")
