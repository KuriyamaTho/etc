print("A B | а) б) в)")
A = False
B = False
print(A, B, "|", not (A and B), not A or B, A or not B)

A = False
B = True
print(A, B, "|", not (A and B), not A or B, A or not B)

A = True
B = False
print(A, B, "|", not (A and B), not A or B, A or not B)

A = True
B = True
print(A, B, "|", not (A and B), not A or B, A or not B)
