A = True
B = False
C = False
print("а)", A or B and not C)
print("б)", not A and not B)
print("в)", not (A and C) or B)
print("г)", A and not B or C)
print("д)", A and (not B or C))
print("е)", A or (not (B and C)))
