s = input("Введите предложение: ")
for i in range(len(s) - 1):
    if s[i] == "н" and s[i + 1] == "н":
        print("нн")
