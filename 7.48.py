n = int(input("Введите количество учеников в классе: "))
sb = 0
kb = 0
sg = 0
kg = 0
for i in range(1, n + 1):
    h = float(input(f"Введите рост ученика {i} (у мальчиков со знаком минус), см: "))
    if h < 0:
        sb = sb - h
        kb = kb + 1
    else:
        sg = sg + h
        kg = kg + 1
if kb > 0:
    print("Средний рост мальчиков:", sb / kb)
else:
    print("Мальчиков в классе нет")
if kg > 0:
    print("Средний рост девочек:", sg / kg)
else:
    print("Девочек в классе нет")
