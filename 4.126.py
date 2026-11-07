k = int(input("Введите натуральное число k: "))
if 11 <= k % 100 <= 14:
    word = "грибов"
elif k % 10 == 1:
    word = "гриб"
elif 2 <= k % 10 <= 4:
    word = "гриба"
else:
    word = "грибов"
print("мы нашли", k, word, "в лесу")
