def procedure1(n):
    if n > 0:
        print(n, end=" ")
        procedure1(n - 1)


def procedure2(n):
    if n > 0:
        procedure2(n - 1)
        print(n, end=" ")


def procedure3(n):
    if n > 0:
        print(n, end=" ")
        procedure3(n - 1)
        print(n, end=" ")


print("а)", end=" ")
procedure1(5)
print()
print("б)", end=" ")
procedure2(5)
print()
print("в)", end=" ")
procedure3(5)
print()
