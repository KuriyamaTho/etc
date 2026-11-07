total = 0
sq = 0
odd = 1
for k in range(1, 11):
    sq = sq + odd
    odd = odd + 2
    total = total + sq
print("Сумма =", total)
