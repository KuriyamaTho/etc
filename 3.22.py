print("X Y Z | а) б) в)")
X = False
Y = False
Z = False
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = False
Y = False
Z = True
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = False
Y = True
Z = False
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = False
Y = True
Z = True
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = True
Y = False
Z = False
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = True
Y = False
Z = True
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = True
Y = True
Z = False
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))

X = True
Y = True
Z = True
print(X, Y, Z, "|", not (X or not Y and Z), Y or (X and not Y or Z), not (not X and Y or Z))
