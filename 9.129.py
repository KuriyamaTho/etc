s = "алигортм"
p = 3
k = 6
s = s[:p - 1] + s[p:k] + s[p - 1] + s[k:]
print(s)
