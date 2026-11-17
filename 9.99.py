s = "очепатка"
t = list(s)
c = t[1]
t[1] = t[3]
t[3] = c
s = "".join(t)
print(s)
