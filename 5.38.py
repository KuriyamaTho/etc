distance = 0
path = 0
sign = 1
for k in range(1, 101):
    distance = distance + sign / k
    path = path + 1 / k
    sign = -sign
print("а) Расстояние от дома после 100-го этапа, км:", distance)
print("б) Общий пройденный путь, км:", path)
