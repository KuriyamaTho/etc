h = float(input("Введите рост нового ученика: "))
k = 0
i = 0
taller = True
while i < 15 and taller:
    x = float(input(f"Введите рост ученика {i + 1}: "))
    i = i + 1
    taller = x > h
    k = k + taller
print("Рост нового ученика займет место:", k + 1)
