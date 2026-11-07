print("X Y | а) б) в)")
X = False
Y = False
print(X, Y, "|", not (not X or Y) or not X, not (not X and not Y) and X, not (X or not Y) or not Y)

X = False
Y = True
print(X, Y, "|", not (not X or Y) or not X, not (not X and not Y) and X, not (X or not Y) or not Y)

X = True
Y = False
print(X, Y, "|", not (not X or Y) or not X, not (not X and not Y) and X, not (X or not Y) or not Y)

X = True
Y = True
print(X, Y, "|", not (not X or Y) or not X, not (not X and not Y) and X, not (X or not Y) or not Y)
