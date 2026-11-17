s = input("Введите слово из 15 букв: ")
k = int(input("Введите k: "))
t = int(input("Введите s (k < s): "))
print(s[:k] + s[k:t - 1][::-1] + s[t - 1:])
