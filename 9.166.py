s = input("Введите предложение: ")
words = s.split()
t = words[0]
words[0] = words[-1]
words[-1] = t
print(" ".join(words))
