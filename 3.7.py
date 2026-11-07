A = True
B = False
C = False
print("а)", A or not (A and B) or C)
print("б)", not A or A and (B or C))
print("в)", (A or B and not C) and C)
