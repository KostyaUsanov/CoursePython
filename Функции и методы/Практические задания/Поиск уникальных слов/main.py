# TODO реализовать функцию
def get_unique_words(a):
    a = list(set(a.split()))
    a.sort()
    return a


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
