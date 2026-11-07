print("A B C | а) б) в)")
A = False
B = False
C = False
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = False
B = False
C = True
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = False
B = True
C = False
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = False
B = True
C = True
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = True
B = False
C = False
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = True
B = False
C = True
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = True
B = True
C = False
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))

A = True
B = True
C = True
print(A, B, C, "|", not (A or not B and C), A and not (B or not C), not (not A or B and C))
