print("X Y Z | а) б) в)")
X = False
Y = False
Z = False
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = False
Y = False
Z = True
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = False
Y = True
Z = False
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = False
Y = True
Z = True
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = True
Y = False
Z = False
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = True
Y = False
Z = True
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = True
Y = True
Z = False
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))

X = True
Y = True
Z = True
print(X, Y, Z, "|", not (X or Y) and (not X or not Z), not (not X and Y) or (X and not Z), X or not Y and not (X or not Z))
