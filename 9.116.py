for label, s in (("а", "АРГЕНТИНА МАНИТ НЕГРА"), ("б", "ПОТ КАК ПОТОП"), ("в", "А РОЗА УПАЛА НА ЛАПУ АЗОРА")):
    t = ""
    for ch in s:
        if ch != " ":
            t = t + ch
    i = 0
    j = len(t) - 1
    while i < j and t[i] == t[j]:
        i = i + 1
        j = j - 1
    if i >= j:
        print(label + ")", s, "- перевертыш")
    else:
        print(label + ")", s, "- не перевертыш")
