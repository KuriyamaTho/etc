s = input("Введите слово: ")
stars = ""
for i in range(len(s)):
    stars = stars + "*"
print(stars + s + stars)
