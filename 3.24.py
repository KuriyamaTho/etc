print("X Y Z | а) б) в)")
X = False
Y = False
Z = False
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = False
Y = False
Z = True
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = False
Y = True
Z = False
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = False
Y = True
Z = True
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = True
Y = False
Z = False
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = True
Y = False
Z = True
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = True
Y = True
Z = False
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)

X = True
Y = True
Z = True
print(X, Y, Z, "|", not (Y or not X and Z) or Z, X and not (not Y or Z) or Y, not (X or Y and Z) or not X)
