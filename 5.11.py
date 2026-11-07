import math

R = 6350
for h in range(1, 11):
    print(h, "км -", f"{math.sqrt(2 * R * h + h ** 2):.3f}", "км")
