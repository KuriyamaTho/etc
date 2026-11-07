print("A B | а) б) в)")
A = False
B = False
print(A, B, "|", not A and not B or A, B or not A and not B, B and not (A and not B))

A = False
B = True
print(A, B, "|", not A and not B or A, B or not A and not B, B and not (A and not B))

A = True
B = False
print(A, B, "|", not A and not B or A, B or not A and not B, B and not (A and not B))

A = True
B = True
print(A, B, "|", not A and not B or A, B or not A and not B, B and not (A and not B))
