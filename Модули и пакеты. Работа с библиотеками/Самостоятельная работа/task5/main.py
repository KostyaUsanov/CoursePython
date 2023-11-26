from random import sample

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
INT_ = '0123456789'
all_ = ascii_lowercase + ascii_uppercase + INT_

def get_random_password(n) -> str:
    passw = "".join(sample(n, 20))
    return passw


print(get_random_password(all_))
