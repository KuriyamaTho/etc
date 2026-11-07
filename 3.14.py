print("X Y | а) б) в)")
X = False
Y = False
print(X, Y, "|", not (X or Y), not X and Y, X and not Y)

X = False
Y = True
print(X, Y, "|", not (X or Y), not X and Y, X and not Y)

X = True
Y = False
print(X, Y, "|", not (X or Y), not X and Y, X and not Y)

X = True
Y = True
print(X, Y, "|", not (X or Y), not X and Y, X and not Y)
