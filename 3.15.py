print("A B | а) б) в)")
A = False
B = False
print(A, B, "|", not A or not B, A and (A or not B), (not A or B) and B)

A = False
B = True
print(A, B, "|", not A or not B, A and (A or not B), (not A or B) and B)

A = True
B = False
print(A, B, "|", not A or not B, A and (A or not B), (not A or B) and B)

A = True
B = True
print(A, B, "|", not A or not B, A and (A or not B), (not A or B) and B)
