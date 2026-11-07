n = int(input("Введите возраст n (1-99): "))
if 11 <= n % 100 <= 14:
    word = "лет"
elif n % 10 == 1:
    word = "год"
elif 2 <= n % 10 <= 4:
    word = "года"
else:
    word = "лет"
print("мне", n, word)
