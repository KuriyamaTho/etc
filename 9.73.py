s = input("Введите предложение с буквами с и Т: ")
last_s = 0
last_t = 0
for i in range(len(s)):
    if s[i] == "с":
        last_s = i + 1
    if s[i] == "Т":
        last_t = i + 1
if last_s > last_t:
    print("Позже встречается буква с")
else:
    print("Позже встречается буква Т")
