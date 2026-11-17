s = "килбайот"
p = 7
k = 4
s = s[:k - 1] + s[p - 1] + s[k - 1:p - 1] + s[p:]
print(s)
