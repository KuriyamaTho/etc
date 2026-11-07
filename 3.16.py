print("X Y | а) б) в)")
X = False
Y = False
print(X, Y, "|", not X and not Y, X or (not X and Y), (not X and Y) or Y)

X = False
Y = True
print(X, Y, "|", not X and not Y, X or (not X and Y), (not X and Y) or Y)

X = True
Y = False
print(X, Y, "|", not X and not Y, X or (not X and Y), (not X and Y) or Y)

X = True
Y = True
print(X, Y, "|", not X and not Y, X or (not X and Y), (not X and Y) or Y)
