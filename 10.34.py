WIDTH = 80
HEIGHT = 25

# 1)
print("1)")
for row in range(HEIGHT):
    for col in range(WIDTH):
        if row == 0 or row == HEIGHT - 1 or col == 0 or col == WIDTH - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 2)
def draw_line():
    for i in range(80):
        print("*", end="")
    print()


print("2)")
draw_line()
for row in range(HEIGHT - 2):
    print("*" + " " * (WIDTH - 2) + "*")
draw_line()
