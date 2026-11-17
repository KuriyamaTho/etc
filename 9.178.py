s = input("Введите предложение: ")
words = s.split()

# а)
result = []
for word in words:
    i = word.find("а")
    if i != -1:
        word = word[:i] + "о" + word[i + 1:]
    result.append(word)
print("а)", " ".join(result))

# б)
result = []
for word in words:
    last = word[-1]
    t = ""
    for ch in word[:-1]:
        if ch != last:
            t = t + ch
    result.append(t + last)
print("б)", " ".join(result))

# в)
result = []
for word in words:
    t = ""
    for ch in word:
        if ch not in t:
            t = t + ch
    result.append(t)
print("в)", " ".join(result))

# г)
longest = 0
for i in range(len(words)):
    if len(words[i]) > len(words[longest]):
        longest = i
result = []
for i in range(len(words)):
    word = words[i]
    if i == longest:
        n = len(word)
        if n % 2 == 1:
            word = word[:n // 2] + word[n // 2 + 1:]
        else:
            word = word[:n // 2 - 1] + word[n // 2 + 1:]
    result.append(word)
print("г)", " ".join(result))
