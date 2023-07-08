def palindrome(a):
    return True if a == a[::-1] else False


a = str(input('Введите слово:'))
print(palindrome(a))
