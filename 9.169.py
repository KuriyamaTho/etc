s = input("Введите предложение: ")
words = s.split()

# а)
print("а) Слова, начинающиеся и оканчивающиеся на одну и ту же букву:")
for word in words:
    if word[0] == word[-1]:
        print(word)

# б)
print("б) Слова, содержащие ровно три буквы е:")
for word in words:
    k = 0
    for ch in word:
        if ch == "е":
            k = k + 1
    if k == 3:
        print(word)

# в)
print("в) Слова, содержащие хотя бы одну букву о:")
for word in words:
    if "о" in word:
        print(word)
