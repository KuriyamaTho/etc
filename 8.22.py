best_course_sum = 10 ** 9
best_course = 0
mn = 10 ** 9
mn_course = 0
mn_group = 0
for course in range(1, 6):
    s = 0
    row_min = 10 ** 9
    row_group = 0
    for group in range(1, 7):
        k = int(input(f"Курс {course}, группа {group}, число студентов: "))
        s = s + k
        if k < row_min:
            row_min = k
            row_group = group
        if k < mn:
            mn = k
            mn_course = course
            mn_group = group
    if s < best_course_sum:
        best_course_sum = s
        best_course = course
    print("в) На курсе", course, "самая малочисленная группа:", row_group)
print("а) Меньше всего студентов обучается на курсе:", best_course)
print("б) Самая малочисленная группа: номер", mn_group, ", курс", mn_course)
