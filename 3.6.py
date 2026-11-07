X = False
Y = False
Z = True
print("а)", X or Y and not Z)
print("б)", not X and not Y)
print("в)", not (X and Z) or Y)
print("г)", X and not Y or Z)
print("д)", X and (not Y or Z))
print("е)", X or (not (Y or Z)))
