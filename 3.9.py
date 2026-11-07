X = True
Y = False
Z = False
print("а)", not X or not Y or not Z)
print("б)", (not X or not Y) and (X or Y))
print("в)", X and Y or X and Z or not Z)
