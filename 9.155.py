s = input("Введите слово, в котором только две одинаковые буквы: ")
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            print("Одинаковые буквы:", s[i], s[j])
