print("X Y | а) б) в)")
X = False
Y = False
print(X, Y, "|", not (X and not Y) or X, Y and not X or not Y, not Y and not X or Y)

X = False
Y = True
print(X, Y, "|", not (X and not Y) or X, Y and not X or not Y, not Y and not X or Y)

X = True
Y = False
print(X, Y, "|", not (X and not Y) or X, Y and not X or not Y, not Y and not X or Y)

X = True
Y = True
print(X, Y, "|", not (X and not Y) or X, Y and not X or not Y, not Y and not X or Y)
