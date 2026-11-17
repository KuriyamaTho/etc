def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True


a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = input("Введите третье слово: ")
if is_palindrome(a) or is_palindrome(b) or is_palindrome(c):
    print("Да, хотя бы одно из слов является палиндромом")
else:
    print("Нет, ни одно из слов не является палиндромом")
