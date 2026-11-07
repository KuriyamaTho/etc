print("A B | а) б) в)")
A = False
B = False
print(A, B, "|", not (not A and not B) and A, not (not A or not B) or A, not (not A or not B) and B)

A = False
B = True
print(A, B, "|", not (not A and not B) and A, not (not A or not B) or A, not (not A or not B) and B)

A = True
B = False
print(A, B, "|", not (not A and not B) and A, not (not A or not B) or A, not (not A or not B) and B)

A = True
B = True
print(A, B, "|", not (not A and not B) and A, not (not A or not B) or A, not (not A or not B) and B)
