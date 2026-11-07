print("A B C | а) б) в)")
A = False
B = False
C = False
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = False
B = False
C = True
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = False
B = True
C = False
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = False
B = True
C = True
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = True
B = False
C = False
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = True
B = False
C = True
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = True
B = True
C = False
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))

A = True
B = True
C = True
print(A, B, C, "|", not (A and B) and (not A or not C), not (A and not B) or (A or not C), A and not B or not (A or not C))
