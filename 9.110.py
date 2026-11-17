s = input("Введите слово: ")

# а)
i = -1
for j in range(len(s)):
    if s[j] == "о" and i == -1:
        i = j
if i != -1:
    t = s[:i] + s[i + 1:] + "_"
else:
    t = s
print("а)", t)

# б)
i = -1
for j in range(len(s)):
    if s[j] == "л":
        i = j
if i != -1:
    t = s[:i] + s[i + 1:] + "_"
else:
    t = s
print("б)", t)
