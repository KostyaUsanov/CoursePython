# TODO Напишите функцию `is_palindrome`
def is_palindrome(pol):
    b = "".join(pol.lower().split())
    b1 = b == b[::-1]
    return b1


a = "А роза упала на лапу Азора"


result = is_palindrome(a)
print(result)

