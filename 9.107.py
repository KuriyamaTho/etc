s = input("Введите слово: ")
first_a = -1
last_o = -1
for i in range(len(s)):
    if s[i] == "а" and first_a == -1:
        first_a = i
    if s[i] == "о":
        last_o = i
if first_a != -1 and last_o != -1:
    t = list(s)
    c = t[first_a]
    t[first_a] = t[last_o]
    t[last_o] = c
    s = "".join(t)
print(s)
