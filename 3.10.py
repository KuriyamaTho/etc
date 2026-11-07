A = False
B = False
C = True
print("а)", (not A or not B) and not C)
print("б)", (not A or not B) and (A or B))
print("в)", A and B or A and C or not C)
