print("A B C | а) б) в)")
A = False
B = False
C = False
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = False
B = False
C = True
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = False
B = True
C = False
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = False
B = True
C = True
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = True
B = False
C = False
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = True
B = False
C = True
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = True
B = True
C = False
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)

A = True
B = True
C = True
print(A, B, C, "|", not (A or not B and C) or C, not (A and not B or C) and B, not (not A or B and C) or A)
