s = input("Введите предложение: ")
words = s.split()
mx = 0
for word in words:
    if len(word) > mx:
        mx = len(word)
if mx > 10:
    print("Да, самое длинное слово имеет больше 10 символов")
else:
    print("Нет, самое длинное слово имеет не больше 10 символов")
