import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

s = 20 * 20
for k in range(19, 0, -1):
    d = s - k * k
    s = d * d
text = str(s)
print("Количество цифр в значении выражения:", len(text))
print(text)
