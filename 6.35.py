x = 500
k = 0
while k < 20:
    x = x + 1
    if x % 13 == 0 or x % 17 == 0:
        print(x)
        k = k + 1
